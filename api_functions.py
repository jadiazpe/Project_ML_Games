
# Definition of the functions to be used by the API
# Five (5) functions are defined below to meet the proposed endpoints
# The input files for the development of the functions are those previously generated in 'Endpoints.ipynb'.

import pandas as pd
import os

# Endpoint 1

# **def PlayTimeGenre( genero : str ):** Debe devolver año con mas horas jugadas para dicho género.
# Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
# Input: **PlayTimeGenre.csv**

def Playtime_Genre(genero: str):
    df = pd.read_csv('./Notebooks/Datasets/api/playtimegenre.csv')

    # Filtrar el DataFrame para el género específico
    df_genre = df[df['genres'] == genero]
    
    # Agrupar por año de lanzamiento y sumar las horas jugadas
    df_genre_grouped = df_genre.groupby('released_year')['hours_game'].sum()
    
    # Encontrar el año con más horas jugadas
    max_hours_year = df_genre_grouped.idxmax()

    # Construye el response_data
    response_data = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_hours_year)}

    # Muestra el resultado
    return response_data