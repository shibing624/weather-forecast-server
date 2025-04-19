# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')

from weather_forecast_server.weather import get_current_weather

if __name__ == '__main__':
    r = get_current_weather('Beijing')
    print(r)
    r = get_current_weather('保定')
    print(r)
