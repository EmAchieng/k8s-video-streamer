import unittest
from src.utils import get_geolocation

class TestUtils(unittest.TestCase):
    def test_get_geolocation(self):
        location = get_geolocation('8.8.8.8')
        self.assertEqual(location, 'CH')
