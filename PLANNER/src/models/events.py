from pydantic import BaseModel, ConfigDict
from beanie import Document

class Event(Document):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str 
    created_at: str
     
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "yap",
                "image": "path/to",
                "description": "화이팅",
                "tags": ["아자자"],
                "location": "삼육대학교",
                "created_at": "2023-10-01T12:00:00Z"
            }
        }
    )
    
    
class Eventupdate(BaseModel):
    title: str | None = None 
    image: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    location: str | None = None