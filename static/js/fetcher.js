const intervalMiliSec = 5000;
const endpoint = "http://127.0.0.1:5000/data";
const usersNode = document.querySelectorAll('.user-name');
const userNames = Array.from(usersNode, v => v.innerText);
const urls = userNames.map(v => endpoint + '/' + v);

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

setInterval(async () => {
  const result = await postData(userNames);
  result.forEach((r, i) => {
    const name = r['name'];
    const multiResult = r['multi'];
    const codeResult = r['code'];
    const codeEle = document.getElementById(`${name}-code`);
    const multiEle = document.getElementById(`${name}-multi`);
    codeEle.style.background = codeResult ? 'red' : 'white';
    multiEle.style.background = multiResult ? 'red' : 'white';
  });
}, intervalMiliSec);
