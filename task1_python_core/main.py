
import csv


# 1. Function using default arguments, *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


# 2. Custom exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


# 4. Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, Salary: {self.salary}, "
            f"Team size: {self.team_size}"
        )


# 5. Read employee data from CSV
# Read employee data from CSV
with open("employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    # Remove extra spaces from column names
    reader.fieldnames = [
        name.strip() for name in reader.fieldnames
    ]

    employees = [
        {
            "id": int(row["id"]),
            "name": row["name"].strip(),
            "department": row["department"].strip(),
            "salary": int(row["salary"]),
            "city": row["city"].strip(),
        }
        for row in reader
    ]

# 6. List comprehension: employees earning above 50000
above_50000 = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]
print("Above 50000:", above_50000)


# 7. map() and lambda: add a 10% raise
raised_salaries = list(
    map(lambda employee: round(employee["salary"] * 1.10, 2), employees)
)
print("Salaries after 10 % raise:", raised_salaries)


# 8. filter(): employees working in Chennai
chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)
print("Chennai:", [employee["name"] for employee in chennai_employees])


# 9. Demonstrate the bonus function
print("Bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 500, 1000))
print("Bonus with cap:", bonus(50000, 0.1, 5000, cap=6000))


# 10. Demonstrate Employee and Manager
employee = Employee("Arun", 30000)
manager = Manager("Priya", 60000, 5)

print(employee.get_details())
print("Annual salary:", employee.annual_salary())
print(manager.get_details())


# 11. Catch the custom exception and always finish the transaction
try:
    invalid_employee = Employee("Test", -500)
except InvalidSalaryError as error:
    print(f"Error: {error}")
finally:
    print("Transaction finished")


# 12. Loop: continue skips zero; break stops above 85000
print("Loop demonstration:")

for employee in employees:
    salary = employee["salary"]

    if salary == 0:
        continue

    if salary > 85000:
        print("Stopping at:", employee["name"], salary)
        break

    print(employee["name"], salary)
