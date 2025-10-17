utf-8utf-8





















importasyncio
importos

frompyrogramimportfilters
frompyrogram.errorsimportFloodWait
frompyrogram.typesimportCallbackQuery,InputMediaPhoto,Message

importconfig
fromShrutiMusicimportapp
fromShrutiMusic.miscimportdb
fromShrutiMusic.utilsimportNandBin,get_channeplayCB,seconds_to_min
fromShrutiMusic.utils.databaseimportget_cmode,is_active_chat,is_music_playing
fromShrutiMusic.utils.decorators.languageimportlanguage,languageCB
fromShrutiMusic.utils.inlineimportqueue_back_markup,queue_markup
fromconfigimportBANNED_USERS

basic={}


defget_image(videoid):
    ifos.path.isfile(f"cache/{videoid}.png"):
        returnf"cache/{videoid}.png"
else:
        returnconfig.YOUTUBE_IMG_URL


defget_duration(playing):
    file_path=playing[0]["file"]
if"index_"infile_pathor"live_"infile_path:
        return"Unknown"
duration_seconds=int(playing[0]["seconds"])
ifduration_seconds==0:
        return"Unknown"
else:
        return"Inline"


@app.on_message(
filters.command(["queue","cqueue","player","cplayer","playing","cplaying"])
&filters.group
&~BANNED_USERS
)
@language
asyncdefget_queue(client,message:Message,_):
    ifmessage.command[0][0]=="c":
        chat_id=awaitget_cmode(message.chat.id)
ifchat_idisNone:
            returnawaitmessage.reply_text(_["setting_7"])
try:
            awaitapp.get_chat(chat_id)
except:
            returnawaitmessage.reply_text(_["cplay_4"])
cplay=True
else:
        chat_id=message.chat.id
cplay=False
ifnotawaitis_active_chat(chat_id):
        returnawaitmessage.reply_text(_["general_5"])
got=db.get(chat_id)
ifnotgot:
        returnawaitmessage.reply_text(_["queue_2"])
file=got[0]["file"]
videoid=got[0]["vidid"]
user=got[0]["by"]
title=(got[0]["title"]).title()
typo=(got[0]["streamtype"]).title()
DUR=get_duration(got)
if"live_"infile:
        IMAGE=get_image(videoid)
elif"vid_"infile:
        IMAGE=get_image(videoid)
elif"index_"infile:
        IMAGE=config.STREAM_IMG_URL
else:
        ifvideoid=="telegram":
            IMAGE=(
config.TELEGRAM_AUDIO_URL
iftypo=="Audio"
elseconfig.TELEGRAM_VIDEO_URL
)
elifvideoid=="soundcloud":
            IMAGE=config.SOUNCLOUD_IMG_URL
else:
            IMAGE=get_image(videoid)
send=_["queue_6"]ifDUR=="Unknown"else_["queue_7"]
cap=_["queue_8"].format(app.mention,title,typo,user,send)
upl=(
queue_markup(_,DUR,"c"ifcplayelse"g",videoid)
ifDUR=="Unknown"
elsequeue_markup(
_,
DUR,
"c"ifcplayelse"g",
videoid,
seconds_to_min(got[0]["played"]),
got[0]["dur"],
)
)
basic[videoid]=True
mystic=awaitmessage.reply_photo(IMAGE,caption=cap,reply_markup=upl)
ifDUR!="Unknown":
        try:
            whiledb[chat_id][0]["vidid"]==videoid:
                awaitasyncio.sleep(5)
ifawaitis_active_chat(chat_id):
                    ifbasic[videoid]:
                        ifawaitis_music_playing(chat_id):
                            try:
                                buttons=queue_markup(
_,
DUR,
"c"ifcplayelse"g",
videoid,
seconds_to_min(db[chat_id][0]["played"]),
db[chat_id][0]["dur"],
)
awaitmystic.edit_reply_markup(reply_markup=buttons)
exceptFloodWait:
                                pass
else:
                            pass
else:
                        break
else:
                    break
except:
            return


@app.on_callback_query(filters.regex("GetTimer")&~BANNED_USERS)
asyncdefquite_timer(client,CallbackQuery:CallbackQuery):
    try:
        awaitCallbackQuery.answer()
except:
        pass


@app.on_callback_query(filters.regex("GetQueued")&~BANNED_USERS)
@languageCB
asyncdefqueued_tracks(client,CallbackQuery:CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
callback_request=callback_data.split(None,1)[1]
what,videoid=callback_request.split("|")
try:
        chat_id,channel=awaitget_channeplayCB(_,what,CallbackQuery)
except:
        return
ifnotawaitis_active_chat(chat_id):
        returnawaitCallbackQuery.answer(_["general_5"],show_alert=True)
got=db.get(chat_id)
ifnotgot:
        returnawaitCallbackQuery.answer(_["queue_2"],show_alert=True)
iflen(got)==1:
        returnawaitCallbackQuery.answer(_["queue_5"],show_alert=True)
awaitCallbackQuery.answer()
basic[videoid]=False
buttons=queue_back_markup(_,what)
med=InputMediaPhoto(
media="https://telegra.ph//file/6f7d35131f69951c74ee5.jpg",
caption=_["queue_1"],
)
awaitCallbackQuery.edit_message_media(media=med)
j=0
msg=""
forxingot:
        j+=1
ifj==1:
            msg+=f'Streaming :\n\n✨ Title : {x["title"]}\nDuration : {x["dur"]}\nBy : {x["by"]}\n\n'
elifj==2:
            msg+=f'Queued :\n\n✨ Title : {x["title"]}\nDuration : {x["dur"]}\nBy : {x["by"]}\n\n'
else:
            msg+=f'✨ Title : {x["title"]}\nDuration : {x["dur"]}\nBy : {x["by"]}\n\n'
if"Queued"inmsg:
        iflen(msg)<700:
            awaitasyncio.sleep(1)
returnawaitCallbackQuery.edit_message_text(msg,reply_markup=buttons)
if"✨"inmsg:
            msg=msg.replace("✨","")
link=awaitNandBin(msg)
med=InputMediaPhoto(media=link,caption=_["queue_3"].format(link))
awaitCallbackQuery.edit_message_media(media=med,reply_markup=buttons)
else:
        awaitasyncio.sleep(1)
returnawaitCallbackQuery.edit_message_text(msg,reply_markup=buttons)


@app.on_callback_query(filters.regex("queue_back_timer")&~BANNED_USERS)
@languageCB
asyncdefqueue_back(client,CallbackQuery:CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
cplay=callback_data.split(None,1)[1]
try:
        chat_id,channel=awaitget_channeplayCB(_,cplay,CallbackQuery)
except:
        return
ifnotawaitis_active_chat(chat_id):
        returnawaitCallbackQuery.answer(_["general_5"],show_alert=True)
got=db.get(chat_id)
ifnotgot:
        returnawaitCallbackQuery.answer(_["queue_2"],show_alert=True)
awaitCallbackQuery.answer(_["set_cb_5"],show_alert=True)
file=got[0]["file"]
videoid=got[0]["vidid"]
user=got[0]["by"]
title=(got[0]["title"]).title()
typo=(got[0]["streamtype"]).title()
DUR=get_duration(got)
if"live_"infile:
        IMAGE=get_image(videoid)
elif"vid_"infile:
        IMAGE=get_image(videoid)
elif"index_"infile:
        IMAGE=config.STREAM_IMG_URL
else:
        ifvideoid=="telegram":
            IMAGE=(
config.TELEGRAM_AUDIO_URL
iftypo=="Audio"
elseconfig.TELEGRAM_VIDEO_URL
)
elifvideoid=="soundcloud":
            IMAGE=config.SOUNCLOUD_IMG_URL
else:
            IMAGE=get_image(videoid)
send=_["queue_6"]ifDUR=="Unknown"else_["queue_7"]
cap=_["queue_8"].format(app.mention,title,typo,user,send)
upl=(
queue_markup(_,DUR,cplay,videoid)
ifDUR=="Unknown"
elsequeue_markup(
_,
DUR,
cplay,
videoid,
seconds_to_min(got[0]["played"]),
got[0]["dur"],
)
)
basic[videoid]=True

med=InputMediaPhoto(media=IMAGE,caption=cap)
mystic=awaitCallbackQuery.edit_message_media(media=med,reply_markup=upl)
ifDUR!="Unknown":
        try:
            whiledb[chat_id][0]["vidid"]==videoid:
                awaitasyncio.sleep(5)
ifawaitis_active_chat(chat_id):
                    ifbasic[videoid]:
                        ifawaitis_music_playing(chat_id):
                            try:
                                buttons=queue_markup(
_,
DUR,
cplay,
videoid,
seconds_to_min(db[chat_id][0]["played"]),
db[chat_id][0]["dur"],
)
awaitmystic.edit_reply_markup(reply_markup=buttons)
exceptFloodWait:
                                pass
else:
                            pass
else:
                        break
else:
                    break
except:
            return












