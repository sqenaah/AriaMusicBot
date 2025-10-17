utf-8utf-8





















importlogging
fromfunctoolsimportwraps
fromtracebackimportformat_excaserr

frompyrogram.errors.exceptions.forbidden_403importChatWriteForbidden
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS


asyncdefmember_permissions(chat_id:int,user_id:int):
    perms=[]
member=(awaitapp.get_chat_member(chat_id,user_id)).privileges
ifnotmember:
        return[]
ifmember.can_post_messages:
        perms.append("can_post_messages")
ifmember.can_edit_messages:
        perms.append("can_edit_messages")
ifmember.can_delete_messages:
        perms.append("can_delete_messages")
ifmember.can_restrict_members:
        perms.append("can_restrict_members")
ifmember.can_promote_members:
        perms.append("can_promote_members")
ifmember.can_change_info:
        perms.append("can_change_info")
ifmember.can_invite_users:
        perms.append("can_invite_users")
ifmember.can_pin_messages:
        perms.append("can_pin_messages")
ifmember.can_manage_video_chats:
        perms.append("can_manage_video_chats")
returnperms


asyncdefauthorised(func,subFunc2,client,message,*args,**kwargs):
    chatID=message.chat.id
try:
        awaitfunc(client,message,*args,**kwargs)
exceptChatWriteForbidden:
        awaitapp.leave_chat(chatID)
exceptExceptionase:
        logging.exception(e)
try:
            awaitmessage.reply_text(str(e.MESSAGE))
exceptAttributeError:
            awaitmessage.reply_text(str(e))
e=err()
print(str(e))
returnsubFunc2


asyncdefunauthorised(
message:Message,permission,subFunc2,bot_lacking_permission=False
):
    chatID=message.chat.id
ifbot_lacking_permission:
        text=(
"I don't have the required permission to perform this action."
+f"\n<b>Permission:</b> <code>{permission}</code>"
)
else:
        text=(
"You don't have the required permission to perform this action."
+f"\n<b>Permission:</b> <code>{permission}</code>"
)
try:
        awaitmessage.reply_text(text)
exceptChatWriteForbidden:
        awaitapp.leave_chat(chatID)
returnsubFunc2


asyncdefbot_permissions(chat_id:int):
    perms=[]
returnawaitmember_permissions(chat_id,app.id)


defadminsOnly(permission):
    defsubFunc(func):
        @wraps(func)
asyncdefsubFunc2(client,message:Message,*args,**kwargs):
            chatID=message.chat.id


bot_perms=awaitbot_permissions(chatID)
ifpermissionnotinbot_perms:
                returnawaitunauthorised(
message,permission,subFunc2,bot_lacking_permission=True
)

ifnotmessage.from_user:

                ifmessage.sender_chatandmessage.sender_chat.id==message.chat.id:
                    returnawaitauthorised(
func,
subFunc2,
client,
message,
*args,
**kwargs,
)
returnawaitunauthorised(message,permission,subFunc2)


userID=message.from_user.id
permissions=awaitmember_permissions(chatID,userID)
ifuserIDnotinSUDOERSandpermissionnotinpermissions:
                returnawaitunauthorised(message,permission,subFunc2)
returnawaitauthorised(func,subFunc2,client,message,*args,**kwargs)

returnsubFunc2

returnsubFunc












