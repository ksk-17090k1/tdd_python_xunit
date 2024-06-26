from pydantic import BaseModel


class TestCase(BaseModel):
    name: str

    def run(self):
        method = getattr(self, self.name)
        method()
