"""
Indicator Visualization Module
Author: Priyanka
Day 3 - Technical Indicator Visualizations
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


class IndicatorVisualizer:
    """Create professional visualizations for technical indicators"""
    
    def __init__(self, style='seaborn-v0_8-darkgrid', figsize=(14, 8)):
        """Initialize the indicator visualizer"""
        plt.style.use(style)
        sns.set_palette("husl")
        self.figsize = figsize
        self.output_dir = "results/figures/indicators"
        os.makedirs(self.output_dir, exist_ok=True)
        print("✅ IndicatorVisualizer initialized!")
    
    def plot_rsi(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """
        Plot price with RSI indicator
        
        Parameters:
        -----------
        df : pd.DataFrame
            Data with price and RSI
        symbol : str
            Stock symbol
        save : bool
            Whether to save the figure
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize, 
                                       gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot price
        ax1.plot(df['date'], df['close'], linewidth=2, label='Close Price', color='blue')
        ax1.set_title(f'{symbol} - Price and RSI', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot RSI
        ax2.plot(df['date'], df['rsi'], linewidth=2, color='purple', label='RSI')
        ax2.axhline(70, color='red', linestyle='--', linewidth=1, label='Overbought (70)')
        ax2.axhline(30, color='green', linestyle='--', linewidth=1, label='Oversold (30)')
        ax2.fill_between(df['date'], 30, 70, alpha=0.1, color='gray')
        ax2.set_ylabel('RSI', fontsize=12)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylim(0, 100)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_rsi.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_macd(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """Plot price with MACD indicator"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize,
                                       gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot price
        ax1.plot(df['date'], df['close'], linewidth=2, label='Close Price', color='blue')
        ax1.set_title(f'{symbol} - Price and MACD', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot MACD
        ax2.plot(df['date'], df['macd'], linewidth=2, label='MACD', color='blue')
        ax2.plot(df['date'], df['macd_signal'], linewidth=2, label='Signal', color='red')
        
        # Plot histogram
        colors = ['green' if x > 0 else 'red' for x in df['macd_histogram']]
        ax2.bar(df['date'], df['macd_histogram'], alpha=0.3, color=colors, label='Histogram')
        
        ax2.axhline(0, color='black', linestyle='-', linewidth=0.5)
        ax2.set_ylabel('MACD', fontsize=12)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_macd.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_bollinger_bands(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """Plot price with Bollinger Bands"""
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # Plot price and bands
        ax.plot(df['date'], df['close'], linewidth=2, label='Close Price', color='blue')
        ax.plot(df['date'], df['bb_upper'], linewidth=1, label='Upper Band', 
               color='red', linestyle='--', alpha=0.7)
        ax.plot(df['date'], df['bb_middle'], linewidth=1, label='Middle Band (SMA)', 
               color='orange', linestyle='--', alpha=0.7)
        ax.plot(df['date'], df['bb_lower'], linewidth=1, label='Lower Band', 
               color='green', linestyle='--', alpha=0.7)
        
        # Fill between bands
        ax.fill_between(df['date'], df['bb_lower'], df['bb_upper'], alpha=0.1, color='gray')
        
        ax.set_title(f'{symbol} - Bollinger Bands', fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_bollinger.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_stochastic(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """Plot price with Stochastic Oscillator"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize,
                                       gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot price
        ax1.plot(df['date'], df['close'], linewidth=2, label='Close Price', color='blue')
        ax1.set_title(f'{symbol} - Price and Stochastic Oscillator', 
                     fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot Stochastic
        ax2.plot(df['date'], df['stoch_k'], linewidth=2, label='%K', color='blue')
        ax2.plot(df['date'], df['stoch_d'], linewidth=2, label='%D', color='red')
        ax2.axhline(80, color='red', linestyle='--', linewidth=1, alpha=0.5)
        ax2.axhline(20, color='green', linestyle='--', linewidth=1, alpha=0.5)
        ax2.fill_between(df['date'], 20, 80, alpha=0.1, color='gray')
        ax2.set_ylabel('Stochastic', fontsize=12)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylim(0, 100)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_stochastic.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_all_indicators(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """
        Create a comprehensive dashboard with all indicators
        
        Parameters:
        -----------
        df : pd.DataFrame
            Data with all indicators
        symbol : str
            Stock symbol
        save : bool
            Whether to save the figure
        """
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(4, 2, hspace=0.3, wspace=0.3)
        
        # 1. Price with Moving Averages
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(df['date'], df['close'], linewidth=2, label='Close', color='black')
        ax1.plot(df['date'], df['sma_20'], linewidth=1, label='SMA 20', alpha=0.7)
        ax1.plot(df['date'], df['sma_50'], linewidth=1, label='SMA 50', alpha=0.7)
        ax1.set_title(f'{symbol} - Technical Analysis Dashboard', 
                     fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)')
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # 2. RSI
        ax2 = fig.add_subplot(gs[1, 0])
        ax2.plot(df['date'], df['rsi'], linewidth=2, color='purple')
        ax2.axhline(70, color='red', linestyle='--', linewidth=1)
        ax2.axhline(30, color='green', linestyle='--', linewidth=1)
        ax2.fill_between(df['date'], 30, 70, alpha=0.1)
        ax2.set_title('RSI (14)')
        ax2.set_ylabel('RSI')
        ax2.set_ylim(0, 100)
        ax2.grid(True, alpha=0.3)
        
        # 3. MACD
        ax3 = fig.add_subplot(gs[1, 1])
        ax3.plot(df['date'], df['macd'], linewidth=1.5, label='MACD')
        ax3.plot(df['date'], df['macd_signal'], linewidth=1.5, label='Signal')
        colors = ['green' if x > 0 else 'red' for x in df['macd_histogram']]
        ax3.bar(df['date'], df['macd_histogram'], alpha=0.3, color=colors)
        ax3.axhline(0, color='black', linewidth=0.5)
        ax3.set_title('MACD')
        ax3.set_ylabel('MACD')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Bollinger Bands Width
        ax4 = fig.add_subplot(gs[2, 0])
        ax4.plot(df['date'], df['bb_width'], linewidth=2, color='orange')
        ax4.set_title('Bollinger Bands Width')
        ax4.set_ylabel('Width')
        ax4.grid(True, alpha=0.3)
        
        # 5. ATR
        ax5 = fig.add_subplot(gs[2, 1])
        ax5.plot(df['date'], df['atr'], linewidth=2, color='red')
        ax5.set_title('Average True Range (ATR)')
        ax5.set_ylabel('ATR')
        ax5.grid(True, alpha=0.3)
        
        # 6. Stochastic
        ax6 = fig.add_subplot(gs[3, 0])
        ax6.plot(df['date'], df['stoch_k'], linewidth=1.5, label='%K')
        ax6.plot(df['date'], df['stoch_d'], linewidth=1.5, label='%D')
        ax6.axhline(80, color='red', linestyle='--', linewidth=1, alpha=0.5)
        ax6.axhline(20, color='green', linestyle='--', linewidth=1, alpha=0.5)
        ax6.set_title('Stochastic Oscillator')
        ax6.set_ylabel('Stochastic')
        ax6.set_ylim(0, 100)
        ax6.set_xlabel('Date')
        ax6.legend()
        ax6.grid(True, alpha=0.3)
        
        # 7. ADX
        ax7 = fig.add_subplot(gs[3, 1])
        ax7.plot(df['date'], df['adx'], linewidth=2, color='blue')
        ax7.axhline(25, color='red', linestyle='--', linewidth=1, alpha=0.5, 
                   label='Strong Trend')
        ax7.set_title('Average Directional Index (ADX)')
        ax7.set_ylabel('ADX')
        ax7.set_xlabel('Date')
        ax7.legend()
        ax7.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_dashboard.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_volume_indicators(self, df: pd.DataFrame, symbol: str, save: bool = True):
        """Plot volume-based indicators"""
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=self.figsize,
                                            gridspec_kw={'height_ratios': [2, 1, 1]})
        
        # Plot price
        ax1.plot(df['date'], df['close'], linewidth=2, label='Close Price', color='blue')
        ax1.plot(df['date'], df['vwap'], linewidth=2, label='VWAP', 
                color='orange', linestyle='--', alpha=0.7)
        ax1.set_title(f'{symbol} - Volume Indicators', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot Volume
        ax2.bar(df['date'], df['volume'], alpha=0.6, color='steelblue', label='Volume')
        ax2.set_ylabel('Volume', fontsize=12)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        # Plot OBV
        ax3.plot(df['date'], df['obv'], linewidth=2, color='purple', label='OBV')
        ax3.set_ylabel('OBV', fontsize=12)
        ax3.set_xlabel('Date', fontsize=12)
        ax3.legend(loc='upper left')
        ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_volume_indicators.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()


# Test function
def test_indicator_visualizer():
    """Test indicator visualizations"""
    import sys
    import os
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)
    
    from src.data.data_loader import DataLoader
    from src.data.preprocessor import DataPreprocessor
    from src.indicators.technical_indicators import TechnicalIndicators
    
    print("\n" + "="*60)
    print("🎨 TESTING INDICATOR VISUALIZATIONS")
    print("="*60)
    
    # Load and process data
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df['date'] = pd.to_datetime(df['date'])
    df_clean = preprocessor.clean_data(df)
    
    # Add all indicators
    df_with_indicators = indicators.add_all_indicators(df_clean)
    
    # Create visualizations
    viz = IndicatorVisualizer()
    
    print("\n📊 Creating indicator visualizations...")
    
    print("\n1️⃣  RSI Chart...")
    viz.plot_rsi(df_with_indicators, 'AAPL', save=True)
    
    print("\n2️⃣  MACD Chart...")
    viz.plot_macd(df_with_indicators, 'AAPL', save=True)
    
    print("\n3️⃣  Bollinger Bands...")
    viz.plot_bollinger_bands(df_with_indicators, 'AAPL', save=True)
    
    print("\n4️⃣  Stochastic Oscillator...")
    viz.plot_stochastic(df_with_indicators, 'AAPL', save=True)
    
    print("\n5️⃣  Volume Indicators...")
    viz.plot_volume_indicators(df_with_indicators, 'AAPL', save=True)
    
    print("\n6️⃣  Complete Dashboard...")
    viz.plot_all_indicators(df_with_indicators, 'AAPL', save=True)
    
    print("\n" + "="*60)
    print("✅ ALL INDICATOR VISUALIZATIONS CREATED!")
    print("="*60)
    print(f"📁 Saved to: results/figures/indicators/")
    print("="*60)


if __name__ == "__main__":
    test_indicator_visualizer()