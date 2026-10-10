"""Run from the project folder: python -m unittest discover -s tests -v"""

import unittest
from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from functions import (
    SUBJECTS, assign_grade, build_summary, load_students,
    process_students, subject_analysis, top_students, validate_students,
)


class AnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Student_ID": ["T1", "T2", "T3"],
            "Name": ["One", "Two", "Three"],
            "Department": ["Test"] * 3,
            **{subject: [90, 40, 80] for subject in SUBJECTS},
            "Attendance": [90, 75, 60],
        })

    def test_totals_and_averages(self):
        result = process_students(self.data)
        np.testing.assert_array_equal(result["Total"], [450, 200, 400])
        np.testing.assert_array_equal(result["Average"], [90, 40, 80])

    def test_grade_boundaries(self):
        for average, grade in [(100, "A+"), (90, "A+"), (89.99, "A"),
                               (80, "A"), (70, "B"), (60, "C"),
                               (50, "D"), (40, "E")]:
            with self.subTest(average=average):
                self.assertEqual(assign_grade(average, True), grade)
        self.assertEqual(assign_grade(95, False), "F")

    def test_single_failed_subject_overrides_high_average(self):
        self.data.loc[0, "Python"] = 39
        result = process_students(self.data)
        self.assertEqual(result.loc[0, "Status"], "Fail")
        self.assertEqual(result.loc[0, "Grade"], "F")

    def test_exact_pass_threshold(self):
        result = process_students(self.data)
        self.assertEqual(result.loc[1, "Status"], "Pass")

    def test_attendance_does_not_change_pass(self):
        result = process_students(self.data)
        self.assertEqual(result.loc[2, "Status"], "Pass")
        self.assertEqual(result.loc[2, "Attendance_Flag"], "Below 75%")
        self.assertEqual(result.loc[1, "Attendance_Flag"], "75% or above")

    def test_missing_column(self):
        with self.assertRaises(ValueError):
            validate_students(self.data.drop(columns="Python"))

    def test_bad_marks(self):
        for value in [-1, 101, "bad", np.nan, np.inf]:
            with self.subTest(value=value):
                copy = self.data.astype({"Python": object})
                copy.loc[0, "Python"] = value
                with self.assertRaises(ValueError):
                    validate_students(copy)

    def test_duplicate_and_blank_ids(self):
        for value in ["T2", "   ", None]:
            with self.subTest(value=value):
                copy = self.data.copy()
                copy.loc[0, "Student_ID"] = value
                with self.assertRaises(ValueError):
                    validate_students(copy)

    def test_empty_dataset(self):
        with self.assertRaises(ValueError):
            validate_students(self.data.iloc[0:0])

    def test_top_boundary_ties(self):
        self.data.loc[2, SUBJECTS] = 90
        leaders = top_students(process_students(self.data), 1)
        self.assertEqual(len(leaders), 2)
        with self.assertRaises(ValueError):
            top_students(process_students(self.data), 0)

    def test_subject_and_class_summary(self):
        result = process_students(self.data)
        subjects = subject_analysis(result)
        summary = build_summary(result, subjects)
        self.assertAlmostEqual(summary["class_average"], 70)
        self.assertEqual(summary["passed"], 3)
        self.assertEqual(summary["failed"], 0)
        self.assertTrue((subjects["Passed"] == 3).all())
        self.assertTrue((subjects["Average"] == 70).all())

    def test_processing_preserves_input(self):
        before = self.data.copy(deep=True)
        process_students(self.data)
        pd.testing.assert_frame_equal(self.data, before)

    def test_packaged_dataset(self):
        data = load_students(Path(__file__).resolve().parents[1] / "students.csv")
        self.assertEqual(len(data), 20)
        result = process_students(data)
        # Independent row-wise Python calculation checks NumPy's results.
        for _, row in result.iterrows():
            marks = [float(row[subject]) for subject in SUBJECTS]
            self.assertAlmostEqual(row["Total"], sum(marks))
            self.assertAlmostEqual(row["Average"], sum(marks) / len(marks))
            self.assertEqual(row["Status"] == "Pass", all(mark >= 40 for mark in marks))


if __name__ == "__main__":
    unittest.main()