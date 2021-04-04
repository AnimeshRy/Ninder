from flask import Flask, render_template
import csv
import random
import requests
import dotenv
import os

from requests import api

dotenv.load_dotenv()

app = Flask(__name__)

apiKey = str(os.getenv('omdpKey'))


@app.route("/")
def home():
    # randomly select a movie
    with open('catalog.csv') as f:
        reader = csv.reader(f)
        row = random.choice(list(reader))

    movie = {
        'id': row[0],
        'category': row[1],
        'title': row[2],
        'director': row[3],
        'cast': row[4],
        'country': row[5],
        'date_added': row[6],
        'release_year': row[7],
        'maturity': row[8],
        'duration': row[9],
        'genre': row[10],
        'description': row[11],
        # default poster just so we see something
        'image': 'https://live.staticflickr.com/4422/36193190861_93b15edb32_z.jpg',
        'imdb': 'Not Available'
    }

    print(apiKey)
    # fetch cover image
    # call OMDB database
    url = f"http://www.omdbapi.com/?t={movie['title']}/&apikey={apiKey}"
    # get back the response
    response = requests.request("GET", url)
    # parse result into JSON and look for matching data if available
    movie_data = response.json()
    if 'Poster' in movie_data:
        movie['image'] = movie_data['Poster']
    if 'imdbRating' in movie_data:
        movie['imdb'] = movie_data['imdbRating']
    # send all this data to the home.html template
    return render_template("index.html", movie=movie)


if __name__ == "__main__":
    app.run(debug=True)
