from pydantic import BaseModel, EmailStr                    #이메일 형식 맞추게
from beanie import Document
from .events import Event


class User(Document):
    email: EmailStr 
    password: str
    events: list[Event] | None = None               # None=None 은 디폴트가 null임임
    
    class Settings:
        name = "users"    
class UserSignIn(BaseModel):
    email: EmailStr
    password: str