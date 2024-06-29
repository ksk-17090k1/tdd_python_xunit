from pydantic import BaseModel


class TestSuite(BaseModel):
    tests: list = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        [t.run(result) for t in self.tests]
        return result
