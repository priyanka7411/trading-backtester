"""
Backtesting Engine
Author: Priyanka
Day 5 - Core Backtesting Logic

This module implements the main backtesting engine that simulates
trading strategies with realistic constraints.
"""
import sys
sys.path.append('.')
import pandas as pd
import numpy as np
from typing import Optional
from src.backtester.portfolio import Portfolio
from src.strategies.base_strategy import BaseStrategy


class Backtester:
    """
    Main backtesting engine
    
    Simulates trading strategies with realistic transaction costs,
    position management, and performance tracking.
    """
    
    def __init__(self, 
                 initial_capital: float = 100000,
                 commission: float = 0.001,  # 0.1%
                 slippage: float = 0.0005):   # 0.05%
        """
        Initialize backtester
        """
        self.initial_capital = initial_capital
        self.commission_rate = commission
        self.slippage_rate = slippage
        self.portfolio = None
        self.results = None
        
        print("Backtester initialized")
        print(f"   Initial Capital: ${initial_capital:,.2f}")
        print(f"   Commission: {commission*100:.2f}%")
        print(f"   Slippage: {slippage*100:.3f}%")
    
    def calculate_position_size(self, capital: float, price: float,
                               position_pct: float = 0.95) -> int:
        """Calculate number of shares to buy"""
        max_investment = capital * position_pct
        shares = int(max_investment / price)
        return shares
    
    def apply_slippage(self, price: float, action: str) -> float:
        """Apply slippage to execution price"""
        if action == 'BUY':
            return price * (1 + self.slippage_rate)
        else:
            return price * (1 - self.slippage_rate)
    
    def calculate_commission(self, shares: int, price: float) -> float:
        """Calculate commission cost"""
        trade_value = shares * price
        return trade_value * self.commission_rate
    
    def run(self, data: pd.DataFrame, strategy: BaseStrategy, 
            symbol: str = 'AAPL') -> 'BacktestResults':
        """Run backtest on historical data"""
        print(f"\nRunning backtest: {strategy.name}")
        print(f"   Symbol: {symbol}")
        print(f"   Data points: {len(data)}")
        
        self.portfolio = Portfolio(self.initial_capital)
        
        signals_df = strategy.generate_signals(data.copy())
        positions_df = strategy.calculate_positions(signals_df)
        
        for idx in range(len(positions_df)):
            row = positions_df.iloc[idx]
            
            current_price = row['close']
            current_date = row['date']
            signal = row['signal']
            position = row['position']
            
            if signal == 1:  # Buy
                if not self.portfolio.has_position(symbol):
                    shares = self.calculate_position_size(
                        self.portfolio.cash, current_price
                    )
                    if shares > 0:
                        execution_price = self.apply_slippage(
                            current_price, 'BUY'
                        )
                        commission = self.calculate_commission(
                            shares, execution_price
                        )
                        success = self.portfolio.buy(
                            symbol, shares, execution_price,
                            current_date, commission
                        )
            
            elif signal == -1:  # Sell
                if self.portfolio.has_position(symbol):
                    shares = self.portfolio.get_position(symbol)
                    if shares > 0:
                        execution_price = self.apply_slippage(
                            current_price, 'SELL'
                        )
                        commission = self.calculate_commission(
                            shares, execution_price
                        )
                        success = self.portfolio.sell(
                            symbol, shares, execution_price,
                            current_date, commission
                        )
            
            self.portfolio.record_equity(current_date, {symbol: current_price})
        
        self.results = BacktestResults(
            self.portfolio, strategy, positions_df, symbol
        )
        
        print("Backtest complete!")
        print(f"   Total trades: {len(self.portfolio.trades_history)}")
        
        return self.results


class BacktestResults:
    """
    Backtest results container
    
    Stores and analyzes backtest results with performance metrics.
    """
    
    def __init__(self, portfolio: Portfolio, strategy: BaseStrategy,
                 data: pd.DataFrame, symbol: str):
        """Initialize results"""
        self.portfolio = portfolio
        self.strategy = strategy
        self.data = data
        self.symbol = symbol
        self._calculate_metrics()
    
    def _calculate_metrics(self):
        """Calculate performance metrics"""
        equity_df = self.portfolio.get_equity_curve()
        
        if len(equity_df) == 0:
            self.metrics = {'error': 'No equity data'}
            return
        
        equity_df['returns'] = equity_df['total_value'].pct_change()
        
        initial_value = self.portfolio.initial_capital
        final_value = equity_df['total_value'].iloc[-1]
        total_return = (final_value - initial_value) / initial_value
        
        days = len(equity_df)
        years = days / 252
        
        if years > 0:
            annual_return = (1 + total_return) ** (1 / years) - 1
        else:
            annual_return = 0
        
        daily_vol = equity_df['returns'].std()
        annual_vol = daily_vol * np.sqrt(252)
        
        risk_free_rate = 0.02
        if annual_vol > 0:
            sharpe_ratio = (annual_return - risk_free_rate) / annual_vol
        else:
            sharpe_ratio = 0
        
        equity_df['cummax'] = equity_df['total_value'].cummax()
        equity_df['drawdown'] = (equity_df['total_value'] - equity_df['cummax']) / equity_df['cummax']
        max_drawdown = equity_df['drawdown'].min()
        
        self.metrics = {
            'initial_capital': initial_value,
            'final_value': final_value,
            'total_return': total_return,
            'annual_return': annual_return,
            'total_trades': len(self.portfolio.trades_history),
            'volatility': annual_vol,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'days_traded': days,
            'years': years
        }
    
    def summary(self) -> pd.Series:
        """Get results summary"""
        return pd.Series(self.metrics)
    
    def print_summary(self):
        """Print formatted summary"""
        if 'error' in self.metrics:
            print(f"Warning: {self.metrics['error']}")
            return
        
        print("\n" + "="*70)
        print(f"BACKTEST RESULTS: {self.strategy.name} - {self.symbol}")
        print("="*70)
        
        print(f"\nReturns:")
        print(f"  Initial Capital:    ${self.metrics['initial_capital']:,.2f}")
        print(f"  Final Value:        ${self.metrics['final_value']:,.2f}")
        print(f"  Total Return:       {self.metrics['total_return']:.2%}")
        print(f"  Annualized Return:  {self.metrics['annual_return']:.2%}")
        
        print(f"\nRisk Metrics:")
        print(f"  Volatility (Annual): {self.metrics['volatility']:.2%}")
        print(f"  Sharpe Ratio:        {self.metrics['sharpe_ratio']:.2f}")
        print(f"  Maximum Drawdown:    {self.metrics['max_drawdown']:.2%}")
        
        print(f"\nTrading:")
        print(f"  Total Trades:    {self.metrics['total_trades']}")
        print(f"  Days Traded:     {self.metrics['days_traded']}")
        print(f"  Years:           {self.metrics['years']:.2f}")
        
        print("\n" + "="*70)


# Test function
def test_backtester():
    """Test backtesting engine"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    from src.strategies.ma_crossover import MovingAverageCrossover
    
    print("\n" + "="*70)
    print("TESTING BACKTESTING ENGINE")
    print("="*70)
    
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    strategy = MovingAverageCrossover(50, 200)
    
    backtester = Backtester(
        initial_capital=100000,
        commission=0.001,
        slippage=0.0005
    )
    
    results = backtester.run(df_with_indicators, strategy, 'AAPL')
    
    results.print_summary()
    print("\n")
    results.portfolio.print_summary()
    
    print("\nBacktester test complete!")
    
    return results


if __name__ == "__main__":
    test_backtester()
