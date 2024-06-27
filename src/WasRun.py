from pydantic import BaseModel
from TestCase import TestCase


class WasRun(TestCase):
    wasRun: int | None = None
    wasSetup: int | None = None

    def __init__(self, name: str):
        super().__init__(name=name)

    # override
    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

    def testMethod(self):
        self.wasRun = 1
