
# Definition of the functions to be used by the API
# Five (5) functions are defined below to meet the proposed endpoints
# The input files for the development of the functions are those previously generated in 'Endpoints.ipynb'.

import pandas as pd
import os

# Endpoint 1

# def Playtime_Genre( genero : str ): Returns the year with the most hours played for that genre.
# Example return: {"Year of release with most hours played for Genre X" : 2013}
# Input: playtimegenre.csv

def Playtime_Genre(genero: str):
    df = pd.read_csv('./Notebooks/Datasets/api/playtimegenre.csv')

    df_genre = df[df['genres'] == genero]       # ---> Filter the DataFrame for the required gender
    
    df_genre_grouped = df_genre.groupby('released_year')['hours_game'].sum()    # ---> Group by year of release, and add up the hours played
    
    max_hours_year = df_genre_grouped.idxmax()  # ---> Find the year with the most hours played

    response_data = {"Year of release with most hours played for {}: {}".format(genero, max_hours_year)}

    return response_data