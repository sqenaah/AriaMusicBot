utf-8utf-8





















importos
frompyrogramimportClient,filters
frompyrogram.errorsimportFloodWait
frompyrogram.typesimportMessage
fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
frompyrogram.enumsimportChatMemberStatus
importasyncio




@app.on_message(filters.command("leave")&SUDOERS)
asyncdefleave(_,message):
    iflen(message.command)!=2:
        returnawaitmessage.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ɢʀᴏᴜᴘ ɪᴅ. ᴜsᴇ ʟɪᴋᴇ: /leave chat_id.")
try:
        chat_id=int(message.command[1])
exceptValueError:
        returnawaitmessage.reply_text(f"ɪɴᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ. ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ɴᴜᴍᴇʀɪᴄ ɪᴅ.")
CHAMPU=awaitmessage.reply_text(f"ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛ... {app.me.mention}")
try:
        awaitapp.send_message(chat_id,f"{app.me.mention} ʟᴇғᴛɪɴɢ ᴄʜᴀᴛ ʙʏᴇ...")
awaitapp.leave_chat(chat_id)
awaitCHAMPU.edit(f"{app.me.mention} ʟᴇғᴛ ᴄʜᴀᴛ {chat_id}.")
exceptExceptionase:
        pass



@app.on_message(filters.command("givelink"))
asyncdefgive_link_command(client,message):

    chat=message.chat.id
link=awaitapp.export_chat_invite_link(chat)
awaitmessage.reply_text(f"ʜᴇʀᴇ's ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ:\n{link}")


@app.on_message(
filters.command(
["link","invitelink"],prefixes=["/","!","%",",","",".","@","#"]
)
&SUDOERS
)
asyncdeflink_command_handler(client:Client,message:Message):
    iflen(message.command)!=2:
        awaitmessage.reply("ɪɴᴠᴀʟɪᴅ ᴜsᴀɢᴇ. ᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ: /link group_id")
return

group_id=message.command[1]
file_name=f"group_info_{group_id}.txt"

try:
        chat=awaitclient.get_chat(int(group_id))

ifchatisNone:
            awaitmessage.reply("ᴜɴᴀʙʟᴇ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢʀᴏᴜᴘ ɪᴅ.")
return

try:
            invite_link=awaitclient.export_chat_invite_link(chat.id)
exceptFloodWaitase:
            awaitmessage.reply(f"ғʟᴏᴏᴅᴡᴀɪᴛ: {e.x} sᴇᴄᴏɴᴅs. ʀᴇᴛʀʏɪɴɢ ɪɴ {e.x} sᴇᴄᴏɴᴅs.")
return

group_data={
"ɪᴅ":chat.id,
"ᴛʏᴘᴇ":str(chat.type),
"ᴛɪᴛʟᴇ":chat.title,
"ᴍᴇᴍʙᴇʀs_ᴄᴏᴜɴᴛ":chat.members_count,
"ᴅᴇsᴄʀɪᴘᴛɪᴏɴ":chat.description,
"ɪɴᴠɪᴛᴇ_ʟɪɴᴋ":invite_link,
"ɪs_ᴠᴇʀɪғɪᴇᴅ":chat.is_verified,
"ɪs_ʀᴇsᴛʀɪᴄᴛᴇᴅ":chat.is_restricted,
"ɪs_ᴄʀᴇᴀᴛᴏʀ":chat.is_creator,
"ɪs_sᴄᴀᴍ":chat.is_scam,
"ɪs_ғᴀᴋᴇ":chat.is_fake,
"ᴅᴄ_ɪᴅ":chat.dc_id,
"ʜᴀs_ᴘʀᴏᴛᴇᴄᴛᴇᴅ_ᴄᴏɴᴛᴇɴᴛ":chat.has_protected_content,
}

withopen(file_name,"w",encoding="utf-8")asfile:
            forkey,valueingroup_data.items():
                file.write(f"{key}: {value}\n")

awaitclient.send_document(
chat_id=message.chat.id,
document=file_name,
caption=f"ʜᴇʀᴇ ɪs ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ\n{chat.title}\nᴛʜᴇ ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ sᴄʀᴀᴘᴇᴅ ʙʏ : @{app.username}",
)

exceptExceptionase:
        awaitmessage.reply(f"Error: {str(e)}")

finally:
        ifos.path.exists(file_name):
            os.remove(file_name)


__MODULE__="Gʀᴏᴜᴘ Lɪɴᴋ"
__HELP__="""
- `/givelink`: Gᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.
- `/link ɢʀᴏᴜᴘ_ɪᴅ`: Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢʀᴏᴜᴘ ID.
"""












