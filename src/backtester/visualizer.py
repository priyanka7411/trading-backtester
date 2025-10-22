"""
Backtest Results Visualization
Author: Priyanka
Day 5 - Performance Visualization

Visualize backtest results including equity curves, drawdowns, and trade analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


class BacktestVisualizer:
    """Visualize backtest results"""
    
    def __init__(self, figsize=(14, 8)):
        """Initialize visualizer"""
        plt.style.use('seaborn-v0_8-darkgrid')
        self.figsize = figsize
        self.output_dir = "results/figures/backtests"
        os.makedirs(self.output_dir, exist_ok=True)
        print("✅ BacktestVisualizer initialized!")
    
    def plot_equity_curve(self, results, save: bool = True):
        """
        Plot equity curve
        
        Parameters:
        -----------
        results : BacktestResults
            Backtest results object
        save : bool
            Whether to save the figure
        """
        equity_df = results.portfolio.get_equity_curve()
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize,
                                       gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot equity curve
        ax1.plot(equity_df['date'], equity_df['total_value'], 
                linewidth=2, label='Portfolio Value', color='blue')
        ax1.axhline(results.portfolio.initial_capital, 
                   color='red', linestyle='--', linewidth=1, 
                   label='Initial Capital', alpha=0.7)
        ax1.fill_between(equity_df['date'], 
                        results.portfolio.initial_capital,
                        equity_df['total_value'],
                        where=equity_df['total_value'] >= results.portfolio.initial_capital,
                        alpha=0.3, color='green', label='Profit')
        ax1.fill_between(equity_df['date'],
                        results.portfolio.initial_capital,
                        equity_df['total_value'],
                        where=equity_df['total_value'] < results.portfolio.initial_capital,
                        alpha=0.3, color='red', label='Loss')
        
        ax1.set_title(f'{results.symbol} - {results.strategy.name} - Equity Curve',
                     fontsize=16, fontweight='bold')
        ax1.set_ylabel('Portfolio Value ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Format y-axis
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        # Plot cash vs invested
        ax2.plot(equity_df['date'], equity_df['cash'], 
                label='Cash', linewidth=2, color='green')
        ax2.plot(equity_df['date'], equity_df['positions_value'],
                label='Invested', linewidth=2, color='orange')
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('Value ($)', fontsize=12)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_equity.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_drawdown(self, results, save: bool = True):
        """Plot drawdown analysis"""
        equity_df = results.portfolio.get_equity_curve()
        
        # Calculate drawdown
        equity_df['cummax'] = equity_df['total_value'].cummax()
        equity_df['drawdown'] = (equity_df['total_value'] - equity_df['cummax']) / equity_df['cummax']
        
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # Plot drawdown
        ax.fill_between(equity_df['date'], 0, equity_df['drawdown'] * 100,
                       alpha=0.3, color='red')
        ax.plot(equity_df['date'], equity_df['drawdown'] * 100,
               linewidth=2, color='darkred', label='Drawdown')
        
        # Mark maximum drawdown
        max_dd_idx = equity_df['drawdown'].idxmin()
        max_dd_date = equity_df.loc[max_dd_idx, 'date']
        max_dd_value = equity_df.loc[max_dd_idx, 'drawdown'] * 100
        
        ax.scatter([max_dd_date], [max_dd_value], color='red', s=100, 
                  zorder=5, label=f'Max DD: {max_dd_value:.2f}%')
        
        ax.set_title(f'{results.symbol} - {results.strategy.name} - Drawdown Analysis',
                     fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Drawdown (%)', fontsize=12)
        ax.legend(loc='lower left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_drawdown.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_returns_distribution(self, results, save: bool = True):
        """Plot returns distribution"""
        equity_df = results.portfolio.get_equity_curve()
        equity_df['returns'] = equity_df['total_value'].pct_change()
        
        # Drop NaN values for plotting
        equity_df_clean = equity_df.dropna()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=self.figsize)
        
        # Histogram
        returns_pct = equity_df_clean['returns'] * 100
        ax1.hist(returns_pct, bins=50, alpha=0.7, color='steelblue', edgecolor='black')
        ax1.axvline(returns_pct.mean(), color='red', linestyle='--', 
                   linewidth=2, label=f'Mean: {returns_pct.mean():.3f}%')
        ax1.axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
        ax1.set_title('Daily Returns Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Daily Return (%)')
        ax1.set_ylabel('Frequency')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Returns over time
        ax2.plot(equity_df_clean['date'], returns_pct, alpha=0.6, linewidth=1)
        ax2.axhline(0, color='red', linestyle='--', linewidth=1)
        ax2.set_title('Daily Returns Over Time', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Daily Return (%)')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_returns.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_trade_analysis(self, results, save: bool = True):
        """Plot trade analysis"""
        trades_df = results.portfolio.get_trades()
        
        if len(trades_df) == 0:
            print("⚠️  No trades to visualize")
            return
        
        # Calculate profit/loss per trade
        buy_trades = trades_df[trades_df['action'] == 'BUY'].copy()
        sell_trades = trades_df[trades_df['action'] == 'SELL'].copy()
        
        if len(buy_trades) == 0 or len(sell_trades) == 0:
            print("⚠️  Incomplete trade pairs")
            return
        
        # Match buy-sell pairs
        trade_pairs = []
        for i, sell in sell_trades.iterrows():
            # Find corresponding buy (last buy before this sell)
            buys_before = buy_trades[buy_trades['date'] < sell['date']]
            if len(buys_before) > 0:
                buy = buys_before.iloc[-1]
                pnl = (sell['price'] - buy['price']) * sell['shares']
                pnl_pct = (sell['price'] - buy['price']) / buy['price']
                trade_pairs.append({
                    'entry_date': buy['date'],
                    'exit_date': sell['date'],
                    'entry_price': buy['price'],
                    'exit_price': sell['price'],
                    'shares': sell['shares'],
                    'pnl': pnl,
                    'pnl_pct': pnl_pct
                })
        
        if len(trade_pairs) == 0:
            print("⚠️  No complete trade pairs found")
            return
        
        pairs_df = pd.DataFrame(trade_pairs)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize)
        
        # P&L per trade
        colors = ['green' if x > 0 else 'red' for x in pairs_df['pnl']]
        ax1.bar(range(len(pairs_df)), pairs_df['pnl'], color=colors, alpha=0.7)
        ax1.axhline(0, color='black', linewidth=1)
        ax1.set_title(f'Profit/Loss per Trade - {results.strategy.name}',
                     fontsize=14, fontweight='bold')
        ax1.set_xlabel('Trade Number')
        ax1.set_ylabel('P&L ($)')
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Cumulative P&L
        pairs_df['cumulative_pnl'] = pairs_df['pnl'].cumsum()
        ax2.plot(range(len(pairs_df)), pairs_df['cumulative_pnl'],
                linewidth=2, color='blue')
        ax2.axhline(0, color='red', linestyle='--', linewidth=1, alpha=0.5)
        ax2.fill_between(range(len(pairs_df)), 0, pairs_df['cumulative_pnl'],
                        where=pairs_df['cumulative_pnl'] >= 0,
                        alpha=0.3, color='green')
        ax2.fill_between(range(len(pairs_df)), 0, pairs_df['cumulative_pnl'],
                        where=pairs_df['cumulative_pnl'] < 0,
                        alpha=0.3, color='red')
        ax2.set_title('Cumulative P&L', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Trade Number')
        ax2.set_ylabel('Cumulative P&L ($)')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_trades.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def plot_monthly_returns(self, results, save: bool = True):
        """Plot monthly returns heatmap"""
        equity_df = results.portfolio.get_equity_curve()
        equity_df['returns'] = equity_df['total_value'].pct_change()
        equity_df['year'] = pd.to_datetime(equity_df['date']).dt.year
        equity_df['month'] = pd.to_datetime(equity_df['date']).dt.month
        
        # Calculate monthly returns
        monthly = equity_df.groupby(['year', 'month'])['returns'].sum() * 100
        monthly_pivot = monthly.reset_index().pivot(index='month', columns='year', values='returns')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        sns.heatmap(monthly_pivot, annot=True, fmt='.2f', cmap='RdYlGn',
                   center=0, linewidths=1, cbar_kws={'label': 'Return (%)'})
        
        ax.set_title(f'{results.symbol} - {results.strategy.name} - Monthly Returns (%)',
                    fontsize=14, fontweight='bold')
        ax.set_ylabel('Month')
        ax.set_xlabel('Year')
        ax.set_yticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_monthly.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()
    
    def create_performance_dashboard(self, results, save: bool = True):
        """Create comprehensive performance dashboard"""
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        equity_df = results.portfolio.get_equity_curve()
        equity_df['returns'] = equity_df['total_value'].pct_change()
        
        # 1. Equity Curve
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(equity_df['date'], equity_df['total_value'], linewidth=2, color='blue')
        ax1.axhline(results.portfolio.initial_capital, color='red', linestyle='--', alpha=0.5)
        ax1.set_title(f'{results.symbol} - {results.strategy.name} - Performance Dashboard',
                     fontsize=16, fontweight='bold')
        ax1.set_ylabel('Portfolio Value ($)')
        ax1.grid(True, alpha=0.3)
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        # 2. Drawdown
        equity_df['cummax'] = equity_df['total_value'].cummax()
        equity_df['drawdown'] = (equity_df['total_value'] - equity_df['cummax']) / equity_df['cummax']
        
        ax2 = fig.add_subplot(gs[1, 0])
        ax2.fill_between(equity_df['date'], 0, equity_df['drawdown'] * 100,
                        alpha=0.3, color='red')
        ax2.plot(equity_df['date'], equity_df['drawdown'] * 100, color='darkred')
        ax2.set_title('Drawdown', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Drawdown (%)')
        ax2.grid(True, alpha=0.3)
        
        # 3. Returns Distribution
        ax3 = fig.add_subplot(gs[1, 1])
        returns_pct = equity_df['returns'].dropna() * 100
        ax3.hist(returns_pct, bins=30, alpha=0.7, color='steelblue', edgecolor='black')
        ax3.axvline(returns_pct.mean(), color='red', linestyle='--', linewidth=2)
        ax3.set_title('Daily Returns Distribution', fontsize=12, fontweight='bold')
        ax3.set_xlabel('Return (%)')
        ax3.set_ylabel('Frequency')
        ax3.grid(True, alpha=0.3)
        
        # 4. Performance Metrics
        ax4 = fig.add_subplot(gs[2, 0])
        ax4.axis('off')
        
        metrics_text = f"""
        Performance Metrics:
        
        Total Return:        {results.metrics['total_return']:.2%}
        Annual Return:       {results.metrics['annual_return']:.2%}
        Volatility:          {results.metrics['volatility']:.2%}
        Sharpe Ratio:        {results.metrics['sharpe_ratio']:.2f}
        Max Drawdown:        {results.metrics['max_drawdown']:.2%}
        
        Total Trades:        {results.metrics['total_trades']}
        Days Traded:         {results.metrics['days_traded']}
        """
        
        ax4.text(0.1, 0.5, metrics_text, fontsize=11, family='monospace',
                verticalalignment='center')
        
        # 5. Rolling Returns
        ax5 = fig.add_subplot(gs[2, 1])
        rolling_returns = equity_df['returns'].rolling(window=20).mean() * 100
        ax5.plot(equity_df['date'], rolling_returns, linewidth=2, color='green')
        ax5.axhline(0, color='red', linestyle='--', linewidth=1)
        ax5.set_title('20-Day Rolling Average Returns', fontsize=12, fontweight='bold')
        ax5.set_ylabel('Return (%)')
        ax5.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            clean_name = results.strategy.name.replace('/', '_').replace('(', '').replace(')', '').replace(' ', '_')
            filename = f"{self.output_dir}/{results.symbol}_{clean_name}_dashboard.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"💾 Saved: {filename}")
        
        plt.show()


# Test function
def test_visualizer():
    """Test backtest visualizer"""
    import sys
    sys.path.insert(0, '.')
    
    from src.data.data_loader import DataLoader
    from src.indicators.technical_indicators import TechnicalIndicators
    from src.strategies.ma_crossover import MovingAverageCrossover
    from src.backtester.engine import Backtester
    
    print("\n" + "="*70)
    print("🧪 TESTING BACKTEST VISUALIZER")
    print("="*70)
    
    # Load data
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    # Create strategy and backtest
    strategy = MovingAverageCrossover(50, 200)
    backtester = Backtester(initial_capital=100000)
    results = backtester.run(df_with_indicators, strategy, 'AAPL')
    
    # Create visualizations
    viz = BacktestVisualizer()
    
    print("\n📊 Creating visualizations...")
    viz.plot_equity_curve(results)
    viz.plot_drawdown(results)
    viz.plot_returns_distribution(results)
    viz.plot_trade_analysis(results)
    viz.plot_monthly_returns(results)
    viz.create_performance_dashboard(results)
    
    print("\n✅ Visualizer test complete!")


if __name__ == "__main__":
    test_visualizer()