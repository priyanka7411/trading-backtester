"""
Test All Trading Strategies
Author: Priyanka
Day 4 - Comprehensive Strategy Testing
"""

import sys
sys.path.append('.')

import pandas as pd
from src.data.data_loader import DataLoader
from src.indicators.technical_indicators import TechnicalIndicators
from src.strategies.ma_crossover import MovingAverageCrossover
from src.strategies.rsi_strategy import RSIStrategy, RSIEnhancedStrategy
from src.strategies.bollinger_strategy import BollingerBandsStrategy, BollingerBandsBreakoutStrategy
from src.strategies.combined_strategy import CombinedStrategy, WeightedCombinedStrategy
from src.strategies.strategy_visualizer import StrategyVisualizer


def test_all_strategies():
    """Test all strategies on AAPL data"""
    
    print("\n" + "="*70)
    print(" TESTING ALL TRADING STRATEGIES")
    print("="*70)
    
    # Load and prepare data
    print("\n Loading data...")
    loader = DataLoader()
    indicators = TechnicalIndicators()
    
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    df_with_indicators = indicators.add_all_indicators(df)
    
    print(f" Loaded {len(df_with_indicators)} days of data")
    
    # Define all strategies
    print("\n Initializing strategies...")
    strategies = [
        # Moving Average Strategies
        MovingAverageCrossover(10, 50),
        MovingAverageCrossover(50, 200),
        
        # RSI Strategies
        RSIStrategy(14, 30, 70),
        RSIEnhancedStrategy(14, 30, 70, 200),
        
        # Bollinger Bands Strategies
        BollingerBandsStrategy(20, 2.0),
        BollingerBandsBreakoutStrategy(20, 2.0),
        
        # Combined Strategies
        CombinedStrategy(30, 70, 2),
        WeightedCombinedStrategy(1.0, 1.5, 1.0, 2.0),
    ]
    
    print(f" Initialized {len(strategies)} strategies")
    
    # Run all strategies
    print("\n" + "="*70)
    print(" RUNNING ALL STRATEGIES")
    print("="*70)
    
    results = {}
    
    for i, strategy in enumerate(strategies, 1):
        print(f"\n[{i}/{len(strategies)}] Running {strategy.name}...")
        try:
            positions = strategy.run(df_with_indicators)
            stats = strategy.get_summary_stats()
            results[strategy.name] = stats
            print(f"    Completed: {stats['total_trades']} trades, "
                  f"{stats['win_rate']:.1%} win rate, "
                  f"{stats['total_return']:.2%} return")
        except Exception as e:
            print(f"    Error: {str(e)}")
            results[strategy.name] = {
                'error': str(e),
                'total_trades': 0,
                'win_rate': 0,
                'total_return': 0
            }
    
    # Create summary table
    print("\n" + "="*70)
    print("STRATEGY PERFORMANCE SUMMARY")
    print("="*70)
    
    summary_df = pd.DataFrame(results).T
    
    # Select key columns
    display_cols = ['total_trades', 'win_rate', 'total_return', 
                   'average_return', 'best_trade', 'worst_trade']
    available_cols = [col for col in display_cols if col in summary_df.columns]
    
    # Format percentages
    for col in ['win_rate', 'total_return', 'average_return', 'best_trade', 'worst_trade']:
        if col in summary_df.columns:
            summary_df[col] = summary_df[col].apply(lambda x: f"{x:.2%}" if isinstance(x, (int, float)) else x)
    
    print("\n" + summary_df[available_cols].to_string())
    
    # Save results
    import os
    os.makedirs('results/reports', exist_ok=True)
    summary_df.to_csv('results/reports/strategy_comparison.csv')
    print(f"\n Saved to: results/reports/strategy_comparison.csv")
    
    # Find best strategies
    print("\n" + "="*70)
    print(" TOP PERFORMING STRATEGIES")
    print("="*70)
    
    valid_results = {k: v for k, v in results.items() if v.get('total_trades', 0) > 0}
    
    if valid_results:
        # Best by total return
        best_return = max(valid_results.items(), key=lambda x: x[1]['total_return'])
        print(f"\n Best Total Return: {best_return[0]}")
        print(f"   Return: {best_return[1]['total_return']:.2%}")
        print(f"   Win Rate: {best_return[1]['win_rate']:.2%}")
        print(f"   Trades: {best_return[1]['total_trades']}")
        
        # Best win rate
        best_winrate = max(valid_results.items(), key=lambda x: x[1]['win_rate'])
        print(f"\n Best Win Rate: {best_winrate[0]}")
        print(f"   Win Rate: {best_winrate[1]['win_rate']:.2%}")
        print(f"   Return: {best_winrate[1]['total_return']:.2%}")
        print(f"   Trades: {best_winrate[1]['total_trades']}")
        
        # Most trades
        most_trades = max(valid_results.items(), key=lambda x: x[1]['total_trades'])
        print(f"\n Most Active: {most_trades[0]}")
        print(f"   Trades: {most_trades[1]['total_trades']}")
        print(f"   Win Rate: {most_trades[1]['win_rate']:.2%}")
        print(f"   Return: {most_trades[1]['total_return']:.2%}")
    
    # Create visualizations
    print("\n" + "="*70)
    print(" CREATING VISUALIZATIONS")
    print("="*70)
    
    viz = StrategyVisualizer()
    
    # Visualize top 3 strategies
    top_strategies = sorted(
        [s for s in strategies if s.name in valid_results],
        key=lambda x: valid_results[x.name]['total_return'],
        reverse=True
    )[:3]
    
    for strategy in top_strategies:
        print(f"\n Visualizing {strategy.name}...")
        viz.plot_signals(strategy, 'AAPL', save=True)
    
    # Create comparison chart
    print(f"\n Creating comparison chart...")
    viz.compare_strategies(strategies[:6], 'AAPL', save=True)
    
    print("\n" + "="*70)
    print(" ALL STRATEGIES TESTED SUCCESSFULLY!")
    print("="*70)
    print(f" Results saved in: results/reports/")
    print(f" Charts saved in: results/figures/strategies/")
    print("="*70)
    
    return strategies, results


if __name__ == "__main__":
    test_all_strategies()