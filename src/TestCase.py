from pydantic import BaseModel


class TestCase(BaseModel):
    name: str

    # abstract method
    def setUp(self): ...

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
