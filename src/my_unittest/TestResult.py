from pydantic import BaseModel


class TestResult(BaseModel):
    run_count: int = 0
    failed_count: int = 0

    def testStarted(self):
        self.run_count += 1

    def testFailed(self):
        self.failed_count += 1

    def summary(self):
        return f"{self.run_count} run, {self.failed_count} failed"
