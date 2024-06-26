from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun(name="testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun


TestCaseTest(name="testRunning").run()
