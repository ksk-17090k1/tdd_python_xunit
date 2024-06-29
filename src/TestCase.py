from pydantic import BaseModel
from TestResult import TestResult


class TestCase(BaseModel):
    name: str

    # abstract method
    def setUp(self): ...

    # abstract method
    def tearDown(self): ...

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.testFailed()
        self.tearDown()
        return result
