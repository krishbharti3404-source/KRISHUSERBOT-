import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Zaid import app   # <-- FIXED! your bot package name is Zaid

API_ID = 123456
API_HASH = "your_api_hash"

@app.on_message(filters.command("genstring") & filters.private)
async def gen_string_start(bot, message: Message):
    await message.reply("📲 **Apna Phone Number bhejo:**\nFormat: +91xxxxxxxxxx")

    response = await bot.listen(message.chat.id, timeout=60)
    phone = response.text

    client = Client(
        name="gen_session",
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True
    )

    await client.connect()

    try:
        sent = await client.send_code(phone)
        await message.reply("📩 **OTP aa gaya!**\n\nOTP bhejo:")
    except Exception as e:
        await message.reply(f"❌ Error: `{e}`")
        return

    otp = await bot.listen(message.chat.id, timeout=60)
    code = otp.text.replace(" ", "")

    try:
        await client.sign_in(phone, sent.phone_code_hash, code)
    except Exception as e:
        await message.reply(f"❌ Error (OTP): `{e}`")
        return

    try:
        string = await client.export_session_string()
        await message.reply(f"**✅ STRING SESSION:**\n```\n{string}\n```")
    except Exception as e:
        await message.reply(f"❌ Error: `{e}`")

    await client.disconnect()
