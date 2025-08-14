# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: weather tool
CLI entry point for the MCP Weather Server.
"""
from loguru import logger
import sys
from weather_forecast_server.server import run_server


def main():
    """Main entry point for the Weather Forecast MCP Server."""
    logger.info("Weather Forecast MCP Server running...")
    try:
        run_server()
    except KeyboardInterrupt:
        logger.info("Server interrupted, shutting down.")
    except Exception as e:
        logger.error(f"Error running server: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
