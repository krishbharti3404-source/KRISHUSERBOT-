import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# Logging setup (same as original)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("banall", ".") & filters.group)
async def banall(bot: Client, message: Message):
    """
    Ban all members in the group.
    Command: .banall
    """
    try:
        await message.delete()
        chat_id = message.chat.id
        logging.info(f"Fetching members from chat {chat_id}")

        async for member in bot.iter_chat_members(chat_id):
            try:
                await bot.ban_chat_member(chat_id, member.user.id)
                logging.info(f"Banned {member.user.id} from {chat_id}")
            except Exception as e:
                logging.warning(f"Failed to ban {member.user.id}: {e}")

        logging.info(f"Banall completed in chat {chat_id}")
        await message.reply_text("✅ **Banall completed successfully.**")

    except Exception as e:
        logging.error(f"Error in banall: {e}")
        await message.reply_text(f"❌ Error: `{e}`")
