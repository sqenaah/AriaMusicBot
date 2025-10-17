utf-8utf-8importasyncio
importtime
fromloggingimportgetLogger
fromtimeimporttime

fromPILimportImage,ImageChops,ImageDraw,ImageEnhance,ImageFont
frompyrogramimportenums,filters
frompyrogram.typesimportChatMemberUpdated

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_assistant
fromconfigimportOWNER_ID

LOGGER=getLogger(__name__)


classAWelDatabase:
    def__init__(self):
        self.data={}

asyncdeffind_one(self,chat_id):
        returnchat_idinself.data

asyncdefadd_wlcm(self,chat_id):
        ifchat_idnotinself.data:
            self.data[chat_id]={"state":"on"}

asyncdefrm_wlcm(self,chat_id):
        ifchat_idinself.data:
            delself.data[chat_id]


wlcm=AWelDatabase()


classtemp:
    ME=None
CURRENT=2
CANCEL=False
MELCOW={}
U_NAME=None
B_NAME=None

user_last_message_time={}
user_command_count={}
SPAM_THRESHOLD=2
SPAM_WINDOW_SECONDS=5


@app.on_message(filters.command("awelcome")&~filters.private)
asyncdefauto_state(_,message):
    user_id=message.from_user.id
current_time=time()
last_message_time=user_last_message_time.get(user_id,0)

ifcurrent_time-last_message_time<SPAM_WINDOW_SECONDS:
        user_last_message_time[user_id]=current_time
user_command_count[user_id]=user_command_count.get(user_id,0)+1
ifuser_command_count[user_id]>SPAM_THRESHOLD:
            hu=awaitmessage.reply_text(
f"{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ"
)
awaitasyncio.sleep(3)
awaithu.delete()
return
else:
        user_command_count[user_id]=1
user_last_message_time[user_id]=current_time

usage="ᴜsᴀɢᴇ:\n⦿ /awelcome [on|off]"
iflen(message.command)==1:
        returnawaitmessage.reply_text(usage)
chat_id=message.chat.id
user=awaitapp.get_chat_member(message.chat.id,message.from_user.id)
ifuser.statusin(
enums.ChatMemberStatus.ADMINISTRATOR,
enums.ChatMemberStatus.OWNER,
):
        A=awaitwlcm.find_one(chat_id)
state=message.text.split(None,1)[1].strip().lower()
ifstate=="off":
            ifA:
                awaitmessage.reply_text(
"ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !"
)
else:
                awaitwlcm.add_wlcm(chat_id)
awaitmessage.reply_text(
f"ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title} ʙʏ ᴀssɪsᴛᴀɴᴛ"
)
elifstate=="on":
            ifnotA:
                awaitmessage.reply_text("ᴇɴᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.")
else:
                awaitwlcm.rm_wlcm(chat_id)
awaitmessage.reply_text(
f"ᴇɴᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ  {message.chat.title}"
)
else:
            awaitmessage.reply_text(usage)
else:
        awaitmessage.reply(
"sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!"
)


@app.on_chat_member_updated(filters.group,group=5)
asyncdefgreet_new_members(_,member:ChatMemberUpdated):
    try:
        chat_id=member.chat.id
chat_name=(awaitapp.get_chat(chat_id)).title
userbot=awaitget_assistant(chat_id)
count=awaitapp.get_chat_members_count(chat_id)
A=awaitwlcm.find_one(chat_id)
ifA:
            return

user=(
member.new_chat_member.userifmember.new_chat_memberelsemember.from_user
)

ifmember.new_chat_memberandnotmember.old_chat_member:
            ifuser.id==OWNER_IDoruser.id==7574330905:
                owner_welcome_text=f"""🌟 <b>𝐓ʜᴇ ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b> 🌟

🔥 <b>ʙᴏss</b> {user.mention} <b>ʜᴀs ᴊᴏɪɴᴇᴅ!</b> 🔥
👑 <b>ᴏᴡɴᴇʀ ɪᴅ:</b> {user.id} ✨
🎯 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username} 🚀
👥 <b>ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs:</b> {count} 📈
🏰 <b>ɢʀᴏᴜᴘ:</b> {chat_name} 

<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜɪs ᴋɪɴɢᴅᴏᴍ, ʙᴏss ! 👑✨</b>"""
awaitasyncio.sleep(3)
awaituserbot.send_message(chat_id,text=owner_welcome_text)
else:
                welcome_text=f"""⛳️ <b>𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ 𝐎ᴜʀ 𝐆ʀᴏᴜᴘ</b> ⛳️

➤ <b>𝐍ᴀᴍᴇ 🖤 ◂⚚▸</b> {user.mention} 💤 ❤️
➤ <b>𝐔ꜱᴇʀ 𝐈ᴅ 🖤 ◂⚚▸</b> {user.id} ❤️🧿
➤ <b>𝐔ꜱᴇʀɴᴀᴍᴇ 🖤 ◂⚚▸</b> @{user.username} ❤️🌎
➤ <b>𝐌ᴇᴍʙᴇʀs 🖤 ◂⚚▸</b> {count} ❤️🍂"""
awaitasyncio.sleep(3)
awaituserbot.send_message(chat_id,text=welcome_text)
exceptExceptionase:
        return
