import yfinance as yf
import matplotlib.pyplot as plt
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

# Create subplots for each company
fig, axs = plt.subplots(len(company_tickers), 1, figsize=(10, 6 * len(company_tickers)))

# Plot Close values for each company
for idx, (ticker, data) in enumerate(company_data.items()):
    ax = axs[idx]
    ax.plot(data.index, data['Close'], label=ticker)
    ax.set_title(f"Close Value Evolution - {ticker}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Value")
    ax.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
