from db.run_sql import run_sql

from models.country import Country
from models.city import City

# NEW CITY
def new_city(city):
    sql = "INSERT INTO cities (city_name, country_id, img_url, visited, reason, reflection) VALUES (%s, %s, %s, %s, %s, %s) returning *"
    values = [city.city_name, city.country_id, city.img_url, city.visited, city.reason, city.reflection]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id=id
    return city

# SELECT ALL
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['city_name'], row['country_id'], row['img_url'], row['visited'], row['reason'], row['reflection'], row['id'])
        cities.append(city)
    return cities

# SELECT ONE
def select(id):
    city = None
    sql = "SELECT * from cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        city = City(result['city_name'], result['country_id'], result['img_url'], result['visited'], result['reason'], result['reflection'], result['id'])
    return city

#  DELETE ONE
def delete(id):
    sql  = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELEETE ALL
def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)

    # UPDATE CITY