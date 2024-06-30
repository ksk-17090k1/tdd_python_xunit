import my_unittest


# テスト対象の関数
def add(x: int, y: int) -> int:
    return x + y


class TestSample(my_unittest.TestCase):
    def setUp(self):
        # setUpの処理が必要な場合はここに追記
        ...

    def tearDown(self):
        # tearDownの処理が必要な場合はここに追記
        ...

    def test_add(self):
        assert add(1, 2) == 3

    def test_add_failed(self):
        assert add(1, 2) == 2


if __name__ == "__main__":
    my_unittest.main(TestSample)
