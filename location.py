'''import sqlite3

# Connect to your specific database (replace with your actual db filename)
conn = sqlite3.connect('stellar diary.db')
cursor = conn.cursor()

# Query the hidden master table for anything categorized as a 'table'
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch the results
tables = cursor.fetchall()

if tables:
    print("Tables found in your database:")
    for table in tables:
        # fetchall() returns a list of tuples like [('table_name',)], so we slice the string out with [0]
        print(f" -> {table[0]}")
else:
    print("Your database is currently empty. No tables found!")

conn.close()'''

import sqlite3

# Connect to your database
conn = sqlite3.connect('stellar diary.db')
cursor = conn.cursor()

# Replace this with the exact name of the table you found in the last step
table_name = "star_info"

# The PRAGMA command fetches the blueprint of the table
cursor.execute(f"PRAGMA table_info('{table_name}');")
columns = cursor.fetchall()

if columns:
    print(f"Blueprint for table: '{table_name}'\n")
    # Formatting a clean header for the terminal
    print(f"{'CID':<5} | {'Column Name':<20} | {'Data Type':<15} | {'Not Null':<10} | {'Primary Key'}")
    print("-" * 75)

    for col in columns:
        cid = col[0]  # Column ID
        name = col[1]  # Column Name
        dtype = col[2]  # Data Type (INTEGER, TEXT, etc.)
        notnull = "Yes" if col[3] == 1 else "No"  # Is it allowed to be empty?
        pk = "Yes" if col[5] == 1 else "No"  # Is it the Primary Key?

        # Printing each row with aligned spacing
        print(f"{cid:<5} | {name:<20} | {dtype:<15} | {notnull:<10} | {pk}")
else:
    print(f"Table '{table_name}' does not exist or is completely empty.")

conn.close()