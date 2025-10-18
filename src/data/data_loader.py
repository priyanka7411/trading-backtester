"""
Simple Data Loader for Day 1
Author: Priyanka
Date: October 2025
"""

import os
import pandas as pd
import yfinance as yf
from datetime import datetime


class DataLoader:
    """Simple data loader for downloading stock data"""
    
    def __init__(self):
        """Initialize the data loader"""
        self.data_dir = "data/raw"
        # Create directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        print("✅ DataLoader initialized!")
    
    def download_data(self, symbol, start_date, end_date):
        """
        Download historical stock data
        
        Parameters:
        -----------
        symbol : str
            Stock ticker symbol (e.g., 'AAPL')
        start_date : str
            Start date in 'YYYY-MM-DD' format
        end_date : str
            End date in 'YYYY-MM-DD' format
            
        Returns:
        --------
        pandas.DataFrame
            Historical stock data with OHLCV columns
        """
        print(f"\n📥 Downloading data for {symbol}...")
        print(f"   From: {start_date}")
        print(f"   To: {end_date}")
        
        try:
            # Download data using yfinance
            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start_date, end=end_date)
            
            # Check if data was downloaded
            if df.empty:
                print(f"❌ No data found for {symbol}")
                return None
            
            # Clean up the data
            df = df.reset_index()
            df.columns = df.columns.str.lower()
            
            # Save to CSV
            filename = f"{self.data_dir}/{symbol}_{start_date}_{end_date}.csv"
            df.to_csv(filename, index=False)
            
            print(f"✅ Downloaded {len(df)} rows")
            print(f"💾 Saved to: {filename}")
            
            return df
            
        except Exception as e:
            print(f"❌ Error downloading {symbol}: {str(e)}")
            return None
    
    def load_data(self, symbol, start_date, end_date):
        """
        Load data from CSV or download if not available
        
        Parameters:
        -----------
        symbol : str
            Stock ticker symbol
        start_date : str
            Start date
        end_date : str
            End date
            
        Returns:
        --------
        pandas.DataFrame
            Historical stock data
        """
        filename = f"{self.data_dir}/{symbol}_{start_date}_{end_date}.csv"
        
        # Check if file exists
        if os.path.exists(filename):
            print(f"📂 Loading data from {filename}")
            df = pd.read_csv(filename)
            # Ensure date column is datetime (handle timezone-aware dates)
            df['date'] = pd.to_datetime(df['date'], utc=True).dt.tz_localize(None)
            print(f"✅ Loaded {len(df)} rows")
            return df
        else:
            print(f"📥 File not found. Downloading...")
            return self.download_data(symbol, start_date, end_date)
    
    def get_data_info(self, df):
        """
        Display information about the downloaded data
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Stock data
        """
        if df is None or df.empty:
            print("❌ No data to display")
            return
        
        print("\n" + "="*50)
        print("📊 DATA INFORMATION")
        print("="*50)
        print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"\nColumns: {list(df.columns)}")
        print(f"\nDate Range: {df['date'].min()} to {df['date'].max()}")
        print(f"\nMissing Values:\n{df.isnull().sum()}")
        print(f"\nFirst Few Rows:")
        print(df.head())
        print("\n" + "="*50)


# Test function to download sample data
def test_download():
    """Test function to download sample data"""
    print("\n🚀 TESTING DATA LOADER")
    print("="*50)
    
    # Create loader
    loader = DataLoader()
    
    # Download Apple stock data for last 2 years
    df = loader.download_data(
        symbol='AAPL',
        start_date='2022-01-01',
        end_date='2024-01-01'
    )
    
    # Show data info
    if df is not None:
        loader.get_data_info(df)
        print("\n✅ Data loader test completed successfully!")
    else:
        print("\n❌ Data loader test failed!")


if __name__ == "__main__":
    test_download()