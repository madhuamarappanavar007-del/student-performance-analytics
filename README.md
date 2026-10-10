# Student Performance Analytics System

A beginner-friendly Python mini project for the EWB Courses Python with AI assignment.
It loads student records from CSV, validates the dataset, calculates results using
NumPy and Pandas, prints an analysis, and exports reusable reports.
No machine learning, web framework, API key, or internet access is needed to run it
after dependencies have been installed.

## Academic-use note

This is an AI-assisted reference implementation with fictional sample data.
The assignment requires individual work and understanding. Read the code, change
the dataset or implementation as appropriate, and follow your trainer's AI-use
policy. Do not claim AI-generated work as unaided work.

## Requirements

- Python 3.10 or newer
- NumPy and Pandas (see `requirements.txt`)
- A terminal, optionally VS Code

## Quick start — Windows

Extract the ZIP, open the project folder in VS Code, and open a terminal there.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

These commands do not require PowerShell activation or execution-policy changes.
If your system uses `python` rather than `py`, use `python -m venv .venv`.

## Quick start — macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
.venv/bin/python -m unittest discover -s tests -v
```

## Project files

```text
student-performance-analytics/
├── main.py                    # Command-line entry point and clear output
├── functions.py               # Reusable calculations and validation
├── students.csv               # 20 fictional student records
├── requirements.txt           # Dependencies
├── README.md                  # Setup, rules and submission instructions
├── Project_Documentation.md   # Project explanation and outcome
├── sample_output.txt          # Captured successful sample run
├── TEST_RESULTS.txt           # Test run and dependency versions
├── tests/
│   └── test_functions.py      # Automated tests
└── output/
    ├── student_results.csv
    ├── subject_analysis.csv
    ├── top_students.csv
    └── summary.json
```

## Dataset

One row represents one student. The 20 records are synthetic, not actual student
performance data. Required fields:

| Field | Meaning |
| --- | --- |
| Student_ID | Unique nonblank student identifier |
| Name | Student name |
| Department | Department label |
| Python, Mathematics, Statistics, Computer_Science, English | Five equally weighted marks, each 0–100 |
| Attendance | Attendance percentage, 0–100 |

The dataset contains high, medium, low, passing and failing results, including
an exact pass boundary and students with low attendance.

## Calculation rules

These are project-defined rules, not grading rules mandated by the PDF.

- **Total:** sum of five subject marks; maximum 500.
- **Average:** total / 5; displayed to two decimal places.
- **Pass:** every subject mark is at least 40.
- **Fail:** any subject mark is below 40, even if the overall average is high.
- **Grade:** any failed subject gives F. Otherwise use this table:

| Unrounded average | Grade |
| --- | --- |
| 90–100 | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| 40 to below 50 | E |

Attendance below 75% is a warning only. Attendance is never added to total marks
and does not affect academic pass/fail.

Class average is the mean of all students' average marks, including failures.
Subject average includes every student. Subject pass rate uses a mark threshold
of 40. Top performers are ranked among all students by unrounded average, with
status shown; all ties at the last included position are retained.

## Features and concepts

- Pandas CSV loading, DataFrame preview, filtering and report exports
- Validation of columns, empty data, duplicate IDs, missing/nonnumeric values,
  nonfinite numbers and values outside 0–100
- NumPy sum, mean, min, max, all, where and count_nonzero
- Reusable functions, loops, conditionals and meaningful variable names
- Per-student totals, averages, grades, status and attendance warnings
- Class highest, lowest, average and pass/fail statistics
- Subject-wise highest, lowest, average and pass percentages
- Top students with tie handling and JSON/CSV exports
- Automated tests, including exact boundaries and invalid input

## Custom input and output

```bash
python main.py --input students.csv --output output --top 5
```

Use the virtual-environment Python executable from the setup instructions if
you have not activated the environment. Default input/output paths are relative
to the script; explicitly supplied relative paths are relative to your terminal's
current directory. Re-running overwrites reports in the selected output folder.
The source CSV is never overwritten.

## Troubleshooting

- **ModuleNotFoundError:** install requirements using the same Python executable
  used to run the program.
- **Missing required columns:** keep the CSV headers exactly as shown.
- **Numeric/range error:** correct the indicated column; use numbers from 0 to 100
  without percent signs.
- **File not found:** check the `--input` path.
- **Permission denied when saving:** close the output CSV in Excel or use another
  `--output` folder.

## GitHub and final submission

1. Review and adapt this reference project; confirm your trainer's rules.
2. Run the program and tests on your own computer.
3. Replace the student-details and repository placeholders in the documentation.
4. Add screenshots of your own terminal output if desired.
5. Create `student-performance-analytics` on GitHub.
6. Upload the code, input CSV, requirements, README and documentation.
   Keep `.venv` and `__pycache__` out of the repository.
7. Verify repository visibility follows the trainer's instructions.
8. Submit its repository URL using the EWB-provided Google Form.
9. Confirm documentation is pushed and check the final repository.

**Deadline: 15 October 2026, on or before.**
The assignment PDF does not provide the Google Form URL. This package does not
create a GitHub repository or submit the form.