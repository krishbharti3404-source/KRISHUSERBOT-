from Zaid import app, API_ID, API_HASH 
from pyrogram import Client, filters
from pyrogram.types import Message

# ========== CLONE COMMAND ==========

@app.on_message(filters.command("clone"))
async def clone_cmd(_, msg: Message):

    if len(msg.command) == 1:
        return await msg.reply(
            "❌ Please provide session string.\n\n"
            "**Usage:**\n`/clone <SESSION_STRING>`"
        )

    session = msg.command[1]

    text = await msg.reply("🚀 Booting your client...")

    try:
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="Zaid/modules")
        )

        await client.start()
        user = await client.get_me()

        await text.edit(
            f"✅ Client Started Successfully as **{user.first_name}!**"
        )

    except Exception as e:
        await text.edit(f"❌ ERROR: `{e}`")
