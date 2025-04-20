# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

__version__ = "0.0.2"

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='weather-forecast-server',
    version=__version__,
    description='weather-forecast-server: MCP server for weather forecast',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/weather-forecast-server',
    license='Apache License 2.0',
    zip_safe=False,
    python_requires='>=3.10',
    entry_points={"console_scripts": ["weather-forecast-server = weather_forecast_server.__main__:main"]},
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='weather_forecast_server, weather forecast, server, weather, forecast',
    install_requires=[
        "mcp",
        "requests",
    ],
    packages=find_packages(exclude=['tests']),
    package_dir={'weather_forecast_server': 'weather_forecast_server'},
    package_data={'weather_forecast_server': ['*.*']}
)
