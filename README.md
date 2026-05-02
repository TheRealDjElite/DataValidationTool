# 🕵️‍♂️ Data Validation Tool

Python-based toolkit for structured data validation and automated error detection across CSV datasets. Designed to support QA workflows that require consistent field-level checks and early identification of data integrity issues.

Applies rule-based logic to identify missing, invalid, or inconsistent values and produces a structured error report for review.

## 🔍 What It Does

- Scans CSV datasets for missing fields, duplicates, and formatting issues  
- Flags invalid or inconsistent values such as malformed dates or missing dependencies  
- Generates `error_report.csv` with identified data quality issues  
- Supports structured QA and audit preparation workflows  

## 🧰 Tools Used

- Python 3 (AI-assisted development)  
- pandas  
- csv  

## 📁 File Overview

- `data_validation_tool.py` - Loads input data, applies validation rules, outputs results  
- `sample_data.csv` - Test dataset with intentional errors  
- `error_report.csv` - Generated output of flagged records  

## ▶ How to Use It

1. Install dependencies: `pip install pandas`  
2. Run `data_validation_tool.py`  
3. Provide or reference input CSV file  
4. Review output report for flagged issues  

## 📌 Purpose

Built for structured environments where automated validation is required to identify data quality issues before QA review or downstream processing. Focuses on improving consistency, reducing manual review effort, and enforcing basic data integrity rules.