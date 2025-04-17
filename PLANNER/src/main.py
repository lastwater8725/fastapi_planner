from contextlib import asynccontextmanager          #약간 메모리 자동 관리
from fastapi import FastAPI 
from .routes.events import event_router
from .routes.users import user_router
from .database.connection import initialize_database


#db관리 
async def lifespan(app: FastAPI):
    # 이 코드 구현하면 서버 시작할 때
    await initialize_database()
    yield
    # 서버 종료시 정리해야할 작업들들
    
app = FastAPI(
    lifespan=lifespan
)
app.include_router(event_router)
app.include_router(user_router)

@app.get("/")
async def root_path():
    return "hello world"

if __name__ == "__main__":
    uvicorn.run(
        "main.app",
        host="127.0.0.1",
        port=8000,
        reload=True
        
    )