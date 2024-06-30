from main import main
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):
    """テストコードに相当するクラス"""

    result: TestResult = TestResult()

    # override
    def setUp(self):
        self.result = TestResult()

    # override
    def tearDown(self): ...

    def testTemplateMethod(self):
        test = WasRun(name="testMethod")
        _ = test.run(self.result, test_case=test)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun(name="testMethod")
        result = test.run(self.result, test_case=test)
        assert "1 run, 0 failed" == result.summary()

    def testFailedResultFormating(self):
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResult(self):
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
    main(TestCaseTest)
