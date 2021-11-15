class Country:
    def __init__(self, name, continent, city, visited = False, id= None):
        self.name = name
        self.continent = continent
        self.city = city
        self.visited = visited
        self.id = id 

    def mark_visited(self):
        self.visited = True