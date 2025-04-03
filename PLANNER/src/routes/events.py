from fastapi import APIRouter 

event_router = APIRouter(
    prefix="/events",
    tag=["Events"]
)