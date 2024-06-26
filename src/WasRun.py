from pydantic import BaseModel


class WasRun(BaseModel):
    wasRun: str = None

    def run(self):
        self.testMethod()

    def testMethod(self):
        self.wasRun = 1
