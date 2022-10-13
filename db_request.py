import os
from dotenv import load_dotenv
from requests import request
import json


load_dotenv()
api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")


def fetch_codeparams_from_id(std_id):
    payload = json.dumps({
        "collection": "codeparams",
        "database": "test",
        "dataSource": "Cluster0",
        "filter": {
            "id": std_id
        }
    })
    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': api_key
    }
    action = 'action/find'
    url = api_url + action
    response = request("POST", url, headers=headers, data=payload)
    res_json = json.loads(response.text)
    return res_json['documents']


def fetch_codeparams_from_time(saved_at):
    payload = json.dumps({
        "collection": "codeparams",
        "database": "test",
        "dataSource": "Cluster0",
        "filter": {
            "savedAt": saved_at
        }
    })
    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': api_key
    }
    action = 'action/findOne'
    url = api_url + action
    response = request("POST", url, headers=headers, data=payload)
    res_json = json.loads(response.text)
    return res_json['document']


def fetch_unique_ids():
    payload = json.dumps({
        "collection": "codeparams",
        "database": "test",
        "dataSource": "Cluster0"
    })
    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': api_key
    }
    action = 'action/find'
    url = api_url + action
    response = request("POST", url, headers=headers, data=payload)
    res_json = json.loads(response.text)
    result = []
    for v in res_json["documents"]:
        if ('id' in v):
            result.append(v['id'])
    return list(set(result))
