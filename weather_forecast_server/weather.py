# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import json
import logging
import requests

logger = logging.getLogger(__name__)


def get_current_weather(city: str) -> str:
    """
    Get current weather for a specified location using wttr.in service.

    Parameters:
        city: Location name, e.g., "Beijing", "New York", "Tokyo", "武汉"

    Returns:
        str: Current weather information in plain text format.
    """
    logger.debug(f"get_current_weather({city})")
    try:
        endpoint = "https://wttr.in"
        # Get text format weather data
        response = requests.get(f"{endpoint}/{city}")
        response.raise_for_status()
        text_result = response.text
        logger.debug(f"Weather data for {city}: {text_result}")
        return text_result
    except Exception as e:
        logger.error(f"Error in getting weather for {city}: {str(e)}")
        return json.dumps({"operation": "get_current_weather", "error": str(e)})
