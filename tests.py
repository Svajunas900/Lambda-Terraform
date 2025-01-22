from lambda_function import my_lambda_handler

def test_function():
  assert my_lambda_handler({"url": "https://github.com/Svajunas900/Lambda-Terraform"},None) == {"response": 200}