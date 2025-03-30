# figment
python script using pandas which generates a sql insert script by pulling manually collected data from a csv

README.md
Rewards Data Processing Script
Overview

This script reads blockchain rewards data from a CSV file (task1.csv), processes it, and generates SQL INSERT statements. The output is saved in sql_query.txt, which includes a table creation script and the INSERT statements.
How It Works

    Reads data from task1.csv.

    Converts each row into an INSERT statement.

    Handles missing values by inserting NULL.

    Saves the SQL statements into sql_query.txt.

    Prints a success message upon completion.

Requirements

    Python 3.x

    pandas library (pip install pandas)

Usage

    Place task1.csv in the same directory as the script.

    Run the script:

    python script.py

    The generated SQL script will be saved as sql_query.txt.

Table Schema

The script creates a Rewards table if it doesn’t exist, with the following structure:
Column	Data Type	Constraints
Date	DATE	NOT NULL, PRIMARY KEY
Address	VARCHAR	NOT NULL, PRIMARY KEY
Protocol	VARCHAR	-
Rewards	DOUBLE	-
Output Example

Generated SQL in sql_query.txt:

CREATE TABLE IF NOT EXISTS Rewards (
    Date DATE NOT NULL,
    Address VARCHAR NOT NULL,
    Protocol VARCHAR,
    Rewards DOUBLE,
    PRIMARY KEY (Date, Address)
);

INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-30', 'addr1', 'AXL', '100.5');
INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-31', 'addr2', 'INJ', NULL);

Notes

    Ensure all dates are in YYYY-MM-DD format.

    Missing values are inserted as NULL.

    Check sql_query.txt after execution.
