import yfinance as yf
from datetime import datetime, timedelta

# List of company tickers
company_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# Calculate the date range
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Create an empty dictionary to store company data
company_data = {}

# Retrieve data for each company
for ticker in company_tickers:
    company = yf.Ticker(ticker)
    data = company.history(start=start_date, end=end_date)
    company_data[ticker] = data

# Print retrieved data for each company
for ticker, data in company_data.items():
    print(f"Company: {ticker}")
    print(data)
    print("\n")