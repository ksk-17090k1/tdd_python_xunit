from pydantic import BaseModel
from TestCase import TestCase


class WasRun(TestCase):
    wasRun: str = None
    name: str

    def __init__(self, name: str):
        super().__init__(name=name)

    def testMethod(self):
        self.wasRun = 1
