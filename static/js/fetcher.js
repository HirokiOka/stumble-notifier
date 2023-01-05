const intervalMiliSec = 10000;
const URL = "http://127.0.0.1:5000";
const users = document.querySelector('.user-name');

setInterval(async () => {
  try {
    const result = await fetch(URL).then(res => res.json());
    console.log(result);
    /*
    users.forEach((v, i) => {
      const codeEle = document.getElementById(`${v}-code`);
      const multiEle = document.getElementById(`${v}-multi`);
      codeEle.style.background = result[i][0] ? 'red' : 'white';
      multiEle.style.background = result[i][1] ? 'red' : 'white';
    });
    */
  } catch(e) {
    console.log(e);
  }
}, intervalMiliSec);
