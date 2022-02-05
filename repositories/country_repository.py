from db.run_sql import run_sql

from models.country import Country

def new_country(country):
    sql = "INSERT INTO countries (country_name, continent, img_url, reason, reflections) VALUES (%s, %s, %s, %s, %s) returning *"
    # returning * or returning id - check this if error
    values = [country.country_name, country.continent, country.img_url, country.reason, country.reflections]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id=id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['continent'], row['img_url'], row['reason'], row['reflections'], row['id'])
        countries.append(country)
    return countries