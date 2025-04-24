from lambda_function import my_lambda_handler
import unittest
from unittest.mock import patch, Mock
from lambda_function import my_lambda_handler


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
