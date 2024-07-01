from my_unittest.TestCase import ITestCase, TestCase
from my_unittest.TestResult import TestResult
from pydantic import BaseModel


class WasRun(BaseModel, ITestCase):
    """runされるクラス. つまりテストしたい対象のクラス"""

    name: str
    test_case: TestCase
    log: str = ""

    def __init__(self, name: str):
        super().__init__(name=name, test_case=TestCase(name=name))

    # override
    def run(self, result: TestResult, test_case: ITestCase):
        return self.test_case.run(result, test_case=test_case)

    # override
    def setUp(self):
        self.log = "setUp" + " "

    # override
    def tearDown(self):
        self.log += "tearDown" + " "

    def testMethod(self):
        """テストしたいメソッド"""
        self.log += "testMethod" + " "

    def testBrokenMethod(self):
        """テストしたいメソッドで、かつエラーが発生するメソッド"""
        raise Exception
