from db.run_sql import run_sql

from models.country import Country

# NEW COUNTRY
def new_country(country):
    sql = "INSERT INTO countries (country_name, continent, img_url, reason, reflection) VALUES (%s, %s, %s, %s, %s) returning *"
    # returning * or returning id - check this if error
    values = [country.country_name, country.continent, country.img_url, country.reason, country.reflection]
    print(values)
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    country.id=id
    return country

# SELECT ALL
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['continent'], row['img_url'], row['reason'], row['reflection'], row['id'])
        countries.append(country)
    return countries

# SELECT_ONE
def select(id):
    country = None
    sql = "SELECT * from countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        country = Country(result['country_name'], result['continent'], result['img_url'], result['reason'], result['reflection'], result['id'])
    return country


def update(country):
    sql = "UPDATE countries SET (country_name, continent, img_url, reason, reflection) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [country.country_name, country.continent, country.img_url, country.reason, country.reflection, country.id]
    run_sql(sql, values)


