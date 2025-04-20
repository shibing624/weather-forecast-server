# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: weather tool
Weather Forecast MCP Server implementation.
This module provides weather information tools via MCP (Model Context Protocol).
"""
from weather_forecast_server.weather import get_current_weather
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP(
    name="WeatherForecastServer",
    description="Provides global weather forecasts and current weather conditions using wttr.in service",
)


@mcp.tool()
def get_weather(city: str = None) -> str:
    """
    Get current weather for a specified location using wttr.in service.

    Parameters:
        city: Location name, e.g., "Beijing", "New York", "Tokyo", "武汉"
        If None, it will return the weather for the current location.
    Returns:
        str: Current weather information in plain text format.
    """
    return get_current_weather(city)


def run_server():
    """
    Run the MCP server with the specified transport.
    """
    mcp.run(transport='stdio')
