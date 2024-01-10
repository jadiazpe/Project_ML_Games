![jd_matrix200](https://github.com/jadiazpe/Project_ML_Games/raw/main/src_img/jd_matrix200.png)
 [By Jairo Díaz](https://www.linkedin.com/in/jairoadiaz/)

<br />

#
# VIDEO GAME RECOMMENDATION SYSTEM FOR STEAM USERS

### About STEAM
STEAM is a digital video game distribution platform developed by Valve Corporation, which allows users to purchase, download and play a wide variety of games online. In addition to being a game store, STEAM also offers social and community features, such as chats, groups and the ability to share personalized content.

### The Project
STEAM has enlisted the expertise of JD Labs to create an automated game recommendation system. The company will supply the necessary source information, with JD Labs tasked to handle all essential project processes, including ETL (Extract, Transform, Load), EDA (Exploratory Data Analysis), API development, and web deployment. Our objective is to deliver a Minimum Viable Product (MVP) capable of providing STEAM users with a game recommendation system based on specific criteria.

### Objectives
1. Perform ETL analysis
2. Perform EDA analysis
3. Create functions and the ML model that will be consumed by the API
4. Implement FastAPI to visualize the data 
5. Deploy FastAPI on the Internet using the RENDER application

<br />

#
# PROJECT STAGES
![steamstages](https://github.com/jadiazpe/Project_ML_Games/raw/main/src_img/Steamstages.png)
<br />

## I. Development <br />
### I.1 Extraction, Transformation and Load (ETL) <br />

The source files provided by STEAM are three (3) and come in JSON formats (all can be accessed via Google Drive, just click on them):
- [australian_user_items.json](https://drive.google.com/drive/folders/10mZQbzMeA77nXgndqvJDuaFTcRqud0WB?usp=sharing)
- [australian_user_reviews.json](https://drive.google.com/drive/folders/10mZQbzMeA77nXgndqvJDuaFTcRqud0WB?usp=sharing)
- [output_steam_games.json](https://drive.google.com/drive/folders/10mZQbzMeA77nXgndqvJDuaFTcRqud0WB?usp=sharing)

After the ETL processes (see files [ETL_items](Notebooks/ETL_items.ipynb), [ETL_reviews](Notebooks/ETL_reviews.ipynb), [ETL_games](Notebooks/ETL_games.ipynb)), four (4) CSV files were obtained with clean data that will be consumed by the API (all can be accessed via Google Drive, just click on them):

- [items.csv](https://drive.google.com/drive/folders/12wM7n_ZeL0tVI9J08CCMI7L2-yQHOGbI?usp=sharing)
- [reviews.csv](https://drive.google.com/drive/folders/12wM7n_ZeL0tVI9J08CCMI7L2-yQHOGbI?usp=sharing)
- [games.csv](https://drive.google.com/drive/folders/12wM7n_ZeL0tVI9J08CCMI7L2-yQHOGbI?usp=sharing)
- [reviews_sa.csv](https://drive.google.com/drive/folders/12wM7n_ZeL0tVI9J08CCMI7L2-yQHOGbI?usp=sharing)
  
  ---> The file `reviews_sa.csv` was specially created to perform sentiment analysis of user reviews (Feature Engineering). The `NLTK (Natural Language Toolkit)` library was used for this purpose with the `Vader Sentiment Analyzer`, which provides an ideal composite score to classify the polarity of the reviews into negative (value '0'), neutral (value '1') or positive (value '2'). Reviews written by absent users were assigned a value of "1". To see details, pls. check the notebook: [Sentiment_analysis](Notebooks/Sentiment_analysis.ipynb)
<br />

### I.2 Exploration Data Analysis (EDA) <br />

While some EDA routines were conducted during the ETL studies, this section specifically involved more in-depth analyses in the following areas: occurrence statistics, variable distribution, relationships between variables, outlier detection, and trend analysis. For further details, please refer to the notebook [EDA](Notebooks/EDA.ipynb).
<br />

### I.3 Functions and ML model <br />
### * Functions

The functions that make up the body of the API were generated to respond promptly to the proposed endpoints. The source data that feed these functions are:
- [playtimegenre.csv](Notebooks/Datasets/api/playtimegenre.csv)
- [userforgenre.csv](Notebooks/Datasets/api/userforgenre.csv)
- [usersrecommend.csv](Notebooks/Datasets/api/usersrecommend.csv)
- [usersworstdeveloper.csv](Notebooks/Datasets/api/usersworstdeveloper.csv)
- [sentiment_analysis.csv](Notebooks/Datasets/api/sentiment_analysis.csv)
- [item_item_recommendation.csv](Notebooks/Datasets/ml/item_item_recommendation.csv)

All these files were obtained from the notebook [Endpoints](Notebooks/Endpoints.ipynb).

The code that will be consumed by the API is contained in the python file [api_functions](api_functions.py), such file contains the functions that respond to:

- **Endpoint 1 (PlayTimeGenre)**: Returns the year with the most hours played for a given genre.
- **Endpoint 2 (UserForGenre)**: Returns the user with the most hours played for the given genre and a list of the accumulation of hours played per year.
- **Endpoint 3 (UsersRecommend)**: Returns the top three (3) most recommended games by users for the given year.
- **Endpoint 4 (UsersWorstDeveloper)**: Returns the top three (3) developers with the least recommended games by users for the given year.
- **Endpoint 5 (Sentiment_analysis)**: According to the developer company, a dictionary is returned with the name of the developer as key and a list with the total amount of user review records that are categorized with sentiment analysis as value.

### * ML Model | Item-to-item recommendation system

- **Description**: This model recommends five (5) games that are similar to the game title entered through the console. For this particular routine, the entered title is the ID, an integer number e.g. 32500, which identifies the game in the database.

- **Methodology**: The CountVectorizer, Cosine Similarity, and the source file games_raw.csv will be employed in this process.

  In a first step, CountVectorizer is used to convert the text in the 'specs' column into vectors for numerical calculations. Subsequently, by defining the 'Recommendations' function and utilizing cosine similarity metrics, the target dataset is analyzed to obtain the recommended games. In order to fine-tune the recommendation system, five successive tests were conducted with 500, 1.000, 4.000, 8.000, and 15.000 records extracted from the source file. To see details, pls. check the notebook: [item_item](Notebooks/item_item.ipynb). 
  
  <br />


## II. Deployment <br />

Once the datasets and functions have been tested, FastAPI consumes the information through the [main](main.py) file. This file initializes all decorators, enabling the visualization of endpoints and the recommendation system, both locally and over the internet.

To see the MVP running with RENDER on the internet, click on [DEPLOY](https://project-ml-games.onrender.com/docs).

<br />
<br />

## >>>

### About the STEAM Project folders in GitHub<br />

**[[/Notebooks]](Notebooks/):** Directory housing the Jupyter notebooks containing ETL, EDA, the Feature Engineering exercise, as well as the outputs from the Endpoints and game recommendations; ETL_games.ipynb, ETL_items.ipynb, ETL_reviews.ipynb, Sentiment_analysis.ipynb, Endpoints.ipynb, item_item.ipynb
<br />

**[[/Notebooks/Datasets/api]](/Notebooks/Datasets/api/):** Directory housing the CSV files consumed by the functions that make the API operational; playtimegenre.csv, sentiment_analysis.csv, userforgenre.csv, usersrecommend.csv, worstdeveloper.csv
<br />

**[[/Notebooks/Datasets/ml]](/Notebooks/Datasets/ml):** Directory housing the CSV file consumed by ML function that makes the recommendation system operational; item_item_recommendation.csv
<br />

**[[/src_img]](assets/):** Directory housing the PNG files used to illustrate the repository contents; jd_matrix200.png, Steamstages.png<br />

