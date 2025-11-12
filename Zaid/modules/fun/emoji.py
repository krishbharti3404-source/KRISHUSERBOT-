from pyrogram import Client, filters
# 💞 Romantic Animated Emoji Commands
@Client.on_message(filters.command("love", ".") & filters.me)
async def love_animation(bot: Client, message: Message):
    texts = [
        "I 💖",
        "I 💖 Y",
        "I 💖 YO",
        "I 💖 YOU",
        "I 💖 YOU 💫",
        "I 💖 YOU 💞",
        "I 💖 YOU 💖",
        "I 💖 YOU FOREVER 💞",
    ]
    try:
        for t in texts:
            await message.edit(t)
            await asyncio.sleep(0.4)
        for _ in range(6):
            await message.edit("💞💓💗💖💘💝💞💓💗💖💘💝")
            await asyncio.sleep(0.3)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("sparkheart", ".") & filters.me)
async def sparkheart(bot: Client, message: Message):
    seq = [
        "❤️‍🔥",
        "💖",
        "💞",
        "💓",
        "💘 Burning Love ❤️‍🔥",
        "💖❤️‍🔥💞💘",
        "🔥 LOVE ON FIRE 🔥",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.4)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("brokenheart", ".") & filters.me)
async def brokenheart(bot: Client, message: Message):
    seq = [
        "💔",
        "💔💔",
        "💔 Broken 💔",
        "💔 Heart 💔",
        "❤️‍🩹 Healing ❤️‍🩹",
        "❤️‍🩹❤️‍🩹❤️‍🩹",
        "❤️ Healed ❤️",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.6)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("beatingheart", ".") & filters.me)
async def beatingheart(bot: Client, message: Message):
    seq = [
        "💓",
        "💗",
        "💖",
        "💞",
        "💓 Beating...",
        "💗💖💗💖",
        "💓💓💓💓💓",
        "💖💖💖💖💖",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.3)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("rainbowheart", ".") & filters.me)
async def rainbowheart(bot: Client, message: Message):
    seq = [
        "❤️🧡💛💚💙💜",
        "🧡💛💚💙💜❤️",
        "💛💚💙💜❤️🧡",
        "💚💙💜❤️🧡💛",
        "💙💜❤️🧡💛💚",
        "💜❤️🧡💛💚💙",
        "🌈 Love in Colors 🌈",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.4)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("fireheart", ".") & filters.me)
async def fireheart(bot: Client, message: Message):
    seq = [
        "🔥❤️🔥",
        "❤️‍🔥🔥❤️‍🔥",
        "🔥 Burning Heart ❤️‍🔥",
        "🔥❤️🔥❤️🔥❤️🔥",
        "❤️‍🔥 I’m on Fire ❤️‍🔥",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.4)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("kiss", ".") & filters.me)
async def kiss(bot: Client, message: Message):
    seq = [
        "😘",
        "😚",
        "😙",
        "💋",
        "💋 Muah 💋",
        "😘💋😘💋😘",
        "💞 Kiss Sent 💞",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.5)
    except Exception:
        await message.delete()


@Client.on_message(filters.command("missyou", ".") & filters.me)
async def missyou(bot: Client, message: Message):
    seq = [
        "😔",
        "🥺",
        "💭 Thinking of You 💭",
        "💌 I Miss You 💌",
        "💞💭💞💭💞",
        "💔 Come Back Soon 💔",
    ]
    try:
        for s in seq:
            await message.edit(s)
            await asyncio.sleep(0.5)
    except Exception:
        await message.delete()
