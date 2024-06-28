from pydantic import BaseModel
from TestResult import TestResult


class TestCase(BaseModel):
    name: str

    # abstract method
    def setUp(self): ...

    # abstract method
    def tearDown(self): ...

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()
