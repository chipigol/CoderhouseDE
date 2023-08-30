from sqlalchemy import create_engine, Column, Float, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from getpass import getpass

# Database connection parameters
dbname = "data-engineer-database"
user = "guidocasella_coderhouse"
host = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com"
port = "5439"  # Default port for Redshift

# Prompt for password securely
password = getpass("Enter your password: ")

# Construct the connection URL
connection_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

# Define the table using SQLAlchemy's declarative_base
Base = declarative_base()

class Stocks(Base):
    __tablename__ = 'stocks'
    __table_args__ = {'schema': 'guidocasella_coderhouse'}
    
    id = Column(Integer, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    dividends = Column(Float)
    stock_splits = Column(Float)
    date = Column(Date)

try:
    # Create an engine
    engine = create_engine(connection_url)

    # Create the table
    Base.metadata.create_all(engine)

    print("Table 'Stocks' created successfully.")

except Exception as e:
    print("Error:", e)
