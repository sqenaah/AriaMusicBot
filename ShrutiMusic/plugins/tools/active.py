utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage
fromunidecodeimportunidecode

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimport(
get_active_chats,
get_active_video_chats,
remove_active_chat,
remove_active_video_chat,
)


@app.on_message(filters.command(["activevc","activevoice"])&SUDOERS)
asyncdefactivevc(_,message:Message):
    mystic=awaitmessage.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
served_chats=awaitget_active_chats()
text=""
j=0
forxinserved_chats:
        try:
            title=(awaitapp.get_chat(x)).title
except:
            awaitremove_active_chat(x)
continue
try:
            if(awaitapp.get_chat(x)).username:
                user=(awaitapp.get_chat(x)).username
text+=f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
else:
                text+=(
f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
)
j+=1
except:
            continue
ifnottext:
        awaitmystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
else:
        awaitmystic.edit_text(
f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}",
disable_web_page_preview=True,
)


@app.on_message(filters.command(["activev","activevideo"])&SUDOERS)
asyncdefactivevi_(_,message:Message):
    mystic=awaitmessage.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
served_chats=awaitget_active_video_chats()
text=""
j=0
forxinserved_chats:
        try:
            title=(awaitapp.get_chat(x)).title
except:
            awaitremove_active_video_chat(x)
continue
try:
            if(awaitapp.get_chat(x)).username:
                user=(awaitapp.get_chat(x)).username
text+=f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
else:
                text+=(
f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
)
j+=1
except:
            continue
ifnottext:
        awaitmystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
else:
        awaitmystic.edit_text(
f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
disable_web_page_preview=True,
)












