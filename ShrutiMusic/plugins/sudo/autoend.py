utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportautoend_off,autoend_on,autoleave_off,autoleave_on,is_autoend,is_autoleave


@app.on_message(filters.command("autoend")&SUDOERS)
asyncdefauto_end_stream(_,message:Message):
    zerostate=awaitis_autoend()
usage=f"<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]\n\n Current state : {zerostate}"
iflen(message.command)!=2:
        returnawaitmessage.reply_text(usage)
state=message.text.split(None,1)[1].strip().lower()
ifstatein["enable","on","yes"]:
        awaitautoend_on()
awaitmessage.reply_text(
"» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғᴛᴇʀ ғᴇᴡ ᴍɪɴs ᴡʜᴇɴ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ."
)
elifstatein["disable","off","no"]:
        awaitautoend_off()
awaitmessage.reply_text("» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ.")
else:
        awaitmessage.reply_text(usage)

@app.on_message(filters.command("autoleave")&SUDOERS)
asyncdefauto_leave_chat(_,message:Message):
    zerostate=awaitis_autoleave()
usage=f"<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoleave [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]\n\n Current state : {zerostate}"
iflen(message.command)!=2:
        returnawaitmessage.reply_text(usage)
state=message.text.split(None,1)[1].strip().lower()
ifstatein["enable","on","yes"]:
        awaitautoleave_on()
awaitmessage.reply_text(
"» ᴀᴜᴛᴏ leave chat ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғᴛᴇʀ ғᴇᴡ ᴍɪɴs ᴡʜᴇɴ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ."
)
elifstatein["disable","off","no"]:
        awaitautoleave_off()
awaitmessage.reply_text("» ᴀᴜᴛᴏ leave chat ᴅɪsᴀʙʟᴇᴅ.")
else:
        awaitmessage.reply_text(usage)













