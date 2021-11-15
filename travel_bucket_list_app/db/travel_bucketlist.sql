DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)

)



def __init__(self, name, continent, city, visited = False, id= None):
        self.name = name
        self.city = city
        self.visited = visited
        self.id = id 