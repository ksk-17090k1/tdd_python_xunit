from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun(name="testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "


TestCaseTest(name="testTemplateMethod").run()
