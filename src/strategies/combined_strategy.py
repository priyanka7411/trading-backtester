"""
Multi-Indicator Combined Strategy
Author: Priyanka
Day 4 - Advanced Strategy

This strategy combines multiple technical indicators for more robust signals.
Uses RSI, MACD, and Bollinger Bands together.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import pandas as pd
import numpy as np
from src.strategies.base_strategy import BaseStrategy


class CombinedStrategy(BaseStrategy):
    """
    Multi-Indicator Combined Strategy
    
    Combines signals from multiple indicators to generate more reliable
    trading signals. Requires agreement from multiple indicators.
    
    Buy Signal (Requires 2 of 3):
        1. RSI < 30 (oversold)
        2. MACD crosses above signal line (bullish)
        3. Price near lower Bollinger Band
    
    Sell Signal (Requires 2 of 3):
        1. RSI > 70 (overbought)
        2. MACD crosses below signal line (bearish)
        3. Price near upper Bollinger Band
    """
    
    def __init__(self, rsi_oversold: float = 30, rsi_overbought: float = 70,
                 min_signals: int = 2):
        """
        Initialize Combined Strategy
        
        Parameters:
        -----------
        rsi_oversold : float
            RSI oversold level
        rsi_overbought : float
            RSI overbought level
        min_signals : int
            Minimum number of confirming signals required (2 or 3)
        """
        super().__init__(f"Combined Strategy (Min Signals={min_signals})")
        self.rsi_oversold = rsi_oversold
        self.rsi_overbought = rsi_overbought
        self.min_signals = min_signals
        
        print(f"RSI Levels: {rsi_oversold}/{rsi_overbought}")
        print(f"Minimum Confirming Signals: {min_signals}")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on multiple indicators
        """
        df = data.copy()
        
        # Ensure all required indicators exist
        required_indicators = ['rsi', 'macd', 'macd_signal', 'bb_upper', 'bb_lower']
        missing = [ind for ind in required_indicators if ind not in df.columns]
        
        if missing:
            raise ValueError(f"Missing required indicators: {missing}")
        
        # Initialize signal columns
        df['rsi_signal'] = 0
        df['macd_signal'] = 0
        df['bb_signal'] = 0
        
        # RSI signals
        df.loc[df['rsi'] < self.rsi_oversold, 'rsi_signal'] = 1
        df.loc[df['rsi'] > self.rsi_overbought, 'rsi_signal'] = -1
        
        # MACD crossovers
        df.loc[(df['macd'] > df['macd_signal']) & 
               (df['macd'].shift(1) <= df['macd_signal'].shift(1)), 'macd_signal'] = 1
        df.loc[(df['macd'] < df['macd_signal']) & 
               (df['macd'].shift(1) >= df['macd_signal'].shift(1)), 'macd_signal'] = -1
        
        # Bollinger Band signals
        df.loc[df['close'] <= df['bb_lower'], 'bb_signal'] = 1
        df.loc[df['close'] >= df['bb_upper'], 'bb_signal'] = -1
        
        # Combine signals
        df['buy_strength'] = (
            (df['rsi_signal'] == 1).astype(int) +
            (df['macd_signal'] == 1).astype(int) +
            (df['bb_signal'] == 1).astype(int)
        )
        
        df['sell_strength'] = (
            (df['rsi_signal'] == -1).astype(int) +
            (df['macd_signal'] == -1).astype(int) +
            (df['bb_signal'] == -1).astype(int)
        )
        
        df['signal'] = 0
        df.loc[df['buy_strength'] >= self.min_signals, 'signal'] = 1
        df.loc[df['sell_strength'] >= self.min_signals, 'signal'] = -1
        
        self.signals = df
        return df


class WeightedCombinedStrategy(BaseStrategy):
    """
    Weighted Multi-Indicator Strategy
    
    Similar to CombinedStrategy but uses weighted scores for each indicator.
    """
    
    def __init__(self, rsi_weight: float = 1.0, 
                 macd_weight: float = 1.5, 
                 bb_weight: float = 1.0,
                 threshold: float = 2.0):
        """
        Initialize Weighted Combined Strategy
        """
        super().__init__("Weighted Combined Strategy")
        self.rsi_weight = rsi_weight
        self.macd_weight = macd_weight
        self.bb_weight = bb_weight
        self.threshold = threshold
        
        print(f"Weights: RSI={rsi_weight}, MACD={macd_weight}, BB={bb_weight}")
        print(f"Signal Threshold: {threshold}")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate signals using weighted indicator scores"""
        df = data.copy()
        
        # Initialize scores
        df['rsi_score'] = 0
        df['macd_score'] = 0
        df['bb_score'] = 0
        
        # RSI scores
        df.loc[df['rsi'] < 30, 'rsi_score'] = 1
        df.loc[df['rsi'] > 70, 'rsi_score'] = -1
        
        # MACD crossovers
        df.loc[(df['macd'] > df['macd_signal']) & 
               (df['macd'].shift(1) <= df['macd_signal'].shift(1)), 'macd_score'] = 1
        df.loc[(df['macd'] < df['macd_signal']) & 
               (df['macd'].shift(1) >= df['macd_signal'].shift(1)), 'macd_score'] = -1
        
        # Bollinger Band scores
        df.loc[df['close'] <= df['bb_lower'], 'bb_score'] = 1
        df.loc[df['close'] >= df['bb_upper'], 'bb_score'] = -1
        
        # Weighted total
        df['total_score'] = (
            df['rsi_score'] * self.rsi_weight +
            df['macd_score'] * self.macd_weight +
            df['bb_score'] * self.bb_weight
        )
        
        df['signal'] = 0
        df.loc[df['total_score'] >= self.threshold, 'signal'] = 1
        df.loc[df['total_score'] <= -self.threshold, 'signal'] = -1
        
        self.signals = df
        return df


# Test function
def test_combined_strategies():
    """Test combined indicator strategies"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "="*60)
    print("TESTING COMBINED STRATEGIES")
    print("="*60)
    
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    strategies = [
        CombinedStrategy(30, 70, 2),
        CombinedStrategy(30, 70, 3),
        WeightedCombinedStrategy(1.0, 1.5, 1.0, 2.0),
        WeightedCombinedStrategy(1.0, 2.0, 1.0, 2.5),
    ]
    
    results = {}
    
    for strategy in strategies:
        print("\n" + "="*60)
        positions = strategy.run(df_with_indicators)
        strategy.print_summary()
        results[strategy.name] = strategy.get_summary_stats()
    
    print("\n" + "="*60)
    print("COMBINED STRATEGY COMPARISON")
    print("="*60)
    
    comparison_df = pd.DataFrame(results).T
    print(comparison_df[['total_trades', 'win_rate', 'total_return', 'average_return']].to_string())
    
    print("\nCombined strategies test complete.")
    
    return strategies


if __name__ == "__main__":
    test_combined_strategies()
