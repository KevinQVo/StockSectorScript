import requests
import pandas as pd
from urllib.parse import quote

# API Key
API_KEY = '*********'
BASE_URL = "https://financialmodelingprep.com/api/v3"

# Function to fetch stock symbols by sector
def get_stocks_by_sector(sector):
    url = f"{BASE_URL}/stock-screener?sector={sector}&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            df = df[['symbol', 'companyName', 'sector', 'price', 'marketCap']]
            return df
        else:
            print("No data found for the specified sector.")
            return None
    else:
        print("Error fetching data:", response.status_code)
        print("Response:", response.text)  
        return None

# Input sector name
sector = input("Please enter the desired sector: ")
sector = quote(sector)  # URL encode for spaces

# Fetch and save stocks data
stocks_df = get_stocks_by_sector(sector)

if stocks_df is not None:
    print(stocks_df)
    stocks_df.to_csv(f"{sector}_stocks.csv", index=False)
    print(f"Data saved to '{sector}_stocks.csv'")
