# Data-Analysis-and-Strategy

## Overview
This project involves analyzing stock data using Python and MySQL. It includes:
1. **Data Import (`1_DataBase_Creation.py`):** Fetches data from Google Sheets and stores it in MySQL.
2. **Data Analysis (`2_Analysis.py`):** Calculates Simple Moving Averages (SMAs) and visualizes results.
3. **Unit Testing (`3_Testing.py`):** Validates data types.

## Setup

### Prerequisites
- Python 3.x
- MySQL server
- Libraries:
  ```bash
  pip install pandas mysql-connector-python matplotlib


- Database Configuration
  ------------------------------------
    1) Create Database and User:(SQL)
     '''
      CREATE DATABASE stock_data_db;
      CREATE USER 'bharath'@'localhost' IDENTIFIED BY 'Bharath';
      GRANT ALL PRIVILEGES ON stock_data_db.* TO 'bharath'@'localhost';
      FLUSH PRIVILEGES;
    '''

    2) Run 1_DataBase_Creation.py : Creates the table and inserts data :
     '''
      1_DataBase_Creation.py
     '''
  
    3) Run 2_Analysis.py : Perform analysis and plot results.
     '''
       2_Analysis.py
     '''
    4) Run 3_Testing.py : Execute unit tests.
     '''
       3_Testing.py
     '''
 

How It Works:
--------------------

- 1_DataBase_Creation.py : It imports stock data from Google Sheets and stores it in a MySQL database.

- 2_Analysis.py : It analyzes the stock prices by calculating SMAs and generating plots for visual insights.

- 3_Testing.py : It validates data using unit tests to ensure correct data types.




