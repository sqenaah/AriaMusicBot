utf-8utf-8





















frompyrogramimportClient,filters
frompyrogram.typesimportMessage,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery,ChatPermissions
frompymongoimportMongoClient
fromShrutiMusicimportapp
importasyncio
fromShrutiMusic.miscimportSUDOERS
fromconfigimportMONGO_DB_URI
frompyrogram.enumsimportChatMembersFilter
frompyrogram.errorsimport(
ChatAdminRequired,
UserNotParticipant,
)

fsubdb=MongoClient(MONGO_DB_URI)
forcesub_collection=fsubdb.status_db.status

@app.on_message(filters.command(["fsub","forcesub"])&filters.group)
asyncdefset_forcesub(client:Client,message:Message):
    chat_id=message.chat.id
user_id=message.from_user.id

member=awaitclient.get_chat_member(chat_id,user_id)

ifnot(member.statusin["owner","administrator"]oruser_idinSUDOERS):
        returnawaitmessage.reply_text("**ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ᴏʀ sᴜᴅᴏᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.**")

iflen(message.command)==2andmessage.command[1].lower()in["off","disable"]:
        forcesub_collection.delete_one({"chat_id":chat_id})
returnawaitmessage.reply_text("**ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ.**")

iflen(message.command)!=2:
        returnawaitmessage.reply_text("**ᴜsᴀɢᴇ: /ғsᴜʙ <ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ> ᴏʀ /ғsᴜʙ ᴏғғ ᴛᴏ ᴅɪsᴀʙʟᴇ**")

channel_input=message.command[1]

try:
        channel_info=awaitclient.get_chat(channel_input)
channel_id=channel_info.id
channel_username=f"{channel_info.username}"ifchannel_info.usernameelseNone

forcesub_collection.update_one(
{"chat_id":chat_id},
{"$set":{"channel_id":channel_id,"channel_username":channel_username}},
upsert=True
)

awaitmessage.reply_text(f"**🎉 Force subscription set to channel:** [{channel_info.title}](https://t.me/{channel_username})")

exceptExceptionase:
        awaitmessage.reply_text("**🚫 Failed to set force subscription.**")

@app.on_chat_member_updated()
asyncdefon_user_join(client:Client,chat_member_updated):
    chat_id=chat_member_updated.chat.id
user_id=chat_member_updated.from_user.id
forcesub_data=forcesub_collection.find_one({"chat_id":chat_id})

ifnotforcesub_data:
        return

channel_id=forcesub_data["channel_id"]
channel_username=forcesub_data["channel_username"]

new_chat_member=chat_member_updated.new_chat_member
ifnew_chat_memberisNone:
        return


ifnew_chat_member.status=="member":
        try:

            user_member=awaitapp.get_chat_member(channel_id,user_id)

return
exceptUserNotParticipant:

            awaitclient.restrict_chat_member(
chat_id,
user_id,
permissions=ChatPermissions(can_send_messages=False)
)
awaitclient.send_message(
chat_id,
f"**🚫 {chat_member_updated.from_user.mention}, you have been muted because you need to join the [channel](https://t.me/{channel_username}) to send messages in this group.**",
disable_web_page_preview=True
)
exceptExceptionase:

            print(f"Error checking channel membership: {e}")
else:

        try:
            user_member=awaitapp.get_chat_member(channel_id,user_id)

ifuser_member.status=="member":
                awaitclient.restrict_chat_member(
chat_id,
user_id,
permissions=ChatPermissions(can_send_messages=True)
)
awaitclient.send_message(
chat_id,
f"**🎉 {chat_member_updated.from_user.mention}, you have been unmuted because you joined the [channel](https://t.me/{channel_username}).**",
disable_web_page_preview=True
)
exceptUserNotParticipant:

            pass
exceptExceptionase:

            print(f"Error checking channel membership on unmute: {e}")

@app.on_callback_query(filters.regex("close_force_sub"))
asyncdefclose_force_sub(client:Client,callback_query:CallbackQuery):
    awaitcallback_query.answer("ᴄʟᴏsᴇᴅ!")
awaitcallback_query.message.delete()


asyncdefcheck_forcesub(client:Client,message:Message):
    chat_id=message.chat.id


ifmessage.from_userisNone:
        return

user_id=message.from_user.id
forcesub_data=forcesub_collection.find_one({"chat_id":chat_id})
ifnotforcesub_data:
        return

channel_id=forcesub_data["channel_id"]
channel_username=forcesub_data["channel_username"]

try:
        user_member=awaitapp.get_chat_member(channel_id,user_id)
ifuser_member:
            return
exceptUserNotParticipant:
        ifchannel_username:
            channel_url=f"https://t.me/{channel_username}"
else:
            invite_link=awaitapp.export_chat_invite_link(channel_id)
channel_url=invite_link
awaitmessage.reply_photo(
photo="https://envs.sh/Tn_.jpg",
caption=(f"**👋 ʜᴇʟʟᴏ {message.from_user.mention},**\n\n**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [ᴄʜᴀɴɴᴇʟ]({channel_url}) ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**"),
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("๏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ๏",url=channel_url)]]),
)
awaitasyncio.sleep(1)
exceptChatAdminRequired:
        forcesub_collection.delete_one({"chat_id":chat_id})
returnawaitmessage.reply_text("**🚫 I'ᴍ ɴᴏ ʟᴏɴɢᴇʀ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ғᴏʀᴄᴇᴅ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ. ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ.**")

@app.on_message(filters.group,group=30)
asyncdefenforce_forcesub(client:Client,message:Message):
    ifnotawaitcheck_forcesub(client,message):
        return


__MODULE__="ғsᴜʙ"
__HELP__="""**
/fsub <ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ> - sᴇᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ.
/fsub off - ᴅɪsᴀʙʟᴇ ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ.**
"""












