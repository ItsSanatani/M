from pyrogram import Client
from config import OWNER_ID

async def auto_join(client, chat_link):
    try:
        await client.join_chat(chat_link)
        return True
    except Exception as e:
        return str(e)
