# 🕵️‍♂️ Data Validation Tool

Python-based tool for structured data validation and automated error detection in CSV datasets. Designed to support QA workflows that require consistent field-level checks and early identification of data integrity issues.

Applies rule-based logic to identify missing, invalid, or inconsistent values and produces a structured error report for review.

## 🔍 What It Does

- Checks required fields (Case ID, Status, Submission Date, Income) for missing values
- Flags duplicate Case IDs
- Flags invalid date formats (expected YYYY-MM-DD) and invalid status values
- Flags rule conflicts, such as an approved case with no or zero income
- Generates `error_report.csv` listing each flagged row and its errors

## 🧰 Tools Used

- Python 3 (AI-assisted development)
- pandas
- re (regular expressions)

## 📁 File Overview

- `data_validation_tool.py` - Loads input data, applies validation rules, outputs results
- `sample_data.csv` - Test dataset with intentional errors
- `error_report.csv` - Generated output of flagged records (created when the script runs)

## ▶ How to Use It

1. Install dependencies: `pip install pandas`
2. Place your data in `sample_data.csv`, or change `INPUT_FILE` in the script to point to your file
3. Run `data_validation_tool.py`
4. Review `error_report.csv` for flagged issues

## 📌 Purpose

Built for structured environments where automated validation is needed to identify data quality issues before QA review or downstream processing. Focuses on improving consistency, reducing manual review effort, and enforcing basic data integrity rules.
