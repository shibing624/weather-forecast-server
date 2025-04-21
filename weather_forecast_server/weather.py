# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import json
import requests
from loguru import logger


def get_weather(city: str = None) -> str:
    """
    Get weather forecast information for a specified city using wttr.in service.

    Parameters:
        city: str, city name, e.g., "Beijing", "New York", "Tokyo", "武汉"
        If None, it will return the weather for the current city.
    Returns:
        str: weather forecast information in Markdown format.
    """
    try:
        endpoint = "https://wttr.in"
        # Get text format weather data
        if city:
            response = requests.get(f"{endpoint}/{city}")
        else:
            response = requests.get(endpoint)
        response.raise_for_status()
        text_result = response.text
        logger.debug(f"Weather data for {city}: \n{text_result}")
        return text_result
    except Exception as e:
        logger.error(f"Error in getting weather for {city}: {str(e)}")
        return json.dumps({"operation": "get_current_weather", "error": str(e)})


if __name__ == '__main__':
    c = "武汉"
    weather_info = get_weather(c)
    print(weather_info)
    c = ''
    weather_info = get_weather(c)
    print(weather_info)
