utf-8utf-8

importrandom
frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup
fromconfigimportLOG_GROUP_ID
fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportadd_served_chat,get_assistant

welcome_photo="https://i.ibb.co/chq4KyFV/image.jpg"

@app.on_message(filters.new_chat_members,group=-10)
asyncdefjoin_watcher(_,message):
    try:
        userbot=awaitget_assistant(message.chat.id)
chat=message.chat
formembersinmessage.new_chat_members:
            ifmembers.id==app.id:
                count=awaitapp.get_chat_members_count(chat.id)
username=message.chat.usernameifmessage.chat.usernameelse"Private Group"


invite_link=""
try:
                    ifnotmessage.chat.username:
                        link=awaitapp.export_chat_invite_link(message.chat.id)
invite_link=f"\nGroup Link: {link}"iflinkelse""
except:
                    pass

msg=(
f"Music Bot Added In A New Group\n\n"
f"Chat Name: {message.chat.title}\n"
f"Chat ID: {message.chat.id}\n"
f"Chat Username: @{username}\n"
f"Group Members: {count}\n"
f"Added By: {message.from_user.mention}"
f"{invite_link}"
)

buttons=[]
ifmessage.from_user.id:
                    buttons.append([InlineKeyboardButton("Added By",
url=f"tg://openmessage?user_id={message.from_user.id}")])

awaitapp.send_photo(
LOG_GROUP_ID,
photo=welcome_photo,
caption=msg,
reply_markup=InlineKeyboardMarkup(buttons)ifbuttonselseNone
)

awaitadd_served_chat(message.chat.id)
ifusername:
                    awaituserbot.join_chat(f"@{username}")

exceptExceptionase:
        print(f"Error: {e}")


frompyrogram.typesimportMessage
fromShrutiMusic.utils.databaseimportdelete_served_chat,get_assistant

photo=[
"https://i.ibb.co/LdyDcfS0/image.jpg",
"https://i.ibb.co/LdyDcfS0/image.jpg",
]


@app.on_message(filters.left_chat_member,group=-12)
asyncdefon_left_chat_member(_,message:Message):
    try:
        userbot=awaitget_assistant(message.chat.id)

left_chat_member=message.left_chat_member
ifleft_chat_memberandleft_chat_member.id==(awaitapp.get_me()).id:
            remove_by=(
message.from_user.mentionifmessage.from_userelse"𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
)
title=message.chat.title
username=(
f"@{message.chat.username}"ifmessage.chat.usernameelse"𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
)
chat_id=message.chat.id
left=f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
awaitapp.send_photo(LOG_GROUP_ID,photo=random.choice(photo),caption=left)
awaitdelete_served_chat(chat_id)
awaituserbot.leave_chat(chat_id)
exceptExceptionase:
        return
