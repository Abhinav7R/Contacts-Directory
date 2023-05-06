import sqlite3

# Connect to the database (will create a new one if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "faculty" table
cursor.execute('''CREATE TABLE faculty
                (id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 phone TEXT,
                 major_research_area TEXT,
                 office_hours TEXT,
                 office TEXT)''')

# Create the "students" table
cursor.execute('''CREATE TABLE students
                (id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 roll_no TEXT,
                 phone TEXT,
                 branch TEXT,
                 cgpa REAL,
                 house TEXT)''')

# Commit the changes and close the connection
conn.commit()
conn.close()
