# Movie Recommender System on Content Based

### The Movie Recommender System on Content Based suggests movies that share similarities with the movie the user enjoys.

The movie details such as title, genre, runtime, rating, poster, etc., are obtained from a database sourced from TMDB (The Movie Database) available at https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata. By utilizing the movie's IMDB ID from the database, I made an API call to fetch the corresponding movie posters. In cases where a movie is not found in the database, I directly searched for its name on TMDB, ensuring its validity. If necessary, I employed web scraping techniques to extract the movie's ID through Google search and subsequently retrieved its detail

<blockquote>
   <b>Note</b>:In the code, I utilized my personal API, which I obtained after creating an account on the https://www.themoviedb.org/ website. To ensure the project functions correctly, please insert your generated API Key from TMDB into the app.py file.
</blockquote>

### Steps for getting the API KEY
1. Register an account on https://www.themoviedb.org/.
2. Access your account settings and navigate to the left-hand sidebar.
3. Click on the API link.
4. Fill in all the required information to apply for an API key.
5. Once your request is approved, you will find the API key in the API sidebar.

<blockquote>
   <b>Note</b>:If you are not able to create API Key, <a href="https://www.youtube.com/watch?v=mbImkkJFxBs"> click here </a>.
</blockquote>

### To set up and run the project, please follow these steps:

1. Clone the repository onto your local system.
2. Begin by installing `Flask` using the command `pip install flask`.
3.  Also install the `tmdbv3api` library using `pip install tmdbv3api`.
4. Locate the app.py file and replace the placeholder "ENTER_YOUR_GENERATED_API_KEY" with your actual API key.
5. Open the command prompt and navigate to your project directory.
6. Execute the command python `app.py` in the command prompt.
7. Finally, open your preferred web browser and enter http://127.0.0.1:8000/ (This is because we have set the PORT:8000 in our `app.py` file. You can use any other port if you want) into the address bar.

## The base of the project, how I find the similar movies
1. Used the `TfidfVectorizer` from the `sklearn.feature_extraction.text` library for making the textual data of movies to the vectorized form, which then used for calculating the similarity score.
2. The similarity score are used for deciding which movies are similar to each other. And for calculating the similarity score, I used `cosine_similarity` from `sklearn.metrics.pairwise` library.
3. Cosine similarity serves as a metric for gauging document similarity, regardless of their respective sizes. In mathematical terms, it quantifies the cosine of the angle formed between two vectors projected in a multi-dimensional space. This metric offers an advantage by considering the orientation of documents rather than solely focusing on their Euclidean distance. Consequently, even if two similar documents are widely separated due to their sizes, there remains a possibility that they are closely aligned. The cosine similarity increases as the angle between the vectors decreases.

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
