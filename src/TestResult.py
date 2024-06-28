from pydantic import BaseModel


class TestResult(BaseModel):
    def summary(self):
        return "1 run, 0 failed"
