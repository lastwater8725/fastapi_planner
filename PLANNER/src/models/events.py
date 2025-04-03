from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
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
                "location": "삼육대학교"
            }
        }
    )
    