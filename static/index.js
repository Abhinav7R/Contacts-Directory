document.addEventListener("DOMContentLoaded", function() {
    var student = document.querySelector(".Student");
    student.addEventListener("click", function(event) {
      window.location.href = "{{ url_for('student') }}";
        });
  
    var faculty = document.querySelector(".Faculty");
    faculty.addEventListener("click", function(event) {
      window.location.href = "{{ url_for('faculty') }}";
    });
  });  

const images = document.querySelectorAll('.slideshow-image');
let currentIndex = 0;

setInterval(() => {
  images[currentIndex].classList.remove('active');
  currentIndex = (currentIndex + 1) % images.length;
  images[currentIndex].classList.add('active');
}, 3000);