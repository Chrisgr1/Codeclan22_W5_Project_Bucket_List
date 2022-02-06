from db.run_sql import run_sql

from models.country import Country
from models.city import City

# NEW CITY

# SELECT ALL

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

#  DELETE ALL
#  DELETE ONE

# UPDATE CITY