# Car Movies WebService

Possibilities:
- Get all records of the cars that starred in movie or movies that are currently shown at the theatre
- Create a record for a car that is starring in movie or movies
- Update information about the car that is starring in movie or movies
- Delete a record of car that is starring in movie or movies

Build and start:
- ./run.sh

or:
- cd WebService2nd/Danno 
- docker-compose up --build -d
- cd .. 
- docker-compose up --build -d

Stop:
- ./stop.sh

View: 
- localhost:80/cars/<car_id>
- localhost:80/cars
