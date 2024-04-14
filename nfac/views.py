import requests
from django.core.paginator import Paginator
from django.shortcuts import render
from base64 import b64encode
from .services import convert_id


class BasicAuthToken(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        authstr = 'Basic ' + b64encode(('token:' + self.token).encode('utf-8')).decode('utf-8')
        r.headers['Authorization'] = authstr
        return r





def search_movies(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        url = f'https://omdbapi.com/?s={search_term}&page=1&apikey=59963625'
        response = requests.get(url)
        data = response.json()
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
            return render(request, 'movie_catalogue/search_results.html', {'movies': movies})
    return render(request, 'movie_catalogue/search_results.html', {'movies': []})


def mdtb_movie_details(request, id):
    id = convert_id(id)
    url = f'http://www.omdbapi.com/?i={id}&apikey=fc1fef96'
    response = requests.get(url)
    movie_details = response.json()
    return render(request, 'movie_catalogue/movie_details.html', {'movie_details': movie_details})


def movie_details(request, imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey=fc1fef96'
    response = requests.get(url)
    movie_details = response.json()
    return render(request, 'movie_catalogue/movie_details.html', {'movie_details': movie_details})




def index(request):
    genres = {"Action": 28, "Adventure": 12, "Animation": 16, "Comedy": 35}
    genre_movies = {}
    for genre, genre_id in genres.items():
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1" \
              f"&sort_by=popularity.desc&with_genres={genre_id}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGNmNWFmYjlkNmIxMmU0OGRjYjMxMDRiYTY3MGVlYyIsInN1YiI6IjY2MWFlZmFlYWY5NTkwMDE2MzVmYmFlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.R0Smw_XO2kMVnqGxhDPGNm_JS0WbY64vDqksMlLSa30"
        }
        response = requests.get(url, headers=headers)
        data = response.json().get('results')[:5]
        genre_movies[genre] = data

    return render(request, 'movie_catalogue/index.html', {'genre_movies': genre_movies})


def catalogue(request):
    genres = {"Action": 28, "Adventure": 12, "Animation": 16, "Comedy": 35, "Horror": 27, "Science Fiction": 878}
    genres_list = genres.keys()
    if request.method == 'POST':
        genre = request.POST.get('selected_genre')

        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1" \
              f"&sort_by=popularity.desc&with_genres={genres[genre]}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGNmNWFmYjlkNmIxMmU0OGRjYjMxMDRiYTY3MGVlYyIsInN1YiI6IjY2MWFlZmFlYWY5NTkwMDE2MzVmYmFlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.R0Smw_XO2kMVnqGxhDPGNm_JS0WbY64vDqksMlLSa30"
        }
        response = requests.get(url, headers=headers)
        movies = response.json().get('results')
        return render(request, 'movie_catalogue/catalogue.html', {"genres_list": genres_list, "movies": movies})

    return render(request, 'movie_catalogue/catalogue.html', {"genres_list": genres_list})
