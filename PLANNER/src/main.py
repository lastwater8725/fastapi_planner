from fastapi import FastAPI 
from .routes.events import envent_router
from .routes.users import user_router


app = FastAPI()
app.include_router(event_router)
app.inclue_router(user_router)

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