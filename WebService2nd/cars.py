from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter, vinArray
from DannoService import DannoService

class Car(Resource):
    def __init__(self):
        self.parserCar = reqparse.RequestParser()
        self.parserCar.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parserCar.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parserCar.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parserCar.add_argument('movie details', type=list, required=True, location='json', help="Movie details must be provided")
    def get(self):
        allCars = []
        for car in Cars.values():
            allCars.append(car)
        if len(allCars) is 0:
            return "List is empty", 200
        else:
            return allCars, 200
    
    def post(self):
        args = self.parserCar.parse_args()
        global keyCounter
        keyCounter += 1
        newCar = {
            'car_id':keyCounter,
            'vin':args['vin'],
            'make':args['make'],
            'model':args['model'],
            'movie details':args['movie details']
        }
        if args['vin'] in vinArray:
            keyCounter -= 1
            return "vin number must be unique to the car", 400

        else:               
            response = DannoService().post_movie(args['movie details'])
            if response == "Movie service is down":
                keyCounter -= 1
                return "Movie service is down, can't post new movies", 503
            elif response == 403:
                keyCounter -= 1
                return 'Every movie has its unique EIDR', 403

            Cars[newCar['car_id']] = newCar
            vinArray.append(newCar['vin'])
            return "Succesfully posted car with id: " + str(keyCounter), 201

    def put(self):
        return "Update is not allowed on this page", 400

    def delete(self):
        return "Delete is not allowed on this page", 400