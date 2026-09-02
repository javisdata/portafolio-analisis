"""
ETL - Precios de criptomonedas (CoinGecko -> SQLite)
========================================================
Script ejecutable y automatizable. Pensado para correrse periódicamente
(ej. con el Programador de Tareas de Windows o un cron job) y así ir
acumulando un histórico de precios en la base de datos local.

Uso manual:
    python etl_cripto.py

Uso automatizado (ejemplo con Programador de Tareas de Windows):
    Programa: python
    Argumentos: C:\\ruta\\completa\\a\\etl_cripto.py
    Frecuencia: diaria
"""

import requests
import pandas as pd
import sqlite3
from pathlib import Path
from datetime import datetime

# --- Configuracion ---
URL_API = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"
RUTA_DB = Path(__file__).resolve().parent.parent / "data" / "cripto.db"
NOMBRE_TABLA = "precios_cripto"

COLUMNAS = ['id', 'symbol', 'name', 'current_price', 'market_cap',
            'market_cap_rank', 'total_volume', 'high_24h', 'low_24h',
            'price_change_percentage_24h']

RENOMBRAR = {
    'id': 'id_moneda',
    'symbol': 'simbolo',
    'name': 'nombre',
    'current_price': 'precio_actual_usd',
    'market_cap': 'capitalizacion_mercado',
    'market_cap_rank': 'ranking',
    'total_volume': 'volumen_24h',
    'high_24h': 'maximo_24h',
    'low_24h': 'minimo_24h',
    'price_change_percentage_24h': 'cambio_porcentual_24h',
}


def extraer():
    """Extrae datos crudos desde la API de CoinGecko."""
    print(f"[{datetime.now()}] Extrayendo datos de la API...")
    respuesta = requests.get(URL_API, timeout=15)

    if respuesta.status_code != 200:
        raise RuntimeError(f"Error en la API: código {respuesta.status_code}")

    datos = respuesta.json()
    print(f"  -> {len(datos)} monedas obtenidas")
    return datos


def transformar(datos_crudos):
    """Limpia y estructura los datos crudos en un DataFrame listo para cargar."""
    print("Transformando datos...")
    df = pd.DataFrame(datos_crudos)
    df = df[COLUMNAS].rename(columns=RENOMBRAR)
    df['fecha_extraccion'] = pd.Timestamp.now()

    nulos = df.isna().sum().sum()
    if nulos > 0:
        print(f"  -> Advertencia: {nulos} valores nulos encontrados")

    return df


def cargar(df):
    """Carga el DataFrame a la base de datos SQLite, acumulando histórico."""
    print(f"Cargando a {RUTA_DB} ...")
    RUTA_DB.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(RUTA_DB) as conexion:
        df.to_sql(NOMBRE_TABLA, conexion, if_exists='append', index=False)
        total = pd.read_sql(f"SELECT COUNT(*) as total FROM {NOMBRE_TABLA}", conexion)

    print(f"  -> Carga completa. Total de registros acumulados: {total['total'][0]}")


def main():
    datos_crudos = extraer()
    df_limpio = transformar(datos_crudos)
    cargar(df_limpio)
    print(f"[{datetime.now()}] Pipeline ETL completado con éxito.\n")


if __name__ == "__main__":
    main()
