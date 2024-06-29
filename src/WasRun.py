from TestCase import TestCase


class WasRun(TestCase):
    """runされるクラス. つまりテストしたい対象のクラス"""

    log: str = ""

    def __init__(self, name: str):
        super().__init__(name=name)

    # override
    def setUp(self):
        self.log = "setUp" + " "

    def testMethod(self):
        """テストしたいメソッド"""
        self.log += "testMethod" + " "

    def testBrokenMethod(self):
        """テストしたいメソッドで、かつエラーが発生するメソッド"""
        raise Exception

    def tearDown(self):
        self.log += "tearDown" + " "
