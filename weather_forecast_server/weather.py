# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: weather tool
Weather forecast via wttr.in, with Open-Meteo free API as fallback.
"""
import requests
from loguru import logger

WTTR_ENDPOINT = "https://wttr.in"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
IP_LOCATION_URL = "http://ip-api.com/json/"

# WMO weather interpretation codes (WW)
WEATHER_CODES = {
    0: "晴",
    1: "大部晴朗", 2: "多云", 3: "阴",
    45: "雾", 48: "雾凇",
    51: "小毛毛雨", 53: "毛毛雨", 55: "大毛毛雨",
    56: "冻毛毛雨", 57: "强冻毛毛雨",
    61: "小雨", 63: "中雨", 65: "大雨",
    66: "冻雨", 67: "强冻雨",
    71: "小雪", 73: "中雪", 75: "大雪", 77: "雪粒",
    80: "小阵雨", 81: "阵雨", 82: "强阵雨",
    85: "小阵雪", 86: "大阵雪",
    95: "雷暴", 96: "雷暴伴小冰雹", 99: "雷暴伴大冰雹",
}


def _weather_desc(code) -> str:
    """Map WMO weather code to Chinese description."""
    return WEATHER_CODES.get(code, "未知")


def _get_weather_wttr_in(city: str = None) -> str:
    """Get weather text from wttr.in. Raises on failure."""
    if city:
        response = requests.get(f"{WTTR_ENDPOINT}/{city}", timeout=0.5)
    else:
        response = requests.get(WTTR_ENDPOINT, timeout=0.5)
    response.raise_for_status()
    return response.text


def _resolve_city(city: str = None) -> str:
    """Return city name; if None, detect from IP."""
    if city:
        return city
    resp = requests.get(IP_LOCATION_URL, params={"lang": "zh"}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("city") or "Beijing"


def _geocode(city: str) -> dict:
    """Geocode a city name, pick the candidate with the largest population."""
    resp = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 5, "language": "zh", "format": "json"},
        timeout=10,
    )
    resp.raise_for_status()
    results = resp.json().get("results") or []
    if not results:
        raise ValueError(f"City not found: {city}")
    return max(results, key=lambda r: r.get("population") or 0)


def _get_weather_open_meteo(city: str = None) -> str:
    """Get weather markdown from Open-Meteo. Raises on failure."""
    city = _resolve_city(city)
    loc = _geocode(city)
    resp = requests.get(
        FORECAST_URL,
        params={
            "latitude": loc["latitude"],
            "longitude": loc["longitude"],
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
            "daily": "weather_code,temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "forecast_days": 3,
        },
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    cur = data["current"]
    daily = data["daily"]
    location_label = " ".join(
        part for part in (loc.get("country"), loc.get("admin1")) if part
    )
    lines = [
        f"## {loc.get('name')} 天气",
        f"- 位置: {location_label}",
        (
            f"- 当前: {_weather_desc(cur['weather_code'])}, "
            f"气温 {cur['temperature_2m']}°C, 体感 {cur['apparent_temperature']}°C, "
            f"湿度 {cur['relative_humidity_2m']}%, 风速 {cur['wind_speed_10m']} km/h"
        ),
        "",
        "| 日期 | 天气 | 最高温 | 最低温 |",
        "|------|------|--------|--------|",
    ]
    for i, date in enumerate(daily["time"]):
        lines.append(
            f"| {date} | {_weather_desc(daily['weather_code'][i])} "
            f"| {daily['temperature_2m_max'][i]}°C | {daily['temperature_2m_min'][i]}°C |"
        )
    return "\n".join(lines)


def get_weather(city: str = None) -> str:
    """
    Get weather forecast information for a specified city.
    Primary service: wttr.in; fallback: Open-Meteo (free, no API key).

    Parameters:
        city: city name, e.g., "Beijing", "北京市", "Tokyo", "武汉".
            If None, the city is detected from the client IP.
    Returns:
        str: weather forecast information.
    """
    try:
        result = _get_weather_wttr_in(city)
        logger.debug(f"Weather data for {city} from wttr.in: \n{result}")
        return result
    except Exception as e:
        logger.warning(f"wttr.in failed for {city}, falling back to Open-Meteo: {e}")
    try:
        result = _get_weather_open_meteo(city)
        logger.debug(f"Weather data for {city} from Open-Meteo: \n{result}")
        return result
    except Exception as e:
        msg = f"Error getting weather for {city}: {str(e)}"
        logger.error(msg)
        return msg


if __name__ == '__main__':
    for c in ("北京市", "Beijing", None):
        print(get_weather(c))
        print()
