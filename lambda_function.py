import json


def lambda_handler(event, context):
    """
    AWS Lambda handler for REST API with GET and POST support.
    
    Args:
        event: API Gateway proxy event containing httpMethod, body, etc.
        context: Lambda context object (not used in this implementation)
    
    Returns:
        dict: HTTP response with statusCode, headers, and body
    """
    # Extract HTTP method from the event
    http_method = event.get("httpMethod", "").upper()
    
    # Common headers for all responses
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    
    # Handle GET request
    if http_method == "GET":
        response_body = {
            "message": "GET request received successfully",
            "method": "GET"
        }
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(response_body)
        }
    
    # Handle POST request
    elif http_method == "POST":
        try:
            # Parse the request body as JSON
            # API Gateway passes body as a string, so we need to parse it
            body = event.get("body", "{}")
            if isinstance(body, str):
                received_data = json.loads(body)
            else:
                received_data = body
            
            response_body = {
                "message": "POST request received successfully",
                "method": "POST",
                "received_data": received_data
            }
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps(response_body)
            }
        except json.JSONDecodeError:
            # Handle invalid JSON gracefully
            error_body = {
                "message": "Invalid JSON in request body",
                "method": "POST",
                "error": "The request body must be valid JSON"
            }
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps(error_body)
            }
    
    # Handle unsupported HTTP methods
    else:
        error_body = {
            "message": f"Unsupported HTTP method: {http_method}",
            "method": http_method,
            "error": "This endpoint only supports GET and POST methods"
        }
        return {
            "statusCode": 405,
            "headers": headers,
            "body": json.dumps(error_body)
        }