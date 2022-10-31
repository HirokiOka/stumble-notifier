const intervalMiliSec = 1000;
const URL = "https://stumble-notifier.herokuapp.com/data";
const ids = ["2011234H", "2061231H", "2140643H", "2150505H"];
ids.sort();


setInterval(async () => {
  try {
    const result = await fetch(URL).then(res => res.json());
    console.log(result);
    ids.forEach((v, i) => {
      const codeEle = document.getElementById(`${v}-code`);
      const multiEle = document.getElementById(`${v}-multi`);
      codeEle.style.background = result[i][0] ? 'red' : 'white';
      multiEle.style.background = result[i][1] ? 'red' : 'white';
    });
  } catch(e) {
    console.log(e);
  }
}, intervalMiliSec);
