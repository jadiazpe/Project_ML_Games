
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict
import pandas as pd
from api_functions import Playtime_Genre, Userfor_Genre, Users_Recommend

app = FastAPI()

@app.get("/")
async def root():
    '''
    System of Recomendation for Video Games
    Release 1.0.0
    '''
    return {"Message": "Individual Project LABS - Jairo Díaz"}


# Endpoint 1

@app.get("/Playtime_Genre/{genero}")
async def endpoint1(genero:str):
    '''
    *---> Description: Return the year with the most hours played for a given genre.
    *---> Parameters:
         genero (str): Genre for which the year with the most hours played is searched. Must be a string, e.g.: Indie.
    *---> Sample of return: {"Release year with the highest number of hours of gameplay for the << X >> genre is : aaaa"}
    '''
    try:
        if not genero or not genero.strip():        # ---> Routine to ensure input is not null or empty
            raise HTTPException(status_code=422, detail="The 'gender' parameter cannot be null or empty.")

        result = Playtime_Genre(genero)
    
        if not result:                              # ---> Routine to check if data exists
            raise HTTPException(status_code=404, detail=f"No information was found for the genre '{genero}'.")

        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file playtimegenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# Endpoint 2
    
@app.get("/Userfor_Genre/{genero}")
async def endpoint2(genero:str):
    '''
    *---> Description: Returns the user who accumulates the most hours played for a given genre, and a list of the accumulation of hours played per year.
    *---> Parameters:
         genero (str): Genre required to search for the user with the most hours played. Must be a string, e.g.: Adventure.
    *---> Sample of return: {"The user with the highest number of hours played for the << X >> genre is": "user", "Played hours":[{Year: xxxx, Hours: xxxx}]}
    '''
    try:
        if not genero or not genero.strip():        # ---> Routine to ensure input is not null or empty
            raise HTTPException(status_code=422, detail="The 'gender' parameter cannot be null or empty.")

        result = Userfor_Genre(genero)
        
        if not result:                              # ---> Routine to check if data exists
            raise HTTPException(status_code=404, detail=f"No information was found for the genre '{genero}'.")
            
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file userforgenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    

# Endpoint 3

@app.get("/Users_Recommend/{year}")
async def endpoint3(year:str):
    '''
    *---> Description: Return to the top 3 most recommended games by users for the given year.
    *---> Parameters:
         year (str): Year for which the top 3 most recommended games are returned. Must be a 4 digit number, e.g.: 2015.
    *---> Sample of return: [{"Place 1" : X}, {"Place 2" : Y},{"Place 3" : Z}]
    '''
    try:
        year = int(year)
    
        if not (2000 <= year <= 2100):
            error_message = f"El año debe estar en el rango entre 2000 y 2100 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})
        
        result = Users_Recommend(year)
    
        if result:
            return result
        else:
            #raise HTTPException(status_code=404, detail=f"No se encontraron recomendaciones para el año {year}.")
            error_message = "No se encontraron recomendaciones para el año {year} {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error al cargar el archivo UsersRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})
    except Exception as e:
        error_message = f"Error interno del servidor: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})