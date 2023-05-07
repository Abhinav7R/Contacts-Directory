#!/usr/bin/python3

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def initialize_db(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    if database == 'students.db':
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     email TEXT,
                     roll_no TEXT,
                     phone TEXT,
                     branch TEXT,
                     cgpa REAL,
                     house TEXT)''')
    elif database == 'faculty.db':
        cursor.execute('''CREATE TABLE IF NOT EXISTS faculty
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     email TEXT,
                     phone TEXT,
                     major_research_area TEXT,
                     office_hours TEXT,
                     office TEXT)''')

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth_students')
def auth_students():
    return render_template('auth_students.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/update_students.html')
def update_students():
    return render_template('update_students.html')

@app.route('/update_faculty.html')
def update_fac():
    return render_template('update_faculty.html')

@app.route('/add_students.html')
def add_students():
    return render_template('add_students.html')

@app.route('/add_faculty.html')
def add_faculty():
    return render_template('add_faculty.html')

@app.route('/search_stud.html')
def search_stud_html():
    return redirect(url_for('search_students'))

@app.route('/search_fac.html')
def search_fac_html():
    return redirect(url_for('search_fac'))

@app.route('/search_stud', methods=['GET', 'POST'])
def search_students():
    if request.method == 'POST':
        search_option = request.form.get('select-option')
        search_term = request.form.get('Value')

        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        
        if search_option == "option1":
            c.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option2":
            c.execute("SELECT * FROM students WHERE roll_no LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option3":
            c.execute("SELECT * FROM students WHERE House LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option4":
            c.execute("SELECT * FROM students WHERE phone LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option5":
            c.execute("SELECT * FROM students WHERE branch LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option6":
            c.execute("SELECT * FROM students WHERE cgpa LIKE ?", ('%' + search_term + '%',))
            
        rows = c.fetchall()
        conn.close()

        return render_template('search_stud.html', rows=rows)

    return render_template('search_stud.html')

@app.route('/search_fac', methods=['GET', 'POST'])
def search_fac():
    if request.method == 'POST':
        search_option = request.form.get('select-option')
        search_term = request.form.get('Value')

        conn = sqlite3.connect('faculty.db')
        c = conn.cursor()
        
        if search_option == "option1":
            c.execute("SELECT * FROM faculty WHERE name LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option2":
            c.execute("SELECT * FROM faculty WHERE email LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option3":
            c.execute("SELECT * FROM faculty WHERE major_research_area LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option4":
            c.execute("SELECT * FROM faculty WHERE phone LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option5":
            c.execute("SELECT * FROM faculty WHERE office_hours LIKE ?", ('%' + search_term + '%',))
        elif search_option == "option6":
            c.execute("SELECT * FROM faculty WHERE office LIKE ?", ('%' + search_term + '%',))
            
        rows = c.fetchall()
        conn.close()

        return render_template('search_fac.html', rows=rows)
    return render_template('search_fac.html')

@app.route('/add_students_submit', methods=['GET'])
def add_students_submit():
    initialize_db('students.db')
    name = request.args.get('name')
    email = request.args.get('email')
    roll_no = request.args.get('roll_no')
    phone = request.args.get('phone')
    branch = request.args.get('branch')
    cgpa = request.args.get('cgpa')
    house = request.args.get('house')

    # Store the data in the database
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, email, roll_no, phone, branch, cgpa, house) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (name, email, roll_no, phone, branch, cgpa, house))
    conn.commit()
    conn.close()

    # Redirect to the generate_student_html() function
    return redirect(url_for('generate_student_html'))

@app.route('/add_faculty_submit', methods=['GET'])
def add_faculty_submit():
    initialize_db('faculty.db')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    major_research_area = request.args.get('major_research_area')
    office_hours = request.args.get('office_hours')
    office = request.args.get('office')

    # Store the data in the database
    conn = sqlite3.connect('faculty.db')
    c = conn.cursor()
    c.execute('INSERT INTO faculty (name, email, phone, major_research_area, office_hours, office) VALUES (?, ?, ?, ?, ?, ?)',
              (name, email, phone, major_research_area, office_hours, office))
    conn.commit()
    conn.close()

    # Redirect to the generate_faculty_html() function
    return redirect(url_for('generate_faculty_html'))

@app.route('/generate_student_html')
def generate_student_html():
    # Connect to the database
    conn = sqlite3.connect('students.db')

    # Retrieve the data
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    result = c.fetchall()

    # Generate HTML code
    html = "<html><head><title>Student Data</title>"
    html += '<link rel="stylesheet" href="' + url_for('static', filename='feat.css') + '">'
    html += "</head><body>"
    html += """<header>
            <a href=\"""" + url_for('index') + """\"><img height="98px" src=\"""" + url_for('static', filename='logo.jpeg') + """\"></a> 
            <h2>International Institute of Information Technology, Hyderabad</h2>
        </header>"""
    html += """<br>
        <button id="search_button" style="float: right; margin-right: 25px">Find A Student</button>
        <button id="add_button" style="float: right; margin-right: 25px">Add A Student</button>
        <button id="update_button" style="float: right; margin-right: 25px">Update Student Info</button>
        <br>
        <br>
        <br>\n"""
    html += """<h1>Students Information</h1>"""
    html += """<table class="tableee" align="center"><tr>
        <th>Name</th>
        <th>Email</th>
        <th>Roll No.</th>
        <th>Phone No.</th>
        <th>Branch</th>
        <th>CGPA</th>
        <th>House</th></tr>"""
    for row in result:
        html += "<tr>"
        for idx,col in enumerate(row):
            if idx==0:
                continue
            html += "<td>" + str(col) + "</td>"
        html += "</tr>"
    html += "</table>"
    html += """<script>
        var button = document.getElementById("add_button");
        button.addEventListener("click", function (event) {
            window.location.href = '/add_students.html';
        });

        var button1 = document.getElementById("search_button");
        button1.addEventListener("click", function (event) {
            window.location.href = '/search_stud.html';  // Update the href here
        });

        var button2 = document.getElementById("update_button");
        button2.addEventListener("click", function (event) {
            window.location.href = '/update_students.html';  // Update the href here
        });
            </script>"""
    html += """<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>"""
    html += """<footer>
            Copyright © 2023, International Institute of Information Technology, Hyderabad. All rights reserved.
            <br>
            Contact us at info@iiit.ac.in
        </footer>"""
    html += "</body></html>"

    path = 'templates/student.html'  # Replace with the path to your file
    if os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(html)

    # Close the database connection
    conn.close()

    # Render the student.html template
    return render_template('student.html')


@app.route('/generate_faculty_html')
def generate_faculty_html():
    # Connect to the database
    conn = sqlite3.connect('faculty.db')

    # Retrieve the data
    c = conn.cursor()
    c.execute("SELECT * FROM faculty")
    result = c.fetchall()

    # Generate HTML code
    html = "<html><head><title>Faculty Data</title>"
    html += '<link rel="stylesheet" href="' + url_for('static', filename='feat.css') + '">'
    html+="</head><body>"
    html += """<header>
            <a href=\"""" + url_for('index') + """\"><img height="98px" src=\"""" + url_for('static', filename='logo.jpeg') + """\"></a>
            <h2>International Institute of Information Technology, Hyderabad</h2>
        </header>"""
    html+="""<br>
        <button id="search_button" style="float: right; margin-right: 25px">Find A Faculty</button>
        <button id="add_button" style="float: right; margin-right: 25px">Add A Faculty</button>
        <button id="update_button" style="float: right; margin-right: 25px">Update Faculty Info</button><br><br><br>
        <br>
        <br>\n"""
    html+="""<h1>Faculty Information</h1>"""
    html += """<table class="tableee" align="center"><tr>
            <th>Sr no.</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone No.</th>
            <th>Major Research Area</th>
            <th>Office Hours</th>
            <th>Office</th></tr>"""
    for row in result:
        html += "<tr>"
        for col in row:
            html += "<td>" + str(col) + "</td>"
        html += "</tr>"
    html += "</table>"
    html += """<script>
    var button = document.querySelector("#add_button");
    button.addEventListener("click", function (event) {
        window.location.href = '/add_faculty.html';
    });

    var button1 = document.querySelector("#search_button");
    button1.addEventListener("click", function (event) {
        window.location.href = '/search_fac.html';
    });

    var button2 = document.querySelector("#update_button");
    button2.addEventListener("click", function (event) {
        window.location.href = '/update_faculty.html';
    });
        </script>"""
    html+="""<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>"""
    html+="""<footer>
            Copyright © 2023, International Institute of Information Technology, Hyderabad. All rights reserved.
            <br>
            Contact us at info@iiit.ac.in
        </footer>"""
    html+="</body></html>"

    # Save the generated HTML to the 'faculty.html' file
    path = 'templates/faculty.html'  # Replace with the path to your file
    if os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(html)

    # Close the database connection
    conn.close()

    # Render the faculty.html template
    return render_template('faculty.html')

@app.route('/update_students_submit', methods=['GET'])
def update_students_submit():
    initialize_db('students.db')
    id = request.args.get('id')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')

    # Store the data in the database
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('UPDATE students SET name = ?, email = ?, phone = ? WHERE id = ?',
                        (name, email, phone, id))
    conn.commit()
    conn.close()

    return redirect(url_for('generate_student_html'))
    # return render_template('student.html')

@app.route('/update_faculty_submit', methods=['GET'])
def update_faculty_submit():
    initialize_db('faculty.db')
    
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    major_research_area = request.args.get('major_research_area')
    office_hours = request.args.get('office_hours')
    office = request.args.get('office')

    # Store the data in the database
    conn = sqlite3.connect('faculty.db')
    c = conn.cursor()
    c.execute('UPDATE faculty SET name = ?, email = ?, phone = ?, major_research_area = ?, office_hours = ?, office = ? WHERE name = ?',
                        (name, email, phone, major_research_area,office_hours,office,name))
    conn.commit()
    conn.close()

    return redirect(url_for('generate_faculty_html'))

if __name__ == '__main__':
    app.run(debug=True)