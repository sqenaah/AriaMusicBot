utf-8utf-8

importasyncio

frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery

fromShrutiMusicimportYouTube,app
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportSUDOERS,db
fromShrutiMusic.utils.databaseimport(
get_active_chats,
get_lang,
get_upvote_count,
is_active_chat,
is_music_playing,
is_nonadmin_chat,
music_off,
music_on,
set_loop,
)
fromShrutiMusic.utils.decorators.languageimportlanguageCB
fromShrutiMusic.utils.formattersimportseconds_to_min
fromShrutiMusic.utils.inlineimportclose_markup,stream_markup,stream_markup_timer
fromShrutiMusic.utils.inline.helpimporthelp_pannel_page1,help_pannel_page2,help_pannel_page3,help_pannel_page4
fromShrutiMusic.utils.stream.autoclearimportauto_clean
fromShrutiMusic.utils.thumbnailsimportgen_thumb
fromconfigimport(
BANNED_USERS,
SOUNCLOUD_IMG_URL,
STREAM_IMG_URL,
TELEGRAM_AUDIO_URL,
TELEGRAM_VIDEO_URL,
adminlist,
confirmer,
votemode,
)
fromstringsimportget_string
importconfig

checker={}
upvoters={}

fromconfigimportSUPPORT_GROUP
@app.on_callback_query(filters.regex("help_page_1"))
asyncdefshow_help_page1(client,callback_query:CallbackQuery):
    try:
        language=awaitget_lang(callback_query.message.chat.id)
_=get_string(language)
except:
        _=get_string("en")

awaitcallback_query.message.edit_caption(
caption=_["help_1"].format(SUPPORT_GROUP),
reply_markup=help_pannel_page1(_,START=True)
)
[
InlineKeyboardButton("🔙 Bᴀᴄᴋ",callback_data="settingsback_helper")
]
]
)
)


frompyrogramimportClient,filters
frompyrogram.typesimportInlineKeyboardMarkup

fromShrutiMusic.utils.inline.startimportabout_panel
fromstringsimportget_string
fromconfigimportBANNED_USERS


frompyrogramimportClient,filters
frompyrogram.typesimportInlineKeyboardMarkup
fromShrutiMusic.utils.inline.startimportowner_panel
fromstringsimportget_string
fromconfigimportBANNED_USERS
fromShrutiMusicimportapp

@app.on_callback_query(filters.regex("about_page")&~BANNED_USERS)
asyncdefabout_cb(client,callback_query):
    try:
        lang="en"
_=get_string(lang)
awaitcallback_query.answer()
awaitcallback_query.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(about_panel(_))
)
exceptExceptionase:
        awaitcallback_query.answer(f"❌ Error: {e}",show_alert=True)

@app.on_callback_query(filters.regex("owner_page")&~BANNED_USERS)
asyncdefowner_page_cb(client,callback_query):
    try:
        lang="en"
_=get_string(lang)
awaitcallback_query.answer()
awaitcallback_query.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(owner_panel(_))
)
exceptExceptionase:
        awaitcallback_query.answer(f"❌ Error: {e}",show_alert=True)



frompyrogramimportfilters
frompyrogram.typesimportCallbackQuery
fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utilsimportbot_sys_stats
importtime,psutil,asyncio

defget_readable_time(seconds:int)->str:
    count=0
ping_time=""
time_list=[]
time_suffix_list=["s","m","h","d"]

whilecount<4:
        count+=1
remainder,result=divmod(seconds,60)ifcount<3elsedivmod(seconds,24)
ifseconds==0andresult==0:
            break
time_list.append(int(result))
seconds=int(remainder)

forxinrange(len(time_list)):
        ping_time=str(time_list[x])+time_suffix_list[x]+" "+ping_time
returnping_time.strip()

@app.on_callback_query(filters.regex("ping_status"))
asyncdefping_status_callback(client,callback_query:CallbackQuery):

    loading=awaitcallback_query.message.reply_text("🔄 ᴘɪɴɢɪɴɢ...")

start=time.time()
try:
        awaitNand.ping()
except:
        pass
end=time.time()
ping=round((end-start)*1000)

try:
        UP,CPU,RAM,DISK=awaitbot_sys_stats()
exceptException:
        UP="Unknown"
CPU=psutil.cpu_percent()
RAM=psutil.virtual_memory().percent
DISK=psutil.disk_usage('/').percent


ifping<100:
        color="🟢"
elifping<300:
        color="🟡"
else:
        color="🔴"

final_text=(
f"📡 ᴘɪɴɢ: {ping}ms {color}\n"
f"⏱ ᴜᴘᴛɪᴍᴇ: {UP}\n"
f"💾 ᴅɪꜱᴋ: {DISK}%\n"
f"📈 ᴍᴇᴍᴏʀʏ: {RAM}%\n"
f"🖥 ᴄᴘᴜ: {CPU}%"
)

awaitloading.edit_text(final_text)

awaitasyncio.sleep(8)
awaitloading.delete()


@app.on_callback_query(filters.regex("help_page_2"))
asyncdefshow_help_page2(client,callback_query:CallbackQuery):
    try:
        language=awaitget_lang(callback_query.message.chat.id)
_=get_string(language)
except:
        _=get_string("en")

awaitcallback_query.message.edit_caption(
caption=_["help_1"].format(SUPPORT_GROUP),
reply_markup=help_pannel_page2(_,START=True)
)

@app.on_callback_query(filters.regex("help_page_3"))
asyncdefshow_help_page3(client,callback_query:CallbackQuery):
    try:
        language=awaitget_lang(callback_query.message.chat.id)
_=get_string(language)
except:
        _=get_string("en")

awaitcallback_query.message.edit_caption(
caption=_["help_1"].format(SUPPORT_GROUP),
reply_markup=help_pannel_page3(_,START=True)
)

@app.on_callback_query(filters.regex("help_page_4"))
asyncdefshow_help_page4(client,callback_query:CallbackQuery):
    try:
        language=awaitget_lang(callback_query.message.chat.id)
_=get_string(language)
except:
        _=get_string("en")

awaitcallback_query.message.edit_caption(
caption=_["help_1"].format(SUPPORT_GROUP),
reply_markup=help_pannel_page4(_,START=True)
)


@app.on_callback_query(filters.regex("ADMIN")&~BANNED_USERS)
@languageCB
asyncdefdel_back_playlist(client,CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
callback_request=callback_data.split(None,1)[1]
command,chat=callback_request.split("|")
counter=None

if"_"instr(chat):
        bet=chat.split("_")
chat=bet[0]
counter=bet[1]

chat_id=int(chat)

ifnotawaitis_active_chat(chat_id):
        returnawaitCallbackQuery.answer(_["general_5"],show_alert=True)

mention=CallbackQuery.from_user.mention

ifcommand=="UpVote":
        ifchat_idnotinvotemode:
            votemode[chat_id]={}
ifchat_idnotinupvoters:
            upvoters[chat_id]={}

voters=(upvoters[chat_id]).get(CallbackQuery.message.id)
ifnotvoters:
            upvoters[chat_id][CallbackQuery.message.id]=[]

vote=(votemode[chat_id]).get(CallbackQuery.message.id)
ifnotvote:
            votemode[chat_id][CallbackQuery.message.id]=0

ifCallbackQuery.from_user.idinupvoters[chat_id][CallbackQuery.message.id]:
            (upvoters[chat_id][CallbackQuery.message.id]).remove(
CallbackQuery.from_user.id
)
votemode[chat_id][CallbackQuery.message.id]-=1
else:
            (upvoters[chat_id][CallbackQuery.message.id]).append(
CallbackQuery.from_user.id
)
votemode[chat_id][CallbackQuery.message.id]+=1

upvote=awaitget_upvote_count(chat_id)
get_upvotes=int(votemode[chat_id][CallbackQuery.message.id])

ifget_upvotes>=upvote:
            votemode[chat_id][CallbackQuery.message.id]=upvote
try:
                exists=confirmer[chat_id][CallbackQuery.message.id]
current=db[chat_id][0]
except:
                returnawaitCallbackQuery.edit_message_text(f"ғᴀɪʟᴇᴅ.")

try:
                ifcurrent["vidid"]!=exists["vidid"]:
                    returnawaitCallbackQuery.edit_message_text(_["admin_35"])
ifcurrent["file"]!=exists["file"]:
                    returnawaitCallbackQuery.edit_message_text(_["admin_35"])
except:
                returnawaitCallbackQuery.edit_message_text(_["admin_36"])

try:
                awaitCallbackQuery.edit_message_text(_["admin_37"].format(upvote))
except:
                pass

command=counter
mention="ᴜᴘᴠᴏᴛᴇs"
else:
            if(
CallbackQuery.from_user.id
inupvoters[chat_id][CallbackQuery.message.id]
):
                awaitCallbackQuery.answer(_["admin_38"],show_alert=True)
else:
                awaitCallbackQuery.answer(_["admin_39"],show_alert=True)

upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=f"👍 {get_upvotes}",
callback_data=f"ADMIN  UpVote|{chat_id}_{counter}",
)
]
]
)
awaitCallbackQuery.answer(_["admin_40"],show_alert=True)
returnawaitCallbackQuery.edit_message_reply_markup(reply_markup=upl)
else:
        is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            ifCallbackQuery.from_user.idnotinSUDOERS:
                admins=adminlist.get(CallbackQuery.message.chat.id)
ifnotadmins:
                    returnawaitCallbackQuery.answer(_["admin_13"],show_alert=True)
else:
                    ifCallbackQuery.from_user.idnotinadmins:
                        returnawaitCallbackQuery.answer(
_["admin_14"],show_alert=True
)

ifcommand=="Pause":
        ifnotawaitis_music_playing(chat_id):
            returnawaitCallbackQuery.answer(_["admin_1"],show_alert=True)
awaitCallbackQuery.answer()
awaitmusic_off(chat_id)
awaitNand.pause_stream(chat_id)
awaitCallbackQuery.message.reply_text(
_["admin_2"].format(mention),reply_markup=close_markup(_)
)

elifcommand=="Resume":
        ifawaitis_music_playing(chat_id):
            returnawaitCallbackQuery.answer(_["admin_3"],show_alert=True)
awaitCallbackQuery.answer()
awaitmusic_on(chat_id)
awaitNand.resume_stream(chat_id)
awaitCallbackQuery.message.reply_text(
_["admin_4"].format(mention),reply_markup=close_markup(_)
)

elifcommand=="Stop"orcommand=="End":
        awaitCallbackQuery.answer()
awaitNand.stop_stream(chat_id)
awaitset_loop(chat_id,0)
awaitCallbackQuery.message.reply_text(
_["admin_5"].format(mention),reply_markup=close_markup(_)
)
awaitCallbackQuery.message.delete()

elifcommand=="Skip"orcommand=="Replay":
        check=db.get(chat_id)
ifnotcheck:
            returnawaitCallbackQuery.answer("No music in queue!",show_alert=True)

ifcommand=="Skip":
            txt=f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
popped=None
try:
                popped=check.pop(0)
ifpopped:
                    awaitauto_clean(popped)
ifnotcheck:
                    awaitCallbackQuery.edit_message_text(
f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
)
awaitCallbackQuery.message.reply_text(
text=_["admin_6"].format(
mention,CallbackQuery.message.chat.title
),
reply_markup=close_markup(_),
)
try:
                        returnawaitNand.stop_stream(chat_id)
except:
                        return
except:
                try:
                    awaitCallbackQuery.edit_message_text(
f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
)
awaitCallbackQuery.message.reply_text(
text=_["admin_6"].format(
mention,CallbackQuery.message.chat.title
),
reply_markup=close_markup(_),
)
returnawaitNand.stop_stream(chat_id)
except:
                    return
else:
            txt=f"➻ sᴛʀᴇᴀᴍ ʀᴇ-ᴘʟᴀʏᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"

awaitCallbackQuery.answer()

ifnotcheck:
            returnawaitCallbackQuery.edit_message_text("Queue is empty!")

queued=check[0]["file"]
title=(check[0]["title"]).title()
user=check[0]["by"]
duration=check[0]["dur"]
streamtype=check[0]["streamtype"]
videoid=check[0]["vidid"]
status=Trueifstr(streamtype)=="video"elseNone

db[chat_id][0]["played"]=0
exis=(check[0]).get("old_dur")
ifexis:
            db[chat_id][0]["dur"]=exis
db[chat_id][0]["seconds"]=check[0]["old_second"]
db[chat_id][0]["speed_path"]=None
db[chat_id][0]["speed"]=1.0

if"live_"inqueued:
            n,link=awaitYouTube.video(videoid,True)
ifn==0:
                returnawaitCallbackQuery.message.reply_text(
text=_["admin_7"].format(title),
reply_markup=close_markup(_),
)
try:
                image=awaitYouTube.thumbnail(videoid,True)
except:
                image=None
try:
                awaitNand.skip_stream(chat_id,link,video=status,image=image)
except:
                returnawaitCallbackQuery.message.reply_text(_["call_6"])

button=stream_markup(_,chat_id)
img=awaitgen_thumb(videoid)
run=awaitCallbackQuery.message.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
duration,
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
awaitCallbackQuery.edit_message_text(txt,reply_markup=close_markup(_))

elif"vid_"inqueued:
            mystic=awaitCallbackQuery.message.reply_text(
_["call_7"],disable_web_page_preview=True
)
try:
                file_path,direct=awaitYouTube.download(
videoid,
mystic,
videoid=True,
video=status,
)
except:
                returnawaitmystic.edit_text(_["call_6"])

try:
                image=awaitYouTube.thumbnail(videoid,True)
except:
                image=None

try:
                awaitNand.skip_stream(chat_id,file_path,video=status,image=image)
except:
                returnawaitmystic.edit_text(_["call_6"])

button=stream_markup(_,chat_id)
img=awaitgen_thumb(videoid)
run=awaitCallbackQuery.message.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
duration,
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"
awaitCallbackQuery.edit_message_text(txt,reply_markup=close_markup(_))
awaitmystic.delete()

elif"index_"inqueued:
            try:
                awaitNand.skip_stream(chat_id,videoid,video=status)
except:
                returnawaitCallbackQuery.message.reply_text(_["call_6"])

button=stream_markup(_,chat_id)
run=awaitCallbackQuery.message.reply_photo(
photo=STREAM_IMG_URL,
caption=_["stream_2"].format(user),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
awaitCallbackQuery.edit_message_text(txt,reply_markup=close_markup(_))

else:
            ifvideoid=="telegram":
                image=None
elifvideoid=="soundcloud":
                image=None
else:
                try:
                    image=awaitYouTube.thumbnail(videoid,True)
except:
                    image=None

try:
                awaitNand.skip_stream(chat_id,queued,video=status,image=image)
except:
                returnawaitCallbackQuery.message.reply_text(_["call_6"])

ifvideoid=="telegram":
                button=stream_markup(_,chat_id)
run=awaitCallbackQuery.message.reply_photo(
photo=TELEGRAM_AUDIO_URL
ifstr(streamtype)=="audio"
elseTELEGRAM_VIDEO_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],duration,user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"

elifvideoid=="soundcloud":
                button=stream_markup(_,chat_id)
run=awaitCallbackQuery.message.reply_photo(
photo=SOUNCLOUD_IMG_URL
ifstr(streamtype)=="audio"
elseTELEGRAM_VIDEO_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],duration,user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"

else:
                button=stream_markup(_,chat_id)
img=awaitgen_thumb(videoid)
run=awaitCallbackQuery.message.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
duration,
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"

awaitCallbackQuery.edit_message_text(txt,reply_markup=close_markup(_))


asyncdefmarkup_timer():
    whileTrue:
        try:
            awaitasyncio.sleep(7)
active_chats=awaitget_active_chats()
forchat_idinactive_chats:
                try:
                    ifnotawaitis_music_playing(chat_id):
                        continue
playing=db.get(chat_id)
ifnotplaying:
                        continue
duration_seconds=int(playing[0]["seconds"])
ifduration_seconds==0:
                        continue
try:
                        mystic=playing[0]["mystic"]
except:
                        continue
try:
                        check=checker[chat_id][mystic.id]
ifcheckisFalse:
                            continue
except:
                        pass
try:
                        language=awaitget_lang(chat_id)
_=get_string(language)
except:
                        _=get_string("en")
try:
                        buttons=stream_markup_timer(
_,
chat_id,
seconds_to_min(playing[0]["played"]),
playing[0]["dur"],
)
awaitmystic.edit_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
except:
                        continue
except:
                    continue
except:
            continue


asyncio.create_task(markup_timer())
