"""Reusable loading, validation, calculation and reporting functions."""

from pathlib import Path

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Statistics", "Computer_Science", "English"]
REQUIRED_COLUMNS = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
PASS_MARK = 40


def load_students(csv_path):
    """Read the CSV without dropping rows or silently filling invalid data."""
    data = pd.read_csv(csv_path, dtype={"Student_ID": str})
    validate_students(data)
    return data


def validate_students(data):
    """Reject missing columns, empty data, invalid IDs and out-of-range values."""
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("The dataset must contain at least one student.")
    for column in ["Student_ID", "Name", "Department"]:
        if data[column].isna().any():
            raise ValueError(f"{column} contains missing values.")
        if data[column].astype(str).str.strip().eq("").any():
            raise ValueError(f"{column} contains blank values.")
    if data["Student_ID"].astype(str).str.strip().duplicated().any():
        raise ValueError("Student_ID values must be unique.")
    # A loop is useful here because the same validation applies to each field.
    for column in [*SUBJECTS, "Attendance"]:
        values = pd.to_numeric(data[column], errors="coerce")
        if values.isna().any() or not np.isfinite(values.to_numpy()).all():
            raise ValueError(f"{column} must contain finite numeric values.")
        if not values.between(0, 100).all():
            raise ValueError(f"{column} values must be between 0 and 100.")
        data[column] = values


def assign_grade(average, passed):
    """A failed subject overrides the average-based grade."""
    if not passed:
        return "F"
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "E"


def process_students(data):
    """Calculate metrics on a copy; never include attendance in marks."""
    validate_students(data.copy())
    result = data.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)
    result["Total"] = np.sum(marks, axis=1)
    result["Average"] = np.mean(marks, axis=1)
    passed = np.all(marks >= PASS_MARK, axis=1)
    result["Status"] = np.where(passed, "Pass", "Fail")
    result["Grade"] = [
        assign_grade(average, did_pass)
        for average, did_pass in zip(result["Average"], passed)
    ]
    # Attendance is reported separately, not used as an academic pass condition.
    result["Attendance_Flag"] = np.where(
        result["Attendance"].astype(float) < 75, "Below 75%", "75% or above"
    )
    return result


def subject_analysis(data):
    """Return one row per subject, using NumPy for numerical summaries."""
    rows = []
    for subject in SUBJECTS:
        marks = data[subject].to_numpy(dtype=float)
        passed = int(np.count_nonzero(marks >= PASS_MARK))
        rows.append({
            "Subject": subject,
            "Highest": float(np.max(marks)),
            "Lowest": float(np.min(marks)),
            "Average": float(np.mean(marks)),
            "Passed": passed,
            "Failed": len(marks) - passed,
            "Pass_Percentage": passed / len(marks) * 100,
        })
    return pd.DataFrame(rows)


def top_students(data, top_n=5):
    """Keep all students tied at the last included average."""
    if top_n < 1:
        raise ValueError("top_n must be at least 1.")
    return data.nlargest(top_n, "Average", keep="all").sort_values(
        ["Average", "Student_ID"], ascending=[False, True]
    )


def build_summary(data, subjects):
    """Build a JSON-compatible summary; retain full precision in exports."""
    passed = int((data["Status"] == "Pass").sum())
    best_average = float(data["Average"].max())
    lowest_average = float(data["Average"].min())
    best_subject_average = float(subjects["Average"].max())
    return {
        "student_count": len(data),
        "subject_count": len(SUBJECTS),
        "maximum_total_marks": len(SUBJECTS) * 100,
        "class_average": float(data["Average"].mean()),
        "highest_average": best_average,
        "lowest_average": lowest_average,
        "passed": passed,
        "failed": len(data) - passed,
        "pass_percentage": passed / len(data) * 100,
        "highest_average_students": data.loc[
            data["Average"] == best_average, ["Student_ID", "Name"]
        ].to_dict(orient="records"),
        "lowest_average_students": data.loc[
            data["Average"] == lowest_average, ["Student_ID", "Name"]
        ].to_dict(orient="records"),
        "best_average_subjects": subjects.loc[
            subjects["Average"] == best_subject_average, "Subject"
        ].tolist(),
        "students_below_75_percent_attendance": int(
            (data["Attendance"].astype(float) < 75).sum()
        ),
        "grade_counts": {
            grade: int((data["Grade"] == grade).sum())
            for grade in ["A+", "A", "B", "C", "D", "E", "F"]
        },
    }


def save_reports(data, subjects, leaders, summary, output_dir):
    """Export analysis without altering the original input CSV."""
    import json

    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    data.to_csv(folder / "student_results.csv", index=False)
    subjects.to_csv(folder / "subject_analysis.csv", index=False)
    leaders.to_csv(folder / "top_students.csv", index=False)
    (folder / "summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )