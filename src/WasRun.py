from pydantic import BaseModel


class WasRun(BaseModel):
    wasRun: str = None
    name: str

    def run(self):
        # pluggable selector pattern
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1
