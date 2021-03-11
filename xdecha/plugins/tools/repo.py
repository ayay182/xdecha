from xdecha import xdecha, Message, Config, versions, get_version


@xdecha.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
**Hey**, __I am using__ 🔥 **xdecha** 🔥

    __Durable as a Serge__

• **xdecha version** : `{get_version()}`
• **license** : {versions.__license__}
• **copyright** : {versions.__copyright__}
• **repo** : [xdecha]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
