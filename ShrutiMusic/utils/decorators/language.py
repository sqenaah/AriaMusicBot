fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportget_lang,is_maintenance
fromconfigimportSUPPORT_GROUP
fromstringsimportget_string


deflanguage(mystic):
    asyncdefwrapper(_,message,**kwargs):
        ifawaitis_maintenance()isFalse:
            ifmessage.from_user.idnotinSUDOERS:
                returnawaitmessage.reply_text(
text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_GROUP}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
disable_web_page_preview=True,
)
try:
            awaitmessage.delete()
except:
            pass

try:
            language=awaitget_lang(message.chat.id)
language=get_string(language)
except:
            language=get_string("en")
returnawaitmystic(_,message,language)

returnwrapper


deflanguageCB(mystic):
    asyncdefwrapper(_,CallbackQuery,**kwargs):
        ifawaitis_maintenance()isFalse:
            ifCallbackQuery.from_user.idnotinSUDOERS:
                returnawaitCallbackQuery.answer(
f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
show_alert=True,
)
try:
            language=awaitget_lang(CallbackQuery.message.chat.id)
language=get_string(language)
except:
            language=get_string("en")
returnawaitmystic(_,CallbackQuery,language)

returnwrapper


defLanguageStart(mystic):
    asyncdefwrapper(_,message,**kwargs):
        try:
            language=awaitget_lang(message.chat.id)
language=get_string(language)
except:
            language=get_string("en")
returnawaitmystic(_,message,language)

returnwrapper
