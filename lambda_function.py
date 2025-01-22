import json
import requests

def lambda_handler(event, context):
  url = event["url"]
  response = requests.get(url)
  return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda!'),
      'event': event,
      'url': url,
      'response': response.status_code
  }