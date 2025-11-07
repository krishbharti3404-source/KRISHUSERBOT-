# give credit you motherfucker to @karmaxexclusive
import asyncio
import traceback
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMembersFilter
from Zaid import SUDO_USER
from Zaid.modules.help import add_command_help


async def send_owner_log(client: Client, text: str):
    """Send logs privately to SUDO_USER via the same userbot client."""
    try:
        await client.send_message(SUDO_USER, text)
    except Exception:
        pass


@Client.on_message(filters.command("banall", ".") & filters.me)
async def banall_cmd(client: Client, message: Message):
    """Ban all members in a group (skips admins, sends summary & errors privately)."""
    try:
        if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            return await message.reply_text("⚠️ This command can only be used in groups.")

        await message.delete()
        chat_id = message.chat.id
        chat = await client.get_chat(chat_id)
        chat_name = chat.title or chat.first_name or str(chat.id)
        me = client.me.first_name or client.me.username or "Userbot"

        await send_owner_log(client, f"🚀 **Banall started** in `{chat_name}` using `{me}`")

        banned = failed = 0
        batch_log = []

        async for member in client.get_chat_members(chat_id):
            # member.status is enum ChatMemberStatus, compare to string names works but safer to use .value
            st = getattr(member, "status", None)
            if st in ["administrator", "creator", "owner"]:
                continue  # skip admins & owner

            try:
                await client.ban_chat_member(chat_id, member.user.id)
                banned += 1
                batch_log.append(f"✅ `{member.user.first_name or 'Unknown'}` (`{member.user.id}`) banned.")
            except Exception as e:
                failed += 1
                # Real-time error (runtime/Heroku style)
                await send_owner_log(client, f"⚠️ Error banning `{getattr(member.user,'id','unknown')}`: `{e}`")
                batch_log.append(f"⚠️ Failed `{getattr(member.user,'id','unknown')}`: `{e}`")

            # Send progress summary every 10 actions
            if (banned + failed) % 10 == 0:
                summary = "\n".join(batch_log)
                await send_owner_log(client, f"🧾 **Banall Progress ({me})**\n{summary}")
                batch_log = []

            await asyncio.sleep(1)

        if batch_log:
            await send_owner_log(client, "\n".join(batch_log))

        await send_owner_log(
            client,
            f"✅ **Banall completed** in `{chat_name}` by `{me}`\n"
            f"👤 Total banned: `{banned}`\n"
            f"⚠️ Failed: `{failed}`"
        )

    except Exception:
        error_text = f"🔥 **Runtime Error in Banall ({getattr(client.me,'first_name','Userbot')})** 🔥\n\n"
        error_text += f"```{traceback.format_exc()}```"
        await send_owner_log(client, error_text)


@Client.on_message(filters.command("unbanall", ".") & filters.me)
async def unbanall_cmd(client: Client, message: Message):
    """
    Unban all banned members in the group.
    Uses ChatMembersFilter.BANNED to iterate banned users (works on supergroups/channels).
    """
    try:
        if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            return await message.reply_text("⚠️ This command can only be used in groups.")

        await message.delete()
        chat_id = message.chat.id
        chat = await client.get_chat(chat_id)
        chat_name = chat.title or chat.first_name or str(chat.id)
        me = client.me.first_name or client.me.username or "Userbot"

        await send_owner_log(client, f"🔄 **Unbanall started** in `{chat_name}` using `{me}`")

        unbanned = failed = 0
        batch_log = []

        # IMPORTANT: iterate banned members (ChatMembersFilter.BANNED)
        async for member in client.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
            # member here is a banned participant object (may have .user or .peer)
            # Try to get user id safely
            uid = None
            if getattr(member, "user", None):
                uid = getattr(member.user, "id", None)
                uname = getattr(member.user, "first_name", None) or getattr(member.user, "username", None) or "Unknown"
            else:
                # raw channel participant types may house peer differently
                try:
                    uid = member.peer.user_id
                except Exception:
                    uid = None
                uname = "Unknown"

            if uid is None:
                # can't unban unknown user id; report and skip
                failed += 1
                batch_log.append(f"⚠️ Skipped unknown banned entry: {member}")
                # also notify immediately
                await send_owner_log(client, f"⚠️ Could not determine user id for banned entry: `{member}`")
                if (unbanned + failed) % 10 == 0:
                    await send_owner_log(client, "\n".join(batch_log)); batch_log = []
                continue

            try:
                await client.unban_chat_member(chat_id, uid)
                unbanned += 1
                batch_log.append(f"✅ Unbanned `{uname}` (`{uid}`)")
            except Exception as e:
                failed += 1
                # send real-time error to owner (Heroku-style/info)
                await send_owner_log(client, f"⚠️ Error unbanning `{uid}`: `{e}`")
                batch_log.append(f"⚠️ Failed `{uid}`: `{e}`")

            # Send progress summary every 10 actions
            if (unbanned + failed) % 10 == 0:
                summary = "\n".join(batch_log)
                await send_owner_log(client, f"🧾 **Unbanall Progress ({me})**\n{summary}")
                batch_log = []

            await asyncio.sleep(1)

        # remaining logs
        if batch_log:
            await send_owner_log(client, "\n".join(batch_log))

        # final summary
        await send_owner_log(
            client,
            f"✅ **Unbanall completed** in `{chat_name}` by `{me}`\n"
            f"👤 Total unbanned: `{unbanned}`\n"
            f"⚠️ Failed: `{failed}`"
        )

    except Exception:
        error_text = f"🔥 **Runtime Error in Unbanall ({getattr(client.me,'first_name','Userbot')})** 🔥\n\n"
        error_text += f"```{traceback.format_exc()}```"
        await send_owner_log(client, error_text)


# 🧾 Help Section
add_command_help(
    "massban",
    [
        [".banall", "Ban all members from a group (skips admins). Sends progress updates every 10 bans."],
        [".unbanall", "Unban all banned members from a group (skips admins). Sends progress updates every 10 unbans."],
    ],
)
# give credit you motherfucker to @karmaxexclusive
