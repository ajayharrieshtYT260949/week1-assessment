# Task 4: Git, Terminal and Jupyter Notebook

## Overview
This task demonstrates Git branching and collaboration, terminal file operations, and employee data analysis using Jupyter Notebook.

## Setup
1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Open `notebooks/week1_analysis.ipynb` in VS Code or Jupyter.
4. Run all notebook cells.
5. Export the notebook with `python -m jupyter nbconvert --to script notebooks/week1_analysis.ipynb`.

## Folder Structure
- `data/` — employee dataset
- `notebooks/` — Jupyter notebook and exported Python script
- `reports/` — copied data and reports
- `src/` — source and terminal-operation example files

## Five-line Summary of Findings
1. The employee dataset contains records from multiple departments.
2. Duplicate rows are removed before the analysis.
3. Missing salaries are imputed using the median.
4. Grouped results summarize department headcount and salary statistics.
5. Jupyter Notebook provides a reproducible workflow and `%timeit` benchmarks a calculation.

## Git Workflow
Work is completed on `feature/analysis`, reviewed through a Pull Request, and merged into `main` after resolving a README conflict.