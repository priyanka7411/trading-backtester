# 📈 Algorithmic Trading Strategy Backtester

> A comprehensive backtesting framework for evaluating algorithmic trading strategies with professional performance analytics and visualization.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Development](https://img.shields.io/badge/development-Day%204%20Complete-brightgreen)]()

## 🎯 Project Overview

This project implements a professional-grade backtesting system that enables quantitative analysis of trading strategies using historical market data. Built as a data science portfolio project, it demonstrates expertise in:

- **Financial Data Analysis**: Processing and analyzing time-series market data
- **Technical Analysis**: Implementing industry-standard trading indicators
- **Algorithm Development**: Building and optimizing trading strategies
- **Strategy Implementation**: Creating trend-following, mean reversion, and breakout systems
- **Statistical Modeling**: Performance evaluation with quantitative metrics
- **Data Visualization**: Creating professional charts and interactive dashboards
- **Software Engineering**: Clean code, OOP principles, modular architecture, and version control

## ✨ Key Features

- 📊 **Multi-Strategy Support**: 7+ trading strategies with multiple variants
- 📈 **Real Market Data**: Integration with Yahoo Finance for historical data
- 🎨 **Professional Visualizations**: Interactive charts and performance dashboards
- 📉 **Comprehensive Metrics**: Industry-standard performance indicators
- 🔄 **Modular Architecture**: Easy to extend with custom strategies
- 📝 **Detailed Logging**: Track every trade and decision
- 🧪 **Data Quality Checks**: Automated validation and preprocessing
- 📊 **9+ Technical Indicators**: RSI, MACD, Bollinger Bands, ATR, and more
- 🎯 **Multi-Indicator Signals**: Combined signal analysis for robust decisions
- 💼 **Strategy Framework**: Object-oriented base class for easy strategy development

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
│   ├── strategies/                # Trading strategies
│   │   ├── base_strategy.py      # ✅ Abstract base class framework
│   │   ├── ma_crossover.py       # ✅ Moving average strategies
│   │   ├── rsi_strategy.py       # ✅ RSI-based strategies
│   │   ├── bollinger_strategy.py # ✅ Bollinger Bands strategies
│   │   ├── combined_strategy.py  # ✅ Multi-indicator strategies
│   │   └── strategy_visualizer.py # ✅ Strategy visualization
│   ├── backtester/                # Core backtesting engine (Day 5)
│   └── utils/                     # Utility functions
│       └── visualizer.py         # ✅ Professional charting
│
├── scripts/                       # Automation scripts
│   ├── download_all_data.py      # ✅ Batch data download
│   ├── process_all_stocks.py     # ✅ Batch processing
│   ├── add_indicators_all_stocks.py  # ✅ Batch indicator addition
│   ├── test_all_strategies.py    # ✅ Strategy testing framework
│   ├── day2_summary.py           # ✅ Progress reporting
│   ├── day3_summary.py           # ✅ Indicator summary
│   └── day4_summary.py           # ✅ Strategy summary
│
├── notebooks/                     # Jupyter analysis notebooks
│   ├── 01_data_exploration.ipynb # ✅ EDA & visualization
│   └── 02_technical_indicators_analysis.ipynb # ✅ Indicator analysis
│
├── tests/                         # Unit tests
├── results/                       # Backtest outputs
│   ├── reports/                   # ✅ Performance reports & summaries
│   │   └── strategy_comparison.csv # ✅ Strategy metrics
│   └── figures/                   # ✅ Generated charts (70+ visualizations)
│       ├── indicators/            # ✅ Technical indicator dashboards
│       └── strategies/            # ✅ Strategy signal & performance charts
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

6. **Test strategies**
```bash
python scripts/test_all_strategies.py
```

## 💡 Usage Examples

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

### Technical Indicators (Day 3)

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
viz_indicators.plot_all_indicators(df_with_indicators, 'AAPL')
```

### Trading Strategies (Day 4 Complete) ✅

```python
from src.strategies.ma_crossover import MovingAverageCrossover
from src.strategies.rsi_strategy import RSIStrategy
from src.strategies.combined_strategy import CombinedStrategy
from src.strategies.strategy_visualizer import StrategyVisualizer

# Initialize strategies
ma_strategy = MovingAverageCrossover(short_window=50, long_window=200)
rsi_strategy = RSIStrategy(rsi_period=14, oversold=30, overbought=70)
combined = CombinedStrategy(min_signals=2)

# Run strategies
ma_results = ma_strategy.run(df_with_indicators)
rsi_results = rsi_strategy.run(df_with_indicators)
combined_results = combined.run(df_with_indicators)

# View performance
ma_strategy.print_summary()
rsi_strategy.print_summary()

# Visualize signals
viz = StrategyVisualizer()
viz.plot_signals(ma_strategy, 'AAPL')
viz.plot_trades(ma_strategy, 'AAPL')
viz.compare_strategies([ma_strategy, rsi_strategy, combined], 'AAPL')
```

### Advanced Usage (Coming in Day 5+)

```python
from src.backtester.engine import Backtester

# Initialize backtester with realistic constraints
backtester = Backtester(
    initial_capital=100000,
    commission=0.001,  # 0.1% commission
    slippage=0.0005    # 0.05% slippage
)

# Run backtest
results = backtester.run(df_with_indicators, ma_strategy)

# View comprehensive results
print(results.summary())
results.plot_equity_curve()
results.plot_drawdown()
```

## 📊 Current Capabilities (Day 4 Complete)

### Data Processing ✅
- Download historical data from Yahoo Finance
- Clean and validate OHLCV data
- Handle missing values and outliers
- Remove duplicates and sort chronologically
- Timezone-aware datetime handling
- Batch processing for multiple stocks

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

### Trading Strategies ✅
| Strategy | Type | Description | Status |
|----------|------|-------------|--------|
| **MA Crossover (10/50)** | Trend Following | Short-term golden/death cross | ✅ Complete |
| **MA Crossover (50/200)** | Trend Following | Classic golden/death cross | ✅ Complete |
| **RSI Strategy** | Mean Reversion | Oversold/overbought trading | ✅ Complete |
| **RSI Enhanced** | Mean Reversion | RSI with trend filter | ✅ Complete |
| **Bollinger Bands** | Mean Reversion | Price extremes at bands | ✅ Complete |
| **BB Breakout** | Breakout | Volatility squeeze breakouts | ✅ Complete |
| **Combined Strategy** | Multi-Indicator | Requires 2 of 3 signals | ✅ Complete |
| **Weighted Combined** | Multi-Indicator | Weighted indicator scores | ✅ Complete |

**Total**: 8 unique strategies with multiple variants

### Strategy Features ✅
- **Signal Generation**: Buy/sell signal logic
- **Position Management**: Long position tracking
- **Trade Identification**: Entry/exit point detection
- **Performance Metrics**: Win rate, returns, trade statistics
- **Visualization**: Signal charts, position plots, trade analysis
- **Comparison Framework**: Multi-strategy performance comparison

### Visualizations ✅
**Basic Charts:**
- Price History with Moving Averages
- Volume Analysis
- Returns Distribution
- Candlestick Charts
- Correlation Matrix
- Monthly Returns
- Portfolio Comparison

**Indicator Charts:**
- RSI with Levels
- MACD with Histogram
- Bollinger Bands
- Stochastic Oscillator
- Volume Indicators
- Complete Dashboards

**Strategy Charts:**
- Buy/Sell Signals
- Position Tracking
- Individual Trades
- Cumulative Returns
- Strategy Comparison

**Total:** 70+ professional visualizations

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
| **Design Patterns** | Abstract Base Classes, Inheritance, Polymorphism |

## 📚 Project Development Timeline

### ✅ Day 1 - Environment Setup (Complete)
- ✅ Python 3.13 environment configured on Mac
- ✅ VSCode setup with extensions (Python, Jupyter, Pylance)
- ✅ Professional project structure created
- ✅ GitHub repository initialized and connected
- ✅ Virtual environment and dependencies installed
- ✅ Basic data loader implemented and tested
- ✅ Git workflow established with professional commits

### ✅ Day 2 - Data Preprocessing & Exploration (Complete)
- ✅ Downloaded 6 stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, SPY)
- ✅ Implemented data cleaning and validation module
- ✅ Feature engineering with 8+ calculated features
- ✅ Created exploratory data analysis notebook
- ✅ Built professional visualization module
- ✅ Generated 20+ charts and reports
- ✅ Portfolio summary and multi-stock comparison
- ✅ Fixed timezone handling in date conversions
- ✅ Batch processing scripts

### ✅ Day 3 - Technical Indicators (Complete) ⭐
- ✅ Implemented 9+ technical indicators:
  - ✅ Moving Averages (SMA, EMA)
  - ✅ RSI (Relative Strength Index)
  - ✅ MACD (Moving Average Convergence Divergence)
  - ✅ Bollinger Bands
  - ✅ ATR (Average True Range)
  - ✅ Stochastic Oscillator
  - ✅ OBV (On-Balance Volume)
  - ✅ VWAP (Volume Weighted Average Price)
  - ✅ ADX (Average Directional Index)
- ✅ Created comprehensive indicator visualization module
- ✅ Built multi-panel technical analysis dashboards
- ✅ Added indicators to all 6 portfolio stocks
- ✅ Implemented multi-indicator signal generation
- ✅ Created indicator correlation analysis
- ✅ Built exploratory notebook for indicator analysis
- ✅ Generated 30+ indicator visualizations

### ✅ Day 4 - Trading Strategies (Complete) 🎯
- ✅ Created BaseStrategy abstract class framework
  - ✅ Signal generation interface
  - ✅ Position calculation logic
  - ✅ Trade identification system
  - ✅ Performance statistics
- ✅ Implemented Moving Average Crossover strategies
  - ✅ Short-term (10/50)
  - ✅ Classic golden cross (50/200)
  - ✅ Medium-term (20/100)
- ✅ Implemented RSI-based strategies
  - ✅ Standard RSI strategy
  - ✅ RSI with trend filter
- ✅ Implemented Bollinger Bands strategies
  - ✅ Mean reversion approach
  - ✅ Breakout strategy
- ✅ Implemented Combined strategies
  - ✅ Multi-indicator aggregation
  - ✅ Weighted scoring approach
- ✅ Created comprehensive strategy visualizer
  - ✅ Signal plotting
  - ✅ Position visualization
  - ✅ Trade analysis charts
  - ✅ Multi-strategy comparison
- ✅ Built automated testing framework
- ✅ Generated strategy performance reports

### 📅 Day 5 - Backtesting Engine (Next)
- Build realistic backtesting framework
- Order execution simulation
- Portfolio management system
- Transaction costs (commission & slippage)
- Position sizing algorithms
- Stop-loss and take-profit
- Trade logging and history
- Equity curve generation

### 📅 Day 6 - Performance Metrics & Analysis
- Calculate return metrics
- Implement risk metrics
- Trade statistics
- Drawdown analysis
- Strategy comparison
- Benchmark comparison
- Statistical significance tests
- Performance visualization

### 📅 Day 7 - Final Documentation & Presentation
- Comprehensive performance reports
- Final visualization suite
- Complete documentation
- Portfolio presentation
- Code cleanup
- Final testing
- Project showcase

## 📊 Current Dataset

| Stock | Ticker | Data Points | Date Range | Indicators | Strategies Tested |
|-------|--------|-------------|------------|------------|-------------------|
| Apple | AAPL | 1,006 | 2020-2024 | 20+ | 8 |
| Microsoft | MSFT | 1,006 | 2020-2024 | 20+ | 8 |
| Google | GOOGL | 1,006 | 2020-2024 | 20+ | 8 |
| Amazon | AMZN | 1,006 | 2020-2024 | 20+ | 8 |
| Tesla | TSLA | 1,006 | 2020-2024 | 20+ | 8 |
| S&P 500 | SPY | 1,006 | 2020-2024 | 20+ | 8 |

**Total**: ~6,000 data points × 30+ features/indicators = ~180,000 data points

## 🎓 Skills Demonstrated

### Technical Skills ✅
- **Python Programming**: OOP, abstract classes, inheritance, polymorphism, type hints
- **Data Science**: Pandas, NumPy, statistical analysis, time-series
- **Financial Analysis**: OHLCV data, returns, technical indicators
- **Algorithm Development**: Trading strategies, signal generation
- **Data Visualization**: Matplotlib, Seaborn, custom plotting, dashboards
- **Version Control**: Git, GitHub, professional commits
- **Software Architecture**: Design patterns, modularity, extensibility
- **Documentation**: Code comments, README, Jupyter notebooks

### Domain Knowledge ✅
- Time-series data processing
- Financial market data structures
- Technical analysis theory
- Trading strategy development
- Signal generation logic
- Position management
- Performance measurement
- Risk-return analysis

### Soft Skills ✅
- Problem-solving and debugging
- Project organization and planning
- Self-directed learning
- Technical documentation
- Portfolio presentation
- Iterative development
- Code quality and standards

## 🧪 Testing

```bash
# Test data loading
python -m src.data.data_loader

# Test preprocessing
python -m src.data.preprocessor

# Test technical indicators
python -m src.indicators.technical_indicators

# Test strategies
python -m src.strategies.ma_crossover
python -m src.strategies.rsi_strategy
python -m src.strategies.bollinger_strategy
python -m src.strategies.combined_strategy

# Test visualizations
python -m src.strategies.strategy_visualizer

# Comprehensive strategy testing
python scripts/test_all_strategies.py

# Generate summaries
python scripts/day2_summary.py
python scripts/day3_summary.py
python scripts/day4_summary.py
```

## 📁 Key Files

| File | Purpose | Lines | Status |
|------|---------|-------|--------|
| `src/data/data_loader.py` | Data acquisition | 150+ | ✅ Complete |
| `src/data/preprocessor.py` | Data cleaning | 200+ | ✅ Complete |
| `src/utils/visualizer.py` | Basic charting | 250+ | ✅ Complete |
| `src/indicators/technical_indicators.py` | Indicators | 450+ | ✅ Complete |
| `src/indicators/indicator_visualizer.py` | Indicator charts | 300+ | ✅ Complete |
| `src/strategies/base_strategy.py` | Strategy framework | 250+ | ✅ Complete |
| `src/strategies/ma_crossover.py` | MA strategies | 150+ | ✅ Complete |
| `src/strategies/rsi_strategy.py` | RSI strategies | 200+ | ✅ Complete |
| `src/strategies/bollinger_strategy.py` | BB strategies | 180+ | ✅ Complete |
| `src/strategies/combined_strategy.py` | Combined strategies | 200+ | ✅ Complete |
| `src/strategies/strategy_visualizer.py` | Strategy viz | 250+ | ✅ Complete |
| `scripts/test_all_strategies.py` | Testing framework | 150+ | ✅ Complete |

**Total Lines of Code**: 2,500+ lines of production-quality Python

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
- ✅ 4 days of focused development completed
- ✅ 9+ technical indicators implemented from scratch
- ✅ 8 trading strategies with multiple variants
- ✅ 70+ professional visualizations created
- ✅ 2,500+ lines of clean, documented code
- ✅ Full Git history showing iterative development
- ✅ Professional project structure and OOP design
- ✅ Comprehensive testing and validation

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

- **Development Time**: 4 days (structured daily progress)
- **Lines of Code**: 2,500+ (Python)
- **Commits**: 30+ (with clear messages)
- **Visualizations**: 70+ (charts and dashboards)
- **Indicators**: 9 (industry-standard implementations)
- **Strategies**: 8 (multiple trading approaches)
- **Data Points**: 180,000+ (6 stocks × 4 years × 30+ features)
- **Test Scripts**: 15+ (automated testing and validation)

---

**Status**: 🟢 Active Development - Day 4 Complete  
**Last Updated**: October 2025  
**Next Milestone**: Day 5 - Backtesting Engine Implementation  
**Completion**: 57% (4/7 days)

---

### 🌟 Star this repository if you find it useful!

### 📊 Progress Tracker

```
[████████████████░░░░░░░░] 57% Complete

✅ Day 1: Environment Setup
✅ Day 2: Data Processing & EDA  
✅ Day 3: Technical Indicators
✅ Day 4: Trading Strategies
⬜ Day 5: Backtesting Engine
⬜ Day 6: Performance Metrics
⬜ Day 7: Final Documentation
```

---

### 🏆 Achievement Summary

| Milestone | Status | Details |
|-----------|--------|---------|
| **Data Pipeline** | ✅ Complete | 6 stocks, 4 years, full preprocessing |
| **Technical Indicators** | ✅ Complete | 9 indicators, all major types covered |
| **Trading Strategies** | ✅ Complete | 8 strategies, 3 strategy types |
| **Visualization** | ✅ Complete | 70+ charts, comprehensive dashboards |
| **Testing Framework** | ✅ Complete | Automated testing, comparisons |
| **Documentation** | ✅ Complete | README, docstrings, notebooks |

---

*Built with ❤️ for learning and portfolio demonstration*  
*Showcasing data science skills in quantitative finance*  
*Demonstrating OOP, algorithm development, and financial analysis*