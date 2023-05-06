document.addEventListener("DOMContentLoaded", function() {
    var student = document.querySelector(".Student");
    student.addEventListener("click", function(event) {
      window.location.href = "student.html";
    });
  
    var staff = document.querySelector(".Staff");
    staff.addEventListener("click", function(event) {
      window.location.href = "staff.html";
    });
  
    var faculty = document.querySelector(".Faculty");
    faculty.addEventListener("click", function(event) {
      window.location.href = "faculty.html";
    });
  });  