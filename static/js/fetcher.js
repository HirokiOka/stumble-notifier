const intervalMiliSec = 5000;
const URL = "http://127.0.0.1:8000/data";
const ids = ["test", "2041201h", "2070877H", "2110645H", "2120823h", "2141064h"];
ids.sort();


setInterval(async () => {
  const result = await fetch(URL).then(res => res.json());
  console.log(result);
  ids.forEach((v, i) => {
    const codeEle = document.getElementById(`${v}-code`);
    const multiEle = document.getElementById(`${v}-multi`);
    codeEle.style.background = result[i][0] ? 'red' : 'white';
    multiEle.style.background = result[i][1] ? 'red' : 'white';
  });
}, intervalMiliSec);
