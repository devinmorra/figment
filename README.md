# Python Data Processing and SQL Insert Generator

This script processes data from a CSV file, converts specific protocol values, and generates SQL `INSERT` statements to populate a database table.

## Overview

- The script reads data from a CSV file (`task1.csv`).
- It applies protocol-specific conversions to reward values (`AXL`, `INJ`).
- It generates SQL `INSERT` statements based on the data and writes them to `sql_query.txt`.

## Features

- **Data Cleaning:** Cleans and converts protocol values using regex.
- **Protocol Conversion:** Converts `AXL` and `INJ` reward values to their proper formats.
- **Extensible:** Easily extendable to handle additional protocols.
- **SQL Generation:** Automatically generates SQL `INSERT` statements.

## How It Works

1. **Imports:** Uses `pandas` for data handling and `re` for regular expressions.
2. **Data Cleaning and Conversion:** 
   - The `clean()` function removes non-digit characters and converts the value to an integer.
   - The `axl_converter()` and `inj_converter()` functions convert `uAXL` and `INJ` values into proper formats.
3. **CSV Handling:** Reads a CSV file (`task1.csv`) and processes each row.
4. **SQL Script Generation:** Generates `INSERT` statements and outputs a file.

## Functions

### `clean(string)`
Cleans the input string, removing non-digit characters, and returns the result as an integer.

### `axl_converter(value)`
Converts `uAXL` values to `AXL` by first cleaning them and then dividing by `1,000,000`.

### `inj_converter(value)`
Converts `INJ` values by first cleaning them and then dividing by `10^18`.

### `protocol_converters`
A dictionary that maps protocol names to their respective conversion functions.
Increases extensibility and maintainability of the script

## Example

Given a CSV file with the following structure:

| Date       | Address     | Protocol | Rewards    |
|------------|-------------|----------|------------|
| 2025-03-01 | 0xAddress1  | AXL      | 9660870969uaxl  |
| 2025-03-01 | 0xAddress2  | INJ      | 3285666740868039103281inj  |

The script generates an `INSERT` statement for each row:

```sql
INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-01', '0xAddress1', 'AXL', 9660.870969);
INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-01', '0xAddress2', 'INJ', 3285.666740868039);
```

## Requirements

- Python 3.x
- pandas library

Install the required package using pip:

```bash
pip install pandas
```

## Usage

1. Place your CSV file (e.g., `task1.csv`) in the same directory as the script.
2. Run the Python script:

```bash
python script_name.py
```

3. The script will generate a file named `sql_query.txt` containing the SQL `CREATE TABLE` and `INSERT INTO` statements.

## CSV File Format

The CSV file should contain the following columns:

- `Date` (`YYYY-MM-DD`, `HH:MM:SS` optional, but will be handled)
- `Address` (string, required)
- `Protocol` (string, optional)
- `Rewards` (numeric, optional)

## Example Output

The generated `sql_query.txt` file will contain SQL statements like this:

```sql
CREATE TABLE IF NOT EXISTS Rewards (
    Date DATETIME NOT NULL,
    Address VARCHAR NOT NULL,
    Protocol VARCHAR,
    Rewards DOUBLE,
    PRIMARY KEY (Date, Address)
);

INSERT INTO Rewards (Date, Address, Protocol, Rewards) VALUES ('2025-03-30', '12345ABC', 'ProtocolName', 100.50);
```

## Notes

- `NULL` values will be inserted for missing optional fields.
- Ensure your CSV file follows the correct format to avoid errors.
