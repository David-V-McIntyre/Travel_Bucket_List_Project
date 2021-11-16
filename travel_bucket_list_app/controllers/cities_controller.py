from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
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

@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    city_name       = request.form['city_name']
    visited         = request.form['visited']
    country         = Country(request.form['country_name'])
    country_repository.save(country)
    city            = City(city_name, country, visited)
    city_repository.save(city)
    return redirect('/')




@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)


@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    countries = country_repository.select_all()
    city = city_repository.select(id)
    return render_template('cities/edit.html', city = city, all_countries = countries)

@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    city_name       = request.form['city_name']
    country_id      = request.form['country_name']    
    visited         = request.form['visited']
    country         = country_repository.select(country_id)
    city            = City(city_name, country, visited, id)
    city_repository.update(city)
    return redirect('/')

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city():
    delete_city = city_repository.select(id)[0]['id']
    city_repository.delete(delete_city)