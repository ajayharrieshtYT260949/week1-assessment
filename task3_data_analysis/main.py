
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Set up project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
EMPLOYEE_FILE = BASE_DIR / "employees.csv"
DEPARTMENT_FILE = BASE_DIR / "departments.csv"
CHART_DIR = BASE_DIR / "charts"

CHART_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("TASK 3: NUMPY, PANDAS AND MATPLOTLIB")
print("=" * 60)


# --------------------------------------------------
# 2. NumPy: student marks and weighted scores
# --------------------------------------------------

print("\n1. NUMPY OPERATIONS")

marks = np.array([
    [78, 85, 90],
    [88, 76, 92],
    [69, 80, 75],
    [95, 91, 89]
])

print("\nMarks array:\n", marks)
print("Array shape:", marks.shape)

student_averages = marks.mean(axis=1)
subject_averages = marks.mean(axis=0)

print("Student averages:", student_averages)
print("Subject averages:", subject_averages)

# Broadcasting: add 5 marks to every subject score
grace_marks = marks + 5

print("\nMarks after adding 5 grace marks:\n", grace_marks)

# Weighted score: Subject 1 = 50%, Subject 2 = 30%, Subject 3 = 20%
weights = np.array([0.50, 0.30, 0.20])
weighted_scores = np.dot(grace_marks, weights)

print("Subject weights:", weights)
print("Weighted scores after grace marks:", weighted_scores)


# --------------------------------------------------
# 3. Pandas: load and inspect employee data
# --------------------------------------------------

print("\n\n2. PANDAS: DATA INSPECTION")

employees = pd.read_csv(EMPLOYEE_FILE)
departments = pd.read_csv(DEPARTMENT_FILE)

print("\nFirst five employee records:")
print(employees.head())

print("\nDataFrame information:")
employees.info()

print("\nDescriptive statistics:")
print(employees.describe())

print("\nUsing loc: employees in Chennai")
print(employees.loc[employees["city"] == "Chennai"])

print("\nUsing iloc: first three rows")
print(employees.iloc[:3])

print("\nFiltering: employees with salary above 50000")
print(employees.loc[employees["salary"] > 50000])


# --------------------------------------------------
# 4. Clean missing salaries, duplicates and data types
# --------------------------------------------------

print("\n\n3. DATA CLEANING")

print("Rows before cleaning:", len(employees))
print("Missing salaries before cleaning:", employees["salary"].isna().sum())
print("Duplicate rows before cleaning:", employees.duplicated().sum())

# Remove exact duplicate rows
employees = employees.drop_duplicates().copy()

# Convert salary to numeric; invalid values become missing
employees["salary"] = pd.to_numeric(
    employees["salary"], errors="coerce"
)

# Fill missing salaries with the median of available salaries
salary_median = employees["salary"].median()
employees["salary"] = employees["salary"].fillna(salary_median)

# Correct data types
employees["id"] = employees["id"].astype(int)
employees["salary"] = employees["salary"].round().astype(int)

employees["name"] = employees["name"].astype(str).str.strip()
employees["department"] = employees["department"].astype(str).str.strip()
employees["city"] = employees["city"].astype(str).str.strip()

print("Median salary used:", salary_median)
print("Rows after cleaning:", len(employees))
print("Missing salaries after cleaning:", employees["salary"].isna().sum())
print("Duplicate rows after cleaning:", employees.duplicated().sum())

print("\nCleaned employee data:")
print(employees.to_string(index=False))

cleaned_file = BASE_DIR / "employees_cleaned.csv"
employees.to_csv(cleaned_file, index=False)
print("\nSaved cleaned data to:", cleaned_file.name)


# --------------------------------------------------
# 5. Group employees by department
# --------------------------------------------------

print("\n\n4. DEPARTMENT SUMMARY")

department_summary = (
    employees.groupby("department")
    .agg(
        headcount=("id", "count"),
        average_salary=("salary", "mean"),
        maximum_salary=("salary", "max")
    )
    .reset_index()
)

department_summary["average_salary"] = (
    department_summary["average_salary"].round(2)
)

print(department_summary.to_string(index=False))

summary_file = BASE_DIR / "department_summary.csv"
department_summary.to_csv(summary_file, index=False)


# --------------------------------------------------
# 6. Merge employees with departments
# --------------------------------------------------

print("\n\n5. DATA MERGING")

inner_join = pd.merge(
    departments, employees, on="department", how="inner"
)

left_join = pd.merge(
    departments, employees, on="department", how="left"
)

outer_join = pd.merge(
    departments, employees, on="department", how="outer"
)

print("\nINNER JOIN: departments that have employees")
print(inner_join.to_string(index=False))

print("\nLEFT JOIN: all departments, including those without employees")
print(left_join.to_string(index=False))

print("\nOUTER JOIN: all departments and all employee records")
print(outer_join.to_string(index=False))

# Find departments with no matching employees
departments_without_employees = outer_join.loc[
    outer_join["name"].isna(), "department"
].unique()

print("\nDepartments with no employees:")
if len(departments_without_employees) > 0:
    for department in departments_without_employees:
        print("-", department)
else:
    print("None")

# Show headcount for every department, including zero
all_department_counts = (
    employees.groupby("department")
    .size()
    .reindex(departments["department"], fill_value=0)
)

print("\nHeadcount by department:")
for department, count in all_department_counts.items():
    print(f"{department}: {count}")

outer_file = BASE_DIR / "outer_join.csv"
outer_join.to_csv(outer_file, index=False)


# --------------------------------------------------
# 7. Matplotlib: create four charts
# --------------------------------------------------

print("\n\n6. CREATING CHARTS")

# Chart 1: Bar chart - average salary by department
average_by_department = employees.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
average_by_department.plot(kind="bar", label="Average salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "bar_chart.png", dpi=150)
plt.close()

print(
    "Bar chart insight: "
    f"{average_by_department.idxmax()} has the highest average salary."
)


# Chart 2: Histogram - salary distribution
plt.figure(figsize=(8, 5))
plt.hist(
    employees["salary"],
    bins=5,
    edgecolor="black",
    label="Employee salaries"
)
plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "histogram.png", dpi=150)
plt.close()

print(
    "Histogram insight: "
    "The bars show how employee salaries are distributed across salary ranges."
)


# Chart 3: Scatter plot - employee ID versus salary
plt.figure(figsize=(8, 5))
plt.scatter(
    employees["id"],
    employees["salary"],
    label="Employees"
)
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "scatter_plot.png", dpi=150)
plt.close()

print(
    "Scatter insight: "
    "The plot compares each employee's salary with their employee ID."
)


# Chart 4: Line chart - salary by employee ID
sorted_employees = employees.sort_values("id")

plt.figure(figsize=(8, 5))
plt.plot(
    sorted_employees["id"],
    sorted_employees["salary"],
    marker="o",
    label="Employee salary"
)
plt.title("Employee Salary by ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "line_chart.png", dpi=150)
plt.close()

print(
    "Line chart insight: "
    "The line shows how salary values vary across employee IDs."
)

print("\nCharts saved in the charts folder:")
for chart in sorted(CHART_DIR.glob("*.png")):
    print("-", chart.name)

print("\nTASK 3 COMPLETED SUCCESSFULLY!")
