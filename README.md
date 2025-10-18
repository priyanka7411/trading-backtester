# 📈 Algorithmic Trading Strategy Backtester

> A comprehensive backtesting framework for evaluating algorithmic trading strategies with professional performance analytics and visualization.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Development](https://img.shields.io/badge/development-Day%203%20Complete-brightgreen)]()

## 🎯 Project Overview

This project implements a professional-grade backtesting system that enables quantitative analysis of trading strategies using historical market data. Built as a data science portfolio project, it demonstrates expertise in:

- **Financial Data Analysis**: Processing and analyzing time-series market data
- **Technical Analysis**: Implementing industry-standard trading indicators
- **Algorithm Development**: Building and optimizing trading strategies
- **Statistical Modeling**: Performance evaluation with quantitative metrics
- **Data Visualization**: Creating professional charts and interactive dashboards
- **Software Engineering**: Clean code, modular architecture, and version control

## ✨ Key Features

- 📊 **Multi-Strategy Support**: Test various trading algorithms simultaneously
- 📈 **Real Market Data**: Integration with Yahoo Finance for historical data
- 🎨 **Professional Visualizations**: Interactive charts and performance dashboards
- 📉 **Comprehensive Metrics**: Industry-standard performance indicators
- 🔄 **Modular Architecture**: Easy to extend with custom strategies
- 📝 **Detailed Logging**: Track every trade and decision
- 🧪 **Data Quality Checks**: Automated validation and preprocessing
- 📊 **9+ Technical Indicators**: RSI, MACD, Bollinger Bands, ATR, and more
- 🎯 **Multi-Indicator Signals**: Combined signal analysis for better decisions

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
│   ├── indicators/                # Technical indicators
│   │   ├── technical_indicators.py  # ✅ 9+ indicator implementations
│   │   └── indicator_visualizer.py  # ✅ Indicator charting & dashboards
│   ├── strategies/                # Trading strategies (Day 4)
│   ├── backtester/                # Core backtesting engine (Day 5)
│   └── utils/                     # Utility functions
│       └── visualizer.py         # ✅ Professional charting
│
├── scripts/                       # Automation scripts
│   ├── download_all_data.py      # ✅ Batch data download
│   ├── process_all_stocks.py     # ✅ Batch processing
│   ├── add_indicators_all_stocks.py  # ✅ Batch indicator addition
│   ├── day2_summary.py           # ✅ Progress reporting
│   └── day3_summary.py           # ✅ Indicator summary
│
├── notebooks/                     # Jupyter analysis notebooks
│   ├── 01_data_exploration.ipynb # ✅ EDA & visualization
│   └── 02_technical_indicators_analysis.ipynb # ✅ Indicator analysis
│
├── tests/                         # Unit tests
├── results/                       # Backtest outputs
│   ├── reports/                   # ✅ Performance reports & summaries
│   └── figures/                   # ✅ Generated charts (50+ visualizations)
│       └── indicators/            # ✅ Technical indicator dashboards
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

5. **Add technical indicators**
```bash
python scripts/add_indicators_all_stocks.py
```

6. **Verify installation**
```bash
python test_indicators_fixed.py
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

### Technical Indicators (Day 3 Complete)

```python
from src.indicators.technical_indicators import TechnicalIndicators
from src.indicators.indicator_visualizer import IndicatorVisualizer

# Initialize indicators
indicators = TechnicalIndicators()
viz_indicators = IndicatorVisualizer()

# Add all indicators to your data
df_with_indicators = indicators.add_all_indicators(df_processed)

# Create indicator visualizations
viz_indicators.plot_rsi(df_with_indicators, 'AAPL')
viz_indicators.plot_macd(df_with_indicators, 'AAPL')
viz_indicators.plot_bollinger_bands(df_with_indicators, 'AAPL')
viz_indicators.plot_all_indicators(df_with_indicators, 'AAPL')  # Complete dashboard
```

### Advanced Usage (Coming in Day 4+)

```python
from src.strategies.ma_crossover import MovingAverageCrossover
from src.backtester.engine import Backtester

# Initialize strategy
strategy = MovingAverageCrossover(short_window=50, long_window=200)

# Run backtest
backtester = Backtester(initial_capital=100000)
results = backtester.run(df_with_indicators, strategy)

# View performance
print(results.summary())
results.plot_equity_curve()
```

## 📊 Current Capabilities (Day 3 Complete)

### Data Processing ✅
- Download historical data from Yahoo Finance
- Clean and validate OHLCV data
- Handle missing values and outliers
- Remove duplicates and sort chronologically
- Timezone-aware datetime handling

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

### Technical Indicators ✅
| Indicator | Type | Purpose | Parameters |
|-----------|------|---------|------------|
| **SMA/EMA** | Trend | Moving averages for trend identification | Period (10, 20, 50) |
| **RSI** | Momentum | Overbought/oversold detection | Period (14), Levels (30/70) |
| **MACD** | Momentum | Trend and momentum signals | Fast (12), Slow (26), Signal (9) |
| **Bollinger Bands** | Volatility | Mean reversion signals | Period (20), Std Dev (2) |
| **ATR** | Volatility | Volatility measurement | Period (14) |
| **Stochastic** | Momentum | Momentum oscillator | %K (14), %D (3) |
| **OBV** | Volume | Volume-price relationship | Cumulative |
| **VWAP** | Volume | Intraday benchmark | Daily reset |
| **ADX** | Trend | Trend strength measurement | Period (14) |

### Visualizations ✅
**Basic Charts:**
- Price History with Moving Averages
- Volume Analysis
- Returns Distribution (Histogram & Time-series)
- Candlestick Charts
- Correlation Matrix
- Monthly Returns Bar Chart
- Portfolio Comparison

**Indicator Charts:**
- RSI with Overbought/Oversold Levels
- MACD with Signal Line and Histogram
- Bollinger Bands with Price Action
- Stochastic Oscillator
- Volume Indicators (OBV, VWAP)
- Complete Technical Analysis Dashboard (8 charts in one)

**Total:** 50+ professional visualizations

## 📊 Implemented Trading Strategies (Coming in Day 4)

| Strategy | Status | Description | Indicators Used |
|----------|--------|-------------|-----------------|
| **Moving Average Crossover** | 🔜 Day 4 | Golden/Death cross signals | SMA 50/200 |
| **RSI Strategy** | 🔜 Day 4 | Overbought/oversold levels | RSI (14) |
| **Mean Reversion** | 🔜 Day 4 | Bollinger Bands breakout | BB (20, 2) |
| **Multi-Indicator** | 🔜 Day 4 | Combined signal analysis | RSI, MACD, BB |

## 🎯 Performance Metrics (Coming in Day 6)

- **Return Metrics**: Total Return, Annualized Return, CAGR
- **Risk Metrics**: Sharpe Ratio, Sortino Ratio, Maximum Drawdown, Calmar Ratio
- **Trade Statistics**: Win Rate, Profit Factor, Average Trade, Total Trades
- **Comparison**: Benchmark comparison with SPY
- **Statistical Tests**: Strategy robustness and significance

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Core** | Python 3.13 |
| **Data Processing** | Pandas 2.1.3, NumPy 1.26.2 |
| **Data Source** | yfinance 0.2.32 |
| **Visualization** | Matplotlib 3.8.2, Seaborn 0.13.0 |
| **Technical Analysis** | TA-Lib 0.11.0, Custom Implementations |
| **Notebooks** | Jupyter 1.0.0 |
| **Development** | Git, GitHub, VSCode |
| **Utilities** | PyYAML, Loguru, tqdm |

## 📚 Project Development Timeline

### ✅ Day 1 - Environment Setup (Complete)
- ✅ Python 3.13 environment configured on Mac
- ✅ VSCode setup with extensions (Python, Jupyter, Pylance)
- ✅ Professional project structure created
- ✅ GitHub repository initialized and connected
- ✅ Virtual environment and dependencies installed
- ✅ Basic data loader implemented and tested
- ✅ Git workflow established

### ✅ Day 2 - Data Preprocessing & Exploration (Complete)
- ✅ Downloaded 6 stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, SPY)
- ✅ Implemented data cleaning and validation module
- ✅ Feature engineering with 8+ calculated features
- ✅ Created exploratory data analysis notebook
- ✅ Built professional visualization module
- ✅ Generated 20+ charts and reports
- ✅ Portfolio summary and multi-stock comparison
- ✅ Fixed timezone handling in date conversions

### ✅ Day 3 - Technical Indicators (Complete) ⭐
- ✅ Implemented 9+ technical indicators:
  - ✅ Moving Averages (SMA, EMA) - Trend identification
  - ✅ RSI (Relative Strength Index) - Momentum indicator
  - ✅ MACD (Moving Average Convergence Divergence) - Trend & momentum
  - ✅ Bollinger Bands - Volatility bands
  - ✅ ATR (Average True Range) - Volatility measurement
  - ✅ Stochastic Oscillator - Momentum indicator
  - ✅ OBV (On-Balance Volume) - Volume indicator
  - ✅ VWAP (Volume Weighted Average Price) - Benchmark
  - ✅ ADX (Average Directional Index) - Trend strength
- ✅ Created comprehensive indicator visualization module
- ✅ Built multi-panel technical analysis dashboards
- ✅ Added indicators to all 6 portfolio stocks
- ✅ Implemented multi-indicator signal generation
- ✅ Created indicator correlation analysis
- ✅ Built exploratory notebook for indicator analysis
- ✅ Generated 30+ indicator visualizations
- ✅ Batch processing scripts for all stocks

### 📅 Day 4 - Trading Strategies (Next)
- Create base strategy class framework
- Implement Moving Average Crossover strategy
- Implement RSI-based trading strategy
- Implement Mean Reversion (Bollinger Bands) strategy
- Implement multi-indicator combined strategy
- Generate buy/sell signals with entry/exit logic
- Create strategy comparison framework
- Test strategies on historical data

### 📅 Day 5 - Backtesting Engine
- Order execution simulation with fills
- Portfolio management and position tracking
- Cash management and margin calculations
- Transaction costs (commission & slippage)
- Trade logging and history tracking
- Stop-loss and take-profit implementation
- Position sizing algorithms
- Realistic backtesting constraints

### 📅 Day 6 - Performance Metrics & Analysis
- Calculate return metrics (Total, Annual, CAGR)
- Implement risk metrics (Sharpe, Sortino, Max DD)
- Trade statistics (Win Rate, Profit Factor)
- Equity curve generation
- Drawdown analysis
- Strategy comparison tables
- Benchmark comparison with SPY
- Statistical significance tests

### 📅 Day 7 - Final Documentation & Presentation
- Comprehensive performance report generation
- Final visualization suite
- Complete documentation update
- Portfolio presentation materials
- Code cleanup and refactoring
- Final testing and validation
- Project showcase preparation

## 📊 Current Dataset

| Stock | Ticker | Data Points | Date Range | Indicators |
|-------|--------|-------------|------------|------------|
| Apple | AAPL | 1,006 | 2020-2024 | 20+ |
| Microsoft | MSFT | 1,006 | 2020-2024 | 20+ |
| Google | GOOGL | 1,006 | 2020-2024 | 20+ |
| Amazon | AMZN | 1,006 | 2020-2024 | 20+ |
| Tesla | TSLA | 1,006 | 2020-2024 | 20+ |
| S&P 500 | SPY | 1,006 | 2020-2024 | 20+ |

**Total**: ~6,000 data points × 30+ features/indicators = ~180,000 data points

## 🎓 Skills Demonstrated

### Technical Skills ✅
- **Python Programming**: OOP, modules, error handling, type hints
- **Data Science**: Pandas, NumPy, statistical analysis
- **Financial Analysis**: OHLCV data, returns calculation, feature engineering
- **Technical Analysis**: Implementing trading indicators from formulas
- **Data Visualization**: Matplotlib, Seaborn, custom plotting, dashboards
- **Version Control**: Git, GitHub, professional commit messages
- **Documentation**: Clear code comments, README, Jupyter notebooks

### Domain Knowledge ✅
- Time-series data processing
- Financial market data structures
- Technical analysis indicators
- Trading signal generation
- Data quality validation
- Feature engineering for trading
- Exploratory data analysis
- Indicator correlation analysis

### Soft Skills ✅
- Problem-solving and debugging (timezone issues, import errors)
- Project organization and planning (7-day roadmap)
- Self-directed learning
- Technical documentation
- Portfolio presentation
- Iterative development

## 🧪 Testing

```bash
# Test data loading
python -m src.data.data_loader

# Test preprocessing
python -m src.data.preprocessor

# Test visualizations
python test_visualizations.py

# Test technical indicators
python test_indicators_fixed.py

# Test indicator visualizations
python -m src.indicators.indicator_visualizer

# Process all stocks with indicators
python scripts/add_indicators_all_stocks.py

# Generate summaries
python scripts/day2_summary.py
python scripts/day3_summary.py
```

## 📁 Key Files

| File | Purpose | Lines | Status |
|------|---------|-------|--------|
| `src/data/data_loader.py` | Data acquisition & loading | 150+ | ✅ Complete |
| `src/data/preprocessor.py` | Data cleaning & validation | 200+ | ✅ Complete |
| `src/utils/visualizer.py` | Basic charting module | 250+ | ✅ Complete |
| `src/indicators/technical_indicators.py` | Indicator library | 450+ | ✅ Complete |
| `src/indicators/indicator_visualizer.py` | Indicator charts | 300+ | ✅ Complete |
| `notebooks/01_data_exploration.ipynb` | EDA notebook | - | ✅ Complete |
| `notebooks/02_technical_indicators_analysis.ipynb` | Indicator analysis | - | ✅ Complete |
| `scripts/download_all_data.py` | Batch download | 80+ | ✅ Complete |
| `scripts/process_all_stocks.py` | Batch processing | 120+ | ✅ Complete |
| `scripts/add_indicators_all_stocks.py` | Batch indicators | 150+ | ✅ Complete |

**Total Lines of Code**: 1,500+ lines of production-quality Python

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome! Feel free to:
- Open an issue for bugs or suggestions
- Fork the repository for your own experiments
- Share feedback on implementation approach
- Suggest new indicators or strategies

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 About Me

**Priyanka Malavade** - Data Science Student

I'm passionate about applying data science to financial markets and building practical, real-world solutions. This project showcases my ability to develop end-to-end data science applications with professional standards, demonstrating both technical skills and financial domain knowledge.

### Connect With Me:
- 📧 Email: priyasmalavade@gmail.com
- 💼 LinkedIn: [Priyanka Malavade](https://www.linkedin.com/in/priyanka-malavade-b34677298/)
- 📱 GitHub: [@priyanka7411](https://github.com/priyanka7411)
- 🌐 Portfolio: [View My Projects](https://github.com/priyanka7411)

### Project Highlights:
- ✅ 3 days of focused development completed
- ✅ 9+ technical indicators implemented from scratch
- ✅ 50+ professional visualizations created
- ✅ 1,500+ lines of clean, documented code
- ✅ Full Git history showing iterative development
- ✅ Professional project structure and documentation

## 🙏 Acknowledgments

- **Data Source**: Yahoo Finance via yfinance library
- **Inspiration**: Quantitative finance literature and industry best practices
- **Learning Resources**: 
  - "Algorithmic Trading" by Ernest Chan
  - "Python for Finance" by Yves Hilpisch
  - QuantStart and QuantConnect tutorials
  - Technical Analysis explained by StockCharts.com
  - Python for Finance community

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/priyanka7411/trading-backtester/issues)
- **Questions**: priyasmalavade@gmail.com
- **Updates**: Follow the repository for latest developments
- **Feedback**: Always appreciated and encouraged!

## 📈 Project Stats

- **Development Time**: 3 days (structured daily progress)
- **Lines of Code**: 1,500+ (Python)
- **Commits**: 20+ (with clear messages)
- **Visualizations**: 50+ (charts and dashboards)
- **Indicators**: 9 (industry-standard implementations)
- **Data Points**: 180,000+ (6 stocks × 4 years × 30+ features)
- **Test Scripts**: 10+ (automated testing and validation)

---

**Status**: 🟢 Active Development - Day 3 Complete  
**Last Updated**: October 2025  
**Next Milestone**: Day 4 - Trading Strategy Implementation  
**Completion**: 42% (3/7 days)

---

### 🌟 Star this repository if you find it useful!

### 📊 Progress Tracker

```
[████████████░░░░░░░░░░░░] 42% Complete

✅ Day 1: Environment Setup
✅ Day 2: Data Processing & EDA  
✅ Day 3: Technical Indicators
⬜ Day 4: Trading Strategies
⬜ Day 5: Backtesting Engine
⬜ Day 6: Performance Metrics
⬜ Day 7: Final Documentation
```

*Built with ❤️ for learning and portfolio demonstration*  
*Showcasing data science skills in quantitative finance*