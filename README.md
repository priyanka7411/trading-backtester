# 📈 Algorithmic Trading Strategy Backtester

> A comprehensive backtesting framework for evaluating algorithmic trading strategies with professional performance analytics and visualization.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Development](https://img.shields.io/badge/development-Day%205%20Complete-brightgreen)]()

## 🎯 Project Overview

This project implements a professional-grade backtesting system that enables quantitative analysis of trading strategies using historical market data. Built as a data science portfolio project, it demonstrates expertise in:

- **Financial Data Analysis**: Processing and analyzing time-series market data
- **Technical Analysis**: Implementing industry-standard trading indicators
- **Algorithm Development**: Building and optimizing trading strategies
- **Backtesting Engineering**: Realistic trade simulation with transaction costs
- **Portfolio Management**: Cash and position tracking systems
- **Performance Analytics**: Comprehensive metrics and risk analysis
- **Statistical Modeling**: Performance evaluation with quantitative metrics
- **Data Visualization**: Creating professional charts and interactive dashboards
- **Software Engineering**: Clean code, OOP principles, modular architecture, and version control

## ✨ Key Features

- 📊 **Multi-Strategy Support**: 8+ trading strategies with multiple variants
- 📈 **Real Market Data**: Integration with Yahoo Finance for historical data
- ⚙️ **Realistic Backtesting**: Order execution with commission & slippage
- 💼 **Portfolio Management**: Complete cash and position tracking
- 🎨 **Professional Visualizations**: 100+ charts and performance dashboards
- 📉 **Comprehensive Metrics**: Sharpe ratio, drawdown, returns analysis
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
│   ├── backtester/                # Core backtesting engine
│   │   ├── portfolio.py          # ✅ Portfolio management
│   │   ├── engine.py             # ✅ Backtesting engine
│   │   └── visualizer.py         # ✅ Backtest visualization
│   └── utils/                     # Utility functions
│       └── visualizer.py         # ✅ Professional charting
│
├── scripts/                       # Automation scripts
│   ├── download_all_data.py      # ✅ Batch data download
│   ├── process_all_stocks.py     # ✅ Batch processing
│   ├── add_indicators_all_stocks.py  # ✅ Batch indicator addition
│   ├── test_all_strategies.py    # ✅ Strategy testing framework
│   ├── run_backtests.py          # ✅ Comprehensive backtesting
│   ├── day2_summary.py           # ✅ Progress reporting
│   ├── day3_summary.py           # ✅ Indicator summary
│   ├── day4_summary.py           # ✅ Strategy summary
│   └── day5_summary.py           # ✅ Backtest summary
│
├── notebooks/                     # Jupyter analysis notebooks
│   ├── 01_data_exploration.ipynb # ✅ EDA & visualization
│   └── 02_technical_indicators_analysis.ipynb # ✅ Indicator analysis
│
├── tests/                         # Unit tests
├── results/                       # Backtest outputs
│   ├── reports/                   # ✅ Performance reports & summaries
│   │   ├── strategy_comparison.csv    # ✅ Strategy metrics
│   │   └── backtest_comparison.csv    # ✅ Backtest results
│   └── figures/                   # ✅ Generated charts (100+ visualizations)
│       ├── indicators/            # ✅ Technical indicator dashboards
│       ├── strategies/            # ✅ Strategy signal & performance charts
│       └── backtests/             # ✅ Backtest equity curves & analysis
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

6. **Run backtests**
```bash
python scripts/run_backtests.py
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

### Trading Strategies (Day 4)

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

# Visualize signals
viz = StrategyVisualizer()
viz.plot_signals(ma_strategy, 'AAPL')
viz.compare_strategies([ma_strategy, rsi_strategy, combined], 'AAPL')
```

### Backtesting (Day 5 Complete) ✅

```python
from src.backtester.engine import Backtester
from src.backtester.visualizer import BacktestVisualizer

# Initialize backtester with realistic constraints
backtester = Backtester(
    initial_capital=100000,
    commission=0.001,  # 0.1% commission
    slippage=0.0005    # 0.05% slippage
)

# Run backtest
results = backtester.run(df_with_indicators, ma_strategy, 'AAPL')

# View performance metrics
results.print_summary()
print(results.summary())

# Create visualizations
viz = BacktestVisualizer()
viz.plot_equity_curve(results)
viz.plot_drawdown(results)
viz.plot_returns_distribution(results)
viz.create_performance_dashboard(results)
```

## 📊 Current Capabilities (Day 5 Complete)

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
| **Moving Averages** | 5, 10, 20, 50-period averages |
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
| Strategy | Type | Description | Backtested |
|----------|------|-------------|------------|
| **MA Crossover (50/200)** | Trend Following | Classic golden/death cross | ✅ |
| **RSI Strategy** | Mean Reversion | Oversold/overbought trading | ✅ |
| **Bollinger Bands** | Mean Reversion | Price extremes at bands | ✅ |
| **Combined Strategy** | Multi-Indicator | Requires 2 of 3 signals | ✅ |

### Backtesting Engine ✅
| Feature | Description | Status |
|---------|-------------|--------|
| **Order Execution** | Realistic buy/sell simulation | ✅ Complete |
| **Transaction Costs** | Commission (0.1%) & Slippage (0.05%) | ✅ Complete |
| **Portfolio Management** | Cash and position tracking | ✅ Complete |
| **Position Sizing** | Percentage-based allocation | ✅ Complete |
| **Trade Logging** | Complete history of all trades | ✅ Complete |
| **Equity Curve** | Portfolio value tracking | ✅ Complete |
| **Performance Metrics** | Returns, Sharpe, Drawdown | ✅ Complete |

### Performance Metrics ✅
- **Total Return**: Overall portfolio return
- **Annualized Return**: Return adjusted for time
- **Sharpe Ratio**: Risk-adjusted returns (vs 2% risk-free rate)
- **Maximum Drawdown**: Largest peak-to-trough decline
- **Volatility**: Annualized standard deviation of returns
- **Total Trades**: Number of round-trip trades executed
- **Days Traded**: Total trading period

### Visualizations ✅
**Data Analysis:**
- Price History
- Volume Analysis
- Returns Distribution
- Correlation Matrix
- Monthly Returns

**Technical Indicators:**
- RSI with Levels
- MACD with Histogram
- Bollinger Bands
- Stochastic Oscillator
- Complete Dashboards

**Strategy Analysis:**
- Buy/Sell Signals
- Position Tracking
- Trade Returns
- Strategy Comparison

**Backtest Results:**
- Equity Curves
- Drawdown Analysis
- Returns Distribution
- Trade P&L
- Monthly Returns Heatmap
- Performance Dashboards

**Total:** 100+ professional visualizations

## 🎯 Performance Metrics (Day 6 - Coming Next)

- **Advanced Risk Metrics**: Sortino Ratio, Calmar Ratio, Conditional VaR
- **Benchmark Comparison**: Compare vs SPY (S&P 500)
- **Statistical Tests**: Strategy significance and robustness
- **Monte Carlo Simulation**: Strategy stress testing
- **Parameter Optimization**: Find optimal strategy parameters

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
- ✅ VSCode setup with extensions
- ✅ Professional project structure created
- ✅ GitHub repository initialized
- ✅ Virtual environment and dependencies installed
- ✅ Git workflow established

### ✅ Day 2 - Data Preprocessing & Exploration (Complete)
- ✅ Downloaded 6 stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, SPY)
- ✅ Data cleaning and validation module
- ✅ Feature engineering (8+ features)
- ✅ Exploratory data analysis notebook
- ✅ Professional visualization module
- ✅ 20+ charts and reports

### ✅ Day 3 - Technical Indicators (Complete) ⭐
- ✅ Implemented 9+ technical indicators
- ✅ Indicator visualization module
- ✅ Multi-panel technical analysis dashboards
- ✅ Multi-indicator signal generation
- ✅ Indicator correlation analysis
- ✅ 30+ indicator visualizations

### ✅ Day 4 - Trading Strategies (Complete) 🎯
- ✅ BaseStrategy abstract class framework
- ✅ 8 trading strategies implemented
  - MA Crossover (3 variants)
  - RSI Strategies (2 variants)
  - Bollinger Bands (2 variants)
  - Combined Strategies (2 variants)
- ✅ Strategy visualization module
- ✅ Automated testing framework
- ✅ Strategy performance comparison

### ✅ Day 5 - Backtesting Engine (Complete) ⚙️
- ✅ Portfolio Management System
  - Cash tracking
  - Position management
  - Trade history logging
  - Equity curve generation
- ✅ Backtesting Engine
  - Order execution simulation
  - Transaction costs (commission & slippage)
  - Position sizing logic
  - Buy/sell order processing
- ✅ Performance Tracking
  - Returns calculation
  - Sharpe ratio
  - Maximum drawdown
  - Volatility measurement
- ✅ Backtest Visualization
  - Equity curves
  - Drawdown analysis
  - Returns distribution
  - Trade P&L charts
  - Monthly returns heatmap
  - Performance dashboards
- ✅ Automated backtest execution
- ✅ Multi-strategy comparison
- ✅ Results reporting and ranking

### 📅 Day 6 - Advanced Performance Metrics (Next)
- Sortino and Calmar ratios
- Value at Risk (VaR)
- Benchmark comparison (vs SPY)
- Statistical significance tests
- Monte Carlo simulations
- Parameter optimization
- Risk-return scatter plots

### 📅 Day 7 - Final Documentation & Presentation
- Comprehensive performance reports
- Final visualization suite
- Complete documentation
- Portfolio presentation materials
- Code cleanup and refactoring
- Final testing
- Project showcase

## 📊 Current Dataset

| Stock | Ticker | Data Points | Date Range | Indicators | Strategies | Backtested |
|-------|--------|-------------|------------|------------|------------|------------|
| Apple | AAPL | 1,006 | 2020-2024 | 20+ | 8 | ✅ |
| Microsoft | MSFT | 1,006 | 2020-2024 | 20+ | 8 | Ready |
| Google | GOOGL | 1,006 | 2020-2024 | 20+ | 8 | Ready |
| Amazon | AMZN | 1,006 | 2020-2024 | 20+ | 8 | Ready |
| Tesla | TSLA | 1,006 | 2020-2024 | 20+ | 8 | Ready |
| S&P 500 | SPY | 1,006 | 2020-2024 | 20+ | 8 | Ready |

**Total**: ~6,000 data points × 30+ features/indicators = ~180,000 data points

## 🎓 Skills Demonstrated

### Technical Skills ✅
- **Python Programming**: OOP, abstract classes, inheritance, polymorphism, type hints
- **Data Science**: Pandas, NumPy, statistical analysis, time-series
- **Financial Engineering**: Portfolio management, order execution, transaction costs
- **Algorithm Development**: Trading strategies, signal generation, backtesting
- **Quantitative Analysis**: Returns calculation, risk metrics, performance measurement
- **Data Visualization**: Matplotlib, Seaborn, custom plotting, dashboards
- **Version Control**: Git, GitHub, professional commits
- **Software Architecture**: Design patterns, modularity, state management
- **Documentation**: Code comments, README, Jupyter notebooks

### Domain Knowledge ✅
- Time-series data processing
- Financial market data structures
- Technical analysis theory
- Trading strategy development
- Portfolio management principles
- Risk-return analysis
- Performance attribution
- Transaction cost modeling

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
# Test portfolio management
python -m src.backtester.portfolio

# Test backtesting engine
python -m src.backtester.engine

# Test visualizations
python -m src.backtester.visualizer

# Run comprehensive backtests
python scripts/run_backtests.py

# Generate summaries
python scripts/day5_summary.py
```

## 📁 Key Files

| File | Purpose | Lines | Status |
|------|---------|-------|--------|
| `src/data/data_loader.py` | Data acquisition | 150+ | ✅ Complete |
| `src/data/preprocessor.py` | Data cleaning | 200+ | ✅ Complete |
| `src/indicators/technical_indicators.py` | Indicators | 450+ | ✅ Complete |
| `src/strategies/base_strategy.py` | Strategy framework | 250+ | ✅ Complete |
| `src/strategies/ma_crossover.py` | MA strategies | 150+ | ✅ Complete |
| `src/strategies/rsi_strategy.py` | RSI strategies | 200+ | ✅ Complete |
| `src/strategies/bollinger_strategy.py` | BB strategies | 180+ | ✅ Complete |
| `src/strategies/combined_strategy.py` | Combined strategies | 200+ | ✅ Complete |
| `src/backtester/portfolio.py` | Portfolio management | 300+ | ✅ Complete |
| `src/backtester/engine.py` | Backtesting engine | 350+ | ✅ Complete |
| `src/backtester/visualizer.py` | Backtest visualization | 400+ | ✅ Complete |
| `scripts/run_backtests.py` | Backtest automation | 150+ | ✅ Complete |

**Total Lines of Code**: 4,000+ lines of production-quality Python

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
- ✅ 5 days of focused development completed
- ✅ 9+ technical indicators implemented from scratch
- ✅ 8 trading strategies with backtesting
- ✅ Complete portfolio management system
- ✅ Realistic backtesting engine with transaction costs
- ✅ 100+ professional visualizations created
- ✅ 4,000+ lines of clean, documented code
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

- **Development Time**: 5 days (structured daily progress)
- **Lines of Code**: 4,000+ (Python)
- **Commits**: 40+ (with clear messages)
- **Visualizations**: 100+ (charts and dashboards)
- **Indicators**: 9 (industry-standard implementations)
- **Strategies**: 8 (multiple trading approaches)
- **Backtests**: Complete with transaction costs
- **Data Points**: 180,000+ (6 stocks × 4 years × 30+ features)
- **Test Scripts**: 20+ (automated testing and validation)

---

**Status**: 🟢 Active Development - Day 5 Complete  
**Last Updated**: October 2025  
**Next Milestone**: Day 6 - Advanced Performance Metrics & Analysis  
**Completion**: 71% (5/7 days)

---

### 🌟 Star this repository if you find it useful!

### 📊 Progress Tracker

```
[████████████████████░░░░] 71% Complete

✅ Day 1: Environment Setup
✅ Day 2: Data Processing & EDA  
✅ Day 3: Technical Indicators
✅ Day 4: Trading Strategies
✅ Day 5: Backtesting Engine
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
| **Backtesting Engine** | ✅ Complete | Realistic simulation with costs |
| **Portfolio Management** | ✅ Complete | Full state tracking system |
| **Visualization** | ✅ Complete | 100+ charts, comprehensive dashboards |
| **Testing Framework** | ✅ Complete | Automated testing, comparisons |
| **Documentation** | ✅ Complete | README, docstrings, notebooks |

---

*Built with ❤️ for learning and portfolio demonstration*  
*Showcasing data science skills in quantitative finance*  
*Demonstrating OOP, algorithm development, financial engineering, and backtesting*