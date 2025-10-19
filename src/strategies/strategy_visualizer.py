"""
Strategy Visualization Module
Author: Priyanka
Day 4 - Strategy Analysis and Visualization
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


class StrategyVisualizer:
    """Visualize trading strategy signals and performance"""
    
    def __init__(self, figsize=(14, 8)):
        """Initialize strategy visualizer"""
        plt.style.use('seaborn-v0_8-darkgrid')
        self.figsize = figsize
        self.output_dir = "results/figures/strategies"
        os.makedirs(self.output_dir, exist_ok=True)
        print("✅ StrategyVisualizer initialized!")
    
    def plot_signals(self, strategy, symbol: str, save: bool = True):
        """
        Plot price with buy/sell signals
        
        Parameters:
        -----------
        strategy : BaseStrategy
            Strategy object with signals
        symbol : str
            Stock symbol
        save : bool
            Whether to save the figure
        """
        df = strategy.signals
        
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # Plot price
        ax.plot(df['date'], df['close'], linewidth=2, label='Close Price', 
               color='black', alpha=0.7)
        
        # Plot buy signals
        buy_signals = df[df['signal'] == 1]
        ax.scatter(buy_signals['date'], buy_signals['close'], 
                  marker='^', color='green', s=100, label='Buy Signal', 
                  zorder=5, alpha=0.8)
        
        # Plot sell signals
        sell_signals = df[df['signal'] == -1]
        ax.scatter(sell_signals['date'], sell_signals['close'], 
                  marker='v', color='red', s=100, label='Sell Signal', 
                  zorder=5, alpha=0.8)
        
        ax.set_title(f'{symbol} - {strategy.name} Signals', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            # Ensure directory exists
            os.makedirs(self.output_dir, exist_ok=True)
            # Clean filename (remove special characters)
            clean_name = strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{symbol}_{clean_name}_signals.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_positions(self, strategy, symbol: str, save: bool = True):
        """Plot price with position shading"""
        df = strategy.positions
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize,
                                       gridspec_kw={'height_ratios': [3, 1]})
        
        # Plot price with position shading
        ax1.plot(df['date'], df['close'], linewidth=2, color='black', 
                label='Close Price')
        
        # Shade long positions
        long_positions = df[df['position'] == 1]
        if len(long_positions) > 0:
            for idx in range(len(long_positions)):
                if idx == 0 or long_positions.index[idx] - long_positions.index[idx-1] > 1:
                    start_idx = long_positions.index[idx]
                    end_idx = start_idx
                    while end_idx < len(df) - 1 and df['position'].iloc[end_idx + 1] == 1:
                        end_idx += 1
                    
                    ax1.axvspan(df['date'].iloc[start_idx], 
                              df['date'].iloc[end_idx],
                              alpha=0.2, color='green', label='Long Position' if idx == 0 else '')
        
        ax1.set_title(f'{symbol} - {strategy.name} Positions', 
                     fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot position indicator
        ax2.fill_between(df['date'], 0, df['position'], 
                        alpha=0.5, color='green', label='Position')
        ax2.set_ylabel('Position', fontsize=12)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylim(-0.1, 1.1)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            clean_name = strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{symbol}_{clean_name}_positions.png"

            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_trades(self, strategy, symbol: str, save: bool = True):
        """Plot individual trade returns"""
        if not strategy.trades:
            print("⚠️  No trades to plot")
            return
        
        trades_df = pd.DataFrame(strategy.trades)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize)
        
        # Plot individual trade returns
        colors = ['green' if r > 0 else 'red' for r in trades_df['return']]
        ax1.bar(range(len(trades_df)), trades_df['return'] * 100, 
               color=colors, alpha=0.7)
        ax1.axhline(0, color='black', linewidth=1)
        ax1.set_title(f'{symbol} - {strategy.name} Trade Returns', 
                     fontsize=16, fontweight='bold')
        ax1.set_xlabel('Trade Number', fontsize=12)
        ax1.set_ylabel('Return (%)', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Plot cumulative returns
        cumulative_returns = (1 + trades_df['return']).cumprod()
        ax2.plot(range(len(trades_df)), cumulative_returns, 
                linewidth=2, color='blue')
        ax2.axhline(1, color='red', linestyle='--', linewidth=1, alpha=0.5)
        ax2.set_title('Cumulative Returns', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Trade Number', fontsize=12)
        ax2.set_ylabel('Cumulative Return', fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            clean_name = strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{symbol}_{clean_name}_trades.png"

            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def compare_strategies(self, strategies: list, symbol: str, save: bool = True):
        """
        Compare multiple strategies
        
        Parameters:
        -----------
        strategies : list
            List of strategy objects
        symbol : str
            Stock symbol
        save : bool
            Whether to save the figure
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Prepare data
        strategy_names = [s.name for s in strategies]
        total_trades = [len(s.trades) for s in strategies]
        win_rates = [s.get_summary_stats()['win_rate'] * 100 for s in strategies]
        total_returns = [s.get_summary_stats()['total_return'] * 100 for s in strategies]
        avg_returns = [s.get_summary_stats()['average_return'] * 100 for s in strategies]
        
        # Plot 1: Total Trades
        axes[0, 0].bar(range(len(strategies)), total_trades, color='steelblue', alpha=0.7)
        axes[0, 0].set_title('Total Trades', fontsize=14, fontweight='bold')
        axes[0, 0].set_xticks(range(len(strategies)))
        axes[0, 0].set_xticklabels([s.split('(')[0] for s in strategy_names], rotation=45, ha='right')
        axes[0, 0].set_ylabel('Number of Trades')
        axes[0, 0].grid(True, alpha=0.3, axis='y')
        
        # Plot 2: Win Rate
        axes[0, 1].bar(range(len(strategies)), win_rates, color='green', alpha=0.7)
        axes[0, 1].axhline(50, color='red', linestyle='--', linewidth=1, alpha=0.5)
        axes[0, 1].set_title('Win Rate', fontsize=14, fontweight='bold')
        axes[0, 1].set_xticks(range(len(strategies)))
        axes[0, 1].set_xticklabels([s.split('(')[0] for s in strategy_names], rotation=45, ha='right')
        axes[0, 1].set_ylabel('Win Rate (%)')
        axes[0, 1].grid(True, alpha=0.3, axis='y')
        
        # Plot 3: Total Return
        colors = ['green' if r > 0 else 'red' for r in total_returns]
        axes[1, 0].bar(range(len(strategies)), total_returns, color=colors, alpha=0.7)
        axes[1, 0].axhline(0, color='black', linewidth=1)
        axes[1, 0].set_title('Total Return', fontsize=14, fontweight='bold')
        axes[1, 0].set_xticks(range(len(strategies)))
        axes[1, 0].set_xticklabels([s.split('(')[0] for s in strategy_names], rotation=45, ha='right')
        axes[1, 0].set_ylabel('Total Return (%)')
        axes[1, 0].grid(True, alpha=0.3, axis='y')
        
        # Plot 4: Average Return per Trade
        colors = ['green' if r > 0 else 'red' for r in avg_returns]
        axes[1, 1].bar(range(len(strategies)), avg_returns, color=colors, alpha=0.7)
        axes[1, 1].axhline(0, color='black', linewidth=1)
        axes[1, 1].set_title('Average Return per Trade', fontsize=14, fontweight='bold')
        axes[1, 1].set_xticks(range(len(strategies)))
        axes[1, 1].set_xticklabels([s.split('(')[0] for s in strategy_names], rotation=45, ha='right')
        axes[1, 1].set_ylabel('Avg Return (%)')
        axes[1, 1].grid(True, alpha=0.3, axis='y')
        
        plt.suptitle(f'{symbol} - Strategy Comparison', 
                    fontsize=18, fontweight='bold', y=0.995)
        plt.tight_layout()
        
        if save:
            filename = f"{self.output_dir}/{symbol}_strategy_comparison.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()


# Test function
def test_strategy_visualizer():
    """Test strategy visualizations"""
    import sys
    sys.path.insert(0, '.')
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    from src.strategies.ma_crossover import MovingAverageCrossover
    from src.strategies.rsi_strategy import RSIStrategy
    from src.strategies.bollinger_strategy import BollingerBandsStrategy
    
    print("\n" + "="*60)
    print("🧪 TESTING STRATEGY VISUALIZER")
    print("="*60)
    
    # Load data
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    # Create strategies
    strategies = [
        MovingAverageCrossover(50, 200),
        RSIStrategy(14, 30, 70),
        BollingerBandsStrategy(20, 2.0),
    ]
    
    # Run strategies
    for strategy in strategies:
        strategy.run(df_with_indicators)
    
    # Create visualizer
    viz = StrategyVisualizer()
    
    # Visualize first strategy
    print("\n📊 Creating visualizations for MA Crossover...")
    viz.plot_signals(strategies[0], 'AAPL')
    viz.plot_positions(strategies[0], 'AAPL')
    viz.plot_trades(strategies[0], 'AAPL')
    
    # Compare all strategies
    print("\n📊 Creating strategy comparison...")
    viz.compare_strategies(strategies, 'AAPL')
    
    print("\n✅ Strategy visualizer test complete!")


if __name__ == "__main__":
    test_strategy_visualizer()
