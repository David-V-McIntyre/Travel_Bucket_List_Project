import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Beijing", "China")

    def test_city_has_name(self):
        self.assertEqual("Beijing", self.city.name)

    def test_city_has_country(self):
        self.assertEqual("China", self.city.country)

    # def test_country_has_city(self):
    #     self.assertEqual("Beijing", self.country.city)
    
    # def test_country_has_visited(self):
    #     self.assertEqual(False, self.country.visited)