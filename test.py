import csv
import os
import tempfile
import unittest
import argparse
import sys
from wrong_solution import merge_csv as wrong_merge_csv
from solution import merge_csv


class TestMergeCsv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file1 = os.path.abspath("file1.csv")
        cls.file2 = os.path.abspath("file2.csv")
        cls.tmpdir = tempfile.TemporaryDirectory()
        cls.out = os.path.join(cls.tmpdir.name, "result.csv")

        if FILENAME == "wrong_solution.py":
            func = wrong_merge_csv
        else:
            func = merge_csv

        func(cls.file1, cls.file2, cls.out, key="key")

        with open(cls.out, "r", newline="") as f:
            dreader = csv.DictReader(f)
            cls.fieldnames = dreader.fieldnames
            cls.rows_dict = list(dreader)
        cls.by_key = {r["key"]: r for r in cls.rows_dict}
        cls.header = cls.fieldnames
        cls.data_keys_order = [r["key"] for r in cls.rows_dict]

    @classmethod
    def tearDownClass(cls):
        cls.tmpdir.cleanup()

    def test_inner_join_keys_set(self):
        expected = {"2", "3", "4"}
        self.assertEqual(expected, set(self.data_keys_order), "Inner join keys mismatch")

    def test_row_order(self):
        expected_keys_order = ["4", "2", "3"]
        self.assertEqual(expected_keys_order, self.data_keys_order, "Row order mismatch")

    def test_header_order(self):
        expected_header = ["key", "name", "age", "city", "salary", "department"]
        self.assertEqual(expected_header, self.header, "Headers mismatch")

    def test_values_are_merged_correctly(self):
        expectations = [
            ("4", "name", "David"),
            ("4", "department", "Management"),
            ("2", "city", "Berlin"),
            ("2", "salary", "50000"),
            ("3", "name", "Charlie"),
            ("3", "salary", "45000"),
        ]

        for key, field, expected in expectations:
            actual = self.by_key[key][field]
            self.assertEqual(
                expected,
                actual,
                f"Mismatch for key={key}, field={field}: expected '{expected}', got '{actual}'"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args, remaining = parser.parse_known_args()
    FILENAME = args.filename
    unittest.main(argv=[sys.argv[0]] + remaining, verbosity=2)