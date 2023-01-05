const intervalMiliSec = 10000;
const baseUrl = "http://127.0.0.1:5000/data";
const usersNode = document.querySelectorAll('.user-name');
const userNames = Array.from(usersNode, v => v.innerText);

setInterval(async () => {
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
}, intervalMiliSec);
