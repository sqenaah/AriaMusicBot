frompyrogram.enumsimportChatType
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS,db
fromShrutiMusic.utils.databaseimport(
get_authuser_names,
get_cmode,
get_lang,
get_upvote_count,
is_active_chat,
is_maintenance,
is_nonadmin_chat,
is_skipmode,
)
fromconfigimportSUPPORT_GROUP,adminlist,confirmer
fromstringsimportget_string

from..formattersimportint_to_alpha


defAdminRightsCheck(mystic):
    asyncdefwrapper(client,message):
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
_=get_string(language)
except:
            _=get_string("en")
ifmessage.sender_chat:
            upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="ʜᴏᴡ ᴛᴏ ғɪx ?",
callback_data="AnonymousAdmin",
),
]
]
)
returnawaitmessage.reply_text(_["general_3"],reply_markup=upl)
ifmessage.command[0][0]=="c":
            chat_id=awaitget_cmode(message.chat.id)
ifchat_idisNone:
                returnawaitmessage.reply_text(_["setting_7"])
try:
                awaitapp.get_chat(chat_id)
except:
                returnawaitmessage.reply_text(_["cplay_4"])
else:
            chat_id=message.chat.id
ifnotawaitis_active_chat(chat_id):
            returnawaitmessage.reply_text(_["general_5"])
is_non_admin=awaitis_nonadmin_chat(message.chat.id)
ifnotis_non_admin:
            ifmessage.from_user.idnotinSUDOERS:
                admins=adminlist.get(message.chat.id)
ifnotadmins:
                    returnawaitmessage.reply_text(_["admin_13"])
else:
                    ifmessage.from_user.idnotinadmins:
                        ifawaitis_skipmode(message.chat.id):
                            upvote=awaitget_upvote_count(chat_id)
text=f"""<b>ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɴᴇᴇᴅᴇᴅ</b>

ʀᴇғʀᴇsʜ ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ᴠɪᴀ : /reload

» {upvote} ᴠᴏᴛᴇs ɴᴇᴇᴅᴇᴅ ғᴏʀ ᴘᴇʀғᴏʀᴍɪɴɢ ᴛʜɪs ᴀᴄᴛɪᴏɴ."""

command=message.command[0]
ifcommand[0]=="c":
                                command=command[1:]
ifcommand=="speed":
                                returnawaitmessage.reply_text(_["admin_14"])
MODE=command.title()
upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="ᴠᴏᴛᴇ",
callback_data=f"ADMIN  UpVote|{chat_id}_{MODE}",
),
]
]
)
ifchat_idnotinconfirmer:
                                confirmer[chat_id]={}
try:
                                vidid=db[chat_id][0]["vidid"]
file=db[chat_id][0]["file"]
except:
                                returnawaitmessage.reply_text(_["admin_14"])
senn=awaitmessage.reply_text(text,reply_markup=upl)
confirmer[chat_id][senn.id]={
"vidid":vidid,
"file":file,
}
return
else:
                            returnawaitmessage.reply_text(_["admin_14"])

returnawaitmystic(client,message,_,chat_id)

returnwrapper


defAdminActual(mystic):
    asyncdefwrapper(client,message):
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
_=get_string(language)
except:
            _=get_string("en")
ifmessage.sender_chat:
            upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="ʜᴏᴡ ᴛᴏ ғɪx ?",
callback_data="AnonymousAdmin",
),
]
]
)
returnawaitmessage.reply_text(_["general_3"],reply_markup=upl)
ifmessage.from_user.idnotinSUDOERS:
            try:
                member=(
awaitapp.get_chat_member(message.chat.id,message.from_user.id)
).privileges
except:
                return
ifnotmember.can_manage_video_chats:
                returnawaitmessage.reply(_["general_4"])
returnawaitmystic(client,message,_)

returnwrapper


defActualAdminCB(mystic):
    asyncdefwrapper(client,CallbackQuery):
        ifawaitis_maintenance()isFalse:
            ifCallbackQuery.from_user.idnotinSUDOERS:
                returnawaitCallbackQuery.answer(
f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
show_alert=True,
)
try:
            language=awaitget_lang(CallbackQuery.message.chat.id)
_=get_string(language)
except:
            _=get_string("en")
ifCallbackQuery.message.chat.type==ChatType.PRIVATE:
            returnawaitmystic(client,CallbackQuery,_)
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            try:
                a=(
awaitapp.get_chat_member(
CallbackQuery.message.chat.id,
CallbackQuery.from_user.id,
)
).privileges
except:
                returnawaitCallbackQuery.answer(_["general_4"],show_alert=True)
ifnota.can_manage_video_chats:
                ifCallbackQuery.from_user.idnotinSUDOERS:
                    token=awaitint_to_alpha(CallbackQuery.from_user.id)
_check=awaitget_authuser_names(CallbackQuery.from_user.id)
iftokennotin_check:
                        try:
                            returnawaitCallbackQuery.answer(
_["general_4"],
show_alert=True,
)
except:
                            return
returnawaitmystic(client,CallbackQuery,_)

returnwrapper
