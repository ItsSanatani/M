from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MassReport.database.database import get_session
from utils import get_report_reason
from config import OWNER_ID, REPORT_REASONS

user_data = {}

@Client.on_message(filters.command("report") & filters.user(OWNER_ID))
async def report_command(client, message):
    user_id = message.from_user.id
    session_string = await get_session(user_id)
    
    if not session_string:
        return await message.reply_text("❌ पहले अपना सेशन जोड़ें `/addsession session_string`")

    user_data[user_id] = {}
    await message.reply_text("📌 Group या Channel का लिंक भेजें:")
    user_data[user_id]["step"] = "group_link"

@Client.on_message(filters.text & filters.user(OWNER_ID))
async def get_user_input(client, message):
    user_id = message.from_user.id
    
    if user_id not in user_data:
        return
    
    step = user_data[user_id].get("step")

    if step == "group_link":
        user_data[user_id]["group_link"] = message.text
        user_data[user_id]["step"] = "message_link"
        await message.reply_text("📌 अब उस Message का लिंक भेजें जिसे रिपोर्ट करना है:")

    elif step == "message_link":
        user_data[user_id]["message_link"] = message.text
        user_data[user_id]["step"] = "reason"
        
        buttons = [
            [InlineKeyboardButton(reason, callback_data=f"report_reason:{reason_code}")]
            for reason, reason_code in REPORT_REASONS.items()
        ]
        await message.reply_text("📌 रिपोर्ट करने का कारण चुनें:", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex(r"report_reason:(.*)"))
async def select_report_reason(client, callback_query):
    user_id = callback_query.from_user.id
    reason = callback_query.data.split(":")[1]

    if user_id not in user_data:
        return
    
    user_data[user_id]["reason"] = reason
    user_data[user_id]["step"] = "report_count"

    await callback_query.message.edit_text("📌 कितनी रिपोर्ट मारनी है? (संख्या भेजें)")

@Client.on_message(filters.text & filters.user(OWNER_ID))
async def get_report_count(client, message):
    user_id = message.from_user.id

    if user_id not in user_data or user_data[user_id].get("step") != "report_count":
        return

    try:
        count = int(message.text)
        if count <= 0:
            raise ValueError
    except ValueError:
        return await message.reply_text("❌ कृपया सही संख्या भेजें (1 या अधिक)")

    user_data[user_id]["count"] = count
    await start_mass_report(client, message, user_data[user_id])

async def start_mass_report(client, message, data):
    user_id = message.from_user.id
    session_string = await get_session(user_id)

    if not session_string:
        return await message.reply_text("❌ Session Not Found! Use `/addsession` First.")

    session = Client(f"reporter_{user_id}", session_string=session_string)
    await session.start()

    try:
        chat_id = await session.resolve_peer(data["group_link"])
        msg_id = int(data["message_link"].split("/")[-1])
        report_reason = get_report_reason(data["reason"])

        for i in range(data["count"]):
            await session.invoke(
                "messages.Report",
                peer=chat_id,
                id=[msg_id],
                reason=report_reason
            )
            await message.reply_text(f"✅ Report #{i+1} Sent!")

        await message.reply_text(f"✅ {data['count']} Reports Sent Successfully!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")
    
    await session.stop()
