from pydantic import BaseModel
from TestResult import TestResult


class TestCase(BaseModel):
    name: str

    def setUp(self): ...

    def tearDown(self): ...

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            print(e)
            result.testFailed()
        self.tearDown()
        return result
