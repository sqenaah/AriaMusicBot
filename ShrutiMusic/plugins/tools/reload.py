utf-8utf-8





















importasyncio
importtime

frompyrogramimportfilters
frompyrogram.enumsimportChatMembersFilter
frompyrogram.typesimportCallbackQuery,Message

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportdb
fromShrutiMusic.utils.databaseimportget_assistant,get_authuser_names,get_cmode
fromShrutiMusic.utils.decoratorsimportActualAdminCB,AdminActual,language
fromShrutiMusic.utils.formattersimportalpha_to_int,get_readable_time
fromconfigimportBANNED_USERS,adminlist,lyrical

rel={}


@app.on_message(
filters.command(["admincache","reload","refresh"])&filters.group&~BANNED_USERS
)
@language
asyncdefreload_admin_cache(client,message:Message,_):
    try:
        ifmessage.chat.idnotinrel:
            rel[message.chat.id]={}
else:
            saved=rel[message.chat.id]
ifsaved>time.time():
                left=get_readable_time((int(saved)-int(time.time())))
returnawaitmessage.reply_text(_["reload_1"].format(left))
adminlist[message.chat.id]=[]
asyncforuserinapp.get_chat_members(
message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
):
            ifuser.privileges.can_manage_video_chats:
                adminlist[message.chat.id].append(user.user.id)
authusers=awaitget_authuser_names(message.chat.id)
foruserinauthusers:
            user_id=awaitalpha_to_int(user)
adminlist[message.chat.id].append(user_id)
now=int(time.time())+180
rel[message.chat.id]=now
awaitmessage.reply_text(_["reload_2"])
except:
        awaitmessage.reply_text(_["reload_3"])


@app.on_message(filters.command(["reboot"])&filters.group&~BANNED_USERS)
@AdminActual
asyncdefrestartbot(client,message:Message,_):
    mystic=awaitmessage.reply_text(_["reload_4"].format(app.mention))
awaitasyncio.sleep(1)
try:
        db[message.chat.id]=[]
awaitNand.stop_stream_force(message.chat.id)
except:
        pass
userbot=awaitget_assistant(message.chat.id)
try:
        ifmessage.chat.username:
            awaituserbot.resolve_peer(message.chat.username)
else:
            awaituserbot.resolve_peer(message.chat.id)
except:
        pass
chat_id=awaitget_cmode(message.chat.id)
ifchat_id:
        try:
            got=awaitapp.get_chat(chat_id)
except:
            pass
userbot=awaitget_assistant(chat_id)
try:
            ifgot.username:
                awaituserbot.resolve_peer(got.username)
else:
                awaituserbot.resolve_peer(chat_id)
except:
            pass
try:
            db[chat_id]=[]
awaitNand.stop_stream_force(chat_id)
except:
            pass
returnawaitmystic.edit_text(_["reload_5"].format(app.mention))


@app.on_callback_query(filters.regex("close")&~BANNED_USERS)
asyncdefclose_menu(_,CallbackQuery):
    try:
        awaitCallbackQuery.answer()
awaitCallbackQuery.message.delete()
awaitCallbackQuery.message.reply_text(
f"Cʟᴏsᴇᴅ ʙʏ : {CallbackQuery.from_user.mention}"
)
except:
        pass


@app.on_callback_query(filters.regex("stop_downloading")&~BANNED_USERS)
@ActualAdminCB
asyncdefstop_download(client,CallbackQuery:CallbackQuery,_):
    message_id=CallbackQuery.message.id
task=lyrical.get(message_id)
ifnottask:
        returnawaitCallbackQuery.answer(_["tg_4"],show_alert=True)
iftask.done()ortask.cancelled():
        returnawaitCallbackQuery.answer(_["tg_5"],show_alert=True)
ifnottask.done():
        try:
            task.cancel()
try:
                lyrical.pop(message_id)
except:
                pass
awaitCallbackQuery.answer(_["tg_6"],show_alert=True)
returnawaitCallbackQuery.edit_message_text(
_["tg_7"].format(CallbackQuery.from_user.mention)
)
except:
            returnawaitCallbackQuery.answer(_["tg_8"],show_alert=True)
awaitCallbackQuery.answer(_["tg_9"],show_alert=True)












