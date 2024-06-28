from pydantic import BaseModel
from TestCase import TestCase


class WasRun(TestCase):
    wasRun: int | None = None
    wasSetup: int | None = None
    log: str = ""

    def __init__(self, name: str):
        super().__init__(name=name)

    # override
    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
