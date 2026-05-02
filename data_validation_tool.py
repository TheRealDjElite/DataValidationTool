
import pandas as pd
import re

INPUT_FILE = "sample_data.csv"
OUTPUT_FILE = "error_report.csv"

def is_valid_date(date_str):
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", str(date_str).strip()))

def validate_row(row, row_num):
    errors = []
    
    # Check for missing required fields
    required_fields = ["Case ID", "Status", "Submission Date", "Income"]
    for field in required_fields:
        if pd.isna(row[field]) or str(row[field]).strip() == "":
            errors.append(f"Missing {field}")
    
    # Approved without income
    if str(row.get("Status")).strip().lower() == "approved":
        income = row.get("Income", 0)
        if pd.isna(income) or float(income) <= 0:
            errors.append("Approved case with no/zero income")
    
    # Invalid date format
    if not is_valid_date(row.get("Submission Date", "")):
        errors.append("Invalid Submission Date format (expected YYYY-MM-DD)")
    
    # Invalid status value
    valid_statuses = ["approved", "pending", "denied"]
    status = str(row.get("Status", "")).strip().lower()
    if status not in valid_statuses:
        errors.append(f"Invalid Status: {row['Status']}")
    
    return errors

def main():
    try:
        df = pd.read_csv(INPUT_FILE)
    except Exception as e:
        print(f"Error reading {INPUT_FILE}: {e}")
        return

    if df.empty:
        print("The input file is empty.")
        return

    # Track duplicate case IDs
    duplicates = df[df.duplicated("Case ID", keep=False)]
    error_log = []

    for idx, row in df.iterrows():
        row_num = idx + 2  # account for header
        row_errors = validate_row(row, row_num)
        
        if row["Case ID"] in duplicates["Case ID"].values:
            row_errors.append("Duplicate Case ID")
        
        if row_errors:
            error_log.append({
                "Row": row_num,
                "Case ID": row.get("Case ID", ""),
                "Errors": "; ".join(row_errors)
            })

    if error_log:
        error_df = pd.DataFrame(error_log)
        error_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Validation complete. Errors found: {len(error_df)}")
        print(f"See '{OUTPUT_FILE}' for full report.")
        print(error_df)
    else:
        print("Validation complete. No errors found.")

if __name__ == "__main__":
    main()
