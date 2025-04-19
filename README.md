# Weather Forecast MCP Server

A Model Context Protocol (MCP) server for retrieving weather information using the wttr.in service.

## Overview

This MCP server provides tools for accessing current weather conditions and forecasts for locations worldwide. It can be easily integrated with MCP clients, including Claude and other LLM applications supporting the MCP protocol.

## Features

- Get current weather for any location
- Get multi-day weather forecasts (up to 3 days)
- Support for both Chinsee/English and other language location names
- Easy integration with MCP client applications

## Installation

You can install the MCP Weather Server using `uv`:

```bash
uv install weather-forecast-server
```

Or using pip:

```bash
pip install weather-forecast-server
```

## Usage

### Running as a standalone server

Run the server with the default transport (stdio):

```bash
uv run weather-forecast-server
```

Or specify a transport type:

```bash
uv run weather-forecast-server --transport sse
```

### Integrating with Claude Desktop

To add the weather server to Claude Desktop:

```bash
uv run mcp install weather-forecast-server --name "Weather Tool"
```

### Tools available

1. `get_weather` - Get current weather conditions for a location (up to 3 days)

## Example

Using the server with the MCP CLI:

```bash
# Start the MCP inspector for testing
uv run mcp dev weather-forecast-server
```

## Development

To set up a development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-server-weather.git
cd weather-forecast-server

uv venv
uv pip install -e .
```

## License

Apache 2.0

## Acknowledgements

- Weather data provided by [wttr.in](https://wttr.in)
- Built with [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) 