import pandas as pd
import re


# with extensibility in mind, we can clean and handle multiple protocols
# simple regex to clean up string and cast as int
def clean(string):
    return int(re.sub(r'\D', '', string))


# I think it's best to handle the conversion in script than have the data gatherer do so
# Convert uaxl to AXL
def axl_converter(value):
    cleaned_value = clean(value)
    return cleaned_value / 1000000 if cleaned_value else 0


# Set proper decimal places for INJ
def inj_converter(value):
    cleaned_value = clean(value)
    return cleaned_value / 10**18 if cleaned_value else 0


# Given that Figment handles dozens of chains, I feel this may be required
# it seems the easiest way to extend and maintain the code
protocol_converters = {
    "AXL": axl_converter,
    "INJ": inj_converter
}

# Read data from CSV
data = pd.read_csv('task1.csv', delimiter=',')

# Generate INSERT statements
insert_statements = []
for index, row in data.iterrows():
    columns = ', '.join([f"{col}" for col in row.index])
    values = ', '.join([
        "NULL" if pd.isna(value) else
        # confirm protocol used per row, applying the appropriate conversion
        f"{protocol_converters.get(row['Protocol'], lambda x: x)(str(value))}" if column == 'Rewards' else
        f"'{value}'"
        for column, value in row.items()
    ])

    insert_statement = f"INSERT INTO Rewards ({columns}) VALUES ({values});"
    insert_statements.append(insert_statement)

# Write INSERT statements to a file
with open('sql_query.txt', 'w') as f:
    f.write("CREATE TABLE IF NOT EXISTS Rewards ("
            "Date DATETIME NOT NULL, "
            "Address VARCHAR NOT NULL, "
            "Protocol VARCHAR, "
            "Rewards DOUBLE, "
            "PRIMARY KEY (Date, Address)"
            ");\n\n")
    for statement in insert_statements:
        f.write(statement + '\n')

print("Insert script generated successfully. Please check sql_query.txt file.")
