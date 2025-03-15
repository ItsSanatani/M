from pyrogram import Client, filters
from MassReport.database.database import add_session, get_session, remove_session
from config import OWNER_ID, SUDO_USERS

@Client.on_message(filters.command("addsession") & filters.user(SUDO_USERS))
async def add_session_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: /addsession <session_string>")
    
    session_string = message.text.split(" ", 1)[1]
    await add_session(message.from_user.id, session_string)
    await message.reply_text("✅ Session Added Successfully!")

@Client.on_message(filters.command("mysession") & filters.user(SUDO_USERS))
async def my_session_cmd(client, message):
    session = await get_session(message.from_user.id)
    if session:
        await message.reply_text(f"🔹 Your Session:\n`{session}`")
    else:
        await message.reply_text("❌ No Session Found!")

@Client.on_message(filters.command("rmsession") & filters.user(SUDO_USERS))
async def remove_session_cmd(client, message):
    await remove_session(message.from_user.id)
    await message.reply_text("✅ Session Removed Successfully!")
