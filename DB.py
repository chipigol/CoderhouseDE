import psycopg2
from psycopg2 import sql
from getpass import getpass

# Database connection parameters
dbname = "data-engineer-database"
user = "guidocasella_coderhouse"
host = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com"
port = "5439"  # Default port for Redshift
password = getpass("Enter your password: ")

# Construct the connection string
connection_string = f"dbname='{dbname}' user='{user}' host='{host}' port='{port}' password='{password}'"

try:
    # Establish the connection
    connection = psycopg2.connect(connection_string)

    # Create a cursor
    cursor = connection.cursor()

    # Define the create table query
    create_table_query = sql.SQL("""
        CREATE TABLE guidocasella_coderhouse.STOCKS (
            id INT IDENTITY(1,1),
            ticker INT ,
            "open" FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume INT,
            dividends FLOAT,
            stock_splits FLOAT,
            date DATE,
            PRIMARY KEY (id)
        )
    """)

    # Execute the create table query
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    print("Table 'STOCKS' created successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error:", e)
