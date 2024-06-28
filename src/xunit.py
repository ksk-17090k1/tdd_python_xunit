from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    test: WasRun | None = None

    # override
    def setUp(self):
        self.test = WasRun(name="testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert self.test.log == "setUp testMethod "


TestCaseTest(name="testTemplateMethod").run()
