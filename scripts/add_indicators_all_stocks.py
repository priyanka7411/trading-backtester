"""
Add Technical Indicators to All Stocks
Author: Priyanka
Day 3 - Batch Indicator Processing
"""

import sys
sys.path.append('.')

import pandas as pd
from src.data.data_loader import DataLoader
from src.data.preprocessor import DataPreprocessor
from src.indicators.technical_indicators import TechnicalIndicators
from src.indicators.indicator_visualizer import IndicatorVisualizer
import os


def add_indicators_to_all_stocks():
    """Add technical indicators to all portfolio stocks"""
    
    print("\n" + "="*70)
    print("📊 ADDING INDICATORS TO ALL STOCKS")
    print("="*70)
    
    # Initialize components
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    indicators = TechnicalIndicators()
    viz = IndicatorVisualizer()
    
    # Portfolio symbols
    symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'SPY']
    date_range = ('2020-01-01', '2024-01-01')
    
    processed_stocks = {}
    summary_data = []
    
    for symbol in symbols:
        print(f"\n{'='*70}")
        print(f"📈 Processing {symbol}")
        print(f"{'='*70}")
        
        try:
            # Load data
            df = loader.load_data(symbol, date_range[0], date_range[1])
            
            if df is None or df.empty:
                print(f"❌ No data available for {symbol}")
                continue
            
            # Ensure date is datetime
            df['date'] = pd.to_datetime(df['date'])
            
            # Clean data
            print("🧹 Cleaning data...")
            df_clean = preprocessor.clean_data(df)
            
            # Add basic features
            print("✨ Adding basic features...")
            df_features = preprocessor.add_basic_features(df_clean)
            
            # Add technical indicators
            print("📊 Adding technical indicators...")
            df_with_indicators = indicators.add_all_indicators(df_features)
            
            # Save processed data with indicators
            output_file = f'data/processed/{symbol}_with_indicators.csv'
            os.makedirs('data/processed', exist_ok=True)
            df_with_indicators.to_csv(output_file, index=False)
            print(f"💾 Saved: {output_file}")
            
            # Store for visualization
            processed_stocks[symbol] = df_with_indicators
            
            # Calculate summary statistics
            summary_data.append({
                'Symbol': symbol,
                'Data Points': len(df_with_indicators),
                'Current Price': f"${df_with_indicators['close'].iloc[-1]:.2f}",
                'Latest RSI': f"{df_with_indicators['rsi'].iloc[-1]:.2f}",
                'Latest MACD': f"{df_with_indicators['macd'].iloc[-1]:.4f}",
                'ATR': f"{df_with_indicators['atr'].iloc[-1]:.2f}",
                'ADX': f"{df_with_indicators['adx'].iloc[-1]:.2f}"
            })
            
            # Create individual visualizations
            print(f"📊 Creating visualizations for {symbol}...")
            viz.plot_rsi(df_with_indicators, symbol, save=True)
            viz.plot_macd(df_with_indicators, symbol, save=True)
            viz.plot_bollinger_bands(df_with_indicators, symbol, save=True)
            
            print(f"✅ {symbol} processing complete!")
            
        except Exception as e:
            print(f"❌ Error processing {symbol}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # Create summary report
    print("\n" + "="*70)
    print("📊 INDICATOR SUMMARY REPORT")
    print("="*70)
    
    summary_df = pd.DataFrame(summary_data)
    print(summary_df.to_string(index=False))
    
    # Save summary
    os.makedirs('results/reports', exist_ok=True)
    summary_df.to_csv('results/reports/indicators_summary.csv', index=False)
    print("\n💾 Summary saved to: results/reports/indicators_summary.csv")
    
    # Create dashboards for top stocks
    print("\n" + "="*70)
    print("📊 CREATING COMPREHENSIVE DASHBOARDS")
    print("="*70)
    
    for symbol in ['AAPL', 'MSFT', 'TSLA']:
        if symbol in processed_stocks:
            print(f"\n📈 Creating dashboard for {symbol}...")
            viz.plot_all_indicators(processed_stocks[symbol], symbol, save=True)
    
    print("\n" + "="*70)
    print("🎉 ALL INDICATORS ADDED SUCCESSFULLY!")
    print("="*70)
    print(f"✅ Processed {len(processed_stocks)} stocks")
    print(f"📁 Data saved in: data/processed/")
    print(f"📊 Charts saved in: results/figures/indicators/")
    print(f"📄 Summary saved in: results/reports/")
    print("="*70)


if __name__ == "__main__":
    add_indicators_to_all_stocks()