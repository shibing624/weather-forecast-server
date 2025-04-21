# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: weather tool
Weather Forecast MCP Server implementation.
This module provides weather information tools via MCP (Model Context Protocol).
"""
from mcp.server.fastmcp import FastMCP
from weather_forecast_server import weather


# Create MCP server instance
mcp = FastMCP(
    name="WeatherForecastServer",
    description="Get weather forecast information using wttr.in service",
)


@mcp.tool()
def get_weather(city: str = None) -> str:
    """
    Get weather forecast information for a specified city using wttr.in service.

    Parameters:
        city: city name, e.g., "Beijing", "New York", "Tokyo", "武汉"
        If None, it will return the weather for the current city.
    Returns:
        str: weather forecast information in Markdown format.
    """
    return weather.get_weather(city)


def run_server():
    """
    Run the MCP server with the specified transport.
    """
    mcp.run(transport='stdio')
