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

city1 = City("Beijing", country1)
city_repository.save(city1)
city2 = City("Toronto", country2)
city_repository.save(city2)