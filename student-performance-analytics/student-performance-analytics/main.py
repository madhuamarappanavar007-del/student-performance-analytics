"""Run with: python main.py"""

import argparse
from pathlib import Path
import sys

import pandas as pd

from functions import (
    build_summary, load_students, process_students,
    save_reports, subject_analysis, top_students,
)

BASE_DIR = Path(__file__).resolve().parent


def display_table(data):
    print(data.to_string(index=False, float_format=lambda value: f"{value:.2f}"))


def main():
    parser = argparse.ArgumentParser(description="Student Performance Analytics System")
    parser.add_argument("--input", type=Path, default=BASE_DIR / "students.csv")
    parser.add_argument("--output", type=Path, default=BASE_DIR / "output")
    parser.add_argument("--top", type=int, default=5, help="Top N, including boundary ties")
    args = parser.parse_args()
    if args.top < 1:
        parser.error("--top must be at least 1")
    try:
        raw = load_students(args.input)
        results = process_students(raw)
        subjects = subject_analysis(results)
        leaders = top_students(results, args.top)
        summary = build_summary(results, subjects)
        save_reports(results, subjects, leaders, summary, args.output)
    except (OSError, ValueError, pd.errors.ParserError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 70)
    print(f"Input: {args.input.name}")
    print("Dataset: fictional demonstration records; marks and attendance out of 100")
    print(f"Records: {len(raw)} | Columns: {len(raw.columns)}")
    print("Columns:", ", ".join(raw.columns))
    print("Missing cells:", int(raw.isna().sum().sum()))
    print("\nDATASET PREVIEW")
    display_table(raw.head())
    print("\nRULES")
    print("Pass: every subject >= 40. Failed subject => grade F.")
    print("Grades by average: A+ >=90, A >=80, B >=70, C >=60, D >=50, E >=40.")
    print("Attendance below 75% is a warning only; it does not change pass/fail.")
    print("\nSTUDENT RESULTS")
    display_table(results[["Student_ID", "Name", "Total", "Average", "Grade",
                           "Status", "Attendance", "Attendance_Flag"]])
    print("\nCLASS SUMMARY")
    print(f"Class average: {summary['class_average']:.2f}/100")
    print(f"Highest average: {summary['highest_average']:.2f}/100")
    print(f"Lowest average: {summary['lowest_average']:.2f}/100")
    print(f"Passed: {summary['passed']} | Failed: {summary['failed']}")
    print(f"Pass percentage: {summary['pass_percentage']:.2f}%")
    print("Highest-average students:", ", ".join(
        item["Name"] for item in summary["highest_average_students"]))
    print("Lowest-average students:", ", ".join(
        item["Name"] for item in summary["lowest_average_students"]))
    print("Best-average subjects:", ", ".join(summary["best_average_subjects"]))
    print("Attendance warnings:", summary["students_below_75_percent_attendance"])
    print("\nGRADE DISTRIBUTION")
    for grade, count in summary["grade_counts"].items():
        print(f"{grade}: {count}")
    print("\nSUBJECT-WISE ANALYSIS")
    display_table(subjects)
    print(f"\nTOP {args.top} STUDENTS (INCLUDING TIES)")
    display_table(leaders[["Student_ID", "Name", "Department", "Average", "Grade", "Status"]])
    print(f"\nReports saved to: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())