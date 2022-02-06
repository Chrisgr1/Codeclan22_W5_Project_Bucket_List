import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country1= Country('Scotland', ' Europe', 'https://images.pexels.com/photos/3225529/pexels-photo-3225529.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', 'Haggis hunting', 'No haggis found but met Nessie')
country_repository.new_country(country1)

country2= Country('Vietnam', ' Asia', 'https://images.pexels.com/photos/1660996/pexels-photo-1660996.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', 'Uong cafe', 'Dep')
country_repository.new_country(country2)

city1 = City("Glasgow", 1, 'https://images.pexels.com/photos/5870360/pexels-photo-5870360.jpeg?cs=srgb&dl=pexels-sinitta-leunen-5870360.jpg&fm=jpg', True, 'I belong to Glasgow', 'Whit?')
city_repository.new_city(city1)

pdb.set_trace()