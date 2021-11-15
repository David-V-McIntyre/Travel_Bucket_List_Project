import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Beijing", "China")

    def test_city_has_name(self):
        self.assertEqual("Beijing", self.city.name)

    def test_city_has_country(self):
        self.assertEqual("China", self.city.country)
    
    def test_city_visited(self):
        self.assertEqual(False, self.city.visited)

    def test_mark_visited(self):
        self.city.mark_visited_city()
        self.assertEqual(True, self.city.visited)