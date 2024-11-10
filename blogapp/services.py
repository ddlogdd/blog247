import requests
from .models import News, Forex, Stock, Sports, Movie
from datetime import datetime

# Example API Keys (replace with actual keys)
NEWS_API_KEY = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=your_news_api_key'
MOVIE_API_KEY = 'https://api.themoviedb.org/3/movie/popular?api_key=your_movie_api_key&language=en-US'
FOREX_API_KEY = 'https://v6.exchangerate-api.com/v6/your_forex_api_key/latest/USD'

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    for article in data.get('articles', []):
        News.objects.create(
            title=article['title'],
            description=article['description'],
            image_url=article['urlToImage'],
            published_at=datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
            source=article['source']['name']
        )

def fetch_forex():
    url = f'https://someforexapi.com/latest?apiKey={FOREX_API_KEY}'
    response = requests.get(url)
    data = response.json()

    for pair, rate in data.get('rates', {}).items():
        Forex.objects.create(
            currency_pair=pair,
            rate=rate,
            updated_at=datetime.now()
        )


def fetch_movies():
    url = f'https://some-movie-api.com/popular?api_key={MOVIE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    for movie in data.get('results', []):
        Movie.objects.create(
            title=movie['title'],
            description=movie['overview'],
            release_date=datetime.strptime(movie['release_date'], '%Y-%m-%d'),
            poster_url=movie['poster_path']
        )
