## Description
This project is to simulate real world project workflow <br/>
Development is in dev branch and everything that is working, tested is in branch prod

This project uses IaaC, terraform to create infrastructure + Github workflows CI/CD for testing and deployment.
All attention here is not the actual code but the whole infrastructure around it to make the deployment and testing autonomous

What it does? It creates lambda function in aws after testing and planning with terraform

## HOW TO SECTION:

Installing Application <br/>

Step 1. Navigate to directory where you want to clone application <br/>
   
Step 2. Clone repository using url https://github.com/Svajunas900/Lambda-Terraform.git <br/>
````
git clone https://github.com/Svajunas900/Lambda-Terraform.git
````

If you want to create and push to aws your lambda function create terraform Api, get aws credentials and configure them then just push any changes to your repository and everything will work

# Test coverage example 

```
from lambda_function import my_lambda_handler
import unittest
from unittest.mock import patch, Mock


class TestMyLambdaHandler(unittest.TestCase):

    @patch('lambda_function.requests.get')
    def test_my_lambda_handler_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "Success!"
        mock_get.return_value = mock_response

        event = {"url": "https://example.com"}
        context = {}

        result = my_lambda_handler(event, context)

        self.assertEqual(result['response'], 200)
        self.assertEqual(result['response text'], "Success!")
        mock_get.assert_called_once_with("https://example.com")


if __name__ == '__main__':
    unittest.main()

```
