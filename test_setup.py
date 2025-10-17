"""
Test script to verify environment setup
Author: Priyanka
"""

import sys
print("=" * 50)
print(" ENVIRONMENT SETUP TEST")
print("=" * 50)

# Test Python version
print(f"\n Python Version: {sys.version}")

# Test imports
try:
    import pandas as pd
    print(f" Pandas: {pd.__version__}")
except ImportError as e:
    print(f" Pandas: {e}")

try:
    import numpy as np
    print(f" NumPy: {np.__version__}")
except ImportError as e:
    print(f" NumPy: {e}")

try:
    import yfinance as yf
    print(f" yfinance: {yf.__version__}")
except ImportError as e:
    print(f" yfinance: {e}")

try:
    import matplotlib
    print(f" Matplotlib: {matplotlib.__version__}")
except ImportError as e:
    print(f" Matplotlib: {e}")

try:
    import seaborn as sns
    print(f" Seaborn: {sns.__version__}")
except ImportError as e:
    print(f" Seaborn: {e}")


import ta
import importlib.metadata
try:
    ta_version = importlib.metadata.version("ta")
    print(f" TA (Technical Analysis): {ta_version}")
except importlib.metadata.PackageNotFoundError:
    print(" TA: Installed (version unknown)")



try:
    from loguru import logger
    print(f" Loguru: Installed")
except ImportError as e:
    print(f" Loguru: {e}")

print("\n" + "=" * 50)
print(" All checks complete!")
print("=" * 50)
print("\n Your environment is ready for Day 2! \n")