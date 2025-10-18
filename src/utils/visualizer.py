"""
Visualization Module
Author: Priyanka
Day 2 - Data Visualization
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


class Visualizer:
    """Create professional visualizations for stock data"""
    
    def __init__(self, style='seaborn-v0_8-darkgrid', figsize=(12, 6)):
        """
        Initialize visualizer
        """
        plt.style.use(style)
        sns.set_palette("husl")
        self.figsize = figsize
        self.output_dir = "results/figures"
        os.makedirs(self.output_dir, exist_ok=True)
        print("✅ Visualizer initialized!")
    
    def plot_price_history(self, df, symbol, save=True):
        """Plot stock price history"""
        fig, ax = plt.subplots(figsize=self.figsize)
        
        ax.plot(df['date'], df['close'], linewidth=2, label='Close Price')
        
        if 'ma_5' in df.columns:
            ax.plot(df['date'], df['ma_5'], alpha=0.7, linestyle='--', label='5-Day MA')
        if 'ma_20' in df.columns:
            ax.plot(df['date'], df['ma_20'], alpha=0.7, linestyle='--', label='20-Day MA')
        
        ax.set_title(f'{symbol} Stock Price History', fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_price_history.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_volume(self, df, symbol, save=True):
        """Plot trading volume"""
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.bar(df['date'], df['volume'], alpha=0.6, color='steelblue')
        ax.set_title(f'{symbol} Trading Volume', fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Volume', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save:
            filename = f"{self.output_dir}/{symbol}_volume.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        plt.show()
    
    def plot_returns_distribution(self, df, symbol, save=True):
        """Plot distribution of returns"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        returns = df['returns'].dropna()
        
        # Histogram
        axes[0].hist(returns, bins=50, alpha=0.7, color='steelblue', edgecolor='black')
        axes[0].axvline(returns.mean(), color='red', linestyle='--', 
                        linewidth=2, label=f'Mean: {returns.mean():.4f}')
        axes[0].set_title('Returns Distribution', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Daily Returns')
        axes[0].set_ylabel('Frequency')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Time series
        axes[1].plot(df['date'], df['returns'], alpha=0.6, linewidth=1)
        axes[1].axhline(0, color='red', linestyle='--', linewidth=1)
        axes[1].set_title('Returns Over Time', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Returns')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save:
            filename = f"{self.output_dir}/{symbol}_returns.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        plt.show()
    
    def plot_candlestick(self, df, symbol, days=60, save=True):
        """Plot candlestick chart (simplified version)"""
        df_recent = df.tail(days).copy()
        df_recent['color'] = df_recent.apply(
            lambda row: 'green' if row['close'] >= row['open'] else 'red', axis=1
        )
        
        fig, ax = plt.subplots(figsize=(14, 7))
        for _, row in df_recent.iterrows():
            ax.plot([row['date'], row['date']], [row['low'], row['high']],
                    color='black', linewidth=0.5)
            ax.plot([row['date'], row['date']], [row['open'], row['close']],
                    color=row['color'], linewidth=3, solid_capstyle='round')
        
        ax.set_title(f'{symbol} Candlestick Chart (Last {days} Days)',
                     fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_candlestick.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        plt.show()
    
    def plot_comparison(self, data_dict, save=True):
        """Compare multiple stocks"""
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        for symbol, df in data_dict.items():
            normalized = (df['close'] / df['close'].iloc[0]) * 100
            axes[0].plot(df['date'], normalized, label=symbol, linewidth=2)
        
        axes[0].set_title('Stock Price Comparison (Normalized to 100)', fontsize=16, fontweight='bold')
        axes[0].set_xlabel('Date', fontsize=12)
        axes[0].set_ylabel('Normalized Price', fontsize=12)
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        for symbol, df in data_dict.items():
            axes[1].plot(df['date'], df['volume'], label=symbol, alpha=0.7)
        
        axes[1].set_title('Volume Comparison', fontsize=16, fontweight='bold')
        axes[1].set_xlabel('Date', fontsize=12)
        axes[1].set_ylabel('Volume', fontsize=12)
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save:
            filename = f"{self.output_dir}/stock_comparison.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        plt.show()
    
    def plot_correlation_matrix(self, df, save=True):
        """Plot correlation heatmap"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_cols = [col for col in ['open', 'high', 'low', 'close', 'volume', 
                                     'returns', 'price_range'] if col in numeric_cols]
        
        correlation_matrix = df[corr_cols].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                    square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Correlation Matrix', fontsize=16, fontweight='bold')
        plt.tight_layout()
        if save:
            filename = f"{self.output_dir}/correlation_matrix.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        plt.show()

    def plot_monthly_returns(self, df, symbol, save=True):
        """Plot monthly returns bar chart (with timezone-safe fix)"""
        df_copy = df.copy()

        # Convert timezone-aware datetimes safely
        df_copy['date'] = pd.to_datetime(df_copy['date'], utc=True)
        df_copy['date'] = df_copy['date'].dt.tz_convert(None)

        df_copy['year'] = df_copy['date'].dt.year
        df_copy['month'] = df_copy['date'].dt.month

        monthly_returns = df_copy.groupby(['year', 'month'])['returns'].sum().reset_index()
        monthly_returns['year_month'] = (
            monthly_returns['year'].astype(str) + '-' +
            monthly_returns['month'].astype(str).str.zfill(2)
        )

        plt.figure(figsize=(14, 6))
        colors = ['green' if x > 0 else 'red' for x in monthly_returns['returns']]
        plt.bar(range(len(monthly_returns)), monthly_returns['returns'], color=colors, alpha=0.7)
        plt.axhline(0, color='black', linewidth=1)
        plt.title(f'{symbol} Monthly Returns', fontsize=16, fontweight='bold')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Returns', fontsize=12)
        plt.xticks(range(len(monthly_returns)), monthly_returns['year_month'], rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()

        if save:
            filename = f"{self.output_dir}/{symbol}_monthly_returns.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")

        plt.show()


# Test function
def test_visualizer():
    """Test visualization functions"""
    import sys
    import os
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, project_root)

    from src.data.data_loader import DataLoader
    from src.data.preprocessor import DataPreprocessor

    print("\n" + "="*60)
    print("🎨 TESTING VISUALIZER")
    print("="*60)

    loader = DataLoader()
    preprocessor = DataPreprocessor()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_clean = preprocessor.clean_data(df)
    df_processed = preprocessor.add_basic_features(df_clean)
    
    viz = Visualizer()

    print("\n📊 Creating visualizations...")
    viz.plot_price_history(df_processed, 'AAPL')
    viz.plot_volume(df_processed, 'AAPL')
    viz.plot_returns_distribution(df_processed, 'AAPL')
    viz.plot_candlestick(df_processed, 'AAPL', days=60)
    viz.plot_correlation_matrix(df_processed)
    viz.plot_monthly_returns(df_processed, 'AAPL')

    print("\n✅ All visualizations created!")
    print("📁 Check results/figures/ folder")


if __name__ == "__main__":
    test_visualizer()
