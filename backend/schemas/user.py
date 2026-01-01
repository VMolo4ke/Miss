from pydantic import BaseModel, Field, field_validator
import re

class UserCreate(BaseModel):
    phone: str = Field(..., example="+79991234567")
    password: str = Field(..., min_length=4)

    @field_validator("phone")
    @classmethod
    def normalize_phone(cls, v: str) -> str:
        digits = re.sub(r"\D", "", v)
        
        if len(digits) == 11 and digits.startswith("8"):
            digits = "7" + digits[1:]
            
        if len(digits) != 11:
            raise ValueError("Номер телефона должен содержать 11 цифр")
            
        return digits

class UserRead(BaseModel):
    id: int
    phone: str
    username: str | None = None # Сделал Optional, так как при регистрации ника еще нет

    class Config:
        from_attributes = True

# Схема для получения токена при логине
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
