import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("China", "Asia", "Beijing")

    def test_country_has_name(self):
        self.assertEqual("China", self.country.name)

    def test_country_has_continent(self):
        self.assertEqual("Asia", self.country.continent)

    def test_country_has_city(self):
        self.assertEqual("Beijing", self.country.city)