import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Database connection parameters
db_config = {
    'user': 'bharath',
    'password': 'Bharath',
    'host': 'localhost',
    'database': 'stock_data_db'
}

# Connect to the database and fetch data
conn = mysql.connector.connect(**db_config)
query = 'SELECT * FROM stock_data ORDER BY datetime'
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Set datetime as index
df.set_index('datetime', inplace=True)

# Calculate SMAs
df['SMA_short'] = df['close'].rolling(window=20).mean()
df['SMA_long'] = df['close'].rolling(window=50).mean()

# Generate signals
df['signal'] = 0
df['signal'][df['SMA_short'] > df['SMA_long']] = 1
df['signal'][df['SMA_short'] < df['SMA_long']] = -1

# Calculate strategy returns
df['returns'] = df['close'].pct_change()
df['strategy_returns'] = df['signal'].shift(1) * df['returns']

# Calculate cumulative returns
df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(df['close'], label='Close Price')
plt.plot(df['SMA_short'], label='20-Day SMA')
plt.plot(df['SMA_long'], label='50-Day SMA')
plt.title('Stock Price and SMA')
plt.legend()
plt.show()

plt.figure(figsize=(14, 7))
plt.plot(df['cumulative_returns'], label='Strategy Returns')
plt.title('Strategy Performance')
plt.legend()
plt.show()
