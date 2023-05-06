from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Define route to display the add student form


@app.route('/')
def add_faculty():
    return render_template('add_faculty.html')

# Define route to handle form submission


@app.route('/add_faculty_submit', methods=['GET'])
def add_faculty_submit():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    major_research_area = request.args.get('major_research_area')
    office_hours = request.args.get('office_hours')
    office = request.args.get('office')

    # Store the data in the database
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, email, roll_no, phone, branch, cgpa, house) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (name, email, phone, major_research_area, office_hours, office))
    conn.commit()
    conn.close()

    message = f'Successfully added {name} to the database!'
    return render_template('add_faculty.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/view_students')
# def view_students():
#     # Connect to the database
#     conn = sqlite3.connect('students.db')
#     c = conn.cursor()

#     # Execute a SELECT statement to retrieve all the rows from the students table
#     c.execute('SELECT * FROM students')
#     rows = c.fetchall()

#     # Close the database connection
#     conn.close()

#     # Render the rows in an HTML table using the view_students.html template
#     return render_template('view_students.html', rows=rows)
