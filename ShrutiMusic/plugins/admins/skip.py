utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardMarkup,Message

importconfig
fromShrutiMusicimportYouTube,app
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportdb
fromShrutiMusic.utils.databaseimportget_loop
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup,stream_markup
fromShrutiMusic.utils.stream.autoclearimportauto_clean
fromShrutiMusic.utils.thumbnailsimportgen_thumb
fromconfigimportBANNED_USERS


@app.on_message(
filters.command(["skip","cskip","next","cnext"])&filters.group&~BANNED_USERS
)
@AdminRightsCheck
asyncdefskip(cli,message:Message,_,chat_id):
    ifnotlen(message.command)<2:
        loop=awaitget_loop(chat_id)
ifloop!=0:
            returnawaitmessage.reply_text(_["admin_8"])
state=message.text.split(None,1)[1].strip()
ifstate.isnumeric():
            state=int(state)
check=db.get(chat_id)
ifcheck:
                count=len(check)
ifcount>2:
                    count=int(count-1)
if1<=state<=count:
                        forxinrange(state):
                            popped=None
try:
                                popped=check.pop(0)
except:
                                returnawaitmessage.reply_text(_["admin_12"])
ifpopped:
                                awaitauto_clean(popped)
ifnotcheck:
                                try:
                                    awaitmessage.reply_text(
text=_["admin_6"].format(
message.from_user.mention,
message.chat.title,
),
reply_markup=close_markup(_),
)
awaitNand.stop_stream(chat_id)
except:
                                    return
break
else:
                        returnawaitmessage.reply_text(_["admin_11"].format(count))
else:
                    returnawaitmessage.reply_text(_["admin_10"])
else:
                returnawaitmessage.reply_text(_["queue_2"])
else:
            returnawaitmessage.reply_text(_["admin_9"])
else:
        check=db.get(chat_id)
popped=None
try:
            popped=check.pop(0)
ifpopped:
                awaitauto_clean(popped)
ifnotcheck:
                awaitmessage.reply_text(
text=_["admin_6"].format(
message.from_user.mention,message.chat.title
),
reply_markup=close_markup(_),
)
try:
                    returnawaitNand.stop_stream(chat_id)
except:
                    return
except:
            try:
                awaitmessage.reply_text(
text=_["admin_6"].format(
message.from_user.mention,message.chat.title
),
reply_markup=close_markup(_),
)
returnawaitNand.stop_stream(chat_id)
except:
                return
queued=check[0]["file"]
title=(check[0]["title"]).title()
user=check[0]["by"]
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
            returnawaitmessage.reply_text(_["admin_7"].format(title))
try:
            image=awaitYouTube.thumbnail(videoid,True)
except:
            image=None
try:
            awaitNand.skip_stream(chat_id,link,video=status,image=image)
except:
            returnawaitmessage.reply_text(_["call_6"])
button=stream_markup(_,chat_id)
img=awaitgen_thumb(videoid)
run=awaitmessage.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
elif"vid_"inqueued:
        mystic=awaitmessage.reply_text(_["call_7"],disable_web_page_preview=True)
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
run=awaitmessage.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"
awaitmystic.delete()
elif"index_"inqueued:
        try:
            awaitNand.skip_stream(chat_id,videoid,video=status)
except:
            returnawaitmessage.reply_text(_["call_6"])
button=stream_markup(_,chat_id)
run=awaitmessage.reply_photo(
photo=config.STREAM_IMG_URL,
caption=_["stream_2"].format(user),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
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
            returnawaitmessage.reply_text(_["call_6"])
ifvideoid=="telegram":
            button=stream_markup(_,chat_id)
run=awaitmessage.reply_photo(
photo=config.TELEGRAM_AUDIO_URL
ifstr(streamtype)=="audio"
elseconfig.TELEGRAM_VIDEO_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],check[0]["dur"],user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
elifvideoid=="soundcloud":
            button=stream_markup(_,chat_id)
run=awaitmessage.reply_photo(
photo=config.SOUNCLOUD_IMG_URL
ifstr(streamtype)=="audio"
elseconfig.TELEGRAM_VIDEO_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],check[0]["dur"],user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
else:
            button=stream_markup(_,chat_id)
img=awaitgen_thumb(videoid)
run=awaitmessage.reply_photo(
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"












