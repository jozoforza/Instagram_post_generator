import requests
import os
from decouple import config
import json

def fetchFact():
    limit = 1
    key = config("NINJA_API_KEY")
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': key})
    if response.status_code == requests.codes.ok:
        fact =json.loads(response.text)
        return fact[0]["fact"]
    else:
        print("Error:", response.status_code, response.text)