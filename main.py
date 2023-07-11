from fastapi import FastAPI
import pandas as pd
import numpy as np
import sklearn

app = FastAPI()



df = pd.read_csv('movies_credits.csv')
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    lista_peli = []
    for peli, lang in zip(df['title'], df['original_language']):
        if idioma == lang:
            lista_peli.append(peli)
    return {'peliculas':len(lista_peli)}

    
@app.get('/peliculas_duracion_anio/{pelicula}')
def obtener_duracion_y_anio(nombre):
    duracion = df[df['title'] == nombre]['runtime'].values[0]
    anio = df[df['title'] == nombre]['release_year'].values[0]
    return str(duracion), str(anio)




@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    # Filtrar las películas que pertenecen a la colección específica
    peliculas_coleccion = df[df['name_collection'] == franquicia]
    
    # Obtener la cantidad de películas
    cantidad_peliculas = len(peliculas_coleccion)
    
    # Calcular las ganancias totales y su promedio
    ganancias_totales = peliculas_coleccion['revenue'].sum()
    promedio_ganancias = peliculas_coleccion['revenue'].mean()
    
    # Devolver los resultados
    return {'franquicia':franquicia, 'cantidad':cantidad_peliculas, 'ganancia_total':str(ganancias_totales), 'ganancia_promedio':str(promedio_ganancias)}

@app.get('/peliculas_pais/{pais}')
def cantidad_peliculas(pais: str):
    # Filtrar el DataFrame por el país especificado
    mascara = df[df['production_countries'].str.contains(pais, case=False, na=False)]

 
    movie_count = len(mascara)

    return {'country': pais, 'movie_count': movie_count}


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    # Filtrar las películas realizadas por la productora especificada
    peliculas_productora = df[df['production_companies'].str.contains(productora)]
    
    # Obtener la cantidad de películas realizadas por la productora
    cantidad_peliculas = len(peliculas_productora)
    
    # Obtener el total de ingresos de las películas realizadas por la productora
    revenue_total = str(peliculas_productora['revenue'].sum())
    
    # Devolver el resultado
    return {'productora':productora, 'revenue_total': revenue_total,'cantidad':cantidad_peliculas}


@app.get('/get_director/{nombre_director}')
def get_director(nombre_director):
    # Filtrar el dataset para obtener las películas del director dado
    director_movies = df[df['Director'] == nombre_director]

    # Extraer las columnas relevantes del dataset filtrado
    movies_info = director_movies[['title', 'release_date', 'return', 'budget', 'revenue']]

    # Crear una lista de diccionarios con la información de cada película
    movies_list = director_movies['title']

    # Calcular el retorno total del director
    retorno_total_director = director_movies['return'].sum().astype(str)

    # Obtener los años de las películas del director
    anios_peliculas = director_movies['release_year'].astype(str)

    # Calcular el retorno promedio de cada película
    retorno_pelicula = director_movies['return'].astype(str)

    # Obtener los presupuestos y los ingresos de las películas
    budget_pelicula = director_movies['budget'].astype(str)
    revenue_pelicula = director_movies['revenue'].astype(str)

    # Crear el diccionario de respuesta
    return [
        nombre_director,
        retorno_total_director,
        movies_list,
        anios_peliculas,
        retorno_pelicula,
        budget_pelicula,
        revenue_pelicula
    ]



# ML
new_df = pd.read_csv('movies_recomendacion.csv')
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
cv.fit_transform(new_df['tags']).toarray().shape
vectors = cv.fit_transform(new_df['tags']).toarray()

import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


new_df['tags'] = new_df['tags'].apply(stem)

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors[:10000,:])

@app.get('/recomendacion/{titulo}')

def recomendacion(titulo:str):
    peli_index = new_df[new_df['title'] == titulo].index[0]
    distancia = similarity[peli_index]
    peli_lista = sorted(list(enumerate(distancia)), reverse=True, key= lambda x:x[1])[1:6]
    lista_recomendar = []
    
    for i in peli_lista:
        lista_recomendar.append(new_df.title[i[0]])
    return {'lista recomendada': lista_recomendar}

# Iniciar el servidor de desarrollo con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    