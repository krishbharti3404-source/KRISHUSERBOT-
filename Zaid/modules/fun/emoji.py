from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# LOVE 💞
@Client.on_message(filters.command("love", ".") & filters.me)
async def love_animation(client: Client, message: Message):
    emojis = ["❤️", "💞", "💓", "💗", "💖", "💘", "💕", "💝", "💟", "❤️‍🔥"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "I ❤️ YOU 😘"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# MISS YOU 😔
@Client.on_message(filters.command("missyou", ".") & filters.me)
async def missyou_animation(client: Client, message: Message):
    emojis = ["🥺", "😔", "💔", "😞", "😢", "😭", "💭", "❤️‍🩹"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "I MISS YOU 💔"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# HAPPY 😄
@Client.on_message(filters.command("happy", ".") & filters.me)
async def happy_animation(client: Client, message: Message):
    emojis = ["😀", "😃", "😄", "😁", "😆", "😊", "🥰", "🤩"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "I’M SO HAPPY 😄💫"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# SAD 😢
@Client.on_message(filters.command("sad", ".") & filters.me)
async def sad_animation(client: Client, message: Message):
    emojis = ["😔", "😢", "😭", "💔", "😞", "🥺", "💧"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "FEELING SO SAD 💔"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# BUTTERFLY 🦋
@Client.on_message(filters.command("butterfly", ".") & filters.me)
async def butterfly_animation(client: Client, message: Message):
    emojis = ["🦋", "🌸", "💐", "🌷", "🌼", "🦋", "💮"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "FLY HIGH BEAUTIFUL 🦋💖"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# SPARKLE ✨
@Client.on_message(filters.command("sparkle", ".") & filters.me)
async def sparkle_animation(client: Client, message: Message):
    emojis = ["✨", "💫", "🌟", "⭐", "🌠", "🌌", "💖"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "YOU SHINE LIKE STARS ✨🌟"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# FIRE 🔥
@Client.on_message(filters.command("fire", ".") & filters.me)
async def fire_animation(client: Client, message: Message):
    emojis = ["🔥", "⚡", "💥", "🔥", "💣", "🔥"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "🔥 FIRE MODE ON 🔥"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)

# STAR 🌟
@Client.on_message(filters.command("star", ".") & filters.me)
async def star_animation(client: Client, message: Message):
    emojis = ["⭐", "🌟", "💫", "✨", "🌠", "🌌"]
    for e in emojis:
        await message.edit_text(e)
        await asyncio.sleep(0.3)
    text = "KEEP SHINING 🌟💫"
    display = ""
    for ch in text:
        display += ch
        await message.edit_text(display)
        await asyncio.sleep(0.2)
