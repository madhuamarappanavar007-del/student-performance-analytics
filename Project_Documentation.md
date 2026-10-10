# Project Documentation

## 1. Project Title and Student Details

**Project:** Student Performance Analytics System

**Student Name:** Madhu Amarappanavar

**Student ID:** 2jr23cs042

**Course:** Python with AI — EWB Courses

**Submission Deadline:** 15 October 2026

**AI Assistance Disclosure:** This project was prepared with AI assistance.
I ran the program and tests on my computer. AI assistance should be disclosed
according to the trainer’s policy, and the implementation should be reviewed
and adapted to meet the assignment’s individual-work requirements.

## 2. Objective

The objective of this project is to analyze student performance using Python,
NumPy, and Pandas.

The system reads student records from a CSV file and calculates total marks,
average marks, grades, and pass/fail status. It also provides class-level
statistics, subject-wise analysis, and a list of top-performing students.

The project demonstrates how programming can reduce repetitive manual
calculations and present academic data in an understandable format.

## 3. Technologies Used

- **Python:** Functions, loops, conditions, command-line arguments, and file handling.
- **NumPy:** Numerical calculations such as totals, averages, minimums, and maximums.
- **Pandas:** CSV loading, DataFrame processing, filtering, and report export.
- **unittest:** Automated testing of calculations, validation, and grading rules.
- **GitHub:** Repository hosting and project submission once the files are uploaded.

## 4. Dataset Description

The input file, `students.csv`, contains 20 fictional student records and
nine columns.

Each row represents one student.

| Column | Description |
| --- | --- |
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Student department |
| Python | Python marks out of 100 |
| Mathematics | Mathematics marks out of 100 |
| Statistics | Statistics marks out of 100 |
| Computer_Science | Computer Science marks out of 100 |
| English | English marks out of 100 |
| Attendance | Attendance percentage |

All five subjects are equally weighted. The maximum total is 500 marks.

Attendance is recorded separately and is not included in the total or average
marks.

The dataset includes high, medium, and low marks, passing and failing students,
and students with low attendance. These are synthetic demonstration records,
not actual student academic records.

## 5. Implementation

### Step 1: Load and Inspect the Dataset

The `load_students()` function uses `pd.read_csv()` to load the CSV file into
a Pandas DataFrame.

Student IDs are read as strings.

The main program displays:

- Number of records
- Number of columns
- Column names
- Number of missing cells
- A preview of the first five records

### Step 2: Validate the Dataset

The `validate_students()` function checks that:

- All required columns are present.
- The dataset is not empty.
- Student IDs, names, and departments are not missing or blank.
- Student IDs are unique.
- Marks and attendance are numeric and finite.
- Marks and attendance are between 0 and 100.

A loop applies numerical validation to each subject and the attendance column.

Invalid data produces an understandable error message instead of silently
removing records or replacing missing marks.

### Step 3: Calculate Student Results

The `process_students()` function creates a copy of the DataFrame and converts
the subject marks into a NumPy array.

The main calculations are:

- `np.sum(marks, axis=1)` for total marks
- `np.mean(marks, axis=1)` for average marks
- `np.all(marks >= 40, axis=1)` for academic pass/fail checks
- `np.where()` for status and attendance flags

The original input CSV is not modified.

### Step 4: Assign Grades

The `assign_grade()` function uses conditional statements to assign grades.

These are project-defined rules.

| Condition | Grade |
| --- | --- |
| Any subject mark below 40 | F |
| All subjects passed and average at least 90 | A+ |
| All subjects passed and average from 80 to below 90 | A |
| All subjects passed and average from 70 to below 80 | B |
| All subjects passed and average from 60 to below 70 | C |
| All subjects passed and average from 50 to below 60 | D |
| All subjects passed and average from 40 to below 50 | E |

A student must score at least 40 in every subject to pass.

A high overall average does not override a failed subject. For example, a
student with an average of 76 still fails if one subject mark is below 40.

Grades are calculated using unrounded averages. Results are displayed to
two decimal places.

### Step 5: Check Attendance

Attendance below 75% produces a warning.

Attendance does not change the academic grade or pass/fail status.

An attendance value of exactly 75% does not produce a warning.

### Step 6: Analyze Class and Subject Performance

The `subject_analysis()` function loops through the five subjects and calculates:

- Highest marks
- Lowest marks
- Average marks
- Number of students who passed
- Number of students who failed
- Subject pass percentage

The `build_summary()` function calculates:

- Overall class average
- Highest and lowest student averages
- Students with the highest and lowest averages
- Total pass and fail counts
- Overall pass percentage
- Best-performing subject by average
- Grade distribution
- Number of attendance warnings

Class and subject averages include all students, including those who failed.

### Step 7: Identify Top Performers

The `top_students()` function uses Pandas `nlargest()` to select students with
the highest averages.

By default, the program selects the top five students. Students tied at the
last included position are also retained.

Ranking includes all students, and their grade and pass/fail status are shown.

### Step 8: Display and Save Reports

The main program prints labeled tables and summaries.

The `save_reports()` function generates:

- `student_results.csv`
- `subject_analysis.csv`
- `top_students.csv`
- `summary.json`

These files are saved in the `output` folder by default.

CSV and JSON exports retain numerical precision. Running the program again
updates the reports in the selected output folder.

## 6. Key Features

- CSV dataset loading using Pandas
- Data validation
- Student total and average calculations
- Clearly defined grade and pass/fail rules
- Class highest, lowest, and average performance
- Pass/fail counts and pass percentage
- Subject-wise performance analysis
- Top-performing student identification
- Tie handling
- Attendance warnings
- CSV and JSON report generation
- Automated tests

## 7. Execution and Output

The program was run successfully on my Windows computer using:

    python main.py

The automated tests were run using:

    python -m unittest discover -s tests -v

The test output reported:

    Ran 13 tests
    OK

The program displayed the dataset preview, student results, class summary,
grade distribution, subject-wise analysis, and top performers.

Reports were saved in the `output` folder.

The included `sample_output.txt` contains a captured sample run. Screenshots
of my own local execution can also be added to the repository if desired.

Screenshots are optional according to the assignment guidelines.

## 8. Final Outcome

The system successfully processed the 20 fictional student records and
generated the required performance summaries.

### Class Results

| Metric | Result |
| --- | --- |
| Student records | 20 |
| Missing cells | 0 |
| Overall class average | 70.99 out of 100 |
| Passed students | 16 |
| Failed students | 4 |
| Overall pass percentage | 80.00% |
| Highest student average | 96.00 |
| Lowest student average | 36.00 |
| Attendance warnings | 4 |

The highest-average student was Tara Bose, with an average of 96.00.

The lowest-average student was Dev Shah, with an average of 36.00.

### Subject-Wise Results

| Subject | Average Marks | Passed | Failed | Pass Percentage |
| --- | --- | --- | --- | --- |
| Python | 70.00 | 18 | 2 | 90.00% |
| Mathematics | 67.85 | 17 | 3 | 85.00% |
| Statistics | 70.95 | 19 | 1 | 95.00% |
| Computer Science | 74.15 | 20 | 0 | 100.00% |
| English | 72.00 | 20 | 0 | 100.00% |

Computer Science had the highest subject average, at 74.15.

### Top Five Students

| Student ID | Name | Average | Grade |
| --- | --- | --- | --- |
| S016 | Tara Bose | 96.00 | A+ |
| S001 | Aarav Sharma | 92.20 | A+ |
| S004 | Ananya Rao | 92.20 | A+ |
| S010 | Saanvi Kulkarni | 90.00 | A+ |
| S002 | Diya Patel | 86.20 | A |

These results describe the supplied fictional dataset only.

### Testing

All 13 automated tests passed on my computer.

The tests cover:

- Total and average calculations
- Grade boundaries
- Exact pass threshold
- Failure caused by a single subject
- Attendance warning behavior
- Missing columns
- Invalid marks
- Duplicate and blank student IDs
- Empty datasets
- Top-performer ties
- Class and subject summaries
- Preservation of the input DataFrame
- Calculations on the packaged dataset

Passing tests confirms the tested behavior, but does not guarantee correctness
for every possible input.

## 9. Challenges and Learning

### Challenge: Running Commands from the Wrong Folder

Initially, I ran the installation command from the parent folder rather than
the folder containing the project files.

This caused an error because Python could not find `requirements.txt`.

I solved the problem by moving into the folder containing `main.py`,
`requirements.txt`, and `students.csv`, then running the commands again.

### Challenge: Incorrect Filename in the Run Command

An earlier command included a formatted link instead of the plain filename.

I corrected the command to:

    python main.py

The program then ran successfully.

### Learning from Local Execution

I learned how to:

- Navigate to the correct project folder in the terminal.
- Create a Python virtual environment.
- Install dependencies from `requirements.txt`.
- Run a Python program.
- Execute automated tests and recognize successful output.

### Important Project Concepts

The implementation demonstrates that:

- Attendance must be kept separate from subject-mark calculations.
- A high average does not guarantee a pass when one subject is below 40.
- Input validation helps prevent misleading results.
- NumPy supports numerical calculations across student records.
- Pandas supports tabular processing and report export.
- Keeping tied top performers avoids excluding equal results arbitrarily.

## 10. GitHub Repository and Submission

[**GitHub Repository URL:** https://github.com/madhuamarappanavar007-del/student-performance-analytics]

**Google Form Submission Status:** Not yet confirmed.

### Remaining Submission Actions

1. Review and adapt the implementation according to the trainer’s rules.
2. Confirm the trainer’s policy on AI assistance.
3. Upload the code, dataset, requirements, README, and documentation to GitHub.
4. Exclude `.venv` and `__pycache__` folders.
5. Set repository visibility according to the trainer’s instructions.
6. Replace the repository URL placeholder in this document.
7. Push the updated documentation to GitHub.
8. Submit the repository link through the EWB Google Form.
9. Verify the final repository and form submission before the deadline.

The Google Form URL is not included in the assignment PDF and must be obtained
from EWB or the trainer.