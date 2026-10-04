# OpenCode Prompt — TechNova Task 3: Serverless Function with REST API

You are helping me build **TechNova Internship Task 3: Serverless Function with REST API**.

## Project

- Platform: AWS Lambda + API Gateway
- Programming language: Python

## IMPORTANT

- Do **NOT** use or request AWS credentials.
- Do **NOT** deploy anything to AWS.
- Do **NOT** create or modify AWS resources.
- Only generate the local project files and code.
- Keep the implementation beginner-friendly and easy to understand.
- Do not over-engineer the project.

## Task Requirements

1. Create a Python AWS Lambda handler.
2. The handler must read the incoming event.
3. Check `event["httpMethod"]`.
4. Handle GET and POST separately.
5. GET should return a JSON response containing:
   - `message`
   - `method`
6. POST should read the request body as JSON and return:
   - `message`
   - `method`
   - `received data`
7. Return proper HTTP-style response objects containing:
   - `statusCode`
   - `headers`
   - `body`
8. Use Python's `json` module.
9. The code must be compatible with AWS Lambda.
10. Handle invalid JSON in POST gracefully.
11. Handle unsupported HTTP methods with an appropriate response.
12. Add clear comments explaining the important parts.

## Files to Create

```text
task3-serverless-rest-api/
│
├── lambda_function.py
├── test_lambda.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `lambda_function.py`

- Main Lambda handler should be:
  ```python
  lambda_handler(event, context)
  ```
- Implement GET and POST.
- Keep dependencies at zero if possible.
- Return JSON through the `body` field.

### `test_lambda.py`

Test the Lambda handler locally.

Include at least:

1. GET test event
2. POST test event
3. Invalid JSON POST test
4. Unsupported HTTP method test

Print readable results.

### `requirements.txt`

- If no external packages are required, leave it empty or add a comment explaining that AWS Lambda's Python runtime and standard library are sufficient.

### `README.md`

Explain:

- What this project does
- What AWS Lambda is
- What API Gateway is
- How Lambda and API Gateway work together
- Project structure
- How to run `test_lambda.py` locally
- Example GET event
- Example POST event
- Expected responses
- AWS deployment steps as a future/manual step
- Do not include any real AWS credentials or secrets.

### `.gitignore`

Include standard Python exclusions such as:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
```

## Important Boundary

For this stage, **only generate the local project files and code**.

Do not:

- Deploy to AWS
- Create Lambda functions
- Create API Gateway resources
- Configure IAM
- Ask for AWS access keys
- Store AWS credentials in the project
