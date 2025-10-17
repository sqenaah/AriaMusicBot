utf-8utf-8





















importtime
importrandom

frompyrogramimportfilters
frompyrogram.enumsimportChatType
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Message
fromyoutubesearchpython.__future__importVideosSearch

importconfig
fromShrutiMusicimportapp
fromShrutiMusic.miscimport_boot_
fromShrutiMusic.plugins.sudo.sudoersimportsudoers_list
fromShrutiMusic.utils.databaseimport(
add_served_chat,
add_served_user,
blacklisted_chats,
get_lang,
is_banned_user,
is_on_off,
)
fromShrutiMusic.utilsimportbot_sys_stats
fromShrutiMusic.utils.decorators.languageimportLanguageStart
fromShrutiMusic.utils.formattersimportget_readable_time
fromShrutiMusic.utils.inlineimporthelp_pannel_page1,private_panel,start_panel
fromconfigimportBANNED_USERS
fromstringsimportget_string


RANDOM_STICKERS=[
"CAACAgUAAxkBAAEEnzFor872a_gYPHu-FxIwv-nxmZ5U8QACyBUAAt5hEFVBanMxRZCc7h4E",
"CAACAgUAAxkBAAEEnzJor88q_xRO1ljlwh_I6fRF7lDR-AACnBsAAlckCFWNCpez-HzWHB4E",
"CAACAgUAAxkBAAEEnzNor88uPuVTSyRImyVXsu1pqrpRLgACKRMAAvOEEFUpvggmgDu6bx4E",
"CAACAgUAAxkBAAEEnzRor880z_spEYEnEfyFXN55tNwydQACIxUAAosKEVUB8iqZMVYroR4E"
]


@app.on_message(filters.command(["start"])&filters.private&~BANNED_USERS)
@LanguageStart
asyncdefstart_pm(client,message:Message,_):

    random_sticker=random.choice(RANDOM_STICKERS)
awaitmessage.reply_sticker(sticker=random_sticker)

awaitadd_served_user(message.from_user.id)
iflen(message.text.split())>1:
        name=message.text.split(None,1)[1]
ifname[0:4]=="help":
            keyboard=help_pannel_page1(_)
returnawaitmessage.reply_photo(
photo=config.START_IMG_URL,
caption=_["help_1"].format(config.SUPPORT_GROUP),

reply_markup=keyboard,
)
ifname[0:3]=="sud":
            awaitsudoers_list(client=client,message=message,_=_)
ifawaitis_on_off(2):
                returnawaitapp.send_message(
chat_id=config.LOG_GROUP_ID,
text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
)
return
ifname[0:3]=="inf":
            m=awaitmessage.reply_text("🔎")
query=(str(name)).replace("info_","",1)
query=f"https://www.youtube.com/watch?v={query}"
results=VideosSearch(query,limit=1)
forresultin(awaitresults.next())["result"]:
                title=result["title"]
duration=result["duration"]
views=result["viewCount"]["short"]
thumbnail=result["thumbnails"][0]["url"].split("?")[0]
channellink=result["channel"]["link"]
channel=result["channel"]["name"]
link=result["link"]
published=result["publishedTime"]
searched_text=_["start_6"].format(
title,duration,views,published,channellink,channel,app.mention
)
key=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text=_["S_B_8"],url=link),
InlineKeyboardButton(text=_["S_B_9"],url=config.SUPPORT_GROUP),
],
]
)
awaitm.delete()
awaitapp.send_photo(
chat_id=message.chat.id,
photo=thumbnail,
caption=searched_text,
reply_markup=key,
)
ifawaitis_on_off(2):
                returnawaitapp.send_message(
chat_id=config.LOG_GROUP_ID,
text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
)
else:
        out=private_panel(_)
UP,CPU,RAM,DISK=awaitbot_sys_stats()
awaitmessage.reply_photo(
photo=config.START_IMG_URL,
caption=_["start_2"].format(message.from_user.mention,app.mention,UP,DISK,CPU,RAM),
reply_markup=InlineKeyboardMarkup(out),
)
ifawaitis_on_off(2):
            returnawaitapp.send_message(
chat_id=config.LOG_GROUP_ID,
text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
)


@app.on_message(filters.command(["start"])&filters.group&~BANNED_USERS)
@LanguageStart
asyncdefstart_gp(client,message:Message,_):

    random_sticker=random.choice(RANDOM_STICKERS)
awaitmessage.reply_sticker(sticker=random_sticker)

out=start_panel(_)
uptime=int(time.time()-_boot_)
awaitmessage.reply_photo(
photo=config.START_IMG_URL,
caption=_["start_1"].format(app.mention,get_readable_time(uptime)),
reply_markup=InlineKeyboardMarkup(out),
)
returnawaitadd_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members,group=-1)
asyncdefwelcome(client,message:Message):
    formemberinmessage.new_chat_members:
        try:
            language=awaitget_lang(message.chat.id)
_=get_string(language)
ifawaitis_banned_user(member.id):
                try:
                    awaitmessage.chat.ban_member(member.id)
except:
                    pass
ifmember.id==app.id:
                ifmessage.chat.type!=ChatType.SUPERGROUP:
                    awaitmessage.reply_text(_["start_4"])
returnawaitapp.leave_chat(message.chat.id)
ifmessage.chat.idinawaitblacklisted_chats():
                    awaitmessage.reply_text(
_["start_5"].format(
app.mention,
f"https://t.me/{app.username}?start=sudolist",
config.SUPPORT_GROUP,
),
disable_web_page_preview=True,
)
returnawaitapp.leave_chat(message.chat.id)


random_sticker=random.choice(RANDOM_STICKERS)
awaitmessage.reply_sticker(sticker=random_sticker)

out=start_panel(_)
awaitmessage.reply_photo(
photo=config.START_IMG_URL,
caption=_["start_3"].format(
message.from_user.first_name,
app.mention,
message.chat.title,
app.mention,
),
reply_markup=InlineKeyboardMarkup(out),
)
awaitadd_served_chat(message.chat.id)
awaitmessage.stop_propagation()
exceptExceptionasex:
            print(ex)












