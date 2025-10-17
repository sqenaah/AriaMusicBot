utf-8utf-8





















frompyrogram.enumsimportParseMode

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportis_on_off
fromconfigimportLOG_GROUP_ID


asyncdefplay_logs(message,streamtype):
    ifawaitis_on_off(2):
        logger_text=f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>
<b>ɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}

<b>ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
ifmessage.chat.id!=LOG_GROUP_ID:
            try:
                awaitapp.send_message(
chat_id=LOG_GROUP_ID,
text=logger_text,
parse_mode=ParseMode.HTML,
disable_web_page_preview=True,
)
except:
                pass
return












