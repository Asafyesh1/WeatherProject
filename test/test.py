import unittest
from src.Weather import WeatherClass


class TestWeather(unittest.TestCase):
    def setUp(self):
        pass
    def test_GetCurrentWeather_EmptyLocation(self):
        w = WeatherClass()
        result = w.GetCurrentWeather("abc")
        self.assertEqual(result,"City Not Found")
    def test_Compare1(self):
        w = WeatherClass()
        result = w.Compare("abc","London")
        self.assertEqual(result," Location 1 Not Found ")
    def test_Compare2(self):
        w = WeatherClass()
        result = w.Compare("London","abc")
        self.assertEqual(result," Location 2 Not Found ")
    def test_posts(self):
        w = WeatherClass()
        result = w.posts("http://api.openweathermap.org/data/2.5/weather?appid=57feef68f65ebda86fcaec59e33312fb")
        self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()

