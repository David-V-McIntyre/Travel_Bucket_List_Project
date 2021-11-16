from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries/new", methods = ['GET'])
def new_country():
    return render_template("/countries/new.html")


@countries_blueprint.route("/countries", methods = ['POST'])
def create_country():
    country_name = request.form["country_name"]
    country = Country(country_name)
    country_repository.save(country)
    return redirect("/cities/new")


