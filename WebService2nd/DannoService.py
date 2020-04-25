import requests
from flask import jsonify

class DannoService:
    def __init__(self):
        self.url = "http://external:9999/"
        #self.url = "http://localhost:9999/"

    def get_all_movies(self):
        movies = []
        try:
            request = requests.get(self.url + 'movies')
            requests.RequestException()
            jsonMovies = request.json()
            body = jsonMovies

            for obj in body:
                movies.append(obj)
            return movies

        except requests.exceptions.RequestException as e:
            return "Movie service is down"

    def post_movie(self, new_movie):
        try:
            for i in range (0, len(new_movie)):
                response = requests.post(self.url + 'movies', json=new_movie[i])
            
            return response.status_code

        except requests.exceptions.RequestException as e:
            return "Movie service is down"

    def put_movie(self, new_movie):

        movies = self.get_all_movies()
        return_code = 404

        try:
            for i in range (0, len(new_movie)):
                for movie in movies:
                    temp_eidr = movie.get('eidr')
                    if temp_eidr == new_movie[i].get('eidr'):
                        return_code = 200
                        response = requests.put(self.url + 'movies/' + str(movie.get('id')), json=new_movie[i])
                        if response.status_code == 403:
                            return 403
            
            return return_code

        except requests.exceptions.RequestException as e:
            return "Movie service is down"


