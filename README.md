# Movie Recommender System on Content Based

### The Movie Recommender System on Content Based suggests movies that share similarities with the movie the user enjoys.

The movie details such as title, genre, runtime, rating, poster, etc., are obtained from a database sourced from TMDB (The Movie Database) available at https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata. By utilizing the movie's IMDB ID from the database, I made an API call to fetch the corresponding movie posters. In cases where a movie is not found in the database, I directly searched for its name on TMDB, ensuring its validity. If necessary, I employed web scraping techniques to extract the movie's ID through Google search and subsequently retrieved its detail

<blockquote>
   <b>Note</b>: In the code, I utilized my personal API, which I obtained after creating an account on the https://www.themoviedb.org/ website. To ensure the project functions correctly, please insert your generated API Key from TMDB into the app.py file.
</blockquote>

### API Key Setup
To use the TMDb API for retrieving movie details and posters, you need to obtain an API key. Follow these steps to set up your API key:
1. Visit the [TMDb website](https://www.themoviedb.org/) and sign up for an account if you don't have one.
2. After logging in, go to your account settings and navigate to the "API" section.
3. Create a new API key by following the instructions provided by TMDb.
4. Fill in all the required information to apply for an API key.
5. Once your request is approved, you will find the API key in the API sidebar.
6. Copy the generated API key.
7. Replace the placeholder 'ENTER_YOUR_GENERATED_API_KEY' in the `app.py` code with your API key.

<blockquote>
   <b>Note</b>: If you are not able to create API Key, <a href="https://www.youtube.com/watch?v=mbImkkJFxBs"> click here </a>.
</blockquote>

## Installation
1. Install Python: Download and install Python from the official website (https://www.python.org/) based on your operating system.
2. Install Flask: Open a command prompt or terminal and execute the following command: `pip install flask`
3. Install required libraries: Run the following commands to install the necessary libraries: 'pip install pandas numpy scikit-learn difflib requests bs4 tmdbv3api'
## To set up and run the project, please follow these steps:

1. Clone the repository onto your local system.
2. Locate the app.py file and replace the placeholder "ENTER_YOUR_GENERATED_API_KEY" with your actual API key.
3. Open the command prompt and navigate to your project directory.
4. Execute the command python `app.py` in the command prompt.
5. Finally, open your preferred web browser and enter http://127.0.0.1:8000/ (This is because we have set the PORT:8000 in our `app.py` file. You can use any other port if you want) into the address bar.

## The base of the project, how I find the similar movies
1. Used the `TfidfVectorizer` from the `sklearn.feature_extraction.text` library for making the textual data of movies to the vectorized form, which then used for calculating the similarity score.
2. The similarity score are used for deciding which movies are similar to each other. And for calculating the similarity score, I used `cosine_similarity` from `sklearn.metrics.pairwise` library.
3. Cosine similarity serves as a metric for gauging document similarity, regardless of their respective sizes. In mathematical terms, it quantifies the cosine of the angle formed between two vectors projected in a multi-dimensional space. This metric offers an advantage by considering the orientation of documents rather than solely focusing on their Euclidean distance. Consequently, even if two similar documents are widely separated due to their sizes, there remains a possibility that they are closely aligned. The cosine similarity increases as the angle between the vectors decreases.

## Data Preparation
The movie recommendation system uses a CSV file named movies.csv to store the movie data. This file should contain the following columns: title, genres, keywords, tagline, cast, director, index, and id.

The system starts by importing the necessary libraries and reading the movie data from the CSV file into a Pandas dataframe (data_of_movies). It then selects relevant features for recommendation, namely genres, keywords, tagline, cast, and director.

Next, the system handles any missing values in the selected features by replacing them with empty strings. It combines the selected features into a single string (combined_features) for each movie in the dataframe.

To convert the textual data into vectorized form, the system uses the TF-IDF vectorization technique provided by the `TfidfVectorizer` class from `scikit-learn`. The feature vectors are obtained by calling the fit_transform method on the vectorizer object.

The system also calculates the similarity between movies using cosine similarity. This is achieved by applying the `cosine_similarity` function from scikit-learn on the feature vectors.

## Usage
Once the movie recommendation system is running, you can use it as follows:

1. **Add movie data to the CSV file**: Create a CSV file named "movies.csv" and populate it with movie data. The CSV should contain the following columns: title, genres, keywords, tagline, cast, director, index, and id. The index column represents the index of the movie in the dataset, and the id column corresponds to the movie's ID in the TMDb (The Movie Database) API.
2. Replace the `ENTER_YOUR_GENERATED_API_KEY` placeholder with your TMDb API key in the code. You can obtain an API key by creating an account on the TMDb website.
3. Run the Flask application by executing the following command: `python app.py`
4. Access the web application by opening a web browser and navigating to http://localhost:8000.
5. Enter a movie name in the search bar and click the "Search" button.
6. If the movie name is found in the database, the application displays a list of similar movies based on the selected features (genres, keywords, tagline, cast, director). The movie posters and names are shown on the recommendation page.
7. If the movie name is not found in the database, the application scrapes the TMDb website to find the closest matching movie name and displays the poster and name of the movie.

## Working of the code
The code in the `app.py` file contains explanatory comments to help you understand how it works. You can freely scroll through the file to gain a better understanding of the code. A brief explanation is given below:
1. For making our moviesdata more organized, I used `pandas` library.
2. For user accidentaly typing out wrong movie name, I am using `difflib` library for giving the closest matching result.
3. For making the textual data of movies to the **vectorized** form, I am using `TfidfVectorizer` from the `sklearn.feature_extraction.text` library.
4. For comparing the similarity between the movies name, I am using `cosine_similarity` from `sklearn.metrics.pairwise` library.
5. Then I used `flask` library for creating the web application, and for getting the details of the movie which are not in the database, I am using `requests` and `bs4` library.
6. Then I used `tmdbv3api` library for making the API Call.
7. I started by adding the movie data from a CSV file to a pandas dataframe.
8. Next, I selected relevant features for recommendation, including genres, keywords, tagline, cast and director.
9. To handle missing values, I replaced them with null strings and combined all five selected features.
10. I then converted the textual data of movies into a vectorized form using a feature vectorization technique.
11. Using cosine similarity, I calculated similarity scores for the movies.
12. Afterward, I developed a web application using Flask.
13. When a user enters a movie title, I found the index of the closest matching movie name.
14. Based on the similarity scores, I sorted the movies.
15. Finally, I added the names of similar movies based on their index.

## Web Application
The movie recommendation system includes a web application implemented using the Flask framework. The web application provides two routes:

1. `/`: This is the home route, which renders the `home.html` template. It serves as the landing page for the web application.
2. `/recommend`: This route is responsible for processing the user's movie search query and providing movie recommendations. It retrieves the movie name from the search bar and stores it as movie_name.
   * It then checks if the movie name matches any movie in the database. If a match is found, it retrieves the index of the movie and calculates the similarity scores between the movies based on their indices. The similar movies are sorted based on their similarity scores and the top 12 recommendations are selected.
   * If the movie name is not found in the database, the system attempts to retrieve the movie details using the TMDb API. If the API call is successful, the system fetches the movie's poster and title. If the API call fails, the system scrapes the Google search results to find the closest movie name on the TMDb website and retrieves the corresponding movie details.
   * The movie recommendations, along with their posters, are stored in the `movie_cards` dictionary. The `recommend.html` template is rendered, passing the `movie_cards` dictionary and the `movie_name` as template variables.

## Conclusion
The movie recommendation system implemented in Python using Flask provides users with movie recommendations based on their input. By utilizing machine learning techniques and external APIs, the system can suggest similar movies to users and enhance their movie-watching experience.
