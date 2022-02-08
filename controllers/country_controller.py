from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

#SHOW ALL
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

#SHOW ONE
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def select(id):
    country = country_repository.select(id)
    all_cities = city_repository.select_all()
    cities = []
    for city in all_cities:
        if city.country.id == country.id:
            cities.append(city)
    return render_template("countries/show.html", country = country, cities=cities)


# NEW
# GET
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", countries = countries)

# POST
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    continent = request.form['continent']
    img_url = request.form['img_url']
    reason = request.form['reason']
    reflection = request.form['reflection']
    country = Country(country_name, continent, img_url, reason, reflection)
    country_repository.new_country(country)
    return redirect('/countries')

# UPDATE
# GET '/countries/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)


# PUT '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):

    country_name = request.form['country_name']
    continent = request.form['continent']
    img_url = request.form['img_url']
    reason = request.form['reason']
    reflection = request.form['reflection']

    country = Country(country_name, continent, img_url, reason, reflection, id)
    print(country.__dict__)
    country_repository.update(country)
    return redirect('/countries')
