import pandas as pd
import numpy as np

class WeatherRiskPipeline:
    """
    Data pipeline for processing historical meteorological time-series data.
    Transitions legacy MATLAB mathematical models (Fourier/Polynomial fits) 
    into scalable Python/Pandas data structures for yield prediction.
    """
    
    def __init__(self, raw_data_path: str):
        self.raw_data_path = raw_data_path
        self.df = None

    def load_and_clean_data(self) -> pd.DataFrame:
        """
        Loads raw daily precipitation/temperature data and handles missing 
        sensor values using piecewise linear interpolation, mirroring the 
        methodology from the LUT precipitation forecasting model.
        """
        # Load raw SYNOP/METAR data
        # self.df = pd.read_csv(self.raw_data_path, parse_dates=['date'])
        
        # Placeholder for demonstration until FMI API is fully connected
        dates = pd.date_range(start="2000-01-01", end="2026-01-01", freq='D')
        self.df = pd.DataFrame({
            'date': dates,
            'precipitation_mm': np.random.uniform(0, 10, len(dates))
        })
        self.df.set_index('date', inplace=True)

        # Interpolate missing sensor gaps linearly (replaces MATLAB piecewise interpolation)
        self.df['precipitation_mm'] = self.df['precipitation_mm'].interpolate(method='linear')
        
        return self.df

    def aggregate_monthly(self) -> pd.DataFrame:
        """
        Aggregates highly stochastic daily weather data into monthly sums 
        to filter out daily noise, preparing the dataset for Fourier 
        seasonal wave modeling and long-term linear trend analysis.
        """
        if self.df is None:
            self.load_and_clean_data()
            
        # Resample daily data to monthly cumulative totals
        monthly_df = self.df.resample('ME').sum()
        monthly_df.rename(columns={'precipitation_mm': 'monthly_total_mm'}, inplace=True)
        
        return monthly_df

    def fit_linear_trend(self, series: pd.Series) -> np.ndarray:
        """
        Applies a first-degree polynomial (least squares) to find the long-term 
        climate trend across the dataset, utilizing NumPy's polyfit.
        """
        x = np.arange(len(series))
        y = series.values
        
        # Fit 1st-degree polynomial (linear trendline)
        coefficients = np.polyfit(x, y, 1)
        trendline = np.polyval(coefficients, x)
        
        return trendline

if __name__ == "__main__":
    print("Initializing Project Auer: Weather Risk Assessment Pipeline...")
    pipeline = WeatherRiskPipeline(raw_data_path="fmi_data_niinisalo.csv")
    
    # Run the processing steps
    monthly_data = pipeline.aggregate_monthly()
    trend = pipeline.fit_linear_trend(monthly_data['monthly_total_mm'])
    
    print(f"Successfully processed {len(monthly_data)} months of historical data.")
    print("Ready for Fourier wave integration.")
