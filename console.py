import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country1= Country('Scotland', ' Europe', 'https://images.pexels.com/photos/3225529/pexels-photo-3225529.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', 'Haggis hunting', 'No haggis found but met Nessie')
country_repository.new_country(country1)

country2= Country('Vietnam', ' Asia', 'https://images.pexels.com/photos/1660996/pexels-photo-1660996.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', 'Uong cafe', 'Dep')
country_repository.new_country(country2)

country3= Country('Zootopia', ' Africa', 'https://i.ibb.co/4TssDvT/Whats-App-Image-2022-02-09-at-12-36-53.jpg', "Zootopia is a huge country because it’s mountains fell down", 'Dep')
country_repository.new_country(country3)

city1 = City("Glasgow", 1, 'https://images.pexels.com/photos/5870360/pexels-photo-5870360.jpeg?cs=srgb&dl=pexels-sinitta-leunen-5870360.jpg&fm=jpg', True, 'Mad choons and chips & vinegar', 'Got pure mad wi it')
city_repository.new_city(city1)

city2 = City("Zootropolis", 1, 'https://i.ibb.co/4TssDvT/Whats-App-Image-2022-02-09-at-12-36-53.jpg', False, 'Zootropolis is a city that has been buried underneath a mountain.', '')
city_repository.new_city(city2)

pdb.set_trace()