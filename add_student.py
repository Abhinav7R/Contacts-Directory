
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Define route to display the add student form


@app.route('/')
def add_students():
    return render_template('add_students.html')

# Define route to handle form submission


@app.route('/add_students_submit', methods=['GET'])
def add_students_submit():
    name = request.args.get('name')
    email = request.args.get('email')
    roll_no = request.args.get('roll_no')
    phone = request.args.get('phone')
    branch = request.args.get('branch')
    cgpa = request.args.get('cgpa')
    house = request.args.get('house')

    # Store the data in the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, email, roll_no, phone, branch, cgpa, house) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (name, email, roll_no, phone, branch, cgpa, house))
    conn.commit()
    conn.close()

    message = f'Successfully added {name} to the database!'
    return render_template('add_students.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
