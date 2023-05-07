ISS-Hackathon-team-25
Welcome to IIIT Contact Directory

This is a web application developed for storing, searching, and updating data in a systematic and efficient way.

To run this application, run "app.py" and open the link generated in the terminal in any browser. This will take you to the home page "index.html," which displays a few photos of our institute followed by some write-up about the institute and our website. What follows next are 2 buttons:

Student Database: This button takes you to the student information page.
Faculty Database: This button takes you to the faculty information page.

The student information page displays details of students, i.e, rollno, phoneno, cgpa, house, branch. This information is available for everyone to view. This page has 3 options:

Update student information: Upon clicking this button, it will ask for a key (unique to every student, much like a password). For our website, we have given this as the id in the database. It can be manipulated by a hash function to generate stronger keys or we can have a password field in the database that will be randomly generated. Only when the key is valid, the information of the student (name, phone, and email) can be updated. This, ofcourse, is to prevent misuse of the site to modify data.

Add student: Adding students to the database will only be permitted to the admin office who will have a key (we have the key here as "appaji_key"). On clicking the add student button, a prompt will be displayed which will ask for a key and only when it is correct, it will redirect to the add student page where you can add all the information of a particular student.

Find a student: This button allows you to search the database based on all the parameters, namely name, email, phone, house, branch, and cgpa. You would have to select from a dropdown the field you want to search based on whatever you need to look for. It displays all the information with respect to the search field, e.g., search by cgpa, and the table displayed would contain all the details of the people with that required cgpa.


The faculty information page displays the details of faculty, such as name, email, phoneno, major research area, office hours, and office. This page also has three buttons that can be clicked on and is very similar to the student:

Update faculty information: When this button is clicked, a prompt asks for a key that all of the faculty have (which we have here as aftab_key). This page has options of email, phone, major research area, office hours, and office that can be changed.

Add a faculty: When this button is clicked, a prompt asks for a key that we assume only the admin has. The details that can be filled are name, email, phoneno, major research area, office hours, and office.

Find a faculty: This button allows the user to filter based on the fields of name, email, phoneno, major research area, office hours, and office.

The key, cannot be found by trying to inspect the webpage. Again, this is to prevent misuse of the site.
