import numpy as np

# For making our data more organized, we are using pandas
import pandas as pd

# If user accidentaly types out wrong movie name, then give the closest matching result
import difflib

# For making the textual data of movies to the vectorized form
from sklearn.feature_extraction.text import TfidfVectorizer

# For comparing the similarity between the movies name
from sklearn.metrics.pairwise import cosine_similarity

# ########################################################################
# The libraries used for creating the web application
from flask import Flask, render_template, request
import json
import requests
# ########################################################################

# ########################################################################
# For getting the details of the movie which are not in the database
import requests
import bs4
headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# ########################################################################

# ########################################################################
# This code is for API Call of TMDb
from tmdbv3api import TMDb
from tmdbv3api import Movie
tmdb = TMDb()
tmdb_movie_name = Movie()
tmdb.api_key = 'ENTER_YOUR_GENERATED_API_KEY'
# ########################################################################

# Adding the movies data from csv file to the pandas dataframe
data_of_movies = pd.read_csv('movies.csv')

# Here selecting the relevant features for recommendation
features_selected = ['genres','keywords','tagline','cast','director']

# Here replacing the null valuess with null string
for feature in features_selected:
    data_of_movies[feature] = data_of_movies[feature].fillna('')

# combining all the 5 selected features
combined_features = data_of_movies['genres']+' '+data_of_movies['keywords']+' '+data_of_movies['tagline']+' '+data_of_movies['cast']+' '+data_of_movies['director']

#  For making the textual data of movies to feature vectorized form
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Using cosine similarity function to get similarity scores
similarity = cosine_similarity(feature_vectors)

# ########################################################################
# The following code for creating the web application
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    # Getting the movie name from the search bar
    movie = request.args.get('movie') 
    
    # Storing the movie name from the user
    movie_name = movie

    # Creating a list with all the movie names given in the dataset
    list_of_all_titles = data_of_movies['title'].tolist()

    #  If user accidentaly types out wrong movie name, then give the closest matching movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    # If the movie is present in the our database
    if(len(find_close_match) != 0):
        close_match = find_close_match[0]

        # finding the index of the movie with title
        index_of_the_movie = data_of_movies[data_of_movies.title == close_match]['index'].values[0]

        # getting a list of similar movies
        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        # sorting the movies based on their similarity score
        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

        # The following code adds the name of similar movies based on the index
        i = 1

        id_list_from_index = []
        similar_movies_found_from_index = []
        similar_movies_posters = []

        for movie in sorted_similar_movies:
            index = movie[0]
            if (i<13):
                movies_id = data_of_movies[data_of_movies.index==index]['id'].values[0]
                id_list_from_index.append(movies_id)
                similar_movies_found_from_index.append(data_of_movies[data_of_movies.index==index]['title'].values[0])
                
                # Used tmdb api to get the posters of the movies using movie id
                response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movies_id,tmdb.api_key))
                data_json = response.json()
                similar_movies_posters.append('https://image.tmdb.org/t/p/original{}'.format(data_json['poster_path']))
                
                i+=1
    
    # Else the data will be scrapped from the original website
    else:
        # If the user enters correct movie name
        if(len(tmdb_movie_name.search(movie_name)) != 0):
            movie_id = tmdb_movie_name.search(movie_name)[0].id

        # Else it will be scrape the google search for getting the closest movie name on the tmdb website
        else:
            # Following code is for scraping the movie id from tmdb
            soup = bs4.BeautifulSoup(requests.get('https://google.com/search?q=' + movie_name + ' tmdb').text, "html.parser")
            linka = []
            for link in soup.find_all('a'):
                if(link.get('href')[0:4] == '/url'):
                    linka.append(link.get('href'))
            id_of_new_movie = (linka[0])[40:]
                
            movie_id = ''
            for a in id_of_new_movie:
                if(a == '-'):
                    break
                movie_id += a
            
        similar_movies_found_from_index = []
        similar_movies_posters = []
        
        # Used tmdb api to get the posters and the name of the movies
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
        data_json = response.json()
        similar_movies_posters.append('https://image.tmdb.org/t/p/original{}'.format(data_json['poster_path']))
        similar_movies_found_from_index.append(format(data_json['title']))
    
    # Creating a dictionary movie_cards which contains movie name along with their posters
    movie_cards = {similar_movies_posters[i]: similar_movies_found_from_index[i] for i in range(len(similar_movies_found_from_index))}
    
    return render_template('recommend.html', cards = movie_cards, movie_name = movie_name)
    
# The following code runs the web app on the 'PORT: 8000'
if __name__ == '__main__':
    app.run(debug=True, port=8000)