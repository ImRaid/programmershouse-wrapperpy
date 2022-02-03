import requests
import json

def joke():
  url = "https://www.programmershouse-api.ga/joke"
  response = requests.get(url)
  data = response.text
  parse_json = json.loads(data)
  input = parse_json['ukraine']
  return input
