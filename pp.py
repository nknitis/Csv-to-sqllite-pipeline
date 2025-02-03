import sqlite3

# Create or connect to an SQLite database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()


import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('people.csv')

# Check the first few rows of the data
print(df)





# Drop rows with missing data (if any)
df = df.dropna()

# Convert the 'age' column to integers (just in case it's not in the right format)
df['age'] = df['age'].astype(int)

# View the transformed data
print(df.head())



# Connect to the SQLite database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Insert the data into the SQL table
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO people (id, name, age, city) 
    VALUES (?, ?, ?, ?)
    ''', (row['id'], row['name'], row['age'], row['city']))

# Commit and close the connection
conn.commit()
conn.close()

print("Data successfully loaded into the database!")


# Connect to the SQLite database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Query the data from the table
cursor.execute("SELECT * FROM people")
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# # Close the connection
# conn.close()

