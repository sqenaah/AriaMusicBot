utf-8utf-8





















frompyrogram.enumsimportChatType,ParseMode
frompyrogram.filtersimportcommand
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Message

fromShrutiMusicimportapp
fromShrutiMusic.utils.functionsimportMARKDOWN


@app.on_message(command("markdownhelp"))
asyncdefmkdwnhelp(_,m:Message):
    keyb=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="Click Here!",
url=f"http://t.me/{app.username}?start=mkdwn_help",
)
]
]
)
ifm.chat.type!=ChatType.PRIVATE:
        awaitm.reply(
"ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍᴀʀᴋᴅᴏᴡɴ ᴜsᴀɢᴇ sʏɴᴛᴀx ɪɴ ᴘᴍ!",
reply_markup=keyb,
)
else:
        awaitm.reply(
MARKDOWN,parse_mode=ParseMode.HTML,disable_web_page_preview=True
)
return












