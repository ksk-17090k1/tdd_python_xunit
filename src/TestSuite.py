from pydantic import BaseModel
from TestCase import TestCase
from TestResult import TestResult


class TestSuite(BaseModel):
    tests: list[TestCase] = []

    def add(self, test: TestCase):
        self.tests.append(test)

    def run(self, result: TestResult):
        [t.run(result) for t in self.tests]
        return result
