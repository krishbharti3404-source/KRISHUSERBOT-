from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# LOVE ANIMATION
@Client.on_message(filters.command("love", ".") & filters.me)
async def love_animation(client: Client, message: Message):
    animations = ["❤️", "💞", "💓", "💗", "💖", "💘", "💕", "💝", "💟", "❤️‍🔥"]
    for emoji in animations:
        await message.edit_text(emoji)
        await asyncio.sleep(0.3)
    await message.edit_text("I ❤️ YOU 😘")

# HEART ANIMATION
@Client.on_message(filters.command("heart", ".") & filters.me)
async def heart_animation(client: Client, message: Message):
    hearts = ["💓", "💗", "💖", "💘", "💝", "💞"]
    for h in hearts:
        await message.edit_text(h)
        await asyncio.sleep(0.3)

# MOON ANIMATION
@Client.on_message(filters.command("moon", ".") & filters.me)
async def moon_animation(client: Client, message: Message):
    moons = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    for m in moons:
        await message.edit_text(m)
        await asyncio.sleep(0.3)

# SPARKLE
@Client.on_message(filters.command("sparkle", ".") & filters.me)
async def sparkle_animation(client: Client, message: Message):
    sparkles = ["✨", "💫", "🌟", "⭐", "🌠"]
    for s in sparkles:
        await message.edit_text(s)
        await asyncio.sleep(0.3)

# FIRE
@Client.on_message(filters.command("fire", ".") & filters.me)
async def fire_animation(client: Client, message: Message):
    flames = ["🔥", "⚡", "💥", "🔥", "💣", "🔥"]
    for f in flames:
        await message.edit_text(f)
        await asyncio.sleep(0.3)
    await message.edit_text("🔥 FIRE MODE ON 🔥")

# THUNDER
@Client.on_message(filters.command("thunder", ".") & filters.me)
async def thunder_animation(client: Client, message: Message):
    bolts = ["🌩️", "⚡", "🌩️⚡", "⛈️", "⚡⚡"]
    for b in bolts:
        await message.edit_text(b)
        await asyncio.sleep(0.3)
    await message.edit_text("⚡ THUNDER STRIKE ⚡")

# STAR
@Client.on_message(filters.command("star", ".") & filters.me)
async def star_animation(client: Client, message: Message):
    stars = ["⭐", "🌟", "💫", "✨", "🌠", "🌌"]
    for s in stars:
        await message.edit_text(s)
        await asyncio.sleep(0.3)

# FLOWER
@Client.on_message(filters.command("flower", ".") & filters.me)
async def flower_animation(client: Client, message: Message):
    flowers = ["🌹", "🌸", "🌷", "🌼", "🌻", "💐"]
    for f in flowers:
        await message.edit_text(f)
        await asyncio.sleep(0.3)
    await message.edit_text("🌸 Beautiful like you 🌸")
