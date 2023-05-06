import sqlite3

# Create a connection to the database
conn = sqlite3.connect('students.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the students table with the desired fields
cursor.execute('''CREATE TABLE students
                (id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 roll_no TEXT,
                 phone TEXT,
                 branch TEXT,
                 cgpa REAL,
                 house TEXT)''')

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection to the database
cursor.close()
conn.close()
