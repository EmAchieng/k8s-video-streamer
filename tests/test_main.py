import unittest
from src.main import app

class TestMain(unittest.TestCase):
    def test_home(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        