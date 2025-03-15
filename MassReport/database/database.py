from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["MassReport"]

session_db = db["sessions"]

async def add_session(user_id: int, session_string: str):
    await session_db.update_one({"user_id": user_id}, {"$set": {"session": session_string}}, upsert=True)

async def get_session(user_id: int):
    data = await session_db.find_one({"user_id": user_id})
    return data["session"] if data else None
