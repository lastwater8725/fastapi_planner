from fastapi import APIRouter, HTTPException, status
from src.models.users import User, UserSignIn
from src.database.connection import Database

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

#users는 dict형식으로 만들고, email을 key로 하고, User를 value로 하자
users_db = Database(User)

@user_router.post("/signup")
async def sign_new_user(user: User):
    user_exit = await users_db.get_all()
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    await users_db.save(user)
    return {"message": "user successfully created"}

#users를 보면서 어떤 데이터 형식일지 예상하기

@user_router.post("/signup")
async def sign_new_user(user: User):
    """회원가입"""
    if user.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    users["email"] = user
    return {"message": "user successfully created"}        


@user_router.post("/signin")
async def sign_new_user_in(credentials: UserSignIn):
    """회원가입이 끝난 회원이 로그인하는 api
    이메일, 비밀번호
    로그인: 이메일, 비번
    """
    if credentials.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    stored_user = users[credentials.email]
    if stored_user.password != users["password"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail  = "Incorrect password"
        )
    return {"message": "user successfully signed in"}


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


@event_router.delete("/{id}")
async def delete_event():
    return ""


