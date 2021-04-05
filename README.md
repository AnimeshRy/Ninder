# Ninder - 'Tinder' for Netflix 🍿

A Flask app that generates random movie recommendations, with details listed for each title, that a user can swipe through and watch with the click of a button.

![app demo](/demo.gif)

## Installation
1. Install using `requirements.txt` or using `pipenv`

    ```$ pip install -r requirements.txt```
    ```$ pipenv install ```

2. Obtain an API Key for OMDB, and add it to your environment file using the following format:

    ```
    export omdbKey="YOUR_KEY"
    ```

3. Download the CSV linked in [this Kaggle dataset](https://www.kaggle.com/shivamb/netflix-shows) and name the file `catalog.csv`. This will store the bulk of our data.


## Usage
#### To launch the app:
    $ python main.py

Once the Flask app is running, navigate to the `localhost` link provided:

<code> * Running on <b>http://127.0.0.1:5000/</b> (Press CTRL+C to quit)</code>


## Thanks

* [Open Movie Database](http://www.omdbapi.com/) - Movie data API to fetch movie poster links and IMDB scores
* [Kaggle Netflix Dataset](https://www.kaggle.com/shivamb/netflix-shows) - Comprehensive dataset with many Netflix movies/tv shows and their metadata

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE) file for details.