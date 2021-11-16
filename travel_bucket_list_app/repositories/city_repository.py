from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (city_name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'] )
        cities.append(city)
    return cities

def select_all_visited():
    visited_cities = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'] )
        visited_cities.append(city)
    return visited_cities

def select_all_not_visited():
    not_visited_cities = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [False]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'] )
        not_visited_cities.append(city)
    return not_visited_cities




def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], country, result['visited'], result['id'] )
    return city


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (city_name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.id]
    print(values)
    run_sql(sql, values)





