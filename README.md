# 📈 Algorithmic Trading Strategy Backtester

> A comprehensive backtesting framework for evaluating algorithmic trading strategies with professional performance analytics and visualization.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Development](https://img.shields.io/badge/development-Day%202%20Complete-brightgreen)]()

## 🎯 Project Overview

This project implements a professional-grade backtesting system that enables quantitative analysis of trading strategies using historical market data. Built as a data science portfolio project, it demonstrates skills in:

- **Financial Data Analysis**: Processing and analyzing time-series market data
- **Algorithm Development**: Implementing and optimizing trading strategies
- **Statistical Modeling**: Performance evaluation with industry-standard metrics
- **Data Visualization**: Creating professional charts and interactive dashboards
- **Software Engineering**: Clean code, modular architecture, and version control

## ✨ Key Features

- 📊 **Multi-Strategy Support**: Test various trading algorithms simultaneously
- 📈 **Real Market Data**: Integration with Yahoo Finance for historical data
- 🎨 **Professional Visualizations**: Interactive charts and performance dashboards
- 📉 **Comprehensive Metrics**: Industry-standard performance indicators (Sharpe, Sortino, Max Drawdown)
- 🔄 **Modular Architecture**: Easy to extend with custom strategies
- 📝 **Detailed Logging**: Track every trade and decision
- 🧪 **Data Quality Checks**: Automated validation and preprocessing

## 🏗️ Project Structure

```
trading-backtester/
│
├── data/                          # Market data storage
│   ├── raw/                       # Downloaded historical data (6 stocks)
│   └── processed/                 # Cleaned and feature-engineered data
│
├── src/                           # Source code
│   ├── data/                      # Data handling modules
│   │   ├── data_loader.py        # ✅ Yahoo Finance integration
│   │   └── preprocessor.py       # ✅ Data cleaning & validation
│   ├── indicators/                # Technical indicators (Day 3)
│   ├── strategies/                # Trading strategies (Day 4)
│   ├── backtester/                # Core backtesting engine (Day 5)
│   └── utils/                     # Utility functions
│       └── visualizer.py         # ✅ Professional charting
│
├── scripts/                       # Automation scripts
│   ├── download_all_data.py      # ✅ Batch data download
│   ├── process_all_stocks.py     # ✅ Batch processing
│   └── day2_summary.py           # ✅ Progress reporting
│
├── notebooks/                     # Jupyter analysis notebooks
│   └── 01_data_exploration.ipynb # ✅ EDA & visualization
│
├── tests/                         # Unit tests
├── results/                       # Backtest outputs
│   ├── reports/                   # ✅ Performance reports & summaries
│   └── figures/                   # ✅ Generated charts (20+ visualizations)
│
├── config/                        # Configuration files
│   └── config.yaml               # Project settings
│
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.11+** (Tested on Python 3.13)
- **pip** package manager
- **Git** for version control
- **4GB RAM** minimum
- **Internet connection** for downloading market data

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/priyanka7411/trading-backtester.git
cd trading-backtester
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Download sample data**
```bash
python scripts/download_all_data.py
```

5. **Verify installation**
```bash
python test_visualizations.py
```

## 💡 Usage Example

### Basic Data Loading and Analysis

```python
from src.data.data_loader import DataLoader
from src.data.preprocessor import DataPreprocessor
from src.utils.visualizer import Visualizer

# Initialize components
loader = DataLoader()
preprocessor = DataPreprocessor()
viz = Visualizer()

# Load historical data
df = loader.download_data('AAPL', start='2020-01-01', end='2024-01-01')

# Clean and add features
df_clean = preprocessor.clean_data(df)
df_processed = preprocessor.add_basic_features(df_clean)

# Create visualizations
viz.plot_price_history(df_processed, 'AAPL')
viz.plot_returns_distribution(df_processed, 'AAPL')
```

### Advanced Usage (Coming in Day 4+)

```python
from src.strategies.ma_crossover import MovingAverageCrossover
from src.backtester.engine import Backtester

# Initialize strategy
strategy = MovingAverageCrossover(short_window=50, long_window=200)

# Run backtest
backtester = Backtester(initial_capital=100000)
results = backtester.run(df_processed, strategy)

# View performance
print(results.summary())
results.plot_equity_curve()
```

## 📊 Current Capabilities (Day 2 Complete)

### Data Processing ✅
- Download historical data from Yahoo Finance
- Clean and validate OHLCV data
- Handle missing values and outliers
- Remove duplicates and sort chronologically

### Feature Engineering ✅
| Feature | Description |
|---------|-------------|
| **Daily Returns** | Percentage change in close price |
| **Log Returns** | Logarithmic returns for analysis |
| **Price Range** | High - Low spread |
| **Price Change** | Close - Open difference |
| **Volume Change** | Percentage change in volume |
| **5-Day MA** | 5-period moving average |
| **20-Day MA** | 20-period moving average |
| **Up/Down Days** | Binary indicator for price direction |

### Visualizations ✅
- **Price History**: Close price with moving averages
- **Volume Analysis**: Trading volume over time
- **Returns Distribution**: Histogram and time-series
- **Candlestick Charts**: Traditional OHLC visualization
- **Correlation Matrix**: Feature correlation heatmap
- **Monthly Returns**: Bar chart of monthly performance
- **Portfolio Comparison**: Multi-stock normalized comparison

## 📈 Implemented Strategies (Coming Soon)

| Strategy | Status | Description |
|----------|--------|-------------|
| **Moving Average Crossover** | 🔜 Day 4 | Golden/Death cross signals |
| **RSI Strategy** | 🔜 Day 4 | Overbought/oversold levels |
| **Mean Reversion** | 🔜 Day 4 | Bollinger Bands breakout |

## 🎯 Performance Metrics (Coming in Day 6)

- **Return Metrics**: Total Return, Annualized Return, CAGR
- **Risk Metrics**: Sharpe Ratio, Sortino Ratio, Maximum Drawdown
- **Trade Statistics**: Win Rate, Profit Factor, Average Trade
- **Comparison**: Benchmark comparison with SPY

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Core** | Python 3.13 |
| **Data Processing** | Pandas 2.1.3, NumPy 1.26.2 |
| **Data Source** | yfinance 0.2.32 |
| **Visualization** | Matplotlib 3.8.2, Seaborn 0.13.0 |
| **Technical Analysis** | TA-Lib 0.11.0 |
| **Notebooks** | Jupyter 1.0.0 |
| **Development** | Git, GitHub, VSCode |

## 📚 Project Development Timeline

### ✅ Day 1 - Environment Setup (Complete)
- ✅ Python 3.13 environment configured
- ✅ VSCode setup with extensions
- ✅ Project structure created
- ✅ GitHub repository initialized
- ✅ Dependencies installed
- ✅ Basic data loader implemented

### ✅ Day 2 - Data Preprocessing & Exploration (Complete)
- ✅ Downloaded 6 stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, SPY)
- ✅ Data cleaning and validation module
- ✅ Feature engineering (8+ features)
- ✅ Exploratory data analysis notebook
- ✅ Professional visualization module
- ✅ 20+ charts and reports generated
- ✅ Portfolio summary and comparison

### 🔄 Day 3 - Technical Indicators (In Progress)
- 🔜 RSI (Relative Strength Index)
- 🔜 MACD (Moving Average Convergence Divergence)
- 🔜 Bollinger Bands
- 🔜 ATR (Average True Range)
- 🔜 Indicator visualization module

### 📅 Day 4 - Trading Strategies
- Strategy base class framework
- Moving Average Crossover strategy
- RSI-based strategy
- Mean Reversion strategy
- Signal generation and backtesting prep

### 📅 Day 5 - Backtesting Engine
- Order execution simulation
- Portfolio management
- Position tracking
- Transaction costs (commission & slippage)
- Trade logging

### 📅 Day 6 - Performance Metrics
- Return calculations
- Risk metrics (Sharpe, Sortino, Max DD)
- Statistical analysis
- Strategy comparison framework
- Benchmark comparison

### 📅 Day 7 - Final Documentation
- Comprehensive visualizations
- Final report generation
- Documentation completion
- Portfolio presentation
- Project showcase

## 📊 Current Dataset

| Stock | Ticker | Data Points | Date Range |
|-------|--------|-------------|------------|
| Apple | AAPL | 1,006 | 2020-2024 |
| Microsoft | MSFT | 1,006 | 2020-2024 |
| Google | GOOGL | 1,006 | 2020-2024 |
| Amazon | AMZN | 1,006 | 2020-2024 |
| Tesla | TSLA | 1,006 | 2020-2024 |
| S&P 500 | SPY | 1,006 | 2020-2024 |

**Total**: ~6,000 data points across 6 securities

## 🎓 Skills Demonstrated

### Technical Skills ✅
- **Python Programming**: OOP, modules, error handling
- **Data Science**: Pandas, NumPy, statistical analysis
- **Financial Analysis**: OHLCV data, returns calculation, feature engineering
- **Data Visualization**: Matplotlib, Seaborn, custom plotting
- **Version Control**: Git, GitHub, commit history
- **Documentation**: Clear code comments, README, notebooks

### Domain Knowledge ✅
- Time-series data processing
- Financial market data structures
- Data quality validation
- Feature engineering for trading
- Exploratory data analysis

### Soft Skills ✅
- Problem-solving and debugging
- Project organization and planning
- Self-directed learning
- Technical documentation
- Portfolio presentation

## 🧪 Testing

```bash
# Run visualization tests
python test_visualizations.py

# Check setup
python check_setup.py

# Generate Day 2 summary
python scripts/day2_summary.py
```

## 📁 Key Files

| File | Purpose | Status |
|------|---------|--------|
| `src/data/data_loader.py` | Data acquisition | ✅ Complete |
| `src/data/preprocessor.py` | Data cleaning | ✅ Complete |
| `src/utils/visualizer.py` | Charting module | ✅ Complete |
| `notebooks/01_data_exploration.ipynb` | EDA | ✅ Complete |
| `scripts/download_all_data.py` | Batch download | ✅ Complete |
| `scripts/process_all_stocks.py` | Batch processing | ✅ Complete |

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome! Feel free to:
- Open an issue for bugs or suggestions
- Fork the repository for your own experiments
- Share feedback on implementation approach

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 About Me

**Priyanka Malavade** - Data Science Student

I'm passionate about applying data science to financial markets and building practical, real-world solutions. This project showcases my ability to develop end-to-end data science applications with professional standards.

- 📧 Email: priyasmalavade@gmail.com
- 💼 LinkedIn: [Priyanka Malavade](https://www.linkedin.com/in/priyanka-malavade-b34677298/)
- 📱 GitHub: [@priyanka7411](https://github.com/priyanka7411)
- 🌐 Portfolio: [View My Work](https://github.com/priyanka7411/trading-backtester)

## 🙏 Acknowledgments

- **Data Source**: Yahoo Finance via yfinance library
- **Inspiration**: Quantitative finance literature and industry best practices
- **Learning Resources**: 
  - "Algorithmic Trading" by Ernest Chan
  - QuantStart and QuantConnect tutorials
  - Python for Finance community

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/priyanka7411/trading-backtester/issues)
- **Questions**: priyasmalavade@gmail.com
- **Updates**: Follow the repository for latest developments

---

**Status**: 🟢 Active Development - Day 2 Complete  
**Last Updated**: October 2025  
**Next Milestone**: Day 3 - Technical Indicators Implementation

---

### 🌟 Star this repository if you find it useful!

*Built with ❤️ for learning and portfolio demonstration*