# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: weather tool
Weather Forecast MCP Server implementation.
This module provides weather information tools via MCP (Model Context Protocol).
"""
import logging
from weather_forecast_server.weather import get_current_weather
from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

# Create MCP server instance
mcp = FastMCP(
    name="WeatherForecastServer",
    description="Provides global weather forecasts and current weather conditions using wttr.in service",
    version="0.1.0"
)


@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get current weather for a specified location using wttr.in service.

    Parameters:
        city: Location name, e.g., "Beijing", "New York", "Tokyo", "武汉"

    Returns:
        str: Current weather information in plain text format.
    """
    return get_current_weather(city)


def run_server(transport="stdio"):
    """
    Run the MCP server with the specified transport.
    
    Args:
        transport: The transport type to use ('stdio', 'sse', etc.)
    """
    logger.info(f"Starting Weather Forecast MCP Server...")
    mcp.run(transport=transport)  # noqa
