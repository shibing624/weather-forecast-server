# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from weather_forecast_server import get_weather

if __name__ == '__main__':
    r = get_weather('Beijing')
    print(r)
    r = get_weather('保定市')
    print(r)
