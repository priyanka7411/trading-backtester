"""
Data Preprocessing Module
Author: Priyanka
Day 2 - Data Cleaning and Validation
"""

import pandas as pd
import numpy as np
from datetime import datetime


class DataPreprocessor:
    """Clean and preprocess stock market data"""
    
    def __init__(self):
        """Initialize preprocessor"""
        print("DataPreprocessor initialized!")
    
    def clean_data(self, df):
        """
        Clean the raw data
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Raw stock data
            
        Returns:
        --------
        pandas.DataFrame
            Cleaned data
        """
        print("\n Cleaning data...")
        
        # Make a copy to avoid modifying original
        df_clean = df.copy()
        
        # 1. Remove duplicates
        initial_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates(subset=['date'])
        duplicates_removed = initial_rows - len(df_clean)
        if duplicates_removed > 0:
            print(f"    Removed {duplicates_removed} duplicate rows")
        
        # 2. Sort by date
        df_clean = df_clean.sort_values('date').reset_index(drop=True)
        print(f"    Sorted data by date")
        
        # 3. Handle missing values
        missing_before = df_clean.isnull().sum().sum()
        if missing_before > 0:
            print(f"     Found {missing_before} missing values")
            # Forward fill for price data
            df_clean = df_clean.fillna(method='ffill')
            # Backward fill any remaining
            df_clean = df_clean.fillna(method='bfill')
            print(f"    Filled missing values")
        
        # 4. Remove rows where price is 0 or negative
        invalid_prices = (df_clean['close'] <= 0).sum()
        if invalid_prices > 0:
            df_clean = df_clean[df_clean['close'] > 0]
            print(f"    Removed {invalid_prices} rows with invalid prices")
        
        # 5. Check for extreme outliers in volume
        volume_mean = df_clean['volume'].mean()
        volume_std = df_clean['volume'].std()
        outliers = df_clean[df_clean['volume'] > volume_mean + 5*volume_std]
        if len(outliers) > 0:
            print(f"     Found {len(outliers)} volume outliers (keeping them)")
        
        print(f"    Final shape: {df_clean.shape}")
        
        return df_clean
    
    def validate_data(self, df):
        """
        Validate data quality
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Data to validate
            
        Returns:
        --------
        dict
            Validation results
        """
        print("\n Validating data...")
        
        validation = {
            'is_valid': True,
            'issues': []
        }
        
        # Check 1: Required columns exist
        required_cols = ['date', 'open', 'high', 'low', 'close', 'volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            validation['is_valid'] = False
            validation['issues'].append(f"Missing columns: {missing_cols}")
        
        # Check 2: No missing values
        if df.isnull().sum().sum() > 0:
            validation['is_valid'] = False
            validation['issues'].append(f"Contains missing values")
        
        # Check 3: Dates are in order
        if not df['date'].is_monotonic_increasing:
            validation['issues'].append("Dates are not in chronological order")
        
        # Check 4: High >= Low
        if (df['high'] < df['low']).any():
            validation['is_valid'] = False
            validation['issues'].append("Some high prices are less than low prices")
        
        # Check 5: Close between High and Low
        invalid_close = ((df['close'] > df['high']) | (df['close'] < df['low'])).sum()
        if invalid_close > 0:
            validation['issues'].append(f"{invalid_close} rows where close is outside high-low range")
        
        # Print results
        if validation['is_valid']:
            print("   Data validation passed!")
        else:
            print("     Data validation found issues:")
            for issue in validation['issues']:
                print(f"      - {issue}")
        
        return validation
    
    def add_basic_features(self, df):
        """
        Add basic calculated features
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Clean stock data
            
        Returns:
        --------
        pandas.DataFrame
            Data with additional features
        """
        print("\n Adding basic features...")
        
        df_features = df.copy()
        
        # 1. Daily returns (percentage change)
        df_features['returns'] = df_features['close'].pct_change()
        print("    Added daily returns")
        
        # 2. Log returns
        df_features['log_returns'] = np.log(df_features['close'] / df_features['close'].shift(1))
        print("    Added log returns")
        
        # 3. Price range (High - Low)
        df_features['price_range'] = df_features['high'] - df_features['low']
        print("    Added price range")
        
        # 4. Price change
        df_features['price_change'] = df_features['close'] - df_features['open']
        print("    Added price change")
        
        # 5. Up/Down day
        df_features['is_up_day'] = (df_features['close'] > df_features['open']).astype(int)
        print("    Added up/down indicator")
        
        # 6. Volume change
        df_features['volume_change'] = df_features['volume'].pct_change()
        print("    Added volume change")
        
        # 7. 5-day rolling average
        df_features['ma_5'] = df_features['close'].rolling(window=5).mean()
        print("    Added 5-day moving average")
        
        # 8. 20-day rolling average
        df_features['ma_20'] = df_features['close'].rolling(window=20).mean()
        print("    Added 20-day moving average")
        
        # Drop the first few rows with NaN values
        initial_len = len(df_features)
        df_features = df_features.dropna()
        dropped = initial_len - len(df_features)
        print(f"    Dropped {dropped} rows with NaN from rolling calculations")
        
        return df_features
    
    def get_data_summary(self, df):
        """
        Get statistical summary of the data
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Stock data
            
        Returns:
        --------
        dict
            Summary statistics
        """
        summary = {
            'total_rows': len(df),
            'date_range': f"{df['date'].min()} to {df['date'].max()}",
            'price_stats': {
                'min': df['close'].min(),
                'max': df['close'].max(),
                'mean': df['close'].mean(),
                'std': df['close'].std()
            },
            'volume_stats': {
                'min': df['volume'].min(),
                'max': df['volume'].max(),
                'mean': df['volume'].mean()
            }
        }
        
        if 'returns' in df.columns:
            summary['returns_stats'] = {
                'mean': df['returns'].mean(),
                'std': df['returns'].std(),
                'min': df['returns'].min(),
                'max': df['returns'].max()
            }
        
        return summary
    
    def save_processed_data(self, df, filename):
        """
        Save processed data to CSV
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Processed data
        filename : str
            Output filename
        """
        output_path = f"data/processed/{filename}"
        df.to_csv(output_path, index=False)
        print(f"\n Saved processed data to: {output_path}")


# Test function
def test_preprocessor():
    """Test the preprocessor"""
    from data_loader import DataLoader
    
    print("\n" + "="*60)
    print(" TESTING DATA PREPROCESSOR")
    print("="*60)
    
    # Load some data
    loader = DataLoader()
    df = loader.load_data('AAPL', '2020-01-01', '2024-01-01')
    
    if df is not None:
        # Initialize preprocessor
        preprocessor = DataPreprocessor()
        
        # Clean data
        df_clean = preprocessor.clean_data(df)
        
        # Validate data
        validation = preprocessor.validate_data(df_clean)
        
        # Add features
        df_features = preprocessor.add_basic_features(df_clean)
        
        # Get summary
        summary = preprocessor.get_data_summary(df_features)
        
        print("\n" + "="*60)
        print("DATA SUMMARY")
        print("="*60)
        print(f"Total Rows: {summary['total_rows']}")
        print(f"Date Range: {summary['date_range']}")
        print(f"\nPrice Statistics:")
        print(f"  Min: ${summary['price_stats']['min']:.2f}")
        print(f"  Max: ${summary['price_stats']['max']:.2f}")
        print(f"  Mean: ${summary['price_stats']['mean']:.2f}")
        print(f"  Std Dev: ${summary['price_stats']['std']:.2f}")
        
        if 'returns_stats' in summary:
            print(f"\nReturns Statistics:")
            print(f"  Mean: {summary['returns_stats']['mean']:.4f}")
            print(f"  Std Dev: {summary['returns_stats']['std']:.4f}")
        
        # Save processed data
        preprocessor.save_processed_data(df_features, 'AAPL_processed.csv')
        
        print("\n Preprocessor test completed!")
        return df_features
    else:
        print(" Failed to load data")
        return None


if __name__ == "__main__":
    test_preprocessor()