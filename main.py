
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict
import pandas as pd
from api_functions import Playtime_Genre


app = FastAPI()


@app.get("/")
async def root():
    """
    System of Recomendation for Video Games

    Release : 1.0.0

    ---

    """
    return {"Message": "Individual Project - Jairo Díaz"}


# Endpoint 1

@app.get("/Playtime_Genre/{genero}")
async def endpoint1(genero: str):
    """
    ---> Description: Return the year with the most hours played for a given genre.
    ---> Parameters:
         genero (str): Genre of the video game for which the year with the most hours played is searched. Must be a string, example: Indie
    
    ---> Example of return: {"Year of release with more hours played for Action Genre" : 2012}
    """
    try:
        
        if not genero or not genero.strip():        # ---> Routine to ensure input is not null or empty
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = Playtime_Genre(genero)
    
       
        if not result:                              # ---> Routine to check if data exists
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo playtimegenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
