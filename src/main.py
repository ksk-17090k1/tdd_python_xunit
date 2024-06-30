from typing import Type

from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from utils import get_test_methods


def main(cls: Type[TestCase]):
    suite = TestSuite()
    for method in get_test_methods(cls):
        suite.add(cls(name=method))
    result = TestResult()
    suite.run(result)
    print(result.summary())
