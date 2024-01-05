
# Definition of the functions to be used by the API
# Five (5) functions are defined below to meet the proposed endpoints
# The input files for the development of the functions are those previously generated in 'Endpoints.ipynb'.

import pandas as pd
import os

# Endpoint 1

# def Playtime_Genre(genero : str): Returns the year with the most hours played for input genre.
# Input: playtimegenre.csv

def Playtime_Genre(genero:str):

    df = pd.read_csv('./Notebooks/Datasets/api/playtimegenre.csv')
    df_genre = df[df['genres'] == genero]       # ---> Filter the DataFrame for the required gender
    df_genre_grouped = df_genre.groupby('released_year')['hours_game'].sum()    # ---> Group by year of release, and add up the hours played
    max_hours_year = df_genre_grouped.idxmax()  # ---> Find the year with the most hours played
    response_data1 = {"Release year with the highest number of hours of gameplay for the << {} >> genre is : {}".format(genero, max_hours_year)}

    return response_data1


# Endpoint 2

# def UserForGenre(genero : str): Returns the user who accumulates the most hours played for the given genre, as well as a list of the accumulated hours played per year.
# Input: userforgenre.csv

def Userfor_Genre(genero:str):
    
    df2 = pd.read_csv('./Notebooks/Datasets/api/userforgenre.csv')
    df2_genre = df2[df2['genres'] == genero]       # ---> Filter the DataFrame for the input gender
    top_user = df2_genre.loc[df2_genre['hours_game'].idxmax()]['user_id']     # ---> Find the user with the most hours played for the required genre
    hours_year = df2_genre.groupby('released_year')['hours_game'].sum().reset_index()    # ---> Accumulation list of hours played per year
    hours_year = hours_year.rename(columns={'released_year': 'Year', 'hours_game': 'Hours'})
    hours_list = hours_year.to_dict(orient='records')
    response_data2 = {"The user with the highest number of hours played for the << {} >> genre is".format(genero): top_user, "Played hours": hours_list}

    return response_data2


# Endpoint 3

# def Users_Recommend(año : int): Returns the top 3 most recommended games by users for the given year (recommend = True and reviews = positive/neutral status).
# Input: usersrecommend.csv

def Users_Recommend(year:int):
    df3 = pd.read_csv('./Notebooks/Datasets/api/usersrecommend.csv')
    
    df_year = df3[df3['released_year'] == year]     # ---> Filter the DataFrame for the input year

    response_data3 = [{"Place 1": df_year.iloc[0]['app_name']},
                     {"Place 2": df_year.iloc[1]['app_name']},
                     {"Place 3": df_year.iloc[2]['app_name']}]

    return response_data3
