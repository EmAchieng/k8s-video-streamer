import unittest
from src.router import route_video

class TestRouter(unittest.TestCase):
    def test_route_video(self):
        result = route_video('CH')
        self.assertEqual(result, 'ch-server')
        