# 📊 Análisis de Ventas E-commerce

## Objetivo

Analizar un año de pedidos de una tienda en línea de tecnología para identificar los productos, ciudades y canales de venta más rentables, detectar problemas de calidad de datos, y entregar recomendaciones accionables al equipo comercial.

## Dataset

- **Fuente:** datos simulados (2,025 pedidos, año 2024)
- **Columnas principales:** `id_pedido`, `fecha_pedido`, `producto`, `categoria`, `cantidad`, `precio_unitario`, `total_pedido`, `ciudad_envio`, `metodo_pago`, `canal_venta`, `calificacion_cliente`, `estado_pedido`
- **Retos del dataset:** valores nulos en ciudad y calificación, filas duplicadas, inconsistencias de formato de texto, y errores de captura (cantidades negativas)

## Herramientas

- **Python** (pandas, matplotlib, seaborn) — limpieza y análisis exploratorio
- **Power BI** — dashboard interactivo
- **Jupyter Notebook** — documentación del proceso paso a paso

## Proceso

1. Diagnóstico inicial de calidad de datos (nulos, duplicados, inconsistencias)
2. Limpieza y estandarización
3. Análisis exploratorio orientado a preguntas de negocio
4. Visualización de hallazgos clave
5. Exportación de datos limpios para el dashboard

## Preguntas de negocio respondidas

- ¿Qué productos generan más ingresos? Laptop gamer, Ultrabook
- ¿Hay estacionalidad en las ventas a lo largo del año? De enero a marzo hay una alta, despues de agosto a diciembre se vuelve a replicar
- ¿Qué ciudad tiene el ticket promedio más alto? Merida
- ¿Qué método de pago y canal de venta son más rentables? App movil y Sitio web
- ¿Qué porcentaje de pedidos se cancelan o devuelven? `Webcam HD 1080p` cargador y router 

## Hallazgos clave

- Hallazgo 1: hay muchos productos con valores nulos
- Hallazgo 2: los reportes indican un crecimiento por temporadas cortas
- Hallazgo 3: Aun con tarjeta de debito, prefieren pago en efectivo

## Recomendaciones

Cómo reproducir este análisis

```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook notebooks/analisis.ipynb
```

## Estructura del proyecto

```
01-analisis-ventas-ecommerce/
├── data/
│   ├── ventas_ecommerce.csv     # datos originales (sin limpiar)
│   └── ventas_limpio.csv        # datos limpios (generado por el notebook)
├── notebooks/
│   └── analisis.ipynb           # análisis completo paso a paso
├── dashboard/
│   └── (dashboard.pbix pendiente)
└── README.md
```
