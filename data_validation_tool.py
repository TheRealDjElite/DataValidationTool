import pandas as pd
from datetime import datetime

INPUT_FILE = "sample_data.csv"
OUTPUT_FILE = "error_report.csv"

REQUIRED_FIELDS = ["Case ID", "Status", "Submission Date", "Income"]
VALID_STATUSES = ["approved", "pending", "denied"]

def is_blank(value):
    return pd.isna(value) or str(value).strip() == ""

def is_valid_date(date_str):
    try:
        datetime.strptime(str(date_str).strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False

def to_number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def validate_row(row):
    errors = []

    # Check for missing required fields
    for field in REQUIRED_FIELDS:
        if is_blank(row[field]):
            errors.append(f"Missing {field}")

    # Invalid status value (only checked when status is present)
    status = "" if is_blank(row["Status"]) else str(row["Status"]).strip()
    if status and status.lower() not in VALID_STATUSES:
        errors.append(f"Invalid Status: {status}")

    # Invalid date (only checked when date is present)
    if not is_blank(row["Submission Date"]) and not is_valid_date(row["Submission Date"]):
        errors.append("Invalid Submission Date (expected a real date in YYYY-MM-DD format)")

    # Income must be a number (only checked when income is present)
    income = None
    income_invalid = False
    if not is_blank(row["Income"]):
        income = to_number(row["Income"])
        if income is None:
            income_invalid = True
            errors.append(f"Invalid Income: {row['Income']}")

    # Approved without income (skipped when income is already flagged as invalid)
    if status.lower() == "approved" and not income_invalid and (income is None or income <= 0):
        errors.append("Approved case with no/zero income")

    return errors

def main():
    try:
        # Read everything as text so IDs stay as written (1001, not 1001.0)
        df = pd.read_csv(INPUT_FILE, dtype=str)
    except Exception as e:
        print(f"Error reading {INPUT_FILE}: {e}")
        return

    if df.empty:
        print("The input file is empty.")
        return

    missing_columns = [field for field in REQUIRED_FIELDS if field not in df.columns]
    if missing_columns:
        print(f"Input file is missing required columns: {', '.join(missing_columns)}")
        return

    # Track duplicate case IDs (blank IDs are reported as missing, not duplicate)
    ids = df["Case ID"].str.strip()
    duplicate_ids = set(ids[ids.duplicated(keep=False) & ids.notna() & (ids != "")])

    error_log = []
    for idx, row in df.iterrows():
        row_num = idx + 2  # account for header row
        row_errors = validate_row(row)

        case_id = "" if is_blank(row["Case ID"]) else str(row["Case ID"]).strip()
        if case_id in duplicate_ids:
            row_errors.append("Duplicate Case ID")

        if row_errors:
            error_log.append({
                "Row": row_num,
                "Case ID": case_id,
                "Errors": "; ".join(row_errors)
            })

    if error_log:
        error_df = pd.DataFrame(error_log)
        error_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Validation complete. Rows with errors: {len(error_df)}")
        print(f"See '{OUTPUT_FILE}' for full report.")
        print(error_df.to_string(index=False))
    else:
        print("Validation complete. No errors found.")

if __name__ == "__main__":
    main()
