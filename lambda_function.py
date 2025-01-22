import json

def lambda_handler(event, context):
  url = event["url"]
  return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda!'),
      'event': event,
      'url': url
  }