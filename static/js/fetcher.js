const URL = 'http://127.0.0.1:8000/data';
const intervalMiliSec = 1000;

setInterval(() => {
  fetch(URL)
    .then(res => res.json())
    .then(result => console.log(result));
}, intervalMiliSec);

