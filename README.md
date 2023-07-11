# Proyecto Individual N1

El proyecto consta de trabajar dos raw datasets, siguiendo los pasos sugeridos, y poniendo un poco mas de magia para poder implementar las funciones requeridas. La cereza del pastel, el modelo de machine learning para el sistema de recomendacion de peliculas

## Requerimientos del proyecto:
Realizar ETL y EDA sobre los datasets originales, desarrollar las funciones y el sistema de recomendacion e implementarlas con FastAPI, dejarlas colgadas en internet de forma publica con Render

Estructura de contenido

1. Este archivo guarda el EDA generado con pandas.profiling.
2. main.py: Archivo de Python que usamos para iniciar y ejecutar la aplicacion FastAPI .
3. movies.ipynb/movies_recomendacion.ipynb: Notebooks donde se realizan el ETL y EDA de los datasets para las funciones y el sistema de recomendacion.
4. movies_credits.csv/movies_recomendacion.csv: Estos archivos .csv son los datasets limpios para aplicar las funciones y el sistema de recomendacion.
5. requirements.txt: Este archivo guarda las librerias del proyecto.


## Sobre la API

Aplicación montada en Render: https://deploy-pablozmr-sistema-recomendacion.onrender.com/docs/

Funciones en la API:

    /peliculas_idioma/{idioma}: 
        Retorna la cantidad de peliculas que existen en el idioma solicitado.

    /peliculas_duracion_anio/{pelicula}:
        Retorna duracion y el anio de la pelicula solicitada.

    /franquicia/{franquicia}:
        Retorna la cantidad de peliculas, las ganancias totales y las ganancias promedio de la franquicia solicitada.

    /peliculas_pais/{pais}:
        Retorna la cantidad de peliculas que se estrenaron en el pais solicitado.

    /productoras_exitosas/{productora}:
        Retorna la cantidad de peliculas y sus ganancias totales de la productora solicitada.

    /get_director/{nombre_director}:
        Devuelve en el formato requerido, retorno total del director, lista de peliculas dirigidas, lista de anios de entreno, 
        lista de los retornos, lista de gastos y lista de ganancias de las peliculas dirigidas por este director.
    /recomendacion/{titulo}:
        Esta funcion devuelve 5 peliculas similares a la pelicula brindada.

## Video de demostracion

https://youtu.be/Sz0HeKBaYQ0

## Contacto

pabloszmr@gmail.com
