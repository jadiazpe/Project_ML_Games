
# Definition of the functions to be used by the API
# Five (5) functions are defined below to meet the proposed endpoints
# The input files for the development of these functions were previously generated by the 'Endpoints.ipynb' file.

import pandas as pd
import os

# Endpoint 1

# def PlayTimeGenre(genre : str): Returns the year with the most hours played for input genre.
# Input: playtimegenre.csv

def PlayTimeGenre(genre:str):

    df = pd.read_csv('./Notebooks/Datasets/api/playtimegenre.csv')
    genre = genre.capitalize()
    df_genre = df[df['genres'] == genre]       # ---> Filter the DataFrame for the required gender
    df_genre_grouped = df_genre.groupby('released_year')['hours_game'].sum()    # ---> Group by year of release, and add up the hours played
    max_hours_year = df_genre_grouped.idxmax()  # ---> Find the year with the most hours played
    response_data1 = {"Release year with the highest number of hours of gameplay for the << {} >> genre is : {}".format(genre, max_hours_year)}

    return response_data1


# Endpoint 2

# def UserForGenre(genre : str): Returns the user who accumulates the most hours played for the given genre, as well as a list of the accumulated hours played per year.
# Input: userforgenre.csv

def UserForGenre(genre:str):
    
    df2 = pd.read_csv('./Notebooks/Datasets/api/userforgenre.csv')
    genre = genre.capitalize()
    df2_genre = df2[df2['genres'] == genre]       # ---> Filter the DataFrame for the input gender
    top_user = df2_genre.loc[df2_genre['hours_game'].idxmax()]['user_id']     # ---> Find the user with the most hours played for the required genre
    hours_year = df2_genre.groupby('released_year')['hours_game'].sum().reset_index()    # ---> Accumulation list of hours played per year
    hours_year = hours_year.rename(columns={'released_year': 'Year', 'hours_game': 'Hours'})
    hours_list = hours_year.to_dict(orient='records')
    response_data2 = {"The user with the highest number of hours played for the << {} >> genre is".format(genre): top_user, "Played hours": hours_list}

    return response_data2


# Endpoint 3

# def UsersRecommend(year : int): Returns the top 3 most recommended games by users for the given year (recommend = True and reviews = positive/neutral status).
# Input: usersrecommend.csv

def UsersRecommend(year:int):
    df3 = pd.read_csv('./Notebooks/Datasets/api/usersrecommend.csv')
    
    df_year3 = df3[df3['released_year'] == year]     # ---> Filter the DataFrame for the input year

    response_data3 = [{"Place 1": df_year3.iloc[0]['app_name']},
                     {"Place 2": df_year3.iloc[1]['app_name']},
                     {"Place 3": df_year3.iloc[2]['app_name']}]

    return response_data3


# Endpoint 4

# def UsersWorstDeveloper(year : int): Returns the top 3 developers with the least recommended games by users for the given year (recommend = False and reviews = negative status)
# Input: worstdeveloper.csv

def UsersWorstDeveloper(year:int):
    df4 = pd.read_csv('./Notebooks/Datasets/api/worstdeveloper.csv')

    df_year4 = df4[df4['released_year'] == year]          # ---> Filter the DataFrame for the input year
    
    response_data4 = [{"Place 1": df_year4.iloc[0]['developer']},
                    {"Place 2": df_year4.iloc[1]['developer']},
                    {"Place 3": df_year4.iloc[2]['developer']}]
    
    return response_data4


# Endpoint 5

# def Sentiment_Analysis(developer : str): Returns a dictionary with the name of the developer entered as a key and a list of the total number of user review records categorized by sentiment analysis. 
# Input: sentiment_analysis.csv

def Sentiment_Analysis(developer:str):
    df5 = pd.read_csv('./Notebooks/Datasets/api/sentiment_analysis.csv')
    developer = developer.capitalize()
    df_sentiment = df5[df5['developer'] == developer]    # ---> Filter the DataFrame for the input developer

    response_data5 = df_sentiment.set_index('developer').to_dict(orient='index')
    
    return response_data5


# ML - Recommendation: item-item

'''
def Game_Recommendation(item_id):
    df_ml = pd.read_csv('./Notebooks/Datasets/ml/recomienda_item_item.csv')       
    
    df_ml1 = df_ml[df_ml['item_id'] == item_id]            # ---> Filter the DataFrame for the input 'item-id'
    
    response_data_ml = df_ml1['Recomendaciones']
 
    return response_data_ml
'''