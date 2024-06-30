from pydantic import BaseModel
from TestCase import ITestCase, TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(BaseModel, ITestCase):
    """テストコードに相当するクラス"""

    result: TestResult | None = None
    test_case: TestCase

    def __init__(self, name: str):
        super().__init__(name=name, test_case=TestCase(name=name))

    # override
    def run(self, result: TestResult, test_case: ITestCase) -> TestResult:
        return self.test_case.run(result, test_case=test_case)

    # override
    def setUp(self):
        self.result = TestResult()

    # override
    def tearDown(self): ...

    def testTemplateMethod(self):
        if self.result is None:
            raise ValueError("result is None")
        test = WasRun(name="testMethod")
        _ = test.run(self.result, test_case=test)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        if self.result is None:
            raise ValueError("result is None")
        test = WasRun(name="testMethod")
        result = test.run(self.result, test_case=test)
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
        result = test.run(self.result, test_case=test)
        assert "1 run, 1 failed" == result.summary()

    def testSuite(self):
        suite = TestSuite()
        # WasRunクラスの２つのメソッドをテスト
        suite.add(WasRun(name="testMethod"))
        suite.add(WasRun(name="testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary()


if __name__ == "__main__":
    suite = TestSuite()
    # [重要!] ここではテストしたい対象はTestCaseTestクラスなのでそれをaddする
    suite.add(TestCaseTest(name="testTemplateMethod"))
    suite.add(TestCaseTest(name="testResult"))
    suite.add(TestCaseTest(name="testFailedResultFormating"))
    suite.add(TestCaseTest(name="testFailedResult"))
    suite.add(TestCaseTest(name="testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
