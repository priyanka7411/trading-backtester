"""
Download historical data for multiple stocks
Author: Priyanka
Day 2 - Data Collection
"""

import sys
sys.path.append('.')

from src.data.data_loader import DataLoader


def download_portfolio_data():
    """Download data for our portfolio of stocks"""
    
    print("\n" + "="*60)
    print(" DOWNLOADING PORTFOLIO DATA")
    print("="*60)
    
    # Initialize loader
    loader = DataLoader()
    
    # List of stocks to download
    symbols = [
        'AAPL',   # Apple
        'MSFT',   # Microsoft
        'GOOGL',  # Google
        'AMZN',   # Amazon
        'TSLA',   # Tesla
        'SPY'     # S&P 500 ETF (for benchmark)
    ]
    
    # Date range
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    
    print(f"\n Date Range: {start_date} to {end_date}")
    print(f" Stocks: {', '.join(symbols)}")
    print("\n" + "-"*60)
    
    # Download each stock
    results = {}
    for symbol in symbols:
        print(f"\n Processing {symbol}...")
        df = loader.download_data(symbol, start_date, end_date)
        
        if df is not None:
            results[symbol] = df
            print(f"    Success! Downloaded {len(df)} rows")
        else:
            print(f"    Failed to download {symbol}")
    
    # Summary
    print("\n" + "="*60)
    print(" DOWNLOAD SUMMARY")
    print("="*60)
    print(f" Successfully downloaded: {len(results)}/{len(symbols)} stocks")
    print(f" Files saved in: data/raw/")
    print("\n" + "="*60)
    
    return results


if __name__ == "__main__":
    download_portfolio_data()
    print("\n Data download complete! Ready for analysis! ✨\n")