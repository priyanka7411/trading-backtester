"""
Base Strategy Class
Author: Priyanka
Day 4 - Trading Strategy Framework

This module defines the base class that all trading strategies inherit from.
"""

from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from typing import Dict, Any


class BaseStrategy(ABC):
    """
    Abstract base class for trading strategies
    
    All trading strategies must inherit from this class and implement
    the generate_signals method.
    """
    
    def __init__(self, name: str):
        """
        Initialize the base strategy
        
        Parameters:
        -----------
        name : str
            Name of the strategy
        """
        self.name = name
        self.signals = None
        self.positions = None
        self.trades = []
        print(f"{self.name} initialized!")
    
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on the strategy logic
        
        This method must be implemented by all strategy subclasses.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Historical price data with indicators
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with signal column added
            Signal values: 1 (Buy), -1 (Sell), 0 (Hold)
        """
        pass
    
    def calculate_positions(self, signals: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate positions based on signals
        
        Parameters:
        -----------
        signals : pd.DataFrame
            DataFrame with signal column
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with positions column
            Position values: 1 (Long), 0 (Out of market), -1 (Short - if allowed)
        """
        df = signals.copy()
        df['position'] = 0
        
        current_position = 0
        positions = []
        
        for i in range(len(df)):
            signal = df['signal'].iloc[i]
            
            if signal == 1 and current_position == 0:
                current_position = 1
            elif signal == -1 and current_position == 1:
                current_position = 0
            
            positions.append(current_position)
        
        df['position'] = positions
        self.positions = df
        
        return df
    
    def identify_trades(self, positions: pd.DataFrame) -> list:
        """
        Identify entry and exit points from positions
        
        Parameters:
        -----------
        positions : pd.DataFrame
            DataFrame with positions
            
        Returns:
        --------
        list
            List of trade dictionaries with entry/exit info
        """
        trades = []
        in_position = False
        entry_idx = None
        
        for i in range(len(positions)):
            position = positions['position'].iloc[i]
            
            if position == 1 and not in_position:
                entry_idx = i
                in_position = True
            
            elif position == 0 and in_position:
                exit_idx = i
                
                trade = {
                    'entry_date': positions['date'].iloc[entry_idx],
                    'entry_price': positions['close'].iloc[entry_idx],
                    'exit_date': positions['date'].iloc[exit_idx],
                    'exit_price': positions['close'].iloc[exit_idx],
                    'return': (positions['close'].iloc[exit_idx] - positions['close'].iloc[entry_idx]) / positions['close'].iloc[entry_idx],
                    'holding_period': exit_idx - entry_idx
                }
                
                trades.append(trade)
                in_position = False
        
        self.trades = trades
        return trades
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """
        Calculate summary statistics for the strategy
        
        Returns:
        --------
        dict
            Dictionary with strategy performance metrics
        """
        if not self.trades:
            return {
                'total_trades': 0,
                'message': 'No trades generated'
            }
        
        returns = [trade['return'] for trade in self.trades]
        winning_trades = [r for r in returns if r > 0]
        losing_trades = [r for r in returns if r < 0]
        
        stats = {
            'strategy_name': self.name,
            'total_trades': len(self.trades),
            'winning_trades': len(winning_trades),
            'losing_trades': len(losing_trades),
            'win_rate': len(winning_trades) / len(self.trades) if self.trades else 0,
            'average_return': np.mean(returns) if returns else 0,
            'total_return': np.sum(returns) if returns else 0,
            'best_trade': max(returns) if returns else 0,
            'worst_trade': min(returns) if returns else 0,
            'avg_winning_trade': np.mean(winning_trades) if winning_trades else 0,
            'avg_losing_trade': np.mean(losing_trades) if losing_trades else 0,
            'avg_holding_period': np.mean([t['holding_period'] for t in self.trades])
        }
        
        return stats
    
    def print_summary(self):
        """Print strategy summary statistics"""
        stats = self.get_summary_stats()
        
        print("\n" + "="*60)
        print(f"STRATEGY SUMMARY: {self.name}")
        print("="*60)
        
        if stats.get('message'):
            print(f"{stats['message']}")
            return
        
        print(f"\nTrade Statistics:")
        print(f"  Total Trades: {stats['total_trades']}")
        print(f"  Winning Trades: {stats['winning_trades']}")
        print(f"  Losing Trades: {stats['losing_trades']}")
        print(f"  Win Rate: {stats['win_rate']:.2%}")
        
        print(f"\nReturns:")
        print(f"  Total Return: {stats['total_return']:.2%}")
        print(f"  Average Return per Trade: {stats['average_return']:.2%}")
        print(f"  Best Trade: {stats['best_trade']:.2%}")
        print(f"  Worst Trade: {stats['worst_trade']:.2%}")
        
        print(f"\nTrade Analysis:")
        print(f"  Avg Winning Trade: {stats['avg_winning_trade']:.2%}")
        print(f"  Avg Losing Trade: {stats['avg_losing_trade']:.2%}")
        print(f"  Avg Holding Period: {stats['avg_holding_period']:.1f} days")
        
        print("\n" + "="*60)
    
    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Complete strategy execution pipeline
        
        Parameters:
        -----------
        data : pd.DataFrame
            Historical price data with indicators
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with signals and positions
        """
        print(f"Running {self.name}...")
        
        signals = self.generate_signals(data)
        positions = self.calculate_positions(signals)
        trades = self.identify_trades(positions)
        
        print(f"Generated {len(trades)} trades")
        
        return positions


class SimpleStrategy(BaseStrategy):
    """
    Simple example strategy for testing the base class
    Buys when price crosses above 20-day MA, sells when crosses below
    """
    
    def __init__(self):
        super().__init__("Simple MA Strategy")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate signals based on MA crossover"""
        df = data.copy()
        df['signal'] = 0
        df.loc[df['close'] > df['sma_20'], 'signal'] = 1
        df.loc[df['close'] < df['sma_20'], 'signal'] = -1
        return df


def test_base_strategy():
    """Test the base strategy class"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "="*60)
    print("TESTING BASE STRATEGY CLASS")
    print("="*60)
    
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    strategy = SimpleStrategy()
    results = strategy.run(df_with_indicators)
    
    strategy.print_summary()
    
    if strategy.trades:
        print("\nSample Trades (First 5):")
        print("-" * 60)
        for i, trade in enumerate(strategy.trades[:5], 1):
            print(f"\nTrade {i}:")
            print(f"  Entry: {trade['entry_date']} @ ${trade['entry_price']:.2f}")
            print(f"  Exit:  {trade['exit_date']} @ ${trade['exit_price']:.2f}")
            print(f"  Return: {trade['return']:.2%}")
            print(f"  Days: {trade['holding_period']}")
    
    print("\nBase strategy test complete!")
    return strategy


if __name__ == "__main__":
    test_base_strategy()
