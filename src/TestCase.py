import abc

from pydantic import BaseModel
from TestResult import TestResult


class ITestCase(abc.ABC):
    name: str

    @abc.abstractmethod
    def setUp(self): ...

    @abc.abstractmethod
    def tearDown(self): ...

    @abc.abstractmethod
    def run(self, result: TestResult, test_case: "ITestCase") -> TestResult: ...


class TestCase(BaseModel, ITestCase):
    """ロジックのコアとなるクラス"""

    name: str

    def setUp(self): ...

    def tearDown(self): ...

    def run(self, result: TestResult, test_case: ITestCase) -> TestResult:
        result.testStarted()
        test_case.setUp()
        try:
            method = getattr(test_case, test_case.name)
            method()
        except Exception as e:
            print(e)
            result.testFailed()
        test_case.tearDown()
        return result
