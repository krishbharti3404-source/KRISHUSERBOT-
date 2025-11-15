from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *

PHONE_NUMBER_TEXT = (
    "✘ Heya My Master👋!\n\n"
    "✘ I'm Your Assistant\n\n"
    "‣ I can help you to host Your Left Clients.\n"
    "‣ Specially for Busy People.\n\n"
    "‣ Use Buttons Below:"
)

# =======================  START PAGE  =======================

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
        [
            InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ", url="t.me/fine_n_ok"),
        ],
        [
            InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url="t.me/kryshupdate"),
        ],
        [
            InlineKeyboardButton("✘ STRING GENERATE", callback_data="genstring_btn"),
        ],
        [
            InlineKeyboardButton("✘ CLONE CLIENT", callback_data="clone_btn"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(
        message.chat.id,
        ALIVE_PIC,
        caption=PHONE_NUMBER_TEXT,
        reply_markup=reply_markup,
    )

# =======================  CALLBACK HANDLERS  =======================

@app.on_callback_query(filters.regex("genstring_btn"))
async def gen_btn(client, cq):
    await cq.message.reply("Use Command:\n\n`/genstring`")

@app.on_callback_query(filters.regex("clone_btn"))
async def clone_btn(client, cq):
    await cq.message.reply("Use Command:\n\n`/clone your_session_string_here`")


# =======================  CLONE COMMAND  =======================

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session_string_here")
    try:
        phone = msg.command[1]
    except:
        return await msg.reply("❌ Please send session string.\nExample: `/clone ABCDEF12345`")

    try:
        await text.edit("Booting Your Client...")

        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=phone,
            plugins=dict(root="Zaid/modules"),
        )

        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As **{user.first_name}** ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")


# =======================  GENSTRING COMMAND  =======================

@app.on_message(filters.command("genstring") & filters.private)
async def genstring(client: app, message: Message):

    await message.reply("📲 **Apna Phone Number bhejo:**\nFormat: +91xxxxxxxxxx")

    phone_msg = await client.listen(message.chat.id)
    phone = phone_msg.text

    session = Client(
        "gen_session",
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True
    )

    await session.connect()

    try:
        sent = await session.send_code(phone)
        await message.reply("📩 **OTP aa gaya!**\n\nOTP bhejo:")
    except Exception as e:
        return await message.reply(f"❌ Error: `{e}`")

    otp_msg = await client.listen(message.chat.id)
    otp = otp_msg.text.replace(" ", "")

    try:
        await session.sign_in(phone, sent.phone_code_hash, otp)
    except Exception as e:
        return await message.reply(f"❌ Incorrect OTP!\nError: `{e}`")

    try:
        string = await session.export_session_string()
        await message.reply(
            "**✅ STRING SESSION GENERATED!**\n\n"
            f"Use it like this:\n\n`/clone {string}`\n\n"
            f"```\n{string}\n```"
        )
    except Exception as e:
        await message.reply(f"❌ Error: `{e}`")

    await session.disconnect()
