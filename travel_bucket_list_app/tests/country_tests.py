import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("China", "Beijing")

    def test_country_has_name(self):
        self.assertEqual("China", self.country.name)

    def test_country_has_city(self):
        self.assertEqual("Beijing", self.country.city)
    
    def test_country_has_visited(self):
        self.assertEqual(False, self.country.visited)

    def test_mark_visited(self):
        self.country.mark_visited_country()
        self.assertEqual(True, self.country.visited)