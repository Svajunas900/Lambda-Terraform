data "aws_iam_policy_document" "assume_role"{
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }  

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_lambda_layer_version" "requests_layer" {
  
  layer_name          = "requests-layer"
  compatible_runtimes = ["python3.13"]
  
  filename = "python.zip"
}


data "aws_iam_role" "lambda_user" {
  name = "lambda-user"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function.zip"
  function_name = "my_lambda_handler"
  role          = data.aws_iam_role.lambda_user.arn
  handler       = "lambda_function.my_lambda_handler"

  source_code_hash = filebase64sha256("lambda_function.zip")

  runtime = "python3.13"

  layers = [
    aws_lambda_layer_version.requests_layer.arn
  ]
}


