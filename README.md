# Proyecto de Web Scraping - Bebemundo

## Descripción

Este proyecto realiza web scraping del sitio web [bebemundo.com.py](https://bebemundo.com.py) para extraer información de productos. Los datos obtenidos incluyen la categoría del producto, nombre del producto, precio y la página en la que se encuentra. Estos datos se almacenan en una base de datos MySQL creada con SQLAlchemy.

## Tecnologías Utilizadas

- **Python 3.10**
- **FastAPI**: Para crear el servidor y manejar las solicitudes HTTP.
- **Uvicorn**: Para ejecutar la aplicación FastAPI.
- **Pydantic**: Para la validación y serialización de datos.
- **SQLAlchemy**: Para interactuar con la base de datos MySQL.
- **Requests**: Para hacer solicitudes HTTP al sitio web.
- **BeautifulSoup4**: Para extraer y parsear datos HTML.

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/walterrivarola/WebScraping.git
    cd WebScraping
    ```

2. Crear un entorno virtual y activarlo:
    ```bash
    python -m venv venv
    source venv/bin/activate # En Windows: venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Mofidicar el archivo `database.py` en la raíz del proyecto y agregar la configuración de la base de datos MySQL:
    ```
    DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/nombre_base_datos
    ```

## Uso

1. Iniciar el servidor:
    ```bash
    uvicorn main:app --reload
    ```

2. Acceder a la API en `http://127.0.0.1:8000`.

## Endpoints

- `POST /scrape`: Realiza el scraping de los datos del sitio web y los almacena en la base de datos MySQL.

## Estructura del Proyecto

main.py `# Archivo principal de la aplicación FastAPI`<br>
models.py `# Definición de los modelos de datos con SQLAlchemy`<br>
database.py `# Configuración de la base de datos`<br>
scraper.py `# Lógica de scraping con Requests y BeautifulSoup4`<br>
requirements.txt `# Lista de dependencias del proyecto`<br>git 