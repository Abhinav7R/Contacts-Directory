import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('faculty.db')

# Retrieve the data
c = conn.cursor()
c.execute("SELECT * FROM faculty")
result = c.fetchall()

# Generate HTML code
html = "<html><head><title>Faculty Data</title>"
html += '<link rel="stylesheet" type="text/css" href="../static/feat.css">'
html+="</head><body>"
html+="""<header>
        <a href="index.html"><img height="98px" src="../static/logo.jpeg"></img></a>
        <h2>International Institute of Information Technology, Hyderabad</h2>
    </header>"""
html+="""<br>
    <button style="float: right; margin-right: 25px">Add A Faculty</button>
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
html+="""<script>
        var button = document.querySelector("button");
        button.addEventListener("click", function (event) {
          window.location.href = "add_faculty.html";
        });
    </script>"""
html+="""<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>"""
html+="""<footer>
        Copyright © 2023, International Institute of Information Technology, Hyderabad. All rights reserved.
        <br>
        Contact us at info@iiit.ac.in
    </footer>"""
html+="</body></html>"


path = 'templates/faculty.html'  # Replace with the path to your file
if os.path.isfile(path):
    with open(path, 'w') as f:
        f.write(html)

# Close the database connection
conn.close()
