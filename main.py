
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict
import pandas as pd
from api_functions import PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, Sentiment_Analysis, Recommendation_Item

app = FastAPI()

@app.get("/", tags=["System of Recomendation for Video Games"])
async def root():
    '''
    System of Recomendation for Video Games
    | STEAM-PROJECT 
    | JD Labs
    '''
    return {"Message" : "Individual Project LABS - Jairo Díaz"}


# -------- Endpoint 1

@app.get("/PlayTimeGenre/{genre}", tags=["Endpoint 1 : PlayTimeGenre"])
async def endpoint1(genre:str):
    '''
    |---| "Description": Return the year with the most hours played for a given genre.
    
    |---| "Parameters (input)":
          <genre (str)>: Must be a string, e.g.: Indie.
    
    |---| "Sample of return": {"Release year with the highest number of hours of gameplay for the << X >> genre is : aaaa"}
    '''
    try:
        if not genre or not genre.strip():        # ---> Routine to ensure input is not null or empty
            raise HTTPException(status_code=422, detail="The 'gender' parameter cannot be null or empty.")

        result = PlayTimeGenre(genre)
    
        if not result:                              # ---> Routine to check if data exists
            raise HTTPException(status_code=404, detail=f"No information was found for the genre '{genre}'.")
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file playtimegenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# -------- Endpoint 2
    
@app.get("/UserForGenre/{genre}", tags=["Endpoint 2 : UserForGenre"])
async def endpoint2(genre:str):
    '''
    |---| "Description": Returns the user who accumulates the most hours played for a given genre, and a list of the accumulation of hours played per year.
    
    |---| "Parameters (input)":
          <genre (str)>: Must be a string, e.g.: Adventure.
    
    |---| "Sample of return": {"The user with the highest number of hours played for the << X >> genre is": "user", "Played hours":[{Year: xxxx, Hours: xxxx}]}
    '''
    try:
        if not genre or not genre.strip():        # ---> Routine to ensure input is not null or empty
            raise HTTPException(status_code=422, detail="The 'gender' parameter cannot be null or empty.")

        result = UserForGenre(genre)
        
        if not result:                              # ---> Routine to check if data exists
            raise HTTPException(status_code=404, detail=f"No information was found for the genre '{genre}'.")      
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file userforgenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    

# -------- Endpoint 3

@app.get("/UsersRecommend/{year}", tags=["Endpoint 3 : UserRecommend"])
async def endpoint3(year:int):
    '''
    |---| "Description": Return to the top 3 most recommended games by users for the given year (range: 2006 <= year <= 2017).
    
    |---| "Parameters (input)":
          <year (int)>: Must be a 4 digit number, e.g.: 2009.
    
    |---| "Sample of return": [{"Place 1" : X}, {"Place 2" : Y},{"Place 3" : Z}]
    '''
    try:
        year = int(year)
    
        if not (2006 <= year <= 2017):
            error_message = f"the year of entry must be between 1993 and 2017 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})
        
        result = UsersRecommend(year)
    
        if result:
            return result
        else:
            error_message = "No information was found for the year {year} {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error loading file UsersRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})
    except Exception as e:
        error_message = f"Internal server error: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})
    

# -------- Endpoint 4

@app.get("/UsersWorstDeveloper/{year}", tags=["Endpoint 4 : UserWorstDeveloper"])
async def endpoint4(year:int):
    '''
    |---| "Description": Returns the top 3 developers with the least recommended games by users for the given year (range: 2006 <= year <= 2017).
    
    |---| "Parameters (input)":
          <year (int)>: Must be a 4 digit number, e.g.: 2011.
    
    |---| "Sample of return": [{"Place 1" : X}, {"Place 2" : Y},{"Place 3" : Z}]
    '''
    try:
        year = int(year)

        if not (2006 <= year <= 2017):
            error_message = f"the year of entry must be between 2003 and 2017 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

        result = UsersWorstDeveloper(year)
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file worstdeveloper.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    

# -------- Endpoint 5

@app.get("/Sentiment_Analysis/{developer}", tags=["Endpoint 5 : Sentiment_Analysis"])
async def enpoint5(developer:str):
    '''
    |---| "Description": Returns a dictionary with the name of the developer entered as a key and a list of the total number of user review records categorized by sentiment analysis.
    
    |---| "Parameters (input)":
          <developer (str)>: Name of the developer company for which the sentiment analysis is performed. Must be a string, e.g.: Valve
    
    |---| "Sample of return": {'Valve' : [Negative = xxxx, Neutral = xxxx, Positive = xxxx]}
    '''
    try:
        result = Sentiment_Analysis(developer)
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error loading file sentiment_analysis.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

   
# -------- ML - Recommendation: item-item

@app.get("/Recommendation_Item/{item_id}", tags=["<<< Recommended Games based on the ITEM ID >>>"])
async def item(item_id: int):
    """
    |---| "Description": Returns a list of the 5 recommended games that are similar to the entered title.
    
    |---| "Parameters (input)":
          item_id (int): Must be a number, e.g.: 63700
    
    |---| "Sample of return": "['Runespell: Overture', 'Rush for Glory', 'Bridge Constructor', 'rymdkapsel', 'Defense Zone 2']"
    """
    try:
        item_id = int(item_id) 
        result= Recommendation_Item(item_id)  
        return result
    
    except Exception as e:
        return {"error":str(e)}
