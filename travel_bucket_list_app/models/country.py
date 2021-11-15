class Country:
    def __init__(self, name, continent, cities, visited = False, id= None):
        self.name = name
        self.continent = continent
        self.cities = cities
        self.visited = visited
        self.id = id 

    def mark_visited(self):
        self.visited = True