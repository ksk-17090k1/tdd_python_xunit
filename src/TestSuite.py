from pydantic import BaseModel
from TestCase import ITestCase
from TestResult import TestResult


class TestSuite(BaseModel):
    tests: list[object] = []

    def add(self, test: ITestCase):
        self.tests.append(test)

    def run(self, result: TestResult):
        [t.run(result, t) for t in self.tests if isinstance(t, ITestCase)]
        return result
