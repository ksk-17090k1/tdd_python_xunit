from my_unittest.TestCase import ITestCase
from my_unittest.TestResult import TestResult
from pydantic import BaseModel


class TestSuite(BaseModel):
    tests: list[object] = []

    def add(self, test: ITestCase):
        self.tests.append(test)

    def run(self, result: TestResult):
        [t.run(result, t) for t in self.tests if isinstance(t, ITestCase)]
        return result
