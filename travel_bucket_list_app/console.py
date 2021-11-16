import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("China")
country_repository.save(country1)
country2 = Country("Canada")
country_repository.save(country2)
country3 = Country("Germany")
country_repository.save(country3)
country4 = Country("Slovenia")
country_repository.save(country4)

city1 = City("Beijing", country1)
city_repository.save(city1)
city2 = City("Toronto", country2)
city_repository.save(city2)
city3 = City("Berlin", country3)
city_repository.save(city3)
city4 = City("Frankfurt", country3)
city_repository.save(city4)
city5 = City("Ljubljana", country4, True)
city_repository.save(city5)
city6 = City("Dresden", country3, True)
city_repository.save(city6)

