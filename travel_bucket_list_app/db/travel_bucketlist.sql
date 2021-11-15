DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)
    )



CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id),
    visited BOOLEAN


)
    def __init__(self, name, country, visited = False, id= None):
        self.name = name
        self.country = country
        self.visited = visited
        self.id = id 

    def mark_visited_city(self):
        self.visited = True
