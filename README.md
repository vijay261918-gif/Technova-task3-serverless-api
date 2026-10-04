# TechNova Task 3: Serverless Function with REST API

## What This Project Does

This project implements a simple serverless REST API using **AWS Lambda** and **API Gateway**. The Lambda function handles two HTTP methods:

- **GET** - Returns a welcome message
- **POST** - Accepts JSON data and echoes it back

All responses follow the standard API Gateway proxy format with `statusCode`, `headers`, and `body`.

---

## What is AWS Lambda?

**AWS Lambda** is a serverless compute service that runs your code in response to events (like HTTP requests via API Gateway) without provisioning or managing servers. You upload your code as a "function" and Lambda executes it when triggered.

Key benefits:
- **No server management** - AWS handles infrastructure
- **Automatic scaling** - Runs as many instances as needed
- **Pay per use** - Only pay for compute time consumed
- **Event-driven** - Responds to HTTP requests, file uploads, database changes, etc.

---

## What is API Gateway?

**Amazon API Gateway** is a fully managed service for creating, publishing, and securing APIs. It acts as the "front door" for your Lambda functions, handling:

- **Request routing** - Directs HTTP requests to the right Lambda
- **Authentication/Authorization** - API keys, IAM, Cognito, Lambda authorizers
- **Request/Response transformation** - Modify payloads before/after Lambda
- **Throttling & Quotas** - Protect backend from overload
- **Caching** - Reduce latency and Lambda invocations
- **Custom Domains** - Use your own domain name

---

## How Lambda and API Gateway Work Together

```
Client (Browser/cURL/Postman)
        │
        ▼
┌───────────────────────┐
│   API Gateway         │  ◄── Receives HTTP request
│   (REST API)          │       Transforms to Lambda event
└─────────┬─────────────┘
          │ Invokes
          ▼
┌───────────────────────┐
│   AWS Lambda          │  ◄── Executes your Python code
│   (Python Function)   │       Returns response object
└─────────┬─────────────┘
          │ Returns
          ▼
┌───────────────────────┐
│   API Gateway         │  ◄── Transforms Lambda response
│                       │       to HTTP response
└─────────┬─────────────┘
          │
          ▼
Client receives JSON response
```

**API Gateway Proxy Integration Event Format (simplified):**
```json
{
  "httpMethod": "GET|POST|PUT|DELETE...",
  "path": "/",
  "headers": { "Content-Type": "application/json" },
  "queryStringParameters": { "key": "value" },
  "body": "{\"key\": \"value\"}"  // String, not parsed object!
}
```

**Lambda Response Format (required by API Gateway):**
```json
{
  "statusCode": 200,
  "headers": { "Content-Type": "application/json" },
  "body": "{\"message\": \"success\"}"  // Must be JSON string!
}
```

---

## Project Structure

```
task3-serverless-rest-api/
│
├── lambda_function.py    # Main Lambda handler (entry point)
├── test_lambda.py        # Local test script
├── requirements.txt      # Dependencies (none needed)
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

---

## How to Run Tests Locally

### Prerequisites
- Python 3.8+ installed

### Run Tests
```bash
# Navigate to project directory
cd task3-serverless-rest-api

# Run the test script
python test_lambda.py
```

### Expected Output
The script runs 6 tests and prints formatted results:
1. **GET Request** - Should return 200 with message
2. **POST Request (Valid JSON)** - Should return 200 with echoed data
3. **POST Request (Invalid JSON)** - Should return 400 with error
4. **POST Request (Empty Body)** - Should return 400 with error
5. **Unsupported Method (PUT)** - Should return 405 with error
6. **Unsupported Method (DELETE)** - Should return 405 with error

---

## Example Events and Expected Responses

### GET Request
**Event:**
```json
{
  "httpMethod": "GET",
  "path": "/",
  "headers": {},
  "queryStringParameters": null,
  "body": null
}
```

**Response:**
```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"message\": \"GET request received successfully\", \"method\": \"GET\"}"
}
```

---

### POST Request (Valid JSON)
**Event:**
```json
{
  "httpMethod": "POST",
  "path": "/",
  "headers": { "Content-Type": "application/json" },
  "queryStringParameters": null,
  "body": "{\"name\": \"Alice\", \"age\": 25, \"city\": \"New York\"}"
}
```

**Response:**
```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"message\": \"POST request received successfully\", \"method\": \"POST\", \"received_data\": {\"name\": \"Alice\", \"age\": 25, \"city\": \"New York\"}}"
}
```

---

### POST Request (Invalid JSON)
**Event:**
```json
{
  "httpMethod": "POST",
  "path": "/",
  "headers": { "Content-Type": "application/json" },
  "queryStringParameters": null,
  "body": "{ invalid json }"
}
```

**Response:**
```json
{
  "statusCode": 400,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"message\": \"Invalid JSON in request body\", \"method\": \"POST\", \"error\": \"The request body must be valid JSON\"}"
}
```

---

### Unsupported Method (e.g., PUT)
**Event:**
```json
{
  "httpMethod": "PUT",
  "path": "/",
  "headers": {},
  "queryStringParameters": null,
  "body": null
}
```

**Response:**
```json
{
  "statusCode": 405,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"message\": \"Unsupported HTTP method: PUT\", \"method\": \"PUT\", \"error\": \"This endpoint only supports GET and POST methods\"}"
}
```

---

## AWS Deployment Steps (Future/Manual)

> **Note:** This project is designed for local development only. The following steps are for reference when you're ready to deploy.

### 1. Create Lambda Function
```bash
# Package the function
zip function.zip lambda_function.py

# Create Lambda (replace with your values)
aws lambda create-function \
  --function-name techNova-task3-api \
  --runtime python3.11 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

### 2. Create API Gateway REST API
```bash
# Create API
aws apigateway create-rest-api --name techNova-task3-api

# Get the API ID from output, then create resource and method
# (Easier to do via AWS Console for beginners)
```

### 3. Configure Integration
- In API Gateway Console: Create `/` resource
- Add GET and POST methods
- Set integration type: **Lambda Function**
- Select your Lambda function
- Enable **Lambda Proxy Integration**

### 4. Deploy API
- Create a **Stage** (e.g., `prod`, `dev`)
- Note the **Invoke URL** - this is your public endpoint

### 5. Test with cURL
```bash
# GET
curl https://YOUR_API_ID.execute-api.REGION.amazonaws.com/prod/

# POST
curl -X POST https://YOUR_API_ID.execute-api.REGION.amazonaws.com/prod/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "value": 123}'
```

---

## Security Notes

⚠️ **Never commit AWS credentials to this repository!**

- No AWS keys, secrets, or ARNs should be in any project file
- Use IAM roles for Lambda execution permissions
- Store any configuration in AWS Systems Manager Parameter Store or Secrets Manager

---

## License

This project is part of the TechNova Internship program.