# Weather Forecast MCP Server

A Model Context Protocol (MCP) server for retrieving weather information using the wttr.in service.

## Overview

This MCP server provides tools for accessing current weather conditions and forecasts for locations worldwide. 
It can be easily integrated with MCP clients, including Claude and other LLM applications supporting the MCP protocol.

## Features

- Get current weather for any location
- Get multi-day weather forecasts (up to 3 days)
- Support for both Chinsee/English and other language location names
- Easy integration with MCP client applications

## Installation

### From pip
You can install the MCP Weather Server using `uv`:

```bash
uv pip install weather-forecast-server
```

Or using pip:

```bash
pip install weather-forecast-server
```

### From source
```bash
git clone https://github.com/shibing624/mcp-server-weather.git
cd weather-forecast-server
pip install -e .
```

## Usage
### Python Demo
```python
from weather_forecast_server import get_weather
print(get_weather('baoding')) # can be "baoding" or "保定"
```

![](https://github.com/shibing624/weather-forecast-server/blob/main/docs/weather-baoding.jpg)

### Running as a standalone MCP server

Run the server with the stdio transport:

```bash
uvx weather-forecast-server
```

or

```bash
uv run weather-forecast-server
```

or 

```bash
python -m weather_forecast_server
```

Then, you can use the server with any MCP client that supports stdio transport.

### Integrating with Cursor

To add the weather MCP server to Cursor, add stdio MCP with command:

```bash
uv run weather-forecast-server
```

![](https://github.com/shibing624/weather-forecast-server/blob/main/docs/cursor-baoding.jpg)

### Tools available

- `get_weather` - Get current weather conditions for a location (up to 3 days)



## Contact

- Issues and suggestions: [![GitHub issues](https://img.shields.io/github/issues/shibing624/weather-forecast-server.svg)](https://github.com/shibing624/weather-forecast-server/issues)
- Email: xuming624@qq.com
- WeChat: Add me (WeChat ID: xuming624) with the message: "Name-Company-NLP" to join our NLP discussion group.

<img src="https://github.com/shibing624/weather-forecast-server/blob/main/docs/wechat.jpeg" width="200" />


## License

This project is licensed under [The Apache License 2.0](/LICENSE) and can be used freely for commercial purposes. 
Please include a link to the `weather-forecast-server` project and the license in your product description.
## Contribute

We welcome contributions to improve this project! Before submitting a pull request, please:

1. Add appropriate unit tests in the `tests` directory
2. Run `python -m pytest` to ensure all tests pass
3. Submit your PR with clear descriptions of the changes

## Acknowledgements

- Weather data provided by [wttr.in](https://wttr.in)
- Built with [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) 