from pydantic import BaseModel
from TestCase import TestCase


class WasRun(TestCase):
    log: str = ""

    def __init__(self, name: str):
        super().__init__(name=name)

    # override
    def setUp(self):
        self.log = "setUp" + " "

    def testMethod(self):
        self.log += "testMethod" + " "
