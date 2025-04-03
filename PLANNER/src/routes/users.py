from fastapi import APIRouter 

user_router = APIRouter(
    prefix="/users",
    tag=["Users"]
)

@user_router.post("/signup")
async def sign_new_user():
    return "not implemented"

@user_router.post("/signin")
async def sign_new_user_in():
    return "not implemented"

@event_router.get("/") 
async def get_all_events():
    return []

@event_router.get("/{id}")
async def get_event():
    return ""

@event_router.post("/")
async def create_event():
    return ""

@event_router.put("/{id}")
async def update_event():
    return ""

@envent_router.delete("/{id}")
async def delete_event():
    return ""