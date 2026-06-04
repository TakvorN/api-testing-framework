# API Testing Framework

A Python-based API testing framework using `pytest` and `requests`.

The project demonstrates automated testing of REST API endpoints, including positive and negative test cases for common CRUD operations.

## Tech Stack

- Python
- pytest
- requests

## Features

- Reusable API client built on `requests.Session`
- Centralized configuration for base URL and timeout
- Pytest fixtures for shared setup
- Parametrized GET tests
- Positive and negative API test cases
- CRUD-oriented request coverage using GET, POST, PUT, PATCH, and DELETE
- GitHub Actions CI for automated test execution

## Project Structure

```text
api-testing-framework/
├── api/
│   ├── __init__.py
│   └── client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_posts.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Current API Target

This project currently uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/) as the initial public REST API target.

JSONPlaceholder is a fake online REST API useful for testing and prototyping. Read operations use predefined sample data, while write operations such as POST, PUT, PATCH, and DELETE are simulated and not persisted.

## Next Steps

- Add schema validation
- Add authentication flow tests using a second API
- Improve reporting and documentation
