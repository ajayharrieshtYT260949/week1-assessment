#!/usr/bin/env python
# coding: utf-8

# # Week 1: Employee Data Analysis
# 
# ## 1. Load the Dataset
# ## 2. Inspect the Data
# ## 3. Clean the Data
# ## 4. Department Analysis
# ## 5. Performance Benchmark
# ## 6. Findings

# 1.Load data
# 

# In[1]:


from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ROOT = Path.cwd()
    if ROOT.name == "notebooks":
        ROOT = ROOT.parent
    elif not (ROOT / "data" / "employees.csv").exists():
        ROOT = ROOT / "task4_git_terminal_notebook"

csv_path = ROOT / "data" / "employees.csv"

print("Task 4 folder:", ROOT)
print("CSV exists:", csv_path.exists())

employees = pd.read_csv(csv_path)
employees.head()


# Load Data

# In[2]:


from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path.cwd()
if ROOT.name == "notebooks":
    ROOT = ROOT.parent

employees = pd.read_csv(ROOT / "data" / "employees.csv")
employees.head()


# Inspect

# In[3]:


employees.info()
employees.describe()


# Clean

# In[4]:


employees = employees.drop_duplicates().copy()
employees["salary"] = pd.to_numeric(
    employees["salary"], errors="coerce"
)
employees["salary"] = employees["salary"].fillna(
    employees["salary"].median()
)
employees["id"] = employees["id"].astype(int)
employees["salary"] = employees["salary"].astype(int)


# Department analysis

# In[5]:


department_summary = employees.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)
display(department_summary)


# In[7]:


from pathlib import Path

reports_dir = ROOT / "reports"
reports_dir.mkdir(parents=True, exist_ok=True)

department_summary.to_csv(
    reports_dir / "department_summary.csv"
)

print("Report saved successfully!")


# Benchmark with %timeit

# In[6]:


import timeit

benchmark = timeit.timeit(
    lambda: employees.groupby("department")["salary"].mean(),
    number=100
)

print(f"Average time per run: {benchmark / 100:.6f} seconds")


# ## Findings
# 
# 1. The dataset contains employees from multiple departments.
# 2. Duplicate records are removed before analysis.
# 3. Missing salaries are filled using the median salary.
# 4. Grouping reveals differences in department headcount and salary.
# 5. Pandas simplifies data cleaning and aggregation, while %timeit measures execution time.
