from flask.wrappers import Response
from movie_model import MovieModel
import requests

def callMovieApi():
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json()
    movies = responseDict["data"]["movies"]
    return convert_model(movies)

def convert_model(movies):
    list = []
    for movie in movies:
        movie_model = MovieModel(movie["title"],movie["rating"],movie["summary"],movie["small_cover_image"])
        list.append(movie_model)
        print(type(movie["title"]))
        print(type(movie["rating"]))
        print(type(movie["summary"]))
        print(type(movie["small_cover_image"]))
    return list

