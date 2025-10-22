"""
Portfolio Management Module
Author: Priyanka
Day 5 - Portfolio Tracking and Management

This module handles portfolio state, positions, and cash management.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime


class Portfolio:
    """
    Portfolio management system for backtesting
    
    Tracks cash, positions, equity, and transaction history.
    """
    
    def __init__(self, initial_capital: float = 100000):
        """
        Initialize portfolio
        
        Parameters:
        -----------
        initial_capital : float
            Starting capital in dollars
        """
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}  # {symbol: shares}
        self.equity_curve = []  # Track portfolio value over time
        self.trades_history = []  # All executed trades
        
        print(f"Portfolio initialized with ${initial_capital:,.2f}")
    
    def get_position(self, symbol: str) -> int:
        """Get current position for a symbol"""
        return self.positions.get(symbol, 0)
    
    def has_position(self, symbol: str) -> bool:
        """Check if we have a position in this symbol"""
        return self.get_position(symbol) > 0
    
    def buy(self, symbol: str, shares: int, price: float, 
            date: datetime, commission: float = 0) -> bool:
        """
        Execute a buy order
        """
        total_cost = (shares * price) + commission
        
        if total_cost > self.cash:
            return False  # Insufficient funds
        
        # Update cash
        self.cash -= total_cost
        
        # Update position
        current_shares = self.positions.get(symbol, 0)
        self.positions[symbol] = current_shares + shares
        
        # Record trade
        self.trades_history.append({
            'date': date,
            'symbol': symbol,
            'action': 'BUY',
            'shares': shares,
            'price': price,
            'commission': commission,
            'total_cost': total_cost,
            'cash_after': self.cash
        })
        
        return True
    
    def sell(self, symbol: str, shares: int, price: float,
             date: datetime, commission: float = 0) -> bool:
        """
        Execute a sell order
        """
        current_shares = self.positions.get(symbol, 0)
        
        if shares > current_shares:
            return False  # Not enough shares
        
        proceeds = (shares * price) - commission
        
        # Update cash
        self.cash += proceeds
        
        # Update position
        self.positions[symbol] = current_shares - shares
        if self.positions[symbol] == 0:
            del self.positions[symbol]
        
        # Record trade
        self.trades_history.append({
            'date': date,
            'symbol': symbol,
            'action': 'SELL',
            'shares': shares,
            'price': price,
            'commission': commission,
            'total_proceeds': proceeds,
            'cash_after': self.cash
        })
        
        return True
    
    def get_portfolio_value(self, current_prices: Dict[str, float]) -> float:
        """
        Calculate total portfolio value
        """
        positions_value = sum(
            shares * current_prices.get(symbol, 0)
            for symbol, shares in self.positions.items()
        )
        
        return self.cash + positions_value
    
    def record_equity(self, date: datetime, prices: Dict[str, float]):
        """
        Record current portfolio value
        """
        total_value = self.get_portfolio_value(prices)
        
        self.equity_curve.append({
            'date': date,
            'cash': self.cash,
            'positions_value': total_value - self.cash,
            'total_value': total_value
        })
    
    def get_equity_curve(self) -> pd.DataFrame:
        """Get equity curve as DataFrame"""
        return pd.DataFrame(self.equity_curve)
    
    def get_trades(self) -> pd.DataFrame:
        """Get all trades as DataFrame"""
        return pd.DataFrame(self.trades_history)
    
    def get_summary(self) -> Dict:
        """Get portfolio summary statistics"""
        if not self.equity_curve:
            return {'error': 'No equity data'}
        
        equity_df = self.get_equity_curve()
        
        final_value = equity_df['total_value'].iloc[-1]
        total_return = (final_value - self.initial_capital) / self.initial_capital
        
        equity_df['returns'] = equity_df['total_value'].pct_change()
        
        summary = {
            'initial_capital': self.initial_capital,
            'final_value': final_value,
            'total_return': total_return,
            'total_return_pct': total_return * 100,
            'total_trades': len(self.trades_history),
            'final_cash': self.cash,
            'active_positions': len(self.positions),
            'max_value': equity_df['total_value'].max(),
            'min_value': equity_df['total_value'].min(),
        }
        
        return summary
    
    def print_summary(self):
        """Print portfolio summary"""
        summary = self.get_summary()
        
        if 'error' in summary:
            print(f"Warning: {summary['error']}")
            return
        
        print("\n" + "="*60)
        print("PORTFOLIO SUMMARY")
        print("="*60)
        print(f"\nCapital:")
        print(f"  Initial: ${summary['initial_capital']:,.2f}")
        print(f"  Final:   ${summary['final_value']:,.2f}")
        print(f"  Return:  {summary['total_return_pct']:.2f}%")
        
        print(f"\nTrading:")
        print(f"  Total Trades: {summary['total_trades']}")
        print(f"  Active Positions: {summary['active_positions']}")
        
        print(f"\nCurrent State:")
        print(f"  Cash: ${summary['final_cash']:,.2f}")
        
        print(f"\nPerformance:")
        print(f"  Max Value: ${summary['max_value']:,.2f}")
        print(f"  Min Value: ${summary['min_value']:,.2f}")
        
        print("\n" + "="*60)


# Test function
def test_portfolio():
    """Test portfolio management"""
    print("\n" + "="*60)
    print("TESTING PORTFOLIO MANAGEMENT")
    print("="*60)
    
    portfolio = Portfolio(initial_capital=100000)
    
    from datetime import datetime
    date1 = datetime(2020, 1, 1)
    date2 = datetime(2020, 1, 5)
    date3 = datetime(2020, 1, 10)
    
    print(f"\nBuying 100 shares at $150")
    success = portfolio.buy('AAPL', 100, 150.0, date1, commission=10)
    print(f"   Success: {success}")
    print(f"   Cash remaining: ${portfolio.cash:,.2f}")
    
    portfolio.record_equity(date1, {'AAPL': 150.0})
    
    print(f"\nBuying 50 shares at $160")
    success = portfolio.buy('AAPL', 50, 160.0, date2, commission=10)
    print(f"   Success: {success}")
    print(f"   Cash remaining: ${portfolio.cash:,.2f}")
    print(f"   Total AAPL shares: {portfolio.get_position('AAPL')}")
    
    portfolio.record_equity(date2, {'AAPL': 160.0})
    
    print(f"\nSelling 75 shares at $170")
    success = portfolio.sell('AAPL', 75, 170.0, date3, commission=10)
    print(f"   Success: {success}")
    print(f"   Cash after: ${portfolio.cash:,.2f}")
    print(f"   Remaining AAPL shares: {portfolio.get_position('AAPL')}")
    
    portfolio.record_equity(date3, {'AAPL': 170.0})
    
    portfolio.print_summary()
    
    print("\nTRADE HISTORY:")
    print(portfolio.get_trades().to_string())
    
    print("\nEQUITY CURVE:")
    print(portfolio.get_equity_curve().to_string())
    
    print("\nPortfolio test complete!")


if __name__ == "__main__":
    test_portfolio()
