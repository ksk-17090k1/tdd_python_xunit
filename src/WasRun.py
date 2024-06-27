from pydantic import BaseModel
from TestCase import TestCase


class WasRun(TestCase):
    wasSetup: str = None
    wasRun: str = None
    name: str

    def __init__(self, name: str):
        super().__init__(name=name)

    def setUp(self):
        self.wasSetup = 1

    def testMethod(self):
        self.wasRun = 1
