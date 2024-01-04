
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict
import pandas as pd
from api_functions import Playtime_Genre


# Crea una instancia de la aplicación FastAPI
app = FastAPI()


@app.get("/")
async def root():
    """
    Proyecto FastAPI - Sistema de Recomendaciones

    Versión: 1.0.0

    ---

    """
    return {"Mensaje": "Proyecto Individual - Jairo Díaz"}


# Endpoint 1

@app.get("/Playtime_Genre/{genero}")
async def endpoint1(genero: str):
    """
    Descripción: Retorna el año con más horas jugadas para un género dado.
    
    Parámetros:
        - genero (str): Género para el cual se busca el año con más horas jugadas. Debe ser un string, ejemplo: Action
    
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género Action" : 2012}
    """
    try:
        # Validación adicional para asegurarse de que el género no sea nulo o esté vacío
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = Playtime_Genre(genero)
    
        # Validación para verificar si el género existe en los datos
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo playtimegenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
