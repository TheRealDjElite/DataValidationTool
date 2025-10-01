# Data Validation Tool

⚠️ Applied learning prototype. Built with Python as a learning project. Not for production use.

A Python-based tool that checks CSV files for missing values, formatting errors, and logic issues in case records. Helps teams catch data problems before audits or eligibility reviews.

## 🔍 What It Does
- Scan CSV files for common data issues (missing fields, duplicates, formatting errors)  
- Flag inconsistent or invalid values (e.g., status without income, bad date formats)  
- Output a clean error report (`error_report.csv`) and a summary of issues  
- Support QA, audit prep, and data quality checks for public program workflows

## 🧰 Tools Used
- Python 3  
- `pandas`  
- `csv`  

## 📁 File Overview
- `data_validation_tool.py` — Script that loads the CSV file, checks for issues, and outputs a report  
- `sample_data.csv` — Demo input file with intentional errors  
- `error_report.csv` — Auto-generated report listing flagged records (if any)

## 🧪 How to Use It
1. Download or clone the repository  
2. Make sure `pandas` is installed:
   ```bash
   pip install pandas
3. Run the script with your CSV file:
4. Review the terminal output or open `error_report.csv` to see the flagged issues

## ✅ Use Case
Designed as a demo for data validation in eligibility and compliance. Shows how Python can be applied to automate checks and catch errors early in case data workflows.

---

Made with 💡 by **Joseph Netherland (TheRealDjElite)**  
[LinkedIn →](https://linkedin.com/in/JoeNetherland)

<details>
<summary>📘 Instructions for Non-Technical Users (Click to Expand)</summary>

### 💡 How to Use This Tool (No Tech Skills Needed)

This tool checks your case data for issues like missing fields, duplicates, and logic problems — and shows you where to fix them. You don’t need to be technical to run it.

---

### ✅ What You’ll Need:
1. A Windows or Mac computer (not a Chromebook)  
2. Python installed (download it at: https://www.python.org/downloads)  
3. Your data saved as a `.csv` file (can be exported from Excel or Google Sheets)

---

### 🧭 Step-by-Step Instructions

#### 1. Download the Tool
- Go to:  
  [https://github.com/TheRealDjElite/DataValidationTool](https://github.com/TheRealDjElite/DataValidationTool)
- Click the green **Code** button → **Download ZIP**
- Unzip the folder

#### 2. Open the Folder
- Find the file: `data_validation_tool.py`

#### 3. Run the Tool
- On **Windows**:
  - Inside the folder, click the **address bar**, type `cmd`, and press **Enter**
  - In the black window that opens, type:
    ```
    python data_validation_tool.py
    ```

- On **Mac**:
  - Open the **Terminal**
  - Drag the folder into the Terminal after typing:
    ```
    cd 
    ```
    Then press **Enter**
  - Run the script:
    ```
    python3 data_validation_tool.py
    ```

#### 4. See Your Results
- The script will flag any problems in the file  
- It will create an `error_report.csv` file showing what needs to be fixed  
- You can open that file in Excel or Google Sheets

---

### 👩‍💼 Example Use
You’re checking Medicaid eligibility cases submitted by field staff. You drop your `.csv` into this tool and it tells you which records are missing dates, case IDs, or have logic errors like “Approved” with no income. You fix what’s needed and re-upload — no manual scanning required.

</details>
