import os
import pytest
from click.testing import CliRunner
from cc_jsonparser.main import compile_json_file


class TestJSONParser:
    runner = CliRunner()
    BASE_PATH = "./tests/"

    def run_single_file(self, filename: os.path) -> bool:
        """Parse a single json file using click's test runner

        Args:
            filename (os.path): path to file to test
        Returns:
            A boolean value, True for valid JSON and False for invalid
            JSON.
        Raises:
            Exception
        """
        result = self.runner.invoke(compile_json_file, [filename])
        return result

    def truthy(self, value):
        return bool(value)

    def falsy(self, value):
        return not bool(value)

    def test_step_one(self):
        step = "step1/"
        invalid = self.run_single_file(f"{self.BASE_PATH}{step}invalid.json")
        valid = self.run_single_file(f"{self.BASE_PATH}{step}valid.json")

        assert self.falsy(invalid) == False
        assert self.truthy(valid) == True

    def test_step_two(self):
        step = "step2/"
        invalid = self.run_single_file(f"{self.BASE_PATH}{step}invalid.json")
        invalid2 = self.run_single_file(f"{self.BASE_PATH}{step}invalid2.json")
        valid = self.run_single_file(f"{self.BASE_PATH}{step}valid.json")
        valid2 = self.run_single_file(f"{self.BASE_PATH}{step}valid2.json")

        assert self.falsy(invalid) == False
        assert self.falsy(invalid2) == False
        assert self.truthy(valid) == True
        assert self.truthy(valid2) == True

    def test_step_three(self):
        step = "step3/"
        invalid = self.run_single_file(f"{self.BASE_PATH}{step}invalid.json")
        valid = self.run_single_file(f"{self.BASE_PATH}{step}valid.json")

        assert self.falsy(invalid) == False
        assert self.truthy(valid) == True

    def test_step_four(self):
        step = "step4/"
        invalid = self.run_single_file(f"{self.BASE_PATH}{step}invalid.json")
        valid = self.run_single_file(f"{self.BASE_PATH}{step}valid.json")
        valid2 = self.run_single_file(f"{self.BASE_PATH}{step}valid2.json")

        assert self.falsy(invalid) == False
        assert self.truthy(valid) == True
        assert self.truthy(valid2) == True
