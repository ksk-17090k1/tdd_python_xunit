from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    test: WasRun | None = None

    # override
    def setUp(self):
        self.test = WasRun(name="testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetup(self):
        self.test.run()
        assert self.test.log == "setUp "


TestCaseTest(name="testRunning").run()
TestCaseTest(name="testSetup").run()
