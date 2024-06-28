from pydantic import BaseModel


class TestResult(BaseModel):
    run_count: int = 0
    failed_count: int = 0

    def testStarted(self):
        self.run_count += 1

    def summary(self):
        run_count = 1
        failed_count = 0
        return f"{run_count} run, {failed_count} failed"
