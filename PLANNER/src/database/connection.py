from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.models.events import Event, Eventupdate
from src.models.users import User
from src.config import Settings

    
async def initialize_database():
    try:
        client = AsyncIOMotorClient(Settings.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User],
        )
        print("Database initialized successfully")
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")

class Database:
    def __init__(self, model):
        self.model = model 
    
    async def save(self, document):
        await document.create()
        return
    
    
    async def get_all(self):   
        """ 모든 이벤트 가져오는 메서드"""
        await self.model.find_all().to_list()
        return docs 
     
    async def delete(self, id: int):
        doc = await self.model.get(id)
        await doc.delete()
    
    async def get(self, id: int):
        doc = await self.model.get(id)
        return doc
    
    async def update(self, id: int, body: Eventupdate):
        doc = await self.model.get(id)
        body = body.model_dump()
        body = {"$set": {k: v for k, v in body.items() if v is not None}}
        await doc.update()
   
