from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
# import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)\

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

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
    reflection = request.form['refelction']
    country = Country(country_name, continent, img_url, reason, reflection)
    country_repository.new_country(country)
    return redirect('/countries')
