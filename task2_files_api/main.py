
import csv
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Keep generated files in this project's folder.
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API_KEY loaded successfully.")
else:
    print("API_KEY is missing. Check your .env file.")

CSV_FILE = BASE_DIR / "employees.csv"


# 1. Read employees.csv and write employees.json
with CSV_FILE.open("r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    employees = []

    for row in reader:
        employees.append({
            "id": int(row["id"]),
            "name": row["name"].strip(),
            "department": row["department"].strip(),
            "salary": int(row["salary"]),
            "city": row["city"].strip(),
        })

with (BASE_DIR / "employees.json").open("w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print(f"Rows read: {len(employees)}")


# 2. Write employees earning above 50000 to high_earners.csv
high_earners = [
    employee for employee in employees
    if employee["salary"] > 50000
]

with (BASE_DIR / "high_earners.csv").open(
    "w", newline="", encoding="utf-8"
) as file:
    fieldnames = ["id", "name", "department", "salary", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(high_earners)

print(f"High earners: {len(high_earners)}")


# 3. Call the users API with a 5-second timeout
API_URL = "https://jsonplaceholder.typicode.com/users"


def get_json(url):
    """Request JSON safely and handle common network errors."""
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print(f"{url.split('typicode.com')[-1]} -> 404 Not found")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print(f"Timeout while requesting {url}")
    except requests.exceptions.ConnectionError:
        print(f"Connection error while requesting {url}")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
    except ValueError:
        print("The API returned invalid JSON.")

    return None


users = get_json(API_URL)

if users is not None:
    # Print the first three users.
    for user in users[:3]:
        print(f'{user.get("id")} - {user.get("name")} - {user.get("email")}')

    # 4. Safely extract nested JSON fields using .get().
    selected_users = []

    for user in users[:3]:
        address = user.get("address", {})
        geo = address.get("geo", {})
        company = user.get("company", {})

        selected_users.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "latitude": geo.get("lat"),
            "longitude": geo.get("lng"),
            "company": company.get("name"),
            "company_catchphrase": company.get("catchPhrase"),
        })

    with (BASE_DIR / "users.json").open("w", encoding="utf-8") as file:
        json.dump(selected_users, file, indent=4)

    print("Saved selected user data to users.json")


# 5. Test the required 404 endpoint.
get_json(f"{API_URL}/9999")
