from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter, vinArray
from DannoService import DannoService

class CarById(Resource):
    def __init__(self):
        self.parserCar = reqparse.RequestParser()
        self.parserCar.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parserCar.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parserCar.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parserCar.add_argument('movie details', type=list, required=True, location='json', help="Movie details must be provided")


    def get(self, car_id):
        if car_id not in Cars:
            return "No car found by provided id", 404
        else:
            return Cars[car_id], 200
    
    def post(self, car_id):
        return "Posting is not allowed on this page", 400

    def put(self, car_id):
        if car_id not in Cars:
            return "Wrong car id provided", 404
        else:
            args = self.parserCar.parse_args()
            tempVin = Cars[car_id].get('vin')
            vinArray.remove(tempVin)
            updateCar = {
                'car_id':car_id,
                'vin':args['vin'],
                'make':args['make'],
                'model':args['model'],
                'movie details':args['movie details']
            }
            if args['vin'] in vinArray:
                vinArray.append(tempVin)
                return "vin number must be unique to the car", 400

            else:
                response = DannoService().put_movie(args['movie details'])
                if response == "Movie service is down":
                    vinArray.append(tempVin)
                    return "Movie service is down, can't post new movies", 503

                elif response == 404:
                    vinArray.append(tempVin)
                    return 'Could not find movie with given EIDR', 404

                Cars[car_id] = updateCar
                vinArray.append(args['vin'])
                return "Succesfully updated car with id: " + str(car_id), 200  

    def delete(self, car_id):
        if car_id not in Cars:
            return "Wrong car id provided", 404
        else:
            Cars.pop(car_id)
            return "Succesfully deleted car with id: " + str(car_id), 200
