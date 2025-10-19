"""
Moving Average Crossover Strategy
Author: Priyanka
Day 4 - Trend Following Strategy

This strategy uses two moving averages:
- Golden Cross: Short MA crosses above Long MA → BUY
- Death Cross: Short MA crosses below Long MA → SELL
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pandas as pd
import numpy as np
from src.strategies.base_strategy import BaseStrategy


class MovingAverageCrossover(BaseStrategy):
    """
    Moving Average Crossover Trading Strategy
    
    Classic trend-following strategy that generates signals based on
    the crossover of two moving averages of different periods.
    
    Buy Signal (Golden Cross):
        When fast MA crosses above slow MA
    
    Sell Signal (Death Cross):
        When fast MA crosses below slow MA
    """
    
    def __init__(self, short_window: int = 50, long_window: int = 200):
        """
        Initialize MA Crossover Strategy
        
        Parameters:
        -----------
        short_window : int
            Period for short (fast) moving average (default: 50)
        long_window : int
            Period for long (slow) moving average (default: 200)
        """
        super().__init__(f"MA Crossover ({short_window}/{long_window})")
        self.short_window = short_window
        self.long_window = long_window
        
        print(f"   Short MA: {short_window} days")
        print(f"   Long MA: {long_window} days")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on MA crossover
        
        Parameters:
        -----------
        data : pd.DataFrame
            Historical price data
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with signal column added
        """
        df = data.copy()
        
        if f'sma_{self.short_window}' not in df.columns:
            df[f'sma_{self.short_window}'] = df['close'].rolling(
                window=self.short_window
            ).mean()
        
        if f'sma_{self.long_window}' not in df.columns:
            df[f'sma_{self.long_window}'] = df['close'].rolling(
                window=self.long_window
            ).mean()
        
        df['signal'] = 0
        
        short_ma = df[f'sma_{self.short_window}']
        long_ma = df[f'sma_{self.long_window}']
        
        df.loc[(short_ma > long_ma) & 
               (short_ma.shift(1) <= long_ma.shift(1)), 'signal'] = 1
        
        df.loc[(short_ma < long_ma) & 
               (short_ma.shift(1) >= long_ma.shift(1)), 'signal'] = -1
        
        df['short_ma'] = short_ma
        df['long_ma'] = long_ma
        
        self.signals = df
        
        return df


def test_ma_crossover():
    """Test the MA Crossover strategy"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "="*60)
    print("TESTING MA CROSSOVER STRATEGY")
    print("="*60)
    
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    strategies = [
        MovingAverageCrossover(10, 50),
        MovingAverageCrossover(50, 200),
        MovingAverageCrossover(20, 100),
    ]
    
    results = {}
    
    for strategy in strategies:
        print(f"\n{'='*60}")
        positions = strategy.run(df_with_indicators)
        strategy.print_summary()
        results[strategy.name] = strategy.get_summary_stats()
    
    print("\n" + "="*60)
    print("STRATEGY COMPARISON")
    print("="*60)
    
    comparison_df = pd.DataFrame(results).T
    print(comparison_df[['total_trades', 'win_rate', 'total_return', 
                        'average_return']].to_string())
    
    print("\nMA Crossover test complete!")
    
    return strategies[1]


if __name__ == "__main__":
    test_ma_crossover()
