import os
import pytest
from click.testing import CliRunner
from cc_jsonparser.main import compile_json_file


class TestJSONParser:
    runner = CliRunner()

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
        invalid = self.run_single_file("./tests/step1/invalid.json")
        valid = self.run_single_file("./tests/step1/valid.json")

        assert self.falsy(invalid) == False
        assert self.truthy(valid) == True
