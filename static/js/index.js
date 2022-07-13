const s1 = document.getElementById("s1");
const s2 = document.getElementById("s2");
const s3 = document.getElementById("s3");
const s4 = document.getElementById("s4");
const s5 = document.getElementById("s5");
const s6 = document.getElementById("s6");

let students = [s1, s2, s3, s4, s5, s6];
setInterval(() => {
  const randIdx = Math.floor(Math.random() * students.length - 1);
  const pickedStudnet = students[randIdx]
  pickedStudnet.style.background = 'red';
  if (Math.random() < 1/2) {
    const whiteIdx = Math.floor(Math.random() * students.length - 1);
    const whiteStudent = students[whiteIdx]
    whiteStudent.style.background = 'white';
  }
}, 3000);
