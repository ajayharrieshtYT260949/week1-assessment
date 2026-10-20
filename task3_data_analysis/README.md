# Task 3: NumPy, Pandas and Matplotlib

## Overview
This project demonstrates numerical computing, employee data analysis, data cleaning, department aggregation, data merging, and data visualization using Python.

## Libraries
- NumPy
- Pandas
- Matplotlib

## Tasks completed
- Created a 4 × 3 NumPy marks array.
- Calculated student and subject averages.
- Applied grace marks using broadcasting and calculated weighted scores using `np.dot()`.
- Inspected employee data using `info()`, `describe()`, `loc`, `iloc`, and filtering.
- Cleaned missing salaries using median imputation and removed duplicate records.
- Corrected data types and saved the cleaned dataset.
- Calculated department headcount, average salary, and maximum salary using `groupby().agg()`.
- Performed inner, left, and outer joins with `departments.csv`.
- Identified the department without employees.
- Created four charts: bar, histogram, scatter, and line.

## How to run

1. Activate the project's virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `python main.py`.

## Output files
- `employees_cleaned.csv`
- `department_summary.csv`
- `outer_join.csv`
- `charts/bar_chart.png`
- `charts/histogram.png`
- `charts/scatter_plot.png`
- `charts/line_chart.png`

## Key concepts
NumPy arrays, broadcasting, `np.dot()`, DataFrames, missing-value handling, duplicate removal, grouping, merging, and Matplotlib visualization.