# API Testing Framework

![Tests](https://github.com/TakvorN/api-testing-framework/actions/workflows/tests.yml/badge.svg)

A Python-based API testing framework using `pytest` and `requests`.

The project demonstrates automated testing of REST API endpoints, including positive and negative test cases for common CRUD operations, schema validation, authentication flows, and CI-based test execution.

## Tech Stack

* Python
* pytest
* requests
* jsonschema
* GitHub Actions

## Features

* Reusable API client built on `requests.Session`
* Centralized configuration for API base URLs and request timeout
* Pytest fixtures for shared setup
* Fixture-based support for multiple API targets
* Parametrized GET tests
* Positive and negative API test cases
* CRUD-oriented request coverage using GET, POST, PUT, PATCH, and DELETE
* JSON schema validation for API response contracts
* Authentication token fixture for authenticated API tests
* Custom header support for authenticated requests
* Positive and negative authentication coverage for protected endpoints
* GitHub Actions CI for automated test execution

## Project Structure

```text
api-testing-framework/
├── api/
│   ├── __init__.py
│   └── client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── schemas/
│   ├── __init__.py
│   ├── booker_schema.py
│   └── jsonplaceholder_post_schema.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_booker_auth.py
│   ├── test_booker_booking.py
│   └── test_jsonplaceholder_posts.py
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

## API Targets

This project uses two public REST API targets.

### JSONPlaceholder

[JSONPlaceholder](https://jsonplaceholder.typicode.com/) is used as the initial public REST API target for CRUD-oriented request testing.

It is a fake online REST API useful for testing and prototyping. Read operations use predefined sample data, while write operations such as POST, PUT, PATCH, and DELETE are simulated and not persisted.

### Restful Booker

[Restful Booker](https://restful-booker.herokuapp.com/) is used as a second API target for authentication flow testing.

The project tests booking creation, authenticated booking updates, authenticated deletion, and negative authentication scenarios for protected endpoints.

