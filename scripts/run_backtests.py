"""
Run Comprehensive Backtests
Author: Priyanka
Day 5 - Backtest All Strategies

Run backtests on all strategies and compare results.
"""

import sys
sys.path.append('.')

import pandas as pd
from src.data.data_loader import DataLoader
from src.indicators.technical_indicators import TechnicalIndicators
from src.strategies.ma_crossover import MovingAverageCrossover
from src.strategies.rsi_strategy import RSIStrategy
from src.strategies.bollinger_strategy import BollingerBandsStrategy
from src.strategies.combined_strategy import CombinedStrategy
from src.backtester.engine import Backtester
from src.backtester.visualizer import BacktestVisualizer


def run_all_backtests():
    """Run backtests on all strategies"""
    
    print("\n" + "="*70)
    print("🚀 RUNNING COMPREHENSIVE BACKTESTS")
    print("="*70)
    
    # Load and prepare data
    print("\n📥 Loading data...")
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    print(f"✅ Loaded {len(df_with_indicators)} days of data")
    
    # Define strategies to test
    print("\n📊 Initializing strategies...")
    strategies = [
        MovingAverageCrossover(50, 200),
        RSIStrategy(14, 30, 70),
        BollingerBandsStrategy(20, 2.0),
        CombinedStrategy(30, 70, 2),
    ]
    
    print(f"✅ Initialized {len(strategies)} strategies")
    
    # Create backtester
    backtester = Backtester(
        initial_capital=100000,
        commission=0.001,   # 0.1%
        slippage=0.0005     # 0.05%
    )
    
    # Run backtests
    print("\n" + "="*70)
    print("🏃 RUNNING BACKTESTS")
    print("="*70)
    
    all_results = []
    results_objects = []
    
    for i, strategy in enumerate(strategies, 1):
        print(f"\n[{i}/{len(strategies)}] Testing {strategy.name}...")
        
        try:
            # Run backtest
            results = backtester.run(df_with_indicators, strategy, 'AAPL')
            results_objects.append(results)
            
            # Collect metrics
            metrics = results.metrics.copy()
            metrics['strategy'] = strategy.name
            all_results.append(metrics)
            
            # Print summary
            results.print_summary()
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # Create comparison table
    print("\n" + "="*70)
    print("📊 BACKTEST RESULTS COMPARISON")
    print("="*70)
    
    results_df = pd.DataFrame(all_results)
    
    # Format display
    display_cols = ['strategy', 'total_return', 'annual_return', 'sharpe_ratio',
                   'max_drawdown', 'volatility', 'total_trades']
    
    # Format percentages
    for col in ['total_return', 'annual_return', 'max_drawdown', 'volatility']:
        if col in results_df.columns:
            results_df[f'{col}_fmt'] = results_df[col].apply(lambda x: f"{x:.2%}")
    
    # Display table
    print("\n" + results_df[display_cols].to_string(index=False))
    
    # Save results
    import os
    os.makedirs('results/reports', exist_ok=True)
    results_df.to_csv('results/reports/backtest_comparison.csv', index=False)
    print(f"\n💾 Saved to: results/reports/backtest_comparison.csv")
    
    # Find best strategy
    print("\n" + "="*70)
    print("🏆 BEST PERFORMING STRATEGIES")
    print("="*70)
    
    # Best by total return
    best_return_idx = results_df['total_return'].idxmax()
    best_return = results_df.loc[best_return_idx]
    print(f"\n🥇 Best Total Return: {best_return['strategy']}")
    print(f"   Total Return: {best_return['total_return']:.2%}")
    print(f"   Sharpe Ratio: {best_return['sharpe_ratio']:.2f}")
    print(f"   Max Drawdown: {best_return['max_drawdown']:.2%}")
    
    # Best Sharpe ratio
    best_sharpe_idx = results_df['sharpe_ratio'].idxmax()
    best_sharpe = results_df.loc[best_sharpe_idx]
    print(f"\n🥇 Best Sharpe Ratio: {best_sharpe['strategy']}")
    print(f"   Sharpe Ratio: {best_sharpe['sharpe_ratio']:.2f}")
    print(f"   Total Return: {best_sharpe['total_return']:.2%}")
    print(f"   Volatility: {best_sharpe['volatility']:.2%}")
    
    # Lowest drawdown
    lowest_dd_idx = results_df['max_drawdown'].idxmax()  # Most negative is worst
    lowest_dd = results_df.loc[lowest_dd_idx]
    print(f"\n🏅 Lowest Drawdown: {lowest_dd['strategy']}")
    print(f"   Max Drawdown: {lowest_dd['max_drawdown']:.2%}")
    print(f"   Total Return: {lowest_dd['total_return']:.2%}")
    
    # Create visualizations
    print("\n" + "="*70)
    print("📈 CREATING VISUALIZATIONS")
    print("="*70)
    
    viz = BacktestVisualizer()
    
    # Visualize best strategy
    best_strategy_results = results_objects[best_return_idx]
    print(f"\n📊 Creating comprehensive dashboard for best strategy...")
    viz.create_performance_dashboard(best_strategy_results, save=True)
    
    # Create individual charts for top 2 strategies
    for idx in [best_return_idx, best_sharpe_idx]:
        if idx < len(results_objects):
            result = results_objects[idx]
            print(f"\n📊 Creating charts for {result.strategy.name}...")
            viz.plot_equity_curve(result, save=True)
            viz.plot_drawdown(result, save=True)
    
    print("\n" + "="*70)
    print("✅ ALL BACKTESTS COMPLETE!")
    print("="*70)
    print(f"📁 Results saved in: results/reports/")
    print(f"📊 Charts saved in: results/figures/backtests/")
    print("="*70)
    
    return results_df, results_objects


if __name__ == "__main__":
    run_all_backtests()