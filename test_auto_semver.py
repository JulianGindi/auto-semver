import os
import unittest


from auto_semver.semver import Semver
from auto_semver.auto_semver import AutoSemver
from auto_semver.file_replacer import SemverFileReplacer


class TestAutoSemver(unittest.TestCase):
    def setUp(self):
        self.semver_list_minor = [
            Semver("0.1.0"),
            Semver("0.6.3"),
            Semver("0.3.65"),
        ]

        self.semver_list_major = [
            Semver("2.1.0"),
            Semver("1.6.3"),
            Semver("0.3.65"),
        ]

        self.semver_list_patch = [
            Semver("1.6.23"),
            Semver("1.6.3"),
            Semver("0.3.65"),
        ]

    def test_get_highest_semver_minor_comparison(self):
        expected_highest = "0.6.3"
        a = AutoSemver(self.semver_list_minor, "minor", False)
        a._get_highest_semver_from_list()

        self.assertEqual(expected_highest, a.current_semver.semver)

    def test_get_highest_semver_major_comparison(self):
        expected_highest = "2.1.0"
        a = AutoSemver(self.semver_list_major, "minor", False)
        a._get_highest_semver_from_list()

        self.assertEqual(expected_highest, a.current_semver.semver)

    def test_get_highest_semver_patch_comparison(self):
        expected_highest = "1.6.23"
        a = AutoSemver(self.semver_list_patch, "minor", False)
        a._get_highest_semver_from_list()

        self.assertEqual(expected_highest, a.current_semver.semver)

    def test_auto_increment_patch_version(self):
        expected_end_result = "1.6.24"
        a = AutoSemver(self.semver_list_patch, "patch", False)
        a._auto_increment_semver()

        self.assertEqual(expected_end_result, a.next_semver.semver)

    def test_auto_increment_minor_version(self):
        expected_end_result = "0.7.0"
        a = AutoSemver(self.semver_list_minor, "minor", False)
        a._auto_increment_semver()

        self.assertEqual(expected_end_result, a.next_semver.semver)


class TestSemverFileReplacer(unittest.TestCase):
    def setUp(self):
        self.filename = "test.txt"

        test_text = """
        apiVersion: v2
        appVersion: 0.1.0
        ports:
            - 8080
            - 3020
        """

        with open(self.filename, "w") as f:
            f.write(test_text)

    def tearDown(self):
        os.remove(self.filename)

    def test_find_and_replace_semver_patch(self):
        expected_file_output = """
        apiVersion: v2
        appVersion: 0.1.1
        ports:
            - 8080
            - 3020
        """

        sfr = SemverFileReplacer(self.filename, "patch")
        sfr.find_and_replace_semver_instances()
        result_data = open(self.filename).read()
        self.assertEqual(result_data, expected_file_output)


if __name__ == "__main__":
    unittest.main()
