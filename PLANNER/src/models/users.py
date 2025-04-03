from pydantic import BaseModel, EmailStr                    #이메일 형식 맞추게
from .events import Event

class User(BaseModel):
    email: EmailStr 
    password: str
    events: list[Event] | None = None
    
class UserSingIn(BaseModel):
    email: EmailStr
    password: str