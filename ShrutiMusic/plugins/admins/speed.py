utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportSUDOERS,db
fromShrutiMusic.utilsimportAdminRightsCheck
fromShrutiMusic.utils.databaseimportis_active_chat,is_nonadmin_chat
fromShrutiMusic.utils.decorators.languageimportlanguageCB
fromShrutiMusic.utils.inlineimportclose_markup,speed_markup
fromconfigimportBANNED_USERS,adminlist

checker=[]


@app.on_message(
filters.command(["cspeed","speed","cslow","slow","playback","cplayback"])
&filters.group
&~BANNED_USERS
)
@AdminRightsCheck
asyncdefplayback(cli,message:Message,_,chat_id):
    playing=db.get(chat_id)
ifnotplaying:
        returnawaitmessage.reply_text(_["queue_2"])
duration_seconds=int(playing[0]["seconds"])
ifduration_seconds==0:
        returnawaitmessage.reply_text(_["admin_27"])
file_path=playing[0]["file"]
if"downloads"notinfile_path:
        returnawaitmessage.reply_text(_["admin_27"])
upl=speed_markup(_,chat_id)
returnawaitmessage.reply_text(
text=_["admin_28"].format(app.mention),
reply_markup=upl,
)


@app.on_callback_query(filters.regex("SpeedUP")&~BANNED_USERS)
@languageCB
asyncdefdel_back_playlist(client,CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
callback_request=callback_data.split(None,1)[1]
chat,speed=callback_request.split("|")
chat_id=int(chat)
ifnotawaitis_active_chat(chat_id):
        returnawaitCallbackQuery.answer(_["general_5"],show_alert=True)
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
        ifCallbackQuery.from_user.idnotinSUDOERS:
            admins=adminlist.get(CallbackQuery.message.chat.id)
ifnotadmins:
                returnawaitCallbackQuery.answer(_["admin_13"],show_alert=True)
else:
                ifCallbackQuery.from_user.idnotinadmins:
                    returnawaitCallbackQuery.answer(_["admin_14"],show_alert=True)
playing=db.get(chat_id)
ifnotplaying:
        returnawaitCallbackQuery.answer(_["queue_2"],show_alert=True)
duration_seconds=int(playing[0]["seconds"])
ifduration_seconds==0:
        returnawaitCallbackQuery.answer(_["admin_27"],show_alert=True)
file_path=playing[0]["file"]
if"downloads"notinfile_path:
        returnawaitCallbackQuery.answer(_["admin_27"],show_alert=True)
checkspeed=(playing[0]).get("speed")
ifcheckspeed:
        ifstr(checkspeed)==str(speed):
            ifstr(speed)==str("1.0"):
                returnawaitCallbackQuery.answer(
_["admin_29"],
show_alert=True,
)
else:
        ifstr(speed)==str("1.0"):
            returnawaitCallbackQuery.answer(
_["admin_29"],
show_alert=True,
)
ifchat_idinchecker:
        returnawaitCallbackQuery.answer(
_["admin_30"],
show_alert=True,
)
else:
        checker.append(chat_id)
try:
        awaitCallbackQuery.answer(
_["admin_31"],
)
except:
        pass
mystic=awaitCallbackQuery.edit_message_text(
text=_["admin_32"].format(CallbackQuery.from_user.mention),
)
try:
        awaitNand.speedup_stream(
chat_id,
file_path,
speed,
playing,
)
except:
        ifchat_idinchecker:
            checker.remove(chat_id)
returnawaitmystic.edit_text(_["admin_33"],reply_markup=close_markup(_))
ifchat_idinchecker:
        checker.remove(chat_id)
awaitmystic.edit_text(
text=_["admin_34"].format(speed,CallbackQuery.from_user.mention),
reply_markup=close_markup(_),
)












