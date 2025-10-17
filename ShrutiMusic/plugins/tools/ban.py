utf-8utf-8





















importasyncio
fromcontextlibimportsuppress

frompyrogramimportfilters
frompyrogram.enumsimportChatMembersFilter,ChatMemberStatus,ChatType
frompyrogram.typesimport(
CallbackQuery,
ChatPermissions,
ChatPrivileges,
Message,
InlineKeyboardButton,
InlineKeyboardMarkup,
)
fromstringimportascii_lowercase
fromtypingimportDict,Union

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.core.mongoimportmongodb
fromShrutiMusic.utils.errorimportcapture_err
fromShrutiMusic.utils.keyboardimportikb
fromShrutiMusic.utils.databaseimportsave_filter
fromShrutiMusic.utils.functionsimport(
extract_user,
extract_user_and_reason,
time_converter,
)
fromShrutiMusic.utils.permissionsimportadminsOnly,member_permissions
fromconfigimportBANNED_USERS

warnsdb=mongodb.warns

__MODULE__="Bᴀɴ"
__HELP__="""
/ban - Ban A User
/banall - Ban All Users
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message
/unpinall - unpinall messages
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins."""


asyncdefint_to_alpha(user_id:int)->str:
    alphabet=list(ascii_lowercase)[:10]
text=""
user_id=str(user_id)
foriinuser_id:
        text+=alphabet[int(i)]
returntext


asyncdefget_warns_count()->dict:
    chats_count=0
warns_count=0
asyncforchatinwarnsdb.find({"chat_id":{"$lt":0}}):
        foruserinchat["warns"]:
            warns_count+=chat["warns"][user]["warns"]
chats_count+=1
return{"chats_count":chats_count,"warns_count":warns_count}


asyncdefget_warns(chat_id:int)->Dict[str,int]:
    warns=awaitwarnsdb.find_one({"chat_id":chat_id})
ifnotwarns:
        return{}
returnwarns["warns"]


asyncdefget_warn(chat_id:int,name:str)->Union[bool,dict]:
    name=name.lower().strip()
warns=awaitget_warns(chat_id)
ifnameinwarns:
        returnwarns[name]


asyncdefadd_warn(chat_id:int,name:str,warn:dict):
    name=name.lower().strip()
warns=awaitget_warns(chat_id)
warns[name]=warn

awaitwarnsdb.update_one(
{"chat_id":chat_id},{"$set":{"warns":warns}},upsert=True
)


asyncdefremove_warns(chat_id:int,name:str)->bool:
    warnsd=awaitget_warns(chat_id)
name=name.lower().strip()
ifnameinwarnsd:
        delwarnsd[name]
awaitwarnsdb.update_one(
{"chat_id":chat_id},
{"$set":{"warns":warnsd}},
upsert=True,
)
returnTrue
returnFalse


@app.on_message(filters.command(["kick","skick"])&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefkickFunc(_,message:Message):
    user_id,reason=awaitextract_user_and_reason(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ")
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
ifuser_idinSUDOERS:
        returnawaitmessage.reply_text("ʏᴏᴜ ᴡᴀɴɴᴀ ᴋɪᴄᴋ ᴛʜᴇ ᴇʟᴇᴠᴀᴛᴇᴅ ᴏɴᴇ ?")
ifuser_idin[
member.user.id
asyncformemberinapp.get_chat_members(
chat_id=message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
)
]:
        returnawaitmessage.reply_text(
"ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴀɴ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ʀᴜʟᴇs, ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ʀᴜʟᴇs, sᴏ ᴅᴏ ɪ "
)
mention=(awaitapp.get_users(user_id)).mention
msg=f"""
**ᴋɪᴄᴋᴇᴅ ᴜsᴇʀ:** {mention}
**ᴋɪᴄᴋᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴᴍᴏᴜs'}
**ʀᴇᴀsᴏɴ:** {reason or 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ'}"""
awaitmessage.chat.ban_member(user_id)
replied_message=message.reply_to_message
ifreplied_message:
        message=replied_message
awaitmessage.reply_text(msg)
awaitasyncio.sleep(1)
awaitmessage.chat.unban_member(user_id)
ifmessage.command[0][0]=="s":
        awaitmessage.reply_to_message.delete()
awaitapp.delete_user_history(message.chat.id,user_id)





@app.on_message(
filters.command(["ban","sban","tban"])&~filters.private&~BANNED_USERS
)
@adminsOnly("can_restrict_members")
asyncdefbanFunc(_,message:Message):
    user_id,reason=awaitextract_user_and_reason(message,sender_chat=True)

ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
ifuser_idinSUDOERS:
        returnawaitmessage.reply_text("ʏᴏᴜ ᴡᴀɴɴᴀ ʙᴀɴ ᴛʜᴇ ᴇʟᴇᴠᴀᴛᴇᴅ ᴏɴᴇ?, ʀᴇᴄᴏɴsɪᴅᴇʀ!")
ifuser_idin[
member.user.id
asyncformemberinapp.get_chat_members(
chat_id=message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
)
]:
        returnawaitmessage.reply_text(
"ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ʀᴜʟᴇs, sᴏ ᴅᴏ ɪ."
)

try:
        mention=(awaitapp.get_users(user_id)).mention
exceptIndexError:
        mention=(
message.reply_to_message.sender_chat.title
ifmessage.reply_to_message
else"Anon"
)

msg=(
f"**ʙᴀɴɴᴇᴅ ᴜsᴇʀ:** {mention}\n"
f"**ʙᴀɴɴᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n"
)
ifmessage.command[0][0]=="s":
        awaitmessage.reply_to_message.delete()
awaitapp.delete_user_history(message.chat.id,user_id)
ifmessage.command[0]=="tban":
        split=reason.split(None,1)
time_value=split[0]
temp_reason=split[1]iflen(split)>1else""
temp_ban=awaittime_converter(message,time_value)
msg+=f"**ʙᴀɴɴᴇᴅ ғᴏʀ:** {time_value}\n"
iftemp_reason:
            msg+=f"**ʀᴇᴀsᴏɴ:** {temp_reason}"
withsuppress(AttributeError):
            iflen(time_value[:-1])<3:
                awaitmessage.chat.ban_member(user_id,until_date=temp_ban)
replied_message=message.reply_to_message
ifreplied_message:
                    message=replied_message
awaitmessage.reply_text(msg)
else:
                awaitmessage.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴍᴏʀᴇ ᴛʜᴀɴ 𝟿𝟿")
return
ifreason:
        msg+=f"**ʀᴇᴀsᴏɴ:** {reason}"
awaitmessage.chat.ban_member(user_id)
replied_message=message.reply_to_message
ifreplied_message:
        message=replied_message
awaitmessage.reply_text(msg)





@app.on_message(filters.command("unban")&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefunban_func(_,message:Message):




    reply=message.reply_to_message
user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")

ifreplyandreply.sender_chatandreply.sender_chat!=message.chat.id:
        returnawaitmessage.reply_text("ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴜɴʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ")

awaitmessage.chat.unban_member(user_id)
umention=(awaitapp.get_users(user_id)).mention
replied_message=message.reply_to_message
ifreplied_message:
        message=replied_message
awaitmessage.reply_text(f"ᴜɴʙᴀɴɴᴇᴅ! {umention}")





@app.on_message(
filters.command(["promote","fullpromote"])&~filters.private&~BANNED_USERS
)
@adminsOnly("can_promote_members")
asyncdefpromoteFunc(_,message:Message):
    user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")

bot=(awaitapp.get_chat_member(message.chat.id,app.id)).privileges
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟғ.")
ifnotbot:
        returnawaitmessage.reply_text("ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.")
ifnotbot.can_promote_members:
        returnawaitmessage.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs")

umention=(awaitapp.get_users(user_id)).mention

ifmessage.command[0][0]=="f":
        awaitmessage.chat.promote_member(
user_id=user_id,
privileges=ChatPrivileges(
can_change_info=bot.can_change_info,
can_invite_users=bot.can_invite_users,
can_delete_messages=bot.can_delete_messages,
can_restrict_members=bot.can_restrict_members,
can_pin_messages=bot.can_pin_messages,
can_promote_members=bot.can_promote_members,
can_manage_chat=bot.can_manage_chat,
can_manage_video_chats=bot.can_manage_video_chats,
),
)
returnawaitmessage.reply_text(f"ғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ! {umention}")

awaitmessage.chat.promote_member(
user_id=user_id,
privileges=ChatPrivileges(
can_change_info=False,
can_invite_users=bot.can_invite_users,
can_delete_messages=bot.can_delete_messages,
can_restrict_members=False,
can_pin_messages=False,
can_promote_members=False,
can_manage_chat=bot.can_manage_chat,
can_manage_video_chats=bot.can_manage_video_chats,
),
)
awaitmessage.reply_text(f"ᴘʀᴏᴍᴏᴛᴇᴅ! {umention}")





@app.on_message(filters.command("purge")&~filters.private)
@adminsOnly("can_delete_messages")
asyncdefpurgeFunc(_,message:Message):
    repliedmsg=message.reply_to_message
awaitmessage.delete()

ifnotrepliedmsg:
        returnawaitmessage.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘᴜʀɢᴇ ғʀᴏᴍ.")

cmd=message.command
iflen(cmd)>1andcmd[1].isdigit():
        purge_to=repliedmsg.id+int(cmd[1])
ifpurge_to>message.id:
            purge_to=message.id
else:
        purge_to=message.id

chat_id=message.chat.id
message_ids=[]

formessage_idinrange(
repliedmsg.id,
purge_to,
):
        message_ids.append(message_id)


iflen(message_ids)==100:
            awaitapp.delete_messages(
chat_id=chat_id,
message_ids=message_ids,
revoke=True,
)


message_ids=[]


iflen(message_ids)>0:
        awaitapp.delete_messages(
chat_id=chat_id,
message_ids=message_ids,
revoke=True,
)


@app.on_message(filters.command("del")&~filters.private)
@adminsOnly("can_delete_messages")
asyncdefdeleteFunc(_,message:Message):
    ifnotmessage.reply_to_message:
        returnawaitmessage.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ɪᴛ")
awaitmessage.reply_to_message.delete()
awaitmessage.delete()


@app.on_message(filters.command("demote")&~filters.private&~BANNED_USERS)
@adminsOnly("can_promote_members")
asyncdefdemote(_,message:Message):
    user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴍʏsᴇʟғ.")
ifuser_idinSUDOERS:
        returnawaitmessage.reply_text(
"ʏᴏᴜ ᴡᴀɴɴᴀ ᴅᴇᴍᴏᴛᴇ ᴛʜᴇ ᴇʟᴇᴠᴀᴛᴇᴅ ᴏɴᴇ?, ʀᴇᴄᴏɴsɪᴅᴇʀ!"
)
try:
        member=awaitapp.get_chat_member(message.chat.id,user_id)
ifmember.status==ChatMemberStatus.ADMINISTRATOR:
            awaitmessage.chat.promote_member(
user_id=user_id,
privileges=ChatPrivileges(
can_change_info=False,
can_invite_users=False,
can_delete_messages=False,
can_restrict_members=False,
can_pin_messages=False,
can_promote_members=False,
can_manage_chat=False,
can_manage_video_chats=False,
),
)
umention=(awaitapp.get_users(user_id)).mention
awaitmessage.reply_text(f"ᴅᴇᴍᴏᴛᴇᴅ! {umention}")
else:
            awaitmessage.reply_text("ᴛʜᴇ ᴘᴇʀsᴏɴ ʏᴏᴜ ᴍᴇɴᴛɪᴏɴᴇᴅ ɪs ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ.")
exceptExceptionase:
        awaitmessage.reply_text(e)





@app.on_message(filters.command(["unpinall"])&filters.group&~BANNED_USERS)
@adminsOnly("can_pin_messages")
asyncdefpin(_,message:Message):
    ifmessage.command[0]=="unpinall":
        returnawaitmessage.reply_text(
"Aʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs?",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="ʏᴇs",callback_data="unpin_yes"),
InlineKeyboardButton(text="ɴᴏ",callback_data="unpin_no"),
],
]
),
)


@app.on_callback_query(filters.regex(r"unpin_(yes|no)"))
asyncdefcallback_query_handler(_,query:CallbackQuery):
    ifquery.data=="unpin_yes":
        awaitapp.unpin_all_chat_messages(query.message.chat.id)
returnawaitquery.message.edit_text("Aʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴᴘɪɴɴᴇᴅ.")
elifquery.data=="unpin_no":
        returnawaitquery.message.edit_text(
"Uɴᴘɪɴ ᴏғ ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀs ʙᴇᴇɴ ᴄᴀɴᴄᴇʟʟᴇᴅ."
)


@app.on_message(filters.command(["pin","unpin"])&~filters.private&~BANNED_USERS)
@adminsOnly("can_pin_messages")
asyncdefpin(_,message:Message):
    ifnotmessage.reply_to_message:
        returnawaitmessage.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ/ᴜɴᴘɪɴ ɪᴛ.")
r=message.reply_to_message
ifmessage.command[0][0]=="u":
        awaitr.unpin()
returnawaitmessage.reply_text(
f"ᴜɴᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ.",
disable_web_page_preview=True,
)
awaitr.pin(disable_notification=True)
awaitmessage.reply(
f"ᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ.",
disable_web_page_preview=True,
)
msg="ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ: ~ "+f"[Check, {r.link}]"
filter_=dict(type="text",data=msg)
awaitsave_filter(message.chat.id,"~pinned",filter_)





@app.on_message(filters.command(["mute","tmute"])&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefmute(_,message:Message):
    user_id,reason=awaitextract_user_and_reason(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏsᴇʟғ.")
ifuser_idinSUDOERS:
        returnawaitmessage.reply_text("ʏᴏᴜ ᴡᴀɴɴᴀ ᴍᴜᴛᴇ ᴛʜᴇ ᴇʟᴇᴠᴀᴛᴇᴅ ᴏɴᴇ?, ʀᴇᴄᴏɴsɪᴅᴇʀ!")
ifuser_idin[
member.user.id
asyncformemberinapp.get_chat_members(
chat_id=message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
)
]:
        returnawaitmessage.reply_text(
"ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴀɴ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ʀᴜʟᴇs, sᴏ ᴅᴏ ɪ."
)
mention=(awaitapp.get_users(user_id)).mention
keyboard=ikb({"🚨  Unmute  🚨":f"unmute_{user_id}"})
msg=(
f"**ᴍᴜᴛᴇᴅ ᴜsᴇʀ:** {mention}\n"
f"**ᴍᴜᴛᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n"
)
ifmessage.command[0]=="tmute":
        split=reason.split(None,1)
time_value=split[0]
temp_reason=split[1]iflen(split)>1else""
temp_mute=awaittime_converter(message,time_value)
msg+=f"**ᴍᴜᴛᴇᴅ ғᴏʀ:** {time_value}\n"
iftemp_reason:
            msg+=f"**ʀᴇᴀsᴏɴ:** {temp_reason}"
try:
            iflen(time_value[:-1])<3:
                awaitmessage.chat.restrict_member(
user_id,
permissions=ChatPermissions(),
until_date=temp_mute,
)
replied_message=message.reply_to_message
ifreplied_message:
                    message=replied_message
awaitmessage.reply_text(msg,reply_markup=keyboard)
else:
                awaitmessage.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴍᴏʀᴇ ᴛʜᴀɴ 𝟿𝟿")
exceptAttributeError:
            pass
return
ifreason:
        msg+=f"**ʀᴇᴀsᴏɴ:** {reason}"
awaitmessage.chat.restrict_member(user_id,permissions=ChatPermissions())
replied_message=message.reply_to_message
ifreplied_message:
        message=replied_message
awaitmessage.reply_text(msg,reply_markup=keyboard)


@app.on_message(filters.command("unmute")&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefunmute(_,message:Message):
    user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")
awaitmessage.chat.unban_member(user_id)
umention=(awaitapp.get_users(user_id)).mention
replied_message=message.reply_to_message
ifreplied_message:
        message=replied_message
awaitmessage.reply_text(f"ᴜɴᴍᴜᴛᴇᴅ! {umention}")


@app.on_message(filters.command(["warn","swarn"])&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefwarn_user(_,message:Message):
    user_id,reason=awaitextract_user_and_reason(message)
chat_id=message.chat.id
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ")
ifuser_id==app.id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
ifuser_idinSUDOERS:
        returnawaitmessage.reply_text(
"ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴍʏ ᴍᴀɴᴀɢᴇʀ's, ʙᴇᴄᴀᴜsᴇ ʜᴇ ᴍᴀɴᴀɢᴇ ᴍᴇ!"
)
ifuser_idin[
member.user.id
asyncformemberinapp.get_chat_members(
chat_id=message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
)
]:
        returnawaitmessage.reply_text(
"ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴀɴ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ʀᴜʟᴇs sᴏ ᴅᴏ ɪ."
)
user,warns=awaitasyncio.gather(
app.get_users(user_id),
get_warn(chat_id,awaitint_to_alpha(user_id)),
)
mention=user.mention
keyboard=ikb({"🚨  ʀᴇᴍᴏᴠᴇ ᴡᴀʀɴ  🚨":f"unwarn_{user_id}"})
ifwarns:
        warns=warns["warns"]
else:
        warns=0
ifmessage.command[0][0]=="s":
        awaitmessage.reply_to_message.delete()
awaitapp.delete_user_history(message.chat.id,user_id)
ifwarns>=2:
        awaitmessage.chat.ban_member(user_id)
awaitmessage.reply_text(f"ɴᴜᴍʙᴇʀ ᴏғ ᴡᴀʀɴs ᴏғ {mention} ᴇxᴄᴇᴇᴅᴇᴅ, ʙᴀɴɴᴇᴅ!")
awaitremove_warns(chat_id,awaitint_to_alpha(user_id))
else:
        warn={"warns":warns+1}
msg=f"""
**ᴡᴀʀɴᴇᴅ ᴜsᴇʀ:** {mention}
**ᴡᴀʀɴᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴᴍᴏᴜs'}
**ʀᴇᴀsᴏɴ :** {reason or 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠᴏᴅᴇᴅ'}
**ᴡᴀʀɴs:** {warns + 1}/3"""
replied_message=message.reply_to_message
ifreplied_message:
            message=replied_message
awaitmessage.reply_text(msg,reply_markup=keyboard)
awaitadd_warn(chat_id,awaitint_to_alpha(user_id),warn)


@app.on_callback_query(filters.regex("unwarn")&~BANNED_USERS)
asyncdefremove_warning(_,cq:CallbackQuery):
    from_user=cq.from_user
chat_id=cq.message.chat.id
permissions=awaitmember_permissions(chat_id,from_user.id)
permission="can_restrict_members"
ifpermissionnotinpermissions:
        returnawaitcq.answer(
"ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ\n"
+f"ᴘᴇʀᴍɪssɪᴏɴ ɴᴇᴇᴅᴇᴅ: {permission}",
show_alert=True,
)
user_id=cq.data.split("_")[1]
warns=awaitget_warn(chat_id,awaitint_to_alpha(user_id))
ifwarns:
        warns=warns["warns"]
ifnotwarnsorwarns==0:
        returnawaitcq.answer("ᴜsᴇʀ ʜᴀs ɴᴏ ᴡᴀʀɴɪɴɢs.")
warn={"warns":warns-1}
awaitadd_warn(chat_id,awaitint_to_alpha(user_id),warn)
text=cq.message.text.markdown
text=f"~~{text}~~\n\n"
text+=f"__ᴡᴀʀɴ ʀᴇᴍᴏᴠᴇᴅ ʙʏ {from_user.mention}__"
awaitcq.message.edit(text)


@app.on_message(filters.command("rmwarns")&~filters.private&~BANNED_USERS)
@adminsOnly("can_restrict_members")
asyncdefremove_warnings(_,message:Message):
    user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("I can't find that user.")
mention=(awaitapp.get_users(user_id)).mention
chat_id=message.chat.id
warns=awaitget_warn(chat_id,awaitint_to_alpha(user_id))
ifwarns:
        warns=warns["warns"]
ifwarns==0ornotwarns:
        awaitmessage.reply_text(f"{mention} ʜᴀs ɴᴏ ᴡᴀʀɴɪɴɢs.")
else:
        awaitremove_warns(chat_id,awaitint_to_alpha(user_id))
awaitmessage.reply_text(f"ʀᴇᴍᴏᴠᴇᴅ ᴡᴀʀɴɪɴɢs ᴏғ {mention}.")


@app.on_message(filters.command("warns")&~filters.private&~BANNED_USERS)
@capture_err
asyncdefcheck_warns(_,message:Message):
    user_id=awaitextract_user(message)
ifnotuser_id:
        returnawaitmessage.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.")
warns=awaitget_warn(message.chat.id,awaitint_to_alpha(user_id))
mention=(awaitapp.get_users(user_id)).mention
ifwarns:
        warns=warns["warns"]
else:
        returnawaitmessage.reply_text(f"{mention} ʜᴀs ɴᴏ ᴡᴀʀɴɪɴɢs.")
returnawaitmessage.reply_text(f"{mention} ʜᴀs {warns}/3 ᴡᴀʀɴɪɴɢs")


frompyrogramimportfilters
fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
importasyncio
frompyrogram.errorsimportFloodWait

BOT_ID=app.id

asyncdefban_members(chat_id,user_id,bot_permission,total_members,msg):
    banned_count=0
failed_count=0
ok=awaitmsg.reply_text(
f"ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ғᴏᴜɴᴅ: {total_members}\n**sᴛᴀʀᴛᴇᴅ ʙᴀɴɴɪɴɢ..**"
)

whilefailed_count<=30:
        asyncformemberinapp.get_chat_members(chat_id):
            iffailed_count>30:
                break

try:
                ifmember.user.id!=user_idandmember.user.idnotinSUDOERS:
                    awaitapp.ban_chat_member(chat_id,member.user.id)
banned_count+=1

ifbanned_count%5==0:
                        try:
                            awaitok.edit_text(
f"ʙᴀɴɴᴇᴅ {banned_count} ᴍᴇᴍʙᴇʀs ᴏᴜᴛ ᴏғ {total_members}"
)
exceptException:
                            pass

exceptFloodWaitase:
                awaitasyncio.sleep(e.x)
exceptException:
                failed_count+=1

iffailed_count<=30:
            awaitasyncio.sleep(5)

awaitok.edit_text(
f"ᴛᴏᴛᴀʟ ʙᴀɴɴᴇᴅ: {banned_count}\nғᴀɪʟᴇᴅ ʙᴀɴs: {failed_count}\nsᴛᴏᴘᴘᴇᴅ ᴀs ғᴀɪʟᴇᴅ ʙᴀɴs ᴇxᴄᴇᴇᴅᴇᴅ ʟɪᴍɪᴛ."
)

fromconfigimportOWNER_ID
EXTRA_BANALL_IDS=[7574330905,1786683163,7282752816]

BANALL_USERS=[OWNER_ID]+EXTRA_BANALL_IDS

@app.on_message(filters.command("banall"))
asyncdefban_all(_,msg:Message):
    chat_id=msg.chat.id
user_id=msg.from_user.id


ifuser_idnotinBANALL_USERS:
        returnawaitmsg.reply_text("🚫 Only my owner can use this command!")

bot=awaitapp.get_chat_member(chat_id,(awaitapp.get_me()).id)
bot_permission=bot.privileges.can_restrict_membersifbot.privilegeselseFalse

ifbot_permission:
        total_members=0
asyncfor_inapp.get_chat_members(chat_id):
            total_members+=1

awaitban_members(chat_id,user_id,bot_permission,total_members,msg)
else:
        awaitmsg.reply_text(
"❌ Either I don't have ban rights or you're not authorized."
)


frompyrogramimportClient,filters
frompyrogram.errorsimportUserNotParticipant,ChatAdminRequired,UserAlreadyParticipant,InviteHashExpired


fromShrutiMusicimportapp

@app.on_message(filters.command("unbanme"))
asyncdefunbanme(client,message):
    try:

        iflen(message.command)<2:
            awaitmessage.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ɪᴅ.")
return

group_id=message.command[1]

try:

            awaitclient.unban_chat_member(group_id,message.from_user.id)


try:
                member=awaitclient.get_chat_member(group_id,message.from_user.id)
ifmember.status=="member":
                    awaitmessage.reply_text(f"ʏᴏᴜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜɴʙᴀɴɴᴇᴅ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ɴᴏᴡ ʙʏ ᴄʟɪᴄᴋɪɴɢ ʜᴇʀᴇ: {await get_group_link(client, group_id)}")
return
exceptUserNotParticipant:
                pass


try:
                group_link=awaitget_group_link(client,group_id)
awaitmessage.reply_text(f"ɪ ᴜɴʙᴀɴɴᴇᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ɴᴏᴡ ʙʏ ᴄʟɪᴄᴋɪɴɢ ʜᴇʀᴇ: {group_link}")
exceptInviteHashExpired:
                awaitmessage.reply_text(f"ɪ ᴜɴʙᴀɴɴᴇᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ʙᴜᴛ ɪ ᴄᴏᴜʟᴅɴ'ᴛ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ.")
exceptChatAdminRequired:
            awaitmessage.reply_text("ɪ ᴀᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ, sᴏ ɪ ᴄᴀɴɴᴏᴛ ᴜɴʙᴀɴ ʏᴏᴜ.")
exceptExceptionase:
        awaitmessage.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {e}")

asyncdefget_group_link(client,group_id):

    chat=awaitclient.get_chat(group_id)
ifchat.username:
        returnf"https://t.me/{chat.username}"
else:
        invite_link=awaitclient.export_chat_invite_link(group_id)
returninvite_link












