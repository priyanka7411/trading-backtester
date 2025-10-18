"""
Technical Indicators Module
Author: Priyanka
Day 3 - Technical Analysis Indicators

This module implements various technical indicators used in algorithmic trading.
"""

import pandas as pd
import numpy as np
from typing import Tuple


class TechnicalIndicators:
    """
    Comprehensive technical indicators for trading strategies
    """
    
    def __init__(self):
        """Initialize the technical indicators calculator"""
        print("✅ TechnicalIndicators initialized!")
    
    # ==================== MOVING AVERAGES ====================
    
    def sma(self, data: pd.Series, period: int) -> pd.Series:
        """
        Simple Moving Average
        
        Parameters:
        -----------
        data : pd.Series
            Price data (usually close price)
        period : int
            Number of periods for calculation
            
        Returns:
        --------
        pd.Series
            Simple moving average
        """
        return data.rolling(window=period).mean()
    
    def ema(self, data: pd.Series, period: int) -> pd.Series:
        """
        Exponential Moving Average
        
        Parameters:
        -----------
        data : pd.Series
            Price data
        period : int
            Number of periods
            
        Returns:
        --------
        pd.Series
            Exponential moving average
        """
        return data.ewm(span=period, adjust=False).mean()
    
    # ==================== RSI ====================
    
    def rsi(self, data: pd.Series, period: int = 14) -> pd.Series:
        """
        Relative Strength Index (RSI)
        
        RSI = 100 - (100 / (1 + RS))
        where RS = Average Gain / Average Loss
        
        Parameters:
        -----------
        data : pd.Series
            Price data (close price)
        period : int
            RSI period (default: 14)
            
        Returns:
        --------
        pd.Series
            RSI values (0-100)
        """
        # Calculate price changes
        delta = data.diff()
        
        # Separate gains and losses
        gains = delta.clip(lower=0)
        losses = -delta.clip(upper=0)
        
        # Calculate average gains and losses
        avg_gains = gains.rolling(window=period).mean()
        avg_losses = losses.rolling(window=period).mean()
        
        # Calculate RS and RSI
        rs = avg_gains / avg_losses
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    # ==================== MACD ====================
    
    def macd(self, data: pd.Series, fast: int = 12, slow: int = 26, 
             signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Moving Average Convergence Divergence (MACD)
        
        MACD Line = EMA(12) - EMA(26)
        Signal Line = EMA(9) of MACD Line
        Histogram = MACD Line - Signal Line
        
        Parameters:
        -----------
        data : pd.Series
            Price data (close price)
        fast : int
            Fast EMA period (default: 12)
        slow : int
            Slow EMA period (default: 26)
        signal : int
            Signal line period (default: 9)
            
        Returns:
        --------
        tuple
            (macd_line, signal_line, histogram)
        """
        # Calculate MACD line
        ema_fast = self.ema(data, fast)
        ema_slow = self.ema(data, slow)
        macd_line = ema_fast - ema_slow
        
        # Calculate signal line
        signal_line = self.ema(macd_line, signal)
        
        # Calculate histogram
        histogram = macd_line - signal_line
        
        return macd_line, signal_line, histogram
    
    # ==================== BOLLINGER BANDS ====================
    
    def bollinger_bands(self, data: pd.Series, period: int = 20, 
                       std_dev: float = 2.0) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Bollinger Bands
        
        Middle Band = SMA(20)
        Upper Band = SMA(20) + (2 * Standard Deviation)
        Lower Band = SMA(20) - (2 * Standard Deviation)
        
        Parameters:
        -----------
        data : pd.Series
            Price data (close price)
        period : int
            Moving average period (default: 20)
        std_dev : float
            Number of standard deviations (default: 2.0)
            
        Returns:
        --------
        tuple
            (upper_band, middle_band, lower_band)
        """
        # Calculate middle band (SMA)
        middle_band = self.sma(data, period)
        
        # Calculate standard deviation
        rolling_std = data.rolling(window=period).std()
        
        # Calculate upper and lower bands
        upper_band = middle_band + (rolling_std * std_dev)
        lower_band = middle_band - (rolling_std * std_dev)
        
        return upper_band, middle_band, lower_band
    
    # ==================== ATR ====================
    
    def atr(self, high: pd.Series, low: pd.Series, close: pd.Series, 
            period: int = 14) -> pd.Series:
        """
        Average True Range (ATR)
        
        Measures market volatility
        
        Parameters:
        -----------
        high : pd.Series
            High prices
        low : pd.Series
            Low prices
        close : pd.Series
            Close prices
        period : int
            ATR period (default: 14)
            
        Returns:
        --------
        pd.Series
            ATR values
        """
        # Calculate True Range
        high_low = high - low
        high_close = np.abs(high - close.shift())
        low_close = np.abs(low - close.shift())
        
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        
        # Calculate ATR (moving average of true range)
        atr = true_range.rolling(window=period).mean()
        
        return atr
    
    # ==================== STOCHASTIC OSCILLATOR ====================
    
    def stochastic(self, high: pd.Series, low: pd.Series, close: pd.Series,
                   k_period: int = 14, d_period: int = 3) -> Tuple[pd.Series, pd.Series]:
        """
        Stochastic Oscillator
        
        %K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
        %D = SMA of %K
        
        Parameters:
        -----------
        high : pd.Series
            High prices
        low : pd.Series
            Low prices
        close : pd.Series
            Close prices
        k_period : int
            %K period (default: 14)
        d_period : int
            %D period (default: 3)
            
        Returns:
        --------
        tuple
            (%K, %D)
        """
        # Calculate %K
        lowest_low = low.rolling(window=k_period).min()
        highest_high = high.rolling(window=k_period).max()
        
        k = 100 * (close - lowest_low) / (highest_high - lowest_low)
        
        # Calculate %D (SMA of %K)
        d = k.rolling(window=d_period).mean()
        
        return k, d
    
    # ==================== OBV ====================
    
    def obv(self, close: pd.Series, volume: pd.Series) -> pd.Series:
        """
        On-Balance Volume (OBV)
        
        Cumulative volume based on price direction
        
        Parameters:
        -----------
        close : pd.Series
            Close prices
        volume : pd.Series
            Volume data
            
        Returns:
        --------
        pd.Series
            OBV values
        """
        obv = (np.sign(close.diff()) * volume).fillna(0).cumsum()
        return obv
    
    # ==================== VWAP ====================
    
    def vwap(self, high: pd.Series, low: pd.Series, close: pd.Series,
             volume: pd.Series) -> pd.Series:
        """
        Volume Weighted Average Price (VWAP)
        
        Parameters:
        -----------
        high : pd.Series
            High prices
        low : pd.Series
            Low prices
        close : pd.Series
            Close prices
        volume : pd.Series
            Volume data
            
        Returns:
        --------
        pd.Series
            VWAP values
        """
        typical_price = (high + low + close) / 3
        vwap = (typical_price * volume).cumsum() / volume.cumsum()
        return vwap
    
    # ==================== ADX ====================
    
    def adx(self, high: pd.Series, low: pd.Series, close: pd.Series,
            period: int = 14) -> pd.Series:
        """
        Average Directional Index (ADX)
        
        Measures trend strength (0-100)
        
        Parameters:
        -----------
        high : pd.Series
            High prices
        low : pd.Series
            Low prices
        close : pd.Series
            Close prices
        period : int
            ADX period (default: 14)
            
        Returns:
        --------
        pd.Series
            ADX values
        """
        # Calculate +DM and -DM
        high_diff = high.diff()
        low_diff = -low.diff()
        
        plus_dm = high_diff.where((high_diff > low_diff) & (high_diff > 0), 0)
        minus_dm = low_diff.where((low_diff > high_diff) & (low_diff > 0), 0)
        
        # Calculate ATR
        atr_values = self.atr(high, low, close, period)
        
        # Calculate +DI and -DI
        plus_di = 100 * (plus_dm.rolling(window=period).mean() / atr_values)
        minus_di = 100 * (minus_dm.rolling(window=period).mean() / atr_values)
        
        # Calculate DX and ADX
        dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di)
        adx = dx.rolling(window=period).mean()
        
        return adx
    
    # ==================== HELPER METHOD ====================
    
    def add_all_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add all technical indicators to a DataFrame
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with OHLCV data
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with all indicators added
        """
        df_indicators = df.copy()
        
        print("📊 Adding technical indicators...")
        
        # Moving Averages
        df_indicators['sma_10'] = self.sma(df['close'], 10)
        df_indicators['sma_20'] = self.sma(df['close'], 20)
        df_indicators['sma_50'] = self.sma(df['close'], 50)
        df_indicators['ema_12'] = self.ema(df['close'], 12)
        df_indicators['ema_26'] = self.ema(df['close'], 26)
        print("   ✅ Added Moving Averages (SMA, EMA)")
        
        # RSI
        df_indicators['rsi'] = self.rsi(df['close'], 14)
        print("   ✅ Added RSI")
        
        # MACD
        macd_line, signal_line, histogram = self.macd(df['close'])
        df_indicators['macd'] = macd_line
        df_indicators['macd_signal'] = signal_line
        df_indicators['macd_histogram'] = histogram
        print("   ✅ Added MACD")
        
        # Bollinger Bands
        upper, middle, lower = self.bollinger_bands(df['close'])
        df_indicators['bb_upper'] = upper
        df_indicators['bb_middle'] = middle
        df_indicators['bb_lower'] = lower
        df_indicators['bb_width'] = upper - lower
        print("   ✅ Added Bollinger Bands")
        
        # ATR
        df_indicators['atr'] = self.atr(df['high'], df['low'], df['close'])
        print("   ✅ Added ATR")
        
        # Stochastic
        k, d = self.stochastic(df['high'], df['low'], df['close'])
        df_indicators['stoch_k'] = k
        df_indicators['stoch_d'] = d
        print("   ✅ Added Stochastic Oscillator")
        
        # OBV
        df_indicators['obv'] = self.obv(df['close'], df['volume'])
        print("   ✅ Added OBV")
        
        # VWAP
        df_indicators['vwap'] = self.vwap(df['high'], df['low'], df['close'], df['volume'])
        print("   ✅ Added VWAP")
        
        # ADX
        df_indicators['adx'] = self.adx(df['high'], df['low'], df['close'])
        print("   ✅ Added ADX")
        
        print(f"\n✨ Total indicators added: {len(df_indicators.columns) - len(df.columns)}")
        
        return df_indicators


# Test function
def test_indicators():
    """Test the technical indicators"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.data.preprocessor import DataPreprocessor
    
    print("\n" + "="*60)
    print("🧪 TESTING TECHNICAL INDICATORS")
    print("="*60)
    
    # Load data
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    # Date is already converted in load_data, no need to convert again
    df_clean = preprocessor.clean_data(df)
    
    # Initialize indicators
    indicators = TechnicalIndicators()
    
    # Add all indicators
    df_with_indicators = indicators.add_all_indicators(df_clean)
    
    # Display summary
    print("\n" + "="*60)
    print("📊 INDICATORS SUMMARY")
    print("="*60)
    print(f"Total columns: {len(df_with_indicators.columns)}")
    print(f"\nNew indicator columns:")
    new_cols = [col for col in df_with_indicators.columns if col not in df_clean.columns]
    for i, col in enumerate(new_cols, 1):
        print(f"{i:2d}. {col}")
    
    print(f"\n📈 Sample RSI values:")
    print(df_with_indicators[['date', 'close', 'rsi']].tail(10))
    
    print("\n✅ Technical indicators test complete!")
    
    return df_with_indicators


if __name__ == "__main__":
    test_indicators()