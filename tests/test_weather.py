# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import unittest
from unittest import mock

import requests
import sys
sys.path.append('..')
from weather_forecast_server.weather import get_weather

GEO_RESULT = {
    "results": [{
        "name": "北京市",
        "latitude": 39.9,
        "longitude": 116.4,
        "country": "中国",
        "admin1": "北京市",
        "population": 21893095,
    }]
}

FORECAST_RESULT = {
    "current": {
        "temperature_2m": 21.9,
        "relative_humidity_2m": 55,
        "apparent_temperature": 21.4,
        "weather_code": 0,
        "wind_speed_10m": 8.2,
    },
    "daily": {
        "time": ["2026-09-14", "2026-09-15", "2026-09-16"],
        "weather_code": [0, 2, 61],
        "temperature_2m_max": [28.1, 26.5, 22.0],
        "temperature_2m_min": [17.2, 16.8, 15.1],
    },
}


class TestWeatherMCPServer(unittest.TestCase):
    """Test cases for Weather MCP Server tools."""

    @mock.patch("requests.get")
    def test_get_weather_wttr_in_success(self, mock_get):
        """Test that wttr.in result is returned directly when it works."""
        mock_resp = mock.Mock()
        mock_resp.text = "Weather data for London"
        mock_resp.raise_for_status = mock.Mock()
        mock_get.return_value = mock_resp

        result = get_weather("London")

        mock_get.assert_called_once_with("https://wttr.in/London", timeout=1)
        self.assertEqual(result, "Weather data for London")

    @mock.patch("requests.get")
    def test_get_weather_fallback_to_open_meteo(self, mock_get):
        """Test that Open-Meteo is used when wttr.in fails."""
        geo_resp = mock.Mock()
        geo_resp.json.return_value = GEO_RESULT
        forecast_resp = mock.Mock()
        forecast_resp.json.return_value = FORECAST_RESULT
        mock_get.side_effect = [
            requests.RequestException("500 Server Error"),
            geo_resp,
            forecast_resp,
        ]

        result = get_weather("北京市")

        self.assertIn("北京市 天气", result)
        self.assertIn("21.9°C", result)
        self.assertEqual(mock_get.call_count, 3)

    @mock.patch("requests.get")
    def test_get_weather_city_not_found(self, mock_get):
        """Test that get_weather returns an error message for unknown cities."""
        geo_resp = mock.Mock()
        geo_resp.json.return_value = {"results": None}
        mock_get.side_effect = [
            requests.RequestException("500 Server Error"),
            geo_resp,
        ]

        result = get_weather("不存在城市xyz")

        self.assertIn("City not found", result)

    @mock.patch("requests.get")
    def test_get_weather_all_fail(self, mock_get):
        """Test that get_weather returns an error message when all services fail."""
        mock_get.side_effect = requests.RequestException("Connection error")

        result = get_weather("London")

        self.assertIn("Connection error", result)


if __name__ == "__main__":
    unittest.main()
