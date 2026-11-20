# ✅ UAT Test Plan and Results

User acceptance test plan for the Data Validation Tool. Each test case ties to a business rule, lists the input and expected result, and records the actual result from a test run.

Testing was done by the tool's author against the business rules below, written in UAT format. Sign-off by business users was out of scope for this portfolio project.

## 🎯 Scope

**In scope:** every field-level rule in `data_validation_tool.py`, input file checks, and the error report output.

**Out of scope:** performance on large files, file types other than CSV, and changes to the source data.

## 📏 Business Rules

| Rule | Description |
|---|---|
| BR-01 | Case ID, Status, Submission Date, and Income are required. Blank or spaces-only values fail. |
| BR-02 | Case ID is unique. Leading and trailing spaces are ignored when comparing IDs. |
| BR-03 | Status is Approved, Pending, or Denied. Capitalization does not matter. |
| BR-04 | Submission Date is a real calendar date in YYYY-MM-DD format. |
| BR-05 | Income is a number. |
| BR-06 | An Approved case needs income above zero. |
| BR-07 | The input file has all four required columns and at least one data row. |

## 🗂️ Test Data

| File | Purpose |
|---|---|
| `sample_data.csv` | 10 records: 1 clean record and 9 with planned errors |
| `test_data/uat_edge_cases.csv` | Edge cases not covered by the sample data |
| `test_data/uat_missing_column.csv` | File without the Submission Date column |
| `test_data/uat_header_only.csv` | File with a header row and no data |
| `test_data/uat_malformed_row.csv` | Row with an extra comma in the Income value |

To run a test file, set `INPUT_FILE` in the script to the file path. Row numbers match spreadsheet rows (row 1 is the header).

## 🧪 Test Cases

### Sample data (`sample_data.csv`)

| ID | Rule | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-01 | BR-02 | Row 2: Case 1001, also on row 7 | Duplicate Case ID | Duplicate Case ID | ✅ Pass |
| TC-02 | BR-06 | Row 3: Approved, income 0 | Approved case with no/zero income | Approved case with no/zero income | ✅ Pass |
| TC-03 | BR-04 | Row 4: date 20250403 | Invalid Submission Date | Invalid Submission Date | ✅ Pass |
| TC-04 | BR-01 | Row 5: blank Status | Missing Status | Missing Status | ✅ Pass |
| TC-05 | BR-01 | Row 6: Denied, blank income | Missing Income only. No approval rule error | Missing Income | ✅ Pass |
| TC-06 | BR-02 | Row 7: Case 1001, second entry | Duplicate Case ID | Duplicate Case ID | ✅ Pass |
| TC-07 | BR-01, BR-03 | Row 8: blank Case ID, status "Unknown" | Both errors on one row | Missing Case ID; Invalid Status: Unknown | ✅ Pass |
| TC-08 | BR-04 | Row 9: date 2025-02-30 | Invalid Submission Date | Invalid Submission Date | ✅ Pass |
| TC-09 | BR-05, BR-06 | Row 10: Approved, income "abc" | Invalid Income only. No second income error | Invalid Income: abc | ✅ Pass |
| TC-10 | All | Row 11: Case 1008, all fields valid | Not flagged | Not flagged | ✅ Pass |

### Edge cases (`test_data/uat_edge_cases.csv`)

| ID | Rule | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-11 | BR-03 | Row 2: status "approved" (lowercase) | Not flagged | Not flagged | ✅ Pass |
| TC-12 | BR-01 | Row 3: Status is spaces only | Missing Status | Missing Status | ✅ Pass |
| TC-13 | BR-06 | Row 4: Approved, income -50 | Flagged | Approved case with no/zero income | ✅ Pass (see OQ-02) |
| TC-14 | BR-06 | Row 5: Pending, income 0 | Not flagged. Rule applies to Approved cases only | Not flagged | ✅ Pass |
| TC-15 | BR-04 | Row 6: date 04/05/2025 | Invalid Submission Date | Invalid Submission Date | ✅ Pass |
| TC-16 | BR-05 | Row 7: income "1,200" (quoted) | Pending business decision | Invalid Income: 1,200 | ⚠️ Open (OQ-01) |
| TC-17 | BR-05 | Row 8: income "$900" | Pending business decision | Invalid Income: $900 | ⚠️ Open (OQ-01) |
| TC-18 | BR-02 | Rows 9 and 10: " 2008" and "2008" | Both flagged as duplicates | Duplicate Case ID on both rows | ✅ Pass |

### File checks

| ID | Rule | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-19 | BR-07 | `uat_missing_column.csv` | Run stops and names the missing column | Input file is missing required columns: Submission Date | ✅ Pass |
| TC-20 | BR-07 | `uat_header_only.csv` | Run stops with a clear message | The input file is empty. | ✅ Pass |
| TC-21 | BR-05 | `uat_malformed_row.csv`: unquoted 1,200 on row 3 | Bad row flagged. Other rows still validated | Run stops with a file parsing error. No report written | ❌ Fail (DEF-01) |

## 📊 Results Summary

| Total | Pass | Open | Fail |
|---|---|---|---|
| 21 | 18 | 2 | 1 |

## 🐞 Defect Log

| ID | Test | Description | Severity | Status |
|---|---|---|---|---|
| DEF-01 | TC-21 | One row with an extra comma stops the whole run. The reviewer gets a technical parsing error and no error report, so none of the valid rows get checked. | Medium | Open |

## ❓ Open Questions

| ID | Question | Impact |
|---|---|---|
| OQ-01 | Should formatted income values such as "$900" or "1,200" pass as valid? | Today these get flagged, which adds review work if the source system exports formatted currency. |
| OQ-02 | Should negative income get its own check? | Negative income on an Approved case gets flagged under the "no/zero income" message. Negative income on Pending or Denied cases passes with no flag. |

## 🏁 Exit Criteria

- Every business rule has at least one passing test case
- Open questions answered by the business owner
- DEF-01 fixed and TC-21 retested, or accepted as a known limit
