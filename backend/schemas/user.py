from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    phone: str = Field(..., example="+79991234567")
    password: str = Field(..., min_length=4)

class UserRead(BaseModel):
    id: int
    phone: str
    username: str

    class Config:
        from_attributes = True