"""
Bollinger Bands Mean Reversion Strategy
Author: Priyanka
Day 4 - Volatility-Based Strategy

This strategy uses Bollinger Bands to identify mean reversion opportunities.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pandas as pd
import numpy as np
from src.strategies.base_strategy import BaseStrategy


class BollingerBandsStrategy(BaseStrategy):
    """
    Bollinger Bands Mean Reversion Strategy
    
    Trades based on price touching or breaking the Bollinger Bands,
    expecting mean reversion to the middle band.
    
    Buy Signal:
        When price touches or crosses below the lower band
    
    Sell Signal:
        When price touches or crosses above the upper band
        OR when price returns to the middle band (take profit)
    """
    
    def __init__(self, bb_period: int = 20, bb_std: float = 2.0):
        """
        Initialize Bollinger Bands Strategy
        
        Parameters:
        -----------
        bb_period : int
            Period for Bollinger Bands calculation (default: 20)
        bb_std : float
            Number of standard deviations (default: 2.0)
        """
        super().__init__(f"Bollinger Bands Strategy (Period={bb_period}, Std={bb_std})")
        self.bb_period = bb_period
        self.bb_std = bb_std
        
        print(f"   BB Period: {bb_period}")
        print(f"   Standard Deviations: {bb_std}")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on Bollinger Bands
        
        Parameters:
        -----------
        data : pd.DataFrame
            Historical price data with Bollinger Bands
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with signal column added
        """
        df = data.copy()
        
        # Check if Bollinger Bands exist
        if 'bb_upper' not in df.columns or 'bb_lower' not in df.columns:
            from src.indicators.technical_indicators import TechnicalIndicators
            indicators = TechnicalIndicators()
            upper, middle, lower = indicators.bollinger_bands(
                df['close'], self.bb_period, self.bb_std
            )
            df['bb_upper'] = upper
            df['bb_middle'] = middle
            df['bb_lower'] = lower
        
        # Initialize signal column
        df['signal'] = 0
        
        # Buy signal: Price touches or crosses below lower band
        df.loc[(df['close'] <= df['bb_lower']) & 
               (df['close'].shift(1) > df['bb_lower'].shift(1)), 'signal'] = 1
        
        # Sell signal: Price touches upper band (exit long)
        df.loc[(df['close'] >= df['bb_upper']) & 
               (df['close'].shift(1) < df['bb_upper'].shift(1)), 'signal'] = -1
        
        self.signals = df
        
        return df


class BollingerBandsBreakoutStrategy(BaseStrategy):
    """
    Bollinger Bands Breakout Strategy
    
    Trades breakouts from Bollinger Bands squeeze (low volatility periods).
    When bands squeeze, a breakout is likely.
    
    Buy Signal:
        Price breaks above upper band after squeeze
    
    Sell Signal:
        Price breaks below middle band (stop loss)
    """
    
    def __init__(self, bb_period: int = 20, bb_std: float = 2.0, 
                 squeeze_threshold: float = 0.05):
        """
        Initialize Bollinger Bands Breakout Strategy
        
        Parameters:
        -----------
        bb_period : int
            Period for Bollinger Bands
        bb_std : float
            Number of standard deviations
        squeeze_threshold : float
            Threshold for identifying squeeze (as fraction of price)
        """
        super().__init__(f"BB Breakout Strategy (Period={bb_period})")
        self.bb_period = bb_period
        self.bb_std = bb_std
        self.squeeze_threshold = squeeze_threshold
        
        print(f"   BB Period: {bb_period}")
        print(f"   Standard Deviations: {bb_std}")
        print(f"   Squeeze Threshold: {squeeze_threshold}")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate signals based on Bollinger Bands breakout"""
        df = data.copy()
        
        # Ensure Bollinger Bands exist
        if 'bb_upper' not in df.columns or 'bb_lower' not in df.columns:
            from src.indicators.technical_indicators import TechnicalIndicators
            indicators = TechnicalIndicators()
            upper, middle, lower = indicators.bollinger_bands(
                df['close'], self.bb_period, self.bb_std
            )
            df['bb_upper'] = upper
            df['bb_middle'] = middle
            df['bb_lower'] = lower
        
        # Calculate band width as percentage of price
        df['bb_width_pct'] = (df['bb_upper'] - df['bb_lower']) / df['close']
        
        # Identify squeeze (narrow bands)
        df['squeeze'] = df['bb_width_pct'] < self.squeeze_threshold
        
        # Initialize signal column
        df['signal'] = 0
        
        # Buy: Breakout above upper band after squeeze
        df.loc[(df['close'] > df['bb_upper']) & 
               (df['close'].shift(1) <= df['bb_upper'].shift(1)) &
               (df['squeeze'].shift(1)), 'signal'] = 1
        
        # Sell: Price drops below middle band (stop loss)
        df.loc[(df['close'] < df['bb_middle']) & 
               (df['close'].shift(1) >= df['bb_middle'].shift(1)), 'signal'] = -1
        
        self.signals = df
        
        return df


def test_bollinger_strategies():
    """Test Bollinger Bands strategies"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "=" * 60)
    print("TESTING BOLLINGER BANDS STRATEGIES")
    print("=" * 60)
    
    # Load data
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    # Test different Bollinger strategies
    strategies = [
        BollingerBandsStrategy(20, 2.0),      # Standard
        BollingerBandsStrategy(20, 2.5),      # Wider bands
        BollingerBandsStrategy(20, 1.5),      # Tighter bands
        BollingerBandsBreakoutStrategy(20, 2.0, 0.05),  # Breakout
    ]
    
    results = {}
    
    for strategy in strategies:
        print("\n" + "=" * 60)
        positions = strategy.run(df_with_indicators)
        strategy.print_summary()
        results[strategy.name] = strategy.get_summary_stats()
    
    # Comparison
    print("\n" + "=" * 60)
    print("BOLLINGER BANDS STRATEGY COMPARISON")
    print("=" * 60)
    
    comparison_df = pd.DataFrame(results).T
    print(comparison_df[['total_trades', 'win_rate', 'total_return', 
                        'average_return']].to_string())
    
    print("\nBollinger Bands strategies test complete!")
    
    return strategies


if __name__ == "__main__":
    test_bollinger_strategies()
