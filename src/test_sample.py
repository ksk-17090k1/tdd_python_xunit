from main import main
from TestCase import TestCase
from TestResult import TestResult


def add(x: int, y: int) -> int:
    return x + y


class TestSample(TestCase):
    # おまじない
    result: TestResult = TestResult()

    def setUp(self):
        # おまじない
        self.result = TestResult()
        # setUpの処理が必要な場合はここに追記

    def tearDown(self):
        # tearDownの処理が必要な場合はここに追記
        ...

    def test_add(self):
        assert add(1, 2) == 3

    def test_add_failed(self):
        assert add(1, 2) == 1


if __name__ == "__main__":
    main(TestSample)
