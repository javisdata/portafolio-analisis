# 🔄 ETL: Precios de Criptomonedas (API → SQLite)

## Objetivo
Construir un pipeline ETL (Extract, Transform, Load) que consuma una API pública en tiempo real, limpie y estructure los datos, y los cargue en una base de datos local para consulta y análisis histórico.

## Fuente de datos
**API:** [CoinGecko](https://www.coingecko.com/en/api/documentation) (pública, sin necesidad de API key)
**Endpoint:** `coins/markets` — top 50 criptomonedas por capitalización de mercado

## Herramientas
- **Python** (`requests` para la extracción, `pandas` para la transformación)
- **SQLite** (`sqlite3`) como base de datos de carga
- **Jupyter Notebook** para el desarrollo y documentación del proceso
- Script `.py` independiente para automatización

## Arquitectura del pipeline

```
API CoinGecko  →  Extract (requests)  →  Transform (pandas)  →  Load (SQLite)
                                                                        │
                                                          data/cripto.db (histórico acumulado)
```

## Proceso
1. **Extract:** petición GET a la API, validación del código de respuesta
2. **Transform:** selección de columnas relevantes, renombrado a español, timestamp de extracción, revisión de nulos
3. **Load:** inserción en SQLite con modo `append` para acumular histórico en cada corrida
4. **Verificación:** consultas SQL directas sobre la base cargada
5. **Automatización:** script ejecutable pensado para correr periódicamente vía Programador de Tareas / cron

## Preguntas de negocio respondidas
- ¿Qué criptomonedas tuvieron mayor variación (positiva/negativa) en 24h?
- ¿Cuáles son las más volátiles del día?
- ¿Qué tan concentrado está el mercado en las top 10 monedas por capitalización?

## Hallazgos clave
*(Completar después de correr el análisis)*

## Cómo reproducir este proyecto

**Desde el notebook (exploración/aprendizaje):**
```bash
pip install requests pandas
jupyter notebook notebooks/etl.ipynb
```

**Como pipeline automatizado:**
```bash
python scripts/etl_cripto.py
```

Para programarlo en Windows: Programador de Tareas → Crear tarea básica → Acción "Iniciar un programa" → Programa: `python`, Argumentos: ruta completa a `etl_cripto.py`.

## Retos técnicos y decisiones
- **Límite de peticiones de la API:** CoinGecko limita las peticiones por minuto en su capa gratuita; el script está pensado para correr una vez por ejecución, no en loop.
- **Acumulación histórica:** se usó `if_exists='append'` deliberadamente (no `'replace'`) para poder analizar tendencias de precio a lo largo del tiempo en corridas futuras.

## Estructura del proyecto
```
02-etl-api-criptomonedas/
├── data/
│   └── cripto.db              # base de datos SQLite (se genera al correr el pipeline)
├── notebooks/
│   └── etl.ipynb              # desarrollo guiado paso a paso
├── scripts/
│   └── etl_cripto.py          # pipeline automatizable
└── README.md
```
