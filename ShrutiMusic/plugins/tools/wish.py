utf-8utf-8importasyncio
importrandom
frompyrogramimportfilters
frompyrogram.typesimportMessage
fromShrutiMusicimportapp

active_chats={}

GM_MESSAGES=[
"🌞 <b>Gᴏᴏᴅ Mᴏʀɴɪɴɢ</b> 🌼\n\n{mention}",
"☕ <b>Rise and Shine!</b>\n\n{mention}",
"🌄 <b>Sᴜʀᴀᴊ Nɪᴋʜʀᴀ, Tᴜᴍʜᴀʀᴀ Dɪɴ Sᴜʙʜ Hᴏ</b>\n\n{mention}",
"🌻 <b>Nᴇᴇᴛʜ Kʜᴀᴛᴀᴍ, Aʙ Kᴀᴀᴍ Sʜᴜʀᴜ</b>\n\n{mention}",
"💫 <b>Jᴀɢᴏ Mᴇʀᴇ Sʜᴇʀᴏ!</b>\n\n{mention}",
"🕊️ <b>Sᴜᴋʜ Sᴀʙʜᴀ Gᴏᴏᴅ Mᴏʀɴɪɴɢ</b>\n\n{mention}",
"🌅 <b>Nᴀʏɪ Sᴜʙᴀʜ, Nᴀʏᴇ Sᴀᴘɴᴇ</b>\n\n{mention}",
"🌸 <b>Pʜᴜᴀʟᴏɴ Sᴇ Bʜᴀʀᴀ Yᴇʜ Sᴜʙᴀʜ</b>\n\n{mention}",
"⭐ <b>Uᴛʜᴏ Mᴇʀᴇ Sɪᴛᴀʀᴏ, Dɪɴ Sᴜʜᴀᴠᴀɴᴀ Hᴏ</b>\n\n{mention}",
"🌺 <b>Kʜᴜsʜɪʏᴏɴ Sᴇ Bʜᴀʀᴀ Hᴏ Yᴇʜ Dɪɴ</b>\n\n{mention}",
"🦋 <b>Tɪᴛʟɪʏᴏɴ Kɪ Tᴀʀᴀʜ Uᴅᴏ Aᴀᴊ</b>\n\n{mention}",
"🌈 <b>Rᴀɴɢ Bʜᴀʀᴀ Hᴏ Yᴇʜ Dɪɴ Tᴜᴍʜᴀʀᴀ</b>\n\n{mention}",
"🎵 <b>Pᴀᴋsʜɪʏᴏɴ Kᴀ Gᴀᴀɴᴀ Sᴜɴᴋᴇ Uᴛʜᴏ</b>\n\n{mention}",
"🌤️ <b>Dʜᴜᴀɴ Kᴀ Gɪʟᴀᴀs Aᴜʀ Tᴜᴍʜᴀʀɪ Hᴀɴsɪ</b>\n\n{mention}",
"🌟 <b>Cʜᴀᴀɴᴅ Sɪᴛᴀʀᴇ Bᴏʟᴇ - Gᴏᴏᴅ Mᴏʀɴɪɴɢ</b>\n\n{mention}",
"💐 <b>Hᴀʀ Kᴀᴀᴍ Mᴇɪɴ Kᴀᴀᴍʏᴀʙɪ Mɪʟᴇ</b>\n\n{mention}"
]

GA_MESSAGES=[
"🌞 <b>Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ</b> ☀️\n\n{mention}",
"🍵 <b>Cʜᴀɪ Pɪ Lᴏ, Aғᴛᴇʀɴᴏᴏɴ Hᴏ Gᴀʏɪ</b>\n\n{mention}",
"🌤️ <b>Hᴀʟᴋɪ Dᴏᴘʜᴀʀ, Aᴜʀ Tᴜᴍʜᴀʀᴀ Nᴀᴀᴍ</b> 💌\n\n{mention}",
"😴 <b>Sᴏɴᴀ Mᴀᴛ, Kᴀᴀᴍ Kᴀʀᴏ</b> 😜\n\n{mention}",
"📢 <b>Hᴇʏ Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ!</b>\n\n{mention}",
"🌅 <b>Dᴏᴘʜᴀʀ Kᴀ Sᴜʀᴀᴊ Tᴇᴢ Hᴀɪ</b>\n\n{mention}",
"🥗 <b>Kʜᴀᴀɴᴀ Kʜᴀʏᴀ Kᴇ Nᴀʜɪ?</b>\n\n{mention}",
"☀️ <b>Tᴇᴢ Dʜᴜᴀᴘ Mᴇɪɴ Tʜᴀɴᴅᴀ Pᴀᴀɴɪ Pɪʏᴏ</b>\n\n{mention}",
"🌻 <b>Dᴏᴘʜᴀʀ Kᴀ Aʀᴀᴀᴍ Kᴀʀᴏ</b>\n\n{mention}",
"🍃 <b>Pᴀᴘᴇᴅ Kᴇ Nᴇᴇᴄʜᴇ Bᴀɪᴛʜᴋᴇ Bᴀᴀᴛᴇɪɴ</b>\n\n{mention}",
"🌸 <b>Lᴜɴᴄʜ Kᴀ Tɪᴍᴇ Hᴏ Gᴀʏᴀ</b>\n\n{mention}",
"🦋 <b>Dᴏᴘʜᴀʀ Kɪ Mᴀsᴛɪ Kᴀʀᴏ</b>\n\n{mention}",
"🍉 <b>Tᴀʀʙᴜᴊ Kʜᴀᴀᴋᴇ Tʜᴀɴᴅᴀ Hᴏ Jᴀᴏ</b>\n\n{mention}",
"🌺 <b>Aᴀsᴍᴀɴ Bʜɪ Sᴀᴀғ Hᴀɪ Aᴀᴊ</b>\n\n{mention}",
"🎵 <b>Gᴜɴɢᴜɴᴀᴛᴇ Hᴜᴇ Kᴀᴀᴍ Kᴀʀᴏ</b>\n\n{mention}",
"🌈 <b>Rᴀɴɢ Bɪʀᴀɴɢᴀ Dᴏᴘʜᴀʀ</b>\n\n{mention}"
]

GN_MESSAGES=[
"🌙 <b>Gᴏᴏᴅ Nɪɢʜᴛ</b>\n\n{mention}",
"💤 <b>Sᴏɴᴇ Cʜᴀʟᴏ, Kʜᴀᴡᴀʙᴏɴ Mᴇɪɴ Mɪʟᴛᴇ Hᴀɪɴ</b> 😴\n\n{mention}",
"🌌 <b>Aᴀsᴍᴀɴ Bʜɪ Sᴏ Gᴀʏᴀ, Aʙ Tᴜᴍʜɪ Bʜɪ Sᴏ Jᴀᴏ!</b>\n\n{mention}",
"✨ <b>Rᴀᴀᴛ Kᴀ Sᴀᴋᴏᴏɴ Tᴜᴍʜᴇɪ Mɪʟᴇ</b>\n\n{mention}",
"🌃 <b>Gᴏᴏᴅ Nɪɢʜᴛ & Sᴡᴇᴇᴛ Dʀᴇᴀᴍs</b>\n\n{mention}",
"🌟 <b>Sɪᴛᴀʀᴏɴ Kᴇ Sᴀᴀᴛʜ Sᴏɴᴀ</b>\n\n{mention}",
"🕊️ <b>Cᴀᴀɴᴅ Kɪ Rᴏsʜɴɪ Mᴇɪɴ Aᴀʀᴀᴀᴍ</b>\n\n{mention}",
"🎭 <b>Sᴀᴘɴᴏɴ Kᴀ Rᴀᴀᴊᴀ Bᴀɴᴋᴇ Sᴏɴᴀ</b>\n\n{mention}",
"🌺 <b>Rᴀᴀᴛ Kᴇ Pʜᴜᴀʟᴏɴ Sᴇ Mɪʟᴏ</b>\n\n{mention}",
"💫 <b>Cʜᴀᴀɴᴅ Mᴀᴀᴍᴀ Kʜᴀᴀɴɪ Sᴜɴᴀᴛᴇ Hᴀɪɴ</b>\n\n{mention}",
"🎵 <b>Lᴏʀɪ Kᴇ Sᴀᴀᴛʜ Sᴏɴᴀ</b>\n\n{mention}",
"🌸 <b>Sᴀᴀʀᴇ Gᴀᴍ Bʜᴜᴀʟᴀᴋᴇ Sᴏɴᴀ</b>\n\n{mention}",
"🦋 <b>Tɪᴛʟɪʏᴏɴ Kᴇ Sᴀᴀᴛʜ Sᴀᴘɴᴇ</b>\n\n{mention}",
"🌈 <b>Rᴀɴɢ Bɪʀᴀɴɢᴇ Kʜᴀᴀʙ Dᴇᴋʜɴᴀ</b>\n\n{mention}",
"🕯️ <b>Dɪʏᴇ Kɪ Rᴏsʜɴɪ Mᴇɪɴ Sᴏɴᴀ</b>\n\n{mention}",
"🌅 <b>Kᴀʟ Pʜɪʀ Mɪʟᴇɴɢᴇ Sᴜʙᴀʜ</b>\n\n{mention}"
]

asyncdefget_chat_users(chat_id):
    """Get all valid users from a chat (excluding bots and deleted accounts)"""
users=[]
asyncformemberinapp.get_chat_members(chat_id):
        ifmember.user.is_botormember.user.is_deleted:
            continue
users.append(member.user)
returnusers

asyncdeftag_users(chat_id,messages,tag_type):
    """Generic function to tag users one by one with specified messages"""
users=awaitget_chat_users(chat_id)

foruserinusers:

        ifchat_idnotinactive_chats:
            break

mention=f"<b><a href='tg://user?id={user.id}'>{user.first_name}</a></b>"
msg=random.choice(messages).format(mention=mention)

awaitapp.send_message(chat_id,msg,disable_web_page_preview=True)
awaitasyncio.sleep(3)

active_chats.pop(chat_id,None)
awaitapp.send_message(chat_id,f"✅ <b>{tag_type} Tᴀɢɢɪɴɢ Dᴏɴᴇ!</b>")


@app.on_message(filters.command("gmtag")&filters.group)
asyncdefgmtag(_,message:Message):
    """Start Good Morning tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        returnawaitmessage.reply("⚠️ <b>Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Aʟʀᴇᴀᴅʏ Rᴜɴɴɪɴɢ.</b>")

active_chats[chat_id]=True
awaitmessage.reply("☀️ <b>Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Sᴛᴀʀᴛᴇᴅ...</b>")

awaittag_users(chat_id,GM_MESSAGES,"Gᴏᴏᴅ Mᴏʀɴɪɴɢ")

@app.on_message(filters.command("gmstop")&filters.group)
asyncdefgmstop(_,message:Message):
    """Stop Good Morning tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        delactive_chats[chat_id]
awaitmessage.reply("🛑 <b>Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Sᴛᴏᴘᴘᴇᴅ.</b>")
else:
        awaitmessage.reply("❌ <b>Nᴏᴛʜɪɴɢ Rᴜɴɴɪɴɢ.</b>")


@app.on_message(filters.command("gatag")&filters.group)
asyncdefgatag(_,message:Message):
    """Start Good Afternoon tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        returnawaitmessage.reply("⚠️ <b>Aғᴛᴇʀɴᴏᴏɴ Tᴀɢɢɪɴɢ Aʟʀᴇᴀᴅʏ Oɴ.</b>")

active_chats[chat_id]=True
awaitmessage.reply("☀️ <b>Aғᴛᴇʀɴᴏᴏɴ Tᴀɢɢɪɴɢ Sᴛᴀʀᴛᴇᴅ...</b>")

awaittag_users(chat_id,GA_MESSAGES,"Aғᴛᴇʀɴᴏᴏɴ")

@app.on_message(filters.command("gastop")&filters.group)
asyncdefgastop(_,message:Message):
    """Stop Good Afternoon tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        delactive_chats[chat_id]
awaitmessage.reply("🛑 <b>Aғᴛᴇʀɴᴏᴏɴ Tᴀɢɢɪɴɢ Sᴛᴏᴘᴘᴇᴅ.</b>")
else:
        awaitmessage.reply("❌ <b>Nᴏᴛʜɪɴɢ Rᴜɴɴɪɴɢ.</b>")


@app.on_message(filters.command("gntag")&filters.group)
asyncdefgntag(_,message:Message):
    """Start Good Night tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        returnawaitmessage.reply("⚠️ <b>Nɪɢʜᴛ Tᴀɢɢɪɴɢ Aʟʀᴇᴀᴅʏ Oɴ.</b>")

active_chats[chat_id]=True
awaitmessage.reply("🌙 <b>Nɪɢʜᴛ Tᴀɢɢɪɴɢ Sᴛᴀʀᴛᴇᴅ...</b>")

awaittag_users(chat_id,GN_MESSAGES,"Gᴏᴏᴅ Nɪɢʜᴛ")

@app.on_message(filters.command("gnstop")&filters.group)
asyncdefgnstop(_,message:Message):
    """Stop Good Night tagging"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        delactive_chats[chat_id]
awaitmessage.reply("🛑 <b>Nɪɢʜᴛ Tᴀɢɢɪɴɢ Sᴛᴏᴘᴘᴇᴅ.</b>")
else:
        awaitmessage.reply("❌ <b>Nᴏᴛʜɪɴɢ Rᴜɴɴɪɴɢ.</b>")


@app.on_message(filters.command("stopall")&filters.group)
asyncdefstopall(_,message:Message):
    """Stop all active tagging in current chat"""
chat_id=message.chat.id

ifchat_idinactive_chats:
        delactive_chats[chat_id]
awaitmessage.reply("🛑 <b>Aʟʟ Tᴀɢɢɪɴɢ Sᴛᴏᴘᴘᴇᴅ.</b>")
else:
        awaitmessage.reply("❌ <b>Nᴏ Aᴄᴛɪᴠᴇ Tᴀɢɢɪɴɢ Fᴏᴜɴᴅ.</b>")

@app.on_message(filters.command("taghelp")&filters.group)
asyncdeftaghelp(_,message:Message):
    """Show help message for tagging commands"""
help_text="""
🏷️ <b>Tagging Commands Help</b>

<b>Good Morning:</b>
• <code>/gmtag</code> - Start Good Morning tagging
• <code>/gmstop</code> - Stop Good Morning tagging

<b>Good Afternoon:</b>
• <code>/gatag</code> - Start Good Afternoon tagging  
• <code>/gastop</code> - Stop Good Afternoon tagging

<b>Good Night:</b>
• <code>/gntag</code> - Start Good Night tagging
• <code>/gnstop</code> - Stop Good Night tagging

<b>Utility:</b>
• <code>/stopall</code> - Stop all active tagging
• <code>/taghelp</code> - Show this help message

<b>Note:</b> Now tags one user at a time with 3 second delay between each user. Only one tagging session can run per chat at a time.
"""
awaitmessage.reply(help_text)












