# DataValidationTool

A Python-based tool to scan CSV data for errors, missing values, and logic issues across case records.

## 🔍 What It Does
- Scans CSV files for common data issues like missing fields, duplicates, and formatting problems  
- Flags records with invalid or inconsistent values (e.g. status without income, date format issues)  
- Outputs a summary of all errors and saves a clean error report  
- Helps teams catch data issues early in eligibility, audit, or quality review processes  

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
Built for teams who need to validate incoming data for Medicaid, SNAP, TANF, QA reviews, or audit prep. Especially useful for public program workflows that rely on accurate case records.

---

Made with 💡 by #EliteTheOctoDog 🐙🐶 [LinkedIn →](https://linkedin.com/in/JoeNetherland)

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
