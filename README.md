# figment
python script using pandas which generates a sql insert script by pulling manually collected data from a csv

Rewards Data Processing Script

Overview

This script processes a CSV file containing blockchain rewards data and generates SQL INSERT statements to populate a database table. The output is saved in a text file (sql_query.txt) for further use.

Features

Reads rewards data from task1.csv.

Converts the data into SQL INSERT statements.

Handles NULL values correctly.

Creates a Rewards table if it does not already exist.

Stores the generated SQL statements in sql_query.txt.

Prerequisites

Python 3.x

pandas library (install using pip install pandas)

Usage

Place your task1.csv file in the same directory as the script.

Run the script using:

python script.py

The generated SQL script will be saved as sql_query.txt.

CSV Format

The task1.csv file should have the following columns:

Date (Date of reward collection)

Address (Blockchain address)

Protocol (Blockchain protocol, e.g., AXL, INJ)

Rewards (Earned rewards amount)

Output

The script generates a SQL file (sql_query.txt) with:

A CREATE TABLE statement for the Rewards table.

INSERT INTO statements for each row in the CSV.

Example Output

SQL Table Creation:

CREATE TABLE IF NOT EXISTS Rewards (
    Date DATE NOT NULL,
    Address VARCHAR NOT NULL,
    Protocol VARCHAR,
    Rewards DOUBLE,
    PRIMARY KEY (Date, Address)
);

SQL Insert Statement:

INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-30', '0xABC123', 'AXL', '100.5');

Notes

Ensure the CSV file is properly formatted before running the script.

The script assumes all data in the CSV is valid and formatted correctly.

NULL values are automatically handled in the generated SQL statements.

License

This project is open-source and can be used or modified as needed.
