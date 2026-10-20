
# Task 2 — Files, APIs and Environment

## Objective
Read and write CSV and JSON files, load environment variables,
and make HTTP requests with safe error handling.

## Files
- `main.py` — CSV processing and API integration.
- `employees.csv` — input employee dataset.
- `employees.json` — all employee records in JSON format.
- `high_earners.csv` — employees with salary above 50000.
- `users.json` — selected user details extracted from nested API JSON.
- `requirements.txt` — Python dependencies.
- `.env.example` — environment variable template.

## Setup
Create and activate a virtual environment, then run:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Create a local `.env` file containing `API_KEY=demo-key-123`.
Never commit `.env` or the `.venv` directory.

## Concepts demonstrated
- CSV reading and writing
- JSON serialization and nested field extraction
- Environment variables with python-dotenv
- HTTP requests, status codes and timeout handling
- Connection errors and missing resources
