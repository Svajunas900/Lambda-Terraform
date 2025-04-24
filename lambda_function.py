import json
import requests


def my_lambda_handler(event, context):

    url = event["url"]
    response = requests.get(url)

    return {
        'response': response.status_code,
        'response text': response.text
    }
