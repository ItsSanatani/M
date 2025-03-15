from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, OWNER_ID, SUDO_USERS

bot = Client(
    "MassReportBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("👋 Hello! Use /addsession to add session & /report to report messages.")

@bot.on_message(filters.command("addsession") & filters.user(OWNER_ID))
async def add_session_command(client, message):
    session = message.text.split(" ", 1)[1] if " " in message.text else None
    if not session:
        return await message.reply_text("❌ Provide session string: `/addsession session_string`")

    from database.database import add_session
    await add_session(message.from_user.id, session)
    await message.reply_text("✅ Session added successfully!")
