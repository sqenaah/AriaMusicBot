utf-8utf-8





















importasyncio

frompyrogramimportenums,filters
frompyrogram.errorsimportFloodWait

fromShrutiMusicimportapp


@app.on_message(filters.command("bots")&filters.group)
asyncdefbots(client,message):

    try:
        botList=[]
asyncforbotinapp.get_chat_members(
message.chat.id,filter=enums.ChatMembersFilter.BOTS
):
            botList.append(bot.user)
lenBotList=len(botList)
text3=f"**ʙᴏᴛ ʟɪsᴛ - {message.chat.title}**\n\n🤖 ʙᴏᴛs\n"
whilelen(botList)>1:
            bot=botList.pop(0)
text3+=f"├ @{bot.username}\n"
else:
            bot=botList.pop(0)
text3+=f"└ @{bot.username}\n\n"
text3+=f"**ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ ʙᴏᴛs**: {lenBotList}**"
awaitapp.send_message(message.chat.id,text3)
exceptFloodWaitase:
        awaitasyncio.sleep(e.value)


__MODULE__="Bᴏᴛs"
__HELP__="""
**ʙᴏᴛs**

• /bots - ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ʙᴏᴛs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""












