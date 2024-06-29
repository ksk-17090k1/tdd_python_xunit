import re

from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):
    result: TestResult | None = None

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun(name="testMethod")
        _ = test.run(self.result)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        if self.result is None:
            raise ValueError("result is None")
        test = WasRun(name="testMethod")
        result = test.run(self.result)
        assert "1 run, 0 failed" == result.summary()

    def testFailedResultFormating(self):
        if self.result is None:
            raise ValueError("result is None")
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResult(self):
        if self.result is None:
            raise ValueError("result is None")
        test = WasRun(name="testBrokenMethod")
        result = test.run(self.result)
        assert "1 run, 1 failed" == result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun(name="testMethod"))
        suite.add(WasRun(name="testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary()


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest(name="testTemplateMethod"))
    suite.add(TestCaseTest(name="testResult"))
    suite.add(TestCaseTest(name="testFailedResultFormating"))
    suite.add(TestCaseTest(name="testFailedResult"))
    suite.add(TestCaseTest(name="testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
