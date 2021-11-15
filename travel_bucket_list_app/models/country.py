class Country:
    def __init__(self, name, city, visited = False, id= None):
        self.name = name
        self.city = city
        self.visited = visited
        self.id = id 

    def mark_visited_country(self):
        self.visited = True