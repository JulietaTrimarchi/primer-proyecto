                                                        # **Proyecto Individual N° 1**

                                                   ## **Machine Learning Operations (MLOps)**

### Contexto

Este proyecto tiene como objetivo hacer el rol de un MLOps Engineer comenzando con un trabajo de Data Engineer y lograr un MVP (Minimum
Viable Product). 

### Instalación y requisitos

- Python 3.12
- fastapi
- pandas
- uvicorn
- pyarrow
- scikit-learn
- nltk
- langdetect

### Pasos de instalación:

1. Clonar el repositorio: git clone https://github.com/usuario/proyecto-ventas-ropa.git
2. Crear un entorno virtual: python -m venv venv
3. Activar el entorno virtual:
  - Windows: venv\Scripts\activate
  - macOS/Linux: source venv/bin/activate
4. Instalar las dependencias: pip install -r requirements.txt

### Estructura del proyecto

- Datasets: Contiene los archivos con la data que va a utilizar la API
- EDA.ipynb: Notebook que contiene el informe EDA
- ETL.ipynb: Notebook que contiene el proceso de ETL
- Modelo.ipynb: Notebook donde esta desarrollado el modelo de Machine Learning
- main.py: Archivo donde esta desarrollada la API
- requirements.txt: Archivo que contiene las librerias necesarias para utilizar el proyecto

### Datos

Los datos utilizados en este proyecto son acerca de películas. Los mismos incluyen información acerca de su sinopsis, su lenguage 
original, su popularidad, directores, actores, entre otros.

### Metodología

Se utilizaron transformaciones de los datos y un análisis exploratorio de los mismos. Se aplicó un modelo de Machine Learning llamado
Similitud del Coseno para crear un sistema de recomendación de películas. 

### Autora:

Este proyecto fue realizado por: Julieta Trimarchi. 
