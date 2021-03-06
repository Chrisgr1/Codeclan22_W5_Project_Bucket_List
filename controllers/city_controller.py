from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# SHOW ALL
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

    #SHOW ONE
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def select(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city = city)

    # CREATE CITY
# GET
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", countries = countries)

# POST
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    img_url = request.form['img_url']
    visited = request.form['visited']
    reason = request.form['reason']
    reflection = request.form['reflection']
    city = City(city_name, country_id, img_url, visited, reason, reflection)
    city_repository.new_city(city)
    return redirect('/cities')

#  DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")

# UPDATE
# GET '/countries/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    list_of_countries = country_repository.select_all()
    city = city_repository.select(id)
    return render_template('cities/edit.html', city=city, list_of_countries=list_of_countries)

# PUT '/citiess/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    img_url = request.form['img_url']
    visited = request.form['visited']
    reason = request.form['reason']
    reflection = request.form['reflection']
    city = City(city_name, country_id, img_url, visited, reason, reflection, id)
    city_repository.update(city)
    return redirect('/cities')