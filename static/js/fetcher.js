const intervalMiliSec = 1000;
//const endpoint = "http://127.0.0.1:5000/data";
const endpoint = "https://stumble-notifier.adaptable.app/data";
const usersNode = document.querySelectorAll('.user-name');
const userNames = Array.from(usersNode, v => v.innerText);
const urls = userNames.map(v => endpoint + '/' + v);
const pTimeEle = document.getElementById('p-time');

async function postData(data) {
  const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      data
    })
  };
  const res = await fetch(endpoint, options);
  const resJson = await res.json();
  return resJson;
}

let result = postData(userNames);

setInterval(async () => {
  result = await postData(userNames);
}, 10000)

let idx = 0;
let lastTime = 0;
setInterval(async () => {
  pTimeEle.innerText = result[0]['data'][idx][0];
  result.forEach((r, i) => {
    const name = r['name'];
    const multiResult = r['data'][idx][1];
    const codeResult = r['data'][idx][2];
    const multiEle = document.getElementById(`${name}-multi`);
    const codeEle = document.getElementById(`${name}-code`);
    multiEle.style.background = multiResult ? 'red' : 'white';
    codeEle.style.background = codeResult ? 'red' : 'white';
  });
  idx = ++idx % result.length;
}, intervalMiliSec);
