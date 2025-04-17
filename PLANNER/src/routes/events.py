from fastapi import APIRouter 
from src.models.events import Event
from src.database.connection import Database

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)
event_db = Database(Event)

@event_router.get("/", response_model=list[Event])      #모든 이벤트 가져오는 라우터
async def get_all_events():                     
    events = await event_db.get_all()
    return events

@event_router.get("/{id}", response_model=Event)            #아이디 받는 라우터
async def get_event(id: int):
    event = await event_db.get(id)
    return event 

@event_router.post("/")                     #이벤트 생성하는 라우터
async def create_event(event: Event):
    await event_db.save(event)
    return {"message": "Event created successfully"}

@event_router.delete("/{id}")                   #이벤트 삭제하는 라우터
async def delete_event(id: int):
    await event_db.delete(id)
    return {"message": "Event deleted successfully"}
    
@event_router.put("/{id}")                  #이벤트 수정하는 라우터
async def update_event(envent: Event, id: int):
    await event_db.update(id, event)
    return {"message": "Event updated successfully"}
 