from TestCase import TestCase
from TestResult import TestResult
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun(name="testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun(name="testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResultFormating(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest(name="testTemplateMethod").run()
TestCaseTest(name="testResult").run()
TestCaseTest(name="testFailedResultFormating").run()
