from typing import Type

from my_unittest.TestCase import TestCase
from my_unittest.TestResult import TestResult
from my_unittest.TestSuite import TestSuite
from my_unittest.utils import get_test_methods


def main(cls: Type[TestCase]):
    suite = TestSuite()
    for method in get_test_methods(cls):
        suite.add(cls(name=method))
    result = TestResult()
    suite.run(result)
    print(result.summary())
