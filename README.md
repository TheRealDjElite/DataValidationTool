# Data Validation Tool

Skill-building project demonstrating AI-assisted Python for structured data quality validation and automated error detection across high-volume tabular datasets.

Performs rule-based validation on CSV records, identifies data quality issues, and generates an error report for structured review workflows.

## 🔍 What It Does

- Scan CSV datasets for missing fields, duplicates, and formatting issues
- Flag invalid or inconsistent values (e.g., missing dependencies, malformed dates)
- Generate `error_report.csv` with detected data quality issues
- Support structured QA and audit preparation workflows

## 🧰 Tools Used

- Python 3 (AI-assisted)
- pandas
- csv

## 📁 File Overview

- `data_validation_tool.py` — Loads CSV input, applies validation rules, outputs issue report
- `sample_data.csv` — Test dataset with intentional data errors
- `error_report.csv` — Generated output report of flagged records

## 🧪 How to Use It

1. Install dependencies: `pip install pandas`
2. Run `data_validation_tool.py`
3. Provide or reference input CSV dataset
4. Review terminal output and `error_report.csv`

## ✅ Use Case

Designed for structured data environments requiring automated validation of high-volume records to detect missing, inconsistent, or invalid values prior to QA review or downstream processing.

---

Made with 💡 by **Joseph Netherland (TheRealDjElite)**  
[LinkedIn →](https://linkedin.com/in/JoeNetherland)
