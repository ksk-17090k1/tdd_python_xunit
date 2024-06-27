from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun(name="testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun

    def testSetup(self):
        test = WasRun(name="testMethod")
        test.run()
        assert test.wasSetup


TestCaseTest(name="testRunning").run()
TestCaseTest(name="testSetup").run()
