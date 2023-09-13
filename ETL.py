import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import psycopg2
from getpass import getpass

# List of company tickers
company_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# Calculate the date range
end_date = datetime.today()
start_date = end_date - timedelta(days=1)

# Create an empty list to store DataFrames for each company
company_dataframes = []

# Retrieve data for each company and append to the list
for ticker in company_tickers:
    company = yf.Ticker(ticker)
    data = company.history(period="1d", start=start_date, end=end_date)
    data['Ticker'] = ticker  # Add a ticker column
    company_dataframes.append(data)

# Concatenate the DataFrames into a single DataFrame
combined_data = pd.concat(company_dataframes)

# Reset the index
combined_data.reset_index(inplace=True)

# Database connection parameters
dbname = "data-engineer-database"
user = "guidocasella_coderhouse"
host = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com"
port = "5439"  # Default port for Redshift
password = getpass("Enter your password: ")

# Create a connection to Redshift
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    host=host,
    port=port,
    password=password
)

# Create a cursor object
cur = conn.cursor()

# Insert data into the "stocks" table
inserted_data = []  # List to store inserted data

for index, row in combined_data.iterrows():
    insert_query = f"INSERT INTO stocks (ticker, \"open\", high, low, close, volume, dividends, stock_splits, date) VALUES ('{row['Ticker']}', {row['Open']}, {row['High']}, {row['Low']}, {row['Close']}, {row['Volume']}, {row['Dividends']}, {row['Stock Splits']}, '{row['Date']}'::DATE);"
    cur.execute(insert_query)
    inserted_data.append(row)  # Append the inserted row to the list

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

# Print the inserted data
print("Data inserted into Redshift:")
print(pd.DataFrame(inserted_data))
