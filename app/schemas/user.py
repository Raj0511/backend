from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from beanie import PydanticObjectId

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Must be at least 8 chars")

class UserResponse(UserBase):
    id: PydanticObjectId = Field(alias="_id")
    
    class Config:
        from_attributes = True
        populate_by_name = True
class Token(BaseModel):
    access_token: str
    token_type: str