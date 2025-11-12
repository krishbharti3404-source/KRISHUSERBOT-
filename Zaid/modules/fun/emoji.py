from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


async def safe_edit(message: Message, text: str):
    """Safely edits a message, skipping if same content."""
    try:
        if message.text != text:
            await message.edit_text(text)
    except Exception:
        pass


@Client.on_message(filters.command("love", ".") & filters.me)
async def love_animation(client: Client, message: Message):
    animations = ["❤️", "💞", "💓", "💗", "💖", "💘", "💕", "💝", "💟", "❤️‍🔥"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "I ❤️ YOU 😘")


@Client.on_message(filters.command("missyou", ".") & filters.me)
async def missyou_animation(client: Client, message: Message):
    animations = ["😔", "🥺", "💔", "😭", "💭", "🦋", "✨", "😞", "💌", "🤍"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "I MISS YOU 💔😔")


@Client.on_message(filters.command("happy", ".") & filters.me)
async def happy_animation(client: Client, message: Message):
    animations = ["😁", "😄", "😆", "😃", "😊", "😇", "🤗", "🥰", "✨", "💫"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "KEEP SMILING 😄💛")


@Client.on_message(filters.command("sad", ".") & filters.me)
async def sad_animation(client: Client, message: Message):
    animations = ["😢", "😭", "🥺", "💔", "😞", "😣", "😔", "😫", "😩", "💭"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "I'M JUST SAD 😢")


@Client.on_message(filters.command("butterfly", ".") & filters.me)
async def butterfly_animation(client: Client, message: Message):
    animations = ["🦋", "🌸", "💐", "🌷", "🌼", "🌻", "🌺", "🍃", "✨", "💫"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "FLY HIGH 🦋💖")


@Client.on_message(filters.command("sparkle", ".") & filters.me)
async def sparkle_animation(client: Client, message: Message):
    animations = ["✨", "💫", "🌟", "⚡", "🌠", "🌈", "💥", "🔥", "🌌", "⭐"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "SHINE BRIGHT ✨💫")


@Client.on_message(filters.command("heart", ".") & filters.me)
async def heart_animation(client: Client, message: Message):
    animations = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💖"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "HEARTS EVERYWHERE 💖")


@Client.on_message(filters.command("dream", ".") & filters.me)
async def dream_animation(client: Client, message: Message):
    animations = ["💭", "🌙", "⭐", "✨", "🌌", "🌠", "🌜", "🌛", "💫", "🌃"]
    for emoji in animations:
        await safe_edit(message, emoji)
        await asyncio.sleep(0.3)
    await safe_edit(message, "DREAM BIG 🌙💭")
