from pydantic import BaseModel

class Owner(BaseModel):
    id: int
    name: str
