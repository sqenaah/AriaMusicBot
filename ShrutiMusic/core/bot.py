utf-8utf-8

try:
    importuvloop
uvloop.install()
exceptImportError:
    pass

importpyrogram
frompyrogramimportClient
frompyrogram.enumsimportChatMemberStatus,ParseMode
frompyrogram.typesimport(
InlineKeyboardButton,
InlineKeyboardMarkup,
)

importconfig

from..loggingimportLOGGER


classNand(Client):
    def__init__(self):
        LOGGER(__name__).info(f"sᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
super().__init__(
name="ShrutiMusic",
api_id=config.API_ID,
api_hash=config.API_HASH,
bot_token=config.BOT_TOKEN,
in_memory=True,
parse_mode=ParseMode.HTML,
max_concurrent_transmissions=7,
)

asyncdefstart(self):
        awaitsuper().start()
get_me=awaitself.get_me()
self.username=get_me.username
self.id=get_me.id
self.name=self.me.first_name+" "+(self.me.last_nameor"")
self.mention=self.me.mention


button=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏",
url=f"https://t.me/{self.username}?startgroup=true",
)
]
]
)


ifconfig.LOG_GROUP_ID:
            try:
                awaitself.send_photo(
config.LOG_GROUP_ID,
photo=config.START_IMG_URL,
caption=f"╔════❰𝗪𝗘𝗟𝗖𝗢𝗠𝗘❱════❍⊱❁۪۪\n║\n║┣⪼🥀ʙᴏᴛ sᴛᴀʀᴛᴇᴅ🎉\n║\n║┣⪼ {self.name}\n║\n║┣⪼🎈ɪᴅ:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ😍\n║\n╚════════════════❍⊱❁",
reply_markup=button,
)
exceptpyrogram.errors.ChatWriteForbiddenase:
                LOGGER(__name__).error(f"Bot cannot write to the log group: {e}")
try:
                    awaitself.send_message(
config.LOG_GROUP_ID,
f"╔═══❰𝗪𝗘𝗟𝗖𝗢𝗠𝗘❱═══❍⊱❁۪۪\n║\n║┣⪼🥀ʙᴏᴛ sᴛᴀʀᴛᴇᴅ🎉\n║\n║◈ {self.name}\n║\n║┣⪼🎈ɪᴅ:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ😍\n║\n╚══════════════❍⊱❁",
reply_markup=button,
)
exceptExceptionase:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
exceptExceptionase:
                LOGGER(__name__).error(
f"Unexpected error while sending to log group: {e}"
)
else:
            LOGGER(__name__).warning(
"LOG_GROUP_ID is not set, skipping log group notifications."
)


ifconfig.LOG_GROUP_ID:
            try:
                chat_member_info=awaitself.get_chat_member(
config.LOG_GROUP_ID,self.id
)
ifchat_member_info.status!=ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
"Please promote Bot as Admin in Logger Group"
)
exceptExceptionase:
                LOGGER(__name__).error(f"Error occurred while checking bot status: {e}")

LOGGER(__name__).info(f"Music Bot Started as {self.name}")

asyncdefstop(self):
        awaitsuper().stop()
