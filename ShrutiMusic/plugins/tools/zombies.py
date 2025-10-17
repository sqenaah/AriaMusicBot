utf-8utf-8





















importasyncio

frompyrogramimportfilters
frompyrogram.enumsimportChatMemberStatus
frompyrogram.errorsimportFloodWait
fromShrutiMusicimportapp
fromShrutiMusic.utils.permissionsimportadminsOnly

chatQueue=[]

stopProcess=False


@app.on_message(filters.command(["zombies"]))
@adminsOnly("can_restrict_members")
asyncdefremove(client,message):

    globalstopProcess
try:
        try:
            sender=awaitapp.get_chat_member(message.chat.id,message.from_user.id)
has_permissions=sender.privileges
exceptBaseException:
            has_permissions=message.sender_chat
ifhas_permissions:
            bot=awaitapp.get_chat_member(message.chat.id,"self")
ifbot.status==ChatMemberStatus.MEMBER:
                awaitmessage.reply(
"➠ | ɪ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs."
)
else:
                iflen(chatQueue)>30:
                    awaitmessage.reply(
"➠ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 30 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
)
else:
                    ifmessage.chat.idinchatQueue:
                        awaitmessage.reply(
"➠ | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢɪɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ [ /stop ] ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
)
else:
                        chatQueue.append(message.chat.id)
deletedList=[]
asyncformemberinapp.get_chat_members(message.chat.id):
                            ifmember.user.is_deleted==True:
                                deletedList.append(member.user)
else:
                                pass
lenDeletedList=len(deletedList)
iflenDeletedList==0:
                            awaitmessage.reply("⟳ | ɴᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.")
chatQueue.remove(message.chat.id)
else:
                            k=0
processTime=lenDeletedList*1
temp=awaitapp.send_message(
message.chat.id,
f"🧭 | ᴛᴏᴛᴀʟ ᴏғ {lenDeletedList} ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ʜᴀs ʙᴇᴇɴ ᴅᴇᴛᴇᴄᴛᴇᴅ.\n🥀 | ᴇsᴛɪᴍᴀᴛᴇᴅ ᴛɪᴍᴇ: {processTime} sᴇᴄᴏɴᴅs ғʀᴏᴍ ɴᴏᴡ.",
)
ifstopProcess:
                                stopProcess=False
whilelen(deletedList)>0andnotstopProcess:
                                deletedAccount=deletedList.pop(0)
try:
                                    awaitapp.ban_chat_member(
message.chat.id,deletedAccount.id
)
exceptFloodWaitase:
                                    awaitasyncio.sleep(e.value)
exceptException:
                                    pass
k+=1
ifk==lenDeletedList:
                                awaitmessage.reply(
f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ᴀʟʟ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄɪᴜɴᴛs ғʀᴏᴍ ᴛʜɪs ᴄʜᴀᴛ."
)
awaittemp.delete()
else:
                                awaitmessage.reply(
f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ {k} ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ ᴛʜɪs ᴄʜᴀᴛ."
)
awaittemp.delete()
chatQueue.remove(message.chat.id)
else:
            awaitmessage.reply(
"👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴ** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ."
)
exceptFloodWaitase:
        awaitasyncio.sleep(e.value)


__MODULE__="Zᴏᴍʙɪᴇs"
__HELP__="""
**commands:**
- /zombies: ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.

**info:**
- ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs
- ᴅᴇsᴄʀɪᴘᴛɪᴏɴ: ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.
- ᴄᴏᴍᴍᴀɴᴅs: /zombies
- ᴘᴇʀᴍɪssɪᴏɴs ɴᴇᴇᴅᴇᴅ: ᴄᴀɴ ʀᴇsᴛʀɪᴄᴛ ᴍᴇᴍʙᴇʀs

**note:**
- ᴜsᴇ ᴅɪʀᴇᴄᴛʟʏ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ғᴏʀ ʙᴇsᴛ ᴇғғᴇᴄᴛ. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ."""












