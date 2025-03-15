import motor.motor_asyncio
from config import MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["MassReportDB"]
sessions = db["sessions"]

async def add_session(user_id, session_string):
    await sessions.update_one(
        {"_id": user_id}, {"$set": {"session": session_string}}, upsert=True
    )

async def get_session(user_id):
    user = await sessions.find_one({"_id": user_id})
    return user["session"] if user else None

async def remove_session(user_id):
    await sessions.delete_one({"_id": user_id})
