importmath
frompyrogram.typesimportInlineKeyboardButton
fromShrutiMusic.utils.formattersimporttime_to_seconds
fromconfigimportBOT_USERNAME,SUPPORT_GROUP,SUPPORT_CHANNEL


deftrack_markup(_,videoid,user_id,channel,fplay):
    buttons=[
[
InlineKeyboardButton(
text=_["P_B_1"],
callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
),
InlineKeyboardButton(
text=_["P_B_2"],
callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
),
],
[
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data=f"forceclose {videoid}|{user_id}",
)
],
]
returnbuttons


defstream_markup_timer(_,chat_id,played,dur):
    played_sec=time_to_seconds(played)
duration_sec=time_to_seconds(dur)
percentage=(played_sec/duration_sec)*100
umm=math.floor(percentage)
if0<umm<=10:
        bar="◉—————————"
elif10<umm<20:
        bar="—◉————————"
elif20<=umm<30:
        bar="——◉———————"
elif30<=umm<40:
        bar="———◉——————"
elif40<=umm<50:
        bar="————◉—————"
elif50<=umm<60:
        bar="—————◉————"
elif60<=umm<70:
        bar="——————◉———"
elif70<=umm<80:
        bar="———————◉——"
elif80<=umm<95:
        bar="————————◉—"
else:
        bar="—————————◉"

buttons=[
[
InlineKeyboardButton(
text=f"{played} {bar} {dur}",
url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
)
],
[
InlineKeyboardButton(text="▷",callback_data=f"ADMIN Resume|{chat_id}"),
InlineKeyboardButton(text="II",callback_data=f"ADMIN Pause|{chat_id}"),
InlineKeyboardButton(text="↻",callback_data=f"ADMIN Replay|{chat_id}"),
InlineKeyboardButton(text="‣‣I",callback_data=f"ADMIN Skip|{chat_id}"),
InlineKeyboardButton(text="▢",callback_data=f"ADMIN Stop|{chat_id}"),
],
[
InlineKeyboardButton(text="💬 sᴜᴘᴘᴏʀᴛ",url=SUPPORT_GROUP),
InlineKeyboardButton(text="📢 ᴄʜᴀɴɴᴇʟ",url=SUPPORT_CHANNEL),
],
[InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close")],
]
returnbuttons


defstream_markup(_,chat_id):
    buttons=[
[
InlineKeyboardButton(text="▷",callback_data=f"ADMIN Resume|{chat_id}"),
InlineKeyboardButton(text="II",callback_data=f"ADMIN Pause|{chat_id}"),
InlineKeyboardButton(text="↻",callback_data=f"ADMIN Replay|{chat_id}"),
InlineKeyboardButton(text="‣‣I",callback_data=f"ADMIN Skip|{chat_id}"),
InlineKeyboardButton(text="▢",callback_data=f"ADMIN Stop|{chat_id}"),
],
[InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close")],
]
returnbuttons


defplaylist_markup(_,videoid,user_id,ptype,channel,fplay):
    buttons=[
[
InlineKeyboardButton(
text=_["P_B_1"],
callback_data=f"NandPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
),
InlineKeyboardButton(
text=_["P_B_2"],
callback_data=f"NandPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
),
],
[
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data=f"forceclose {videoid}|{user_id}",
),
],
]
returnbuttons


deflivestream_markup(_,videoid,user_id,mode,channel,fplay):
    buttons=[
[
InlineKeyboardButton(
text=_["P_B_3"],
callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
),
],
[
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data=f"forceclose {videoid}|{user_id}",
),
],
]
returnbuttons


defslider_markup(_,videoid,user_id,query,query_type,channel,fplay):
    query=f"{query[:20]}"
buttons=[
[
InlineKeyboardButton(
text=_["P_B_1"],
callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
),
InlineKeyboardButton(
text=_["P_B_2"],
callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
),
],
[
InlineKeyboardButton(
text="◁",
callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data=f"forceclose {query}|{user_id}",
),
InlineKeyboardButton(
text="▷",
callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
),
],
]
returnbuttons
