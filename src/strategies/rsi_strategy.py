"""
RSI Trading Strategy
Author: Priyanka
Day 4 - Mean Reversion Strategy

This strategy uses RSI (Relative Strength Index) to identify
overbought and oversold conditions for mean reversion trading.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pandas as pd
import numpy as np
from src.strategies.base_strategy import BaseStrategy


class RSIStrategy(BaseStrategy):
    """
    RSI (Relative Strength Index) Trading Strategy
    
    Mean reversion strategy that buys when RSI indicates oversold
    conditions and sells when RSI indicates overbought conditions.
    
    Buy Signal:
        When RSI crosses below oversold threshold (e.g., 30)
    
    Sell Signal:
        When RSI crosses above overbought threshold (e.g., 70)
    """
    
    def __init__(self, rsi_period: int = 14, 
                 oversold: float = 30, 
                 overbought: float = 70):
        """
        Initialize RSI Strategy
        
        Parameters:
        -----------
        rsi_period : int
            Period for RSI calculation (default: 14)
        oversold : float
            RSI level considered oversold (default: 30)
        overbought : float
            RSI level considered overbought (default: 70)
        """
        super().__init__(f"RSI Strategy (Period={rsi_period})")
        self.rsi_period = rsi_period
        self.oversold = oversold
        self.overbought = overbought
        
        print(f"   RSI Period: {rsi_period}")
        print(f"   Oversold Level: {oversold}")
        print(f"   Overbought Level: {overbought}")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on RSI levels
        
        Parameters:
        -----------
        data : pd.DataFrame
            Historical price data with RSI indicator
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with signal column added
        """
        df = data.copy()
        
        # Check if RSI exists, if not calculate it
        if 'rsi' not in df.columns:
            from src.indicators.technical_indicators import TechnicalIndicators
            indicators = TechnicalIndicators()
            df['rsi'] = indicators.rsi(df['close'], self.rsi_period)
        
        # Initialize signal column
        df['signal'] = 0
        
        # Buy signal: RSI crosses below oversold level
        df.loc[(df['rsi'] < self.oversold) & 
               (df['rsi'].shift(1) >= self.oversold), 'signal'] = 1
        
        # Sell signal: RSI crosses above overbought level
        df.loc[(df['rsi'] > self.overbought) & 
               (df['rsi'].shift(1) <= self.overbought), 'signal'] = -1
        
        self.signals = df
        
        return df


class RSIEnhancedStrategy(BaseStrategy):
    """
    Enhanced RSI Strategy with trend filter
    
    Only takes trades in the direction of the trend:
    - Buy on oversold RSI when above 200-day MA (uptrend)
    - Sell on overbought RSI when below 200-day MA (downtrend)
    """
    
    def __init__(self, rsi_period: int = 14, 
                 oversold: float = 30, 
                 overbought: float = 70,
                 trend_ma: int = 200):
        """
        Initialize Enhanced RSI Strategy
        
        Parameters:
        -----------
        rsi_period : int
            Period for RSI calculation
        oversold : float
            RSI oversold level
        overbought : float
            RSI overbought level
        trend_ma : int
            Moving average for trend filter
        """
        super().__init__(f"Enhanced RSI Strategy (RSI={rsi_period}, MA={trend_ma})")
        self.rsi_period = rsi_period
        self.oversold = oversold
        self.overbought = overbought
        self.trend_ma = trend_ma
        
        print(f"   RSI Period: {rsi_period}")
        print(f"   Oversold: {oversold}, Overbought: {overbought}")
        print(f"   Trend Filter: {trend_ma}-day MA")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate signals with trend filter"""
        df = data.copy()
        
        # Ensure indicators exist
        if 'rsi' not in df.columns:
            from src.indicators.technical_indicators import TechnicalIndicators
            indicators = TechnicalIndicators()
            df['rsi'] = indicators.rsi(df['close'], self.rsi_period)
        
        if f'sma_{self.trend_ma}' not in df.columns:
            df[f'sma_{self.trend_ma}'] = df['close'].rolling(
                window=self.trend_ma
            ).mean()
        
        # Initialize signal column
        df['signal'] = 0
        
        # Determine trend
        df['uptrend'] = df['close'] > df[f'sma_{self.trend_ma}']
        
        # Buy: Oversold RSI in uptrend
        df.loc[(df['rsi'] < self.oversold) & 
               (df['rsi'].shift(1) >= self.oversold) & 
               (df['uptrend']), 'signal'] = 1
        
        # Sell: Overbought RSI (exit long positions)
        df.loc[(df['rsi'] > self.overbought) & 
               (df['rsi'].shift(1) <= self.overbought), 'signal'] = -1
        
        self.signals = df
        
        return df


def test_rsi_strategies():
    """Test RSI-based strategies"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "=" * 60)
    print("TESTING RSI STRATEGIES")
    print("=" * 60)
    
    # Load data
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    # Test different RSI strategies
    strategies = [
        RSIStrategy(14, 30, 70),          # Standard
        RSIStrategy(14, 20, 80),          # Conservative
        RSIStrategy(14, 40, 60),          # Aggressive
        RSIEnhancedStrategy(14, 30, 70),  # With trend filter
    ]
    
    results = {}
    
    for strategy in strategies:
        print("\n" + "=" * 60)
        positions = strategy.run(df_with_indicators)
        strategy.print_summary()
        results[strategy.name] = strategy.get_summary_stats()
    
    # Comparison
    print("\n" + "=" * 60)
    print("RSI STRATEGY COMPARISON")
    print("=" * 60)
    
    comparison_df = pd.DataFrame(results).T
    print(comparison_df[['total_trades', 'win_rate', 'total_return', 
                        'average_return']].to_string())
    
    print("\nRSI strategies test complete!")
    
    return strategies


if __name__ == "__main__":
    test_rsi_strategies()
