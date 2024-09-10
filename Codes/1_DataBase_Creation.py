import mysql.connector
import pandas as pd

# Database connection parameters
db_config = {
    'user': 'bharath',
    'password': 'Bharath',
    'host': 'localhost',
    'database': 'stock_data_db'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cur = conn.cursor()

# Create table
cur.execute('''
    CREATE TABLE stock_data (
        datetime DATETIME,
        open DECIMAL(10, 2),
        high DECIMAL(10, 2),
        low DECIMAL(10, 2),
        close DECIMAL(10, 2),
        volume INT,
        instrument VARCHAR(10)
    );
''')

conn.commit()
cur.close()

# Fetch data from Google Sheets and insert into the database
sheet_url = 'https://docs.google.com/spreadsheets/d/1-rIkEb94tZ69FvsjXnfkVETYu6rftF-8/export?format=csv'
df = pd.read_csv(sheet_url)

# Convert datetime column to proper format
df['datetime'] = pd.to_datetime(df['datetime'])

# Insert data into the table
insert_query = '''
    INSERT INTO stock_data (datetime, open, high, low, close, volume, instrument)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
'''

with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute(insert_query, (
                row['datetime'],
                row['open'],
                row['high'],
                row['low'],
                row['close'],
                row['volume'],
                row['instrument']
            ))
        conn.commit()


print('Succefully the Database and the Tables are created')