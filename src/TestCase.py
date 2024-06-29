from pydantic import BaseModel
from TestResult import TestResult


class TestCase(BaseModel):
    """ロジックのコアとなるクラス"""

    name: str

    def setUp(self): ...

    def tearDown(self): ...

    def run(self, result: TestResult) -> TestResult:
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
