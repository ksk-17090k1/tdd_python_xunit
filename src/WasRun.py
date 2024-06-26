from pydantic import BaseModel


class WasRun(BaseModel):
    wasRun: str = None

    def testMethod(self):
        self.wasRun = 1
