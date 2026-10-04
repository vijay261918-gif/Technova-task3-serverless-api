"""
Local test script for the Lambda function.
Run with: python test_lambda.py
"""

import json
from lambda_function import lambda_handler


def print_test_result(test_name, response):
    """Print test result in a readable format."""
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print(f"{'='*60}")
    print(f"Status Code: {response['statusCode']}")
    print(f"Headers: {json.dumps(response['headers'], indent=2)}")
    print(f"Body: {response['body']}")
    print(f"{'='*60}")


def test_get():
    """Test GET request."""
    event = {
        "httpMethod": "GET",
        "path": "/",
        "headers": {},
        "queryStringParameters": None,
        "body": None
    }
    response = lambda_handler(event, None)
    print_test_result("GET Request", response)
    return response


def test_post_valid():
    """Test POST request with valid JSON."""
    event = {
        "httpMethod": "POST",
        "path": "/",
        "headers": {"Content-Type": "application/json"},
        "queryStringParameters": None,
        "body": json.dumps({
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        })
    }
    response = lambda_handler(event, None)
    print_test_result("POST Request (Valid JSON)", response)
    return response


def test_post_invalid_json():
    """Test POST request with invalid JSON."""
    event = {
        "httpMethod": "POST",
        "path": "/",
        "headers": {"Content-Type": "application/json"},
        "queryStringParameters": None,
        "body": "{ invalid json: missing quotes }"
    }
    response = lambda_handler(event, None)
    print_test_result("POST Request (Invalid JSON)", response)
    return response


def test_post_empty_body():
    """Test POST request with empty body."""
    event = {
        "httpMethod": "POST",
        "path": "/",
        "headers": {"Content-Type": "application/json"},
        "queryStringParameters": None,
        "body": ""
    }
    response = lambda_handler(event, None)
    print_test_result("POST Request (Empty Body)", response)
    return response


def test_unsupported_method():
    """Test unsupported HTTP method (PUT)."""
    event = {
        "httpMethod": "PUT",
        "path": "/",
        "headers": {},
        "queryStringParameters": None,
        "body": None
    }
    response = lambda_handler(event, None)
    print_test_result("Unsupported Method (PUT)", response)
    return response


def test_delete_method():
    """Test unsupported HTTP method (DELETE)."""
    event = {
        "httpMethod": "DELETE",
        "path": "/",
        "headers": {},
        "queryStringParameters": None,
        "body": None
    }
    response = lambda_handler(event, None)
    print_test_result("Unsupported Method (DELETE)", response)
    return response


if __name__ == "__main__":
    print("Running Lambda Function Tests Locally")
    print("=" * 60)
    
    # Run all tests
    test_get()
    test_post_valid()
    test_post_invalid_json()
    test_post_empty_body()
    test_unsupported_method()
    test_delete_method()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)