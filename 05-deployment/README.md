# Nombre del Proyecto

Aplicación de análisis y visualización de datos construida con **Pandas**, **Plotly** y **Streamlit**.

## Descripción

Este proyecto permite:

- Cargar y transformar datos con Pandas.
- Explorar métricas clave de forma interactiva.
- Visualizar resultados con gráficos dinámicos en Plotly.
- Publicar un dashboard web con Streamlit.

Está pensado como base para proyectos de analítica, monitoreo y reporting rápido.

## Características

- Limpieza y preparación de datos tabulares.
- Filtros interactivos por categorías, fechas u otras variables.
- Gráficos de líneas, barras, dispersión y tablas resumen.
- KPIs principales en una interfaz simple y clara.
- Estructura modular para crecer por componentes.

## Tecnologías

- Python 3.10+
- Pandas
- Plotly
- Streamlit

## Estructura de Datos

El proyecto asume una tabla principal en formato CSV/Parquet con columnas como:

| Columna     | Tipo sugerido | Descripción                      |
| ----------- | ------------- | -------------------------------- |
| `id`        | entero        | Identificador único del registro |
| `fecha`     | fecha/hora    | Fecha del evento o medición      |
| `categoria` | texto         | Segmento o clasificación         |
| `valor`     | numérico      | Métrica principal a analizar     |
| `region`    | texto         | Ubicación geográfica (opcional)  |

### Ejemplo de archivo

```csv
id,fecha,categoria,valor,region
1,2026-01-01,A,120,Norte
2,2026-01-02,B,98,Sur
3,2026-01-03,A,150,Centro
```

## Requisitos

- Python 3.10 o superior.
- `pip` actualizado.

## Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <RUTA_AL_PROYECTO>
```

2. Crear y activar entorno virtual:

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Iniciar la aplicación Streamlit:

```bash
streamlit run main.py
```

Luego abrir en el navegador la URL indicada en consola (por defecto `http://localhost:8501`).

## Configuración

Si se requiere configuración por entorno, se sugiere usar variables de entorno:

- `DATA_PATH`: ruta de datos de entrada.
- `APP_ENV`: entorno (`dev`, `test`, `prod`).

Ejemplo en PowerShell:

```powershell
$env:DATA_PATH = "./data/raw/datos.csv"
$env:APP_ENV = "dev"
```

## Contacto

Autor/a: Tu Nombre

Correo: tu_correo@dominio.com
