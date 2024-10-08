from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
from pydantic import BaseModel

app = FastAPI()

@app.get("/filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes:str) -> str:
    
    """
    Devuelve la cantidad de películas estrenadas en el mes ingresado.

    Args:
        mes (str): mes en idioma español.

    Returns:
        str: Mensaje con la cantidad de películas estrenadas o mensaje de error.
    """

    # Almaceno en una variable la data necesaria 

    cantidad_mes = pd.read_parquet("./Datasets/Peliculas por mes")

    mes = mes.lower()

    # Filtro el DataFrame para encontrar el mes

    cantidad = cantidad_mes[cantidad_mes['name_month'].str.lower() == mes]
    
    # Verifico si el DataFrame filtrado está vacío

    if cantidad.empty:
        return "Valor no encontrado"
    
    else:
        # Extraigo la cantidad de películas

        cantidad = cantidad['total_movies'].values[0]
        return f"{cantidad} películas fueron estrenadas en el mes de {mes}"
    

@app.get("/filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia:str) -> str:
    
    """
    Devuelve la cantidad de películas estrenadas en el día ingresado.

    Args:
        dia (str): día en idioma español.

    Returns:
        str: Mensaje con la cantidad de películas estrenadas o mensaje de error.
    """

    # Almaceno en una variable la data necesaria

    cantidad_dia = pd.read_parquet("./Datasets/Peliculas por dia")

    dia = dia.lower()

    # Filtro el DataFrame para encontrar el dia

    cantidad = cantidad_dia[cantidad_dia['release_day'].str.lower() == dia]
    
    # Verifico si el DataFrame filtrado está vacío

    if cantidad.empty:
        return "Valor no encontrado"
    
    else:
        # Extraigo la cantidad de películas

        cantidad = cantidad['total_peliculas'].values[0]
        return f"{cantidad} películas fueron estrenadas en los días {dia}"


@app.get("/score_titulo/{titulo}")
async def score_titulo(titulo:str) -> str:
    
    """
    Busca una película por su título y devuelve el título, año de estreno y popularidad.

    Args:
        titulo (str): Título de la película a buscar.

    Returns:
        str: Frase con la información de la película o un mensaje de error si no se encuentra.
    """

    # Almaceno en una variable la data necesaria

    score = pd.read_parquet("./Datasets/Score")

    # Filtro el DataFrame para encontrar la película con el título proporcionado
    
    score = score[score['title'].str.lower() == titulo.lower()]
    
    # Verifico si se encontró la película

    if not score.empty:

        # Extraigo la información de la película

        titulo_encontrado = score['title'].values[0]
        año_estreno = score['release_year'].values[0]
        popularidad = score['popularity'].values[0]
        
        # Formateo la respuesta

        return f"La película {titulo_encontrado} fue estrenada en el año {año_estreno} con un score/popularidad de {popularidad}."
    
    else:
        return "La película no se ha encontrado."


@app.get("/votos_titulo/{titulo}")
async def votos_titulo(titulo:str) -> str:
    
    """
    Busca una película por su título y devuelve el título, la cantidad de votos y el valor promedio de las votaciones.

    Args:
        titulo (str): Título de la película a buscar.

    Returns:
        str: Frase con la información de la película o un mensaje de error si no se encuentra o no cumple los requisitos.
    """

    # Almaceno en una variable la data necesaria

    votos = pd.read_parquet("./Datasets/Votos")

    # Filtro el DataFrame para encontrar la película con el título proporcionado
    
    pelicula = votos[votos['title'].str.lower() == titulo.lower()]

    # Verifico si se encontró la película

    if not pelicula.empty:

        # Extraigo la información de la película

        titulo_encontrado = pelicula['title'].values[0]
        votos = pelicula['vote_count'].values[0]
        promedio_votos = pelicula['vote_average'].values[0]
        
        # Verifico la cantidad de valoraciones

        if votos >= 2000:

            # Formateo la respuesta

            return (f"La película {titulo_encontrado} cuenta con un total de {votos} valoraciones, con un promedio de {promedio_votos}.")
        
        else:
            return "La película tiene menos de 2000 valoraciones, por lo tanto no se devuelve información."
        
    else:
        return "La película no ha sido encontrada."
    
 
@app.get("/peliculas_recomendadas/{titulo}")
async def recomendacion(titulo:str) -> list:

    """Devuelve una lista de las 5 películas más similares.

    Args:
        titulo (str): Título de una película.

    Returns:
        list: Lista de 5 películas recomendadas.
    """
    # Importo ruta de datos necesarios
    data = pd.read_parquet("./Datasets/Data para modelo")
    recomendaciones = joblib.load('./Datasets/recomendaciones.pkl') 

    # Convertir el título a minúsculas
    titulo_lower = titulo.strip().lower()

    data['title_lower'] = data['title'].str.lower().str.strip()
    # Buscar el índice de la película con el título dado
    
    if titulo_lower not in data['title_lower'].values:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    idx = data[data['title_lower'] == titulo_lower].index[0]
    
    # Obtener las recomendaciones usando el índice
    if idx not in recomendaciones:
        raise HTTPException(status_code=404, detail="No hay recomendaciones disponibles para esta película.")
    
    recommended_indices = recomendaciones[idx]
    
    # Convertir los índices recomendados en títulos
    recommended_titles = data.loc[data.index.isin(recommended_indices),'title'].tolist()
    
    return {"recomendaciones": recommended_titles}