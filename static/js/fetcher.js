const URL = 'http://127.0.0.1:8000/data';
const intervalMiliSec = 1000;

const API_URL = "https://data.mongodb-api.com/app/data-bxlxk/endpoint/data/v1/action/findOne"
const API_KEY = "v0w45xdmq3Wx31SJ9KA07DofnOvne5XNkC4ORGjthyIJXiMRXQrFywuVGhBEhxyx"
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'api-key': API_KEY
    },
    body: JSON.stringify({
        'collection': 'features_and_predictions',
        'database': 'test',
        'dataSource': 'Cluster0',
        'filter': {
            "std_id": 'test'
        }
      })
    };


/*
setInterval(async () => {
  fetch(API_URL, options)
    .then(res => res.json())
    .then(result => console.log(result));
  
}, intervalMiliSec);
*/
