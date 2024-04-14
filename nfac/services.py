import requests

def convert_id(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/external_ids"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGNmNWFmYjlkNmIxMmU0OGRjYjMxMDRiYTY3MGVlYyIsInN1YiI6IjY2MWFlZmFlYWY5NTkwMDE2MzVmYmFlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.R0Smw_XO2kMVnqGxhDPGNm_JS0WbY64vDqksMlLSa30"
    }
    response = requests.get(url, headers=headers)
    data = response.json()['imdb_id']


    return(data)



