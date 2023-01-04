#Python
from uuid import UUID
from datetime import date
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File

app = FastAPI()

#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        example='kjh23kjh'
    )
    
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='George'
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Peregrine'
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    pass

# Paths
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags=['Home'],
    summary='Home path'
)
def home():
    return {"Twitter API": "Working!"}