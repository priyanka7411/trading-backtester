"""
Process all downloaded stock data
Author: Priyanka
Day 2 - Batch Processing
"""

import sys
sys.path.append('.')

from src.data.data_loader import DataLoader
from src.data.preprocessor import DataPreprocessor
from src.utils.visualizer import Visualizer
import pandas as pd


def process_all_stocks():
    """Process all stocks in our portfolio"""
    
    print("\n" + "="*60)
    print("🔄 PROCESSING ALL STOCKS")
    print("="*60)
    
    # Initialize tools
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    viz = Visualizer()
    
    # Our portfolio
    symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'SPY']
    date_range = ('2020-01-01', '2024-01-01')
    
    processed_data = {}
    summary_stats = []
    
    for symbol in symbols:
        print(f"\n{'='*60}")
        print(f"📊 Processing {symbol}")
        print(f"{'='*60}")
        
        # Load data
        df = loader.load_data(symbol, date_range[0], date_range[1])
        
        if df is not None and not df.empty:
            # Clean data
            df_clean = preprocessor.clean_data(df)
            
            # Validate
            validation = preprocessor.validate_data(df_clean)
            
            # Add features
            df_processed = preprocessor.add_basic_features(df_clean)
            
            # Save processed data
            preprocessor.save_processed_data(
                df_processed, 
                f'{symbol}_processed.csv'
            )
            
            # Store in dict for comparison
            processed_data[symbol] = df_processed
            
            # Get summary statistics
            summary = preprocessor.get_data_summary(df_processed)
            
            # Add to summary list
            summary_stats.append({
                'Symbol': symbol,
                'Total Days': summary['total_rows'],
                'Min Price': f"${summary['price_stats']['min']:.2f}",
                'Max Price': f"${summary['price_stats']['max']:.2f}",
                'Avg Price': f"${summary['price_stats']['mean']:.2f}",
                'Avg Return': f"{summary['returns_stats']['mean']:.4f}",
                'Volatility': f"{summary['returns_stats']['std']:.4f}"
            })
            
            # Create individual visualizations
            print(f"\n📊 Creating visualizations for {symbol}...")
            viz.plot_price_history(df_processed, symbol, save=True)
            
            print(f"\n✅ {symbol} processing complete!")
        else:
            print(f"❌ Failed to process {symbol}")
    
    # Create summary table
    print("\n" + "="*60)
    print("📊 PORTFOLIO SUMMARY")
    print("="*60)
    summary_df = pd.DataFrame(summary_stats)
    print(summary_df.to_string(index=False))
    
    # Save summary
    summary_df.to_csv('results/reports/portfolio_summary.csv', index=False)
    print("\n💾 Summary saved to: results/reports/portfolio_summary.csv")
    
    # Create comparison visualization
    if len(processed_data) > 1:
        print("\n📊 Creating comparison charts...")
        viz.plot_comparison(processed_data, save=True)
    
    print("\n" + "="*60)
    print("🎉 ALL STOCKS PROCESSED SUCCESSFULLY!")
    print("="*60)
    print(f"✅ Processed {len(processed_data)} stocks")
    print(f"📁 Data saved in: data/processed/")
    print(f"📊 Charts saved in: results/figures/")
    print(f"📄 Summary saved in: results/reports/")
    print("="*60)


if __name__ == "__main__":
    process_all_stocks()