from flask import Flask, render_template
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/", methods=['GET'])
def all_cities():
    all_cities_not_visited = city_repository.select_all_not_visited()
    all_cities_visited = city_repository.select_all_visited() 
    return render_template("index.html", all_cities_visited = all_cities_visited, all_cities_not_visited = all_cities_not_visited)

@cities_blueprint.route("/cities/not_visited", methods=['GET'])
def cities_not_visited():
    all_cities_not_visited = city_repository.select_all_not_visited()
    return render_template("/cities/not_visited.html", all_cities_not_visited = all_cities_not_visited)

@cities_blueprint.route("/cities/visited", methods=['GET'])
def cities_visited():
    all_cities_visited = city_repository.select_all_visited()
    return render_template("/cities/visited.html", all_cities_visited = all_cities_visited)

@cities_blueprint.route("/cities/new", methods = ['GET'])
def new_city():
    return render_template("cities/new.html")

