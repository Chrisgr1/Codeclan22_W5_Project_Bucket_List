from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

    #SHOW ONE
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def select(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city = city)