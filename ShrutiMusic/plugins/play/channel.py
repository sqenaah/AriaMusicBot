utf-8utf-8





















frompyrogramimportfilters
frompyrogram.enumsimportChatMembersFilter,ChatMemberStatus,ChatType
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportset_cmode
fromShrutiMusic.utils.decorators.adminsimportAdminActual
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["channelplay"])&filters.group&~BANNED_USERS)
@AdminActual
asyncdefplaymode_(client,message:Message,_):
    iflen(message.command)<2:
        returnawaitmessage.reply_text(_["cplay_1"].format(message.chat.title))
query=message.text.split(None,2)[1].lower().strip()
if(str(query)).lower()=="disable":
        awaitset_cmode(message.chat.id,None)
returnawaitmessage.reply_text(_["cplay_7"])
elifstr(query)=="linked":
        chat=awaitapp.get_chat(message.chat.id)
ifchat.linked_chat:
            chat_id=chat.linked_chat.id
awaitset_cmode(message.chat.id,chat_id)
returnawaitmessage.reply_text(
_["cplay_3"].format(chat.linked_chat.title,chat.linked_chat.id)
)
else:
            returnawaitmessage.reply_text(_["cplay_2"])
else:
        try:
            chat=awaitapp.get_chat(query)
except:
            returnawaitmessage.reply_text(_["cplay_4"])
ifchat.type!=ChatType.CHANNEL:
            returnawaitmessage.reply_text(_["cplay_5"])
try:
            asyncforuserinapp.get_chat_members(
chat.id,filter=ChatMembersFilter.ADMINISTRATORS
):
                ifuser.status==ChatMemberStatus.OWNER:
                    cusn=user.user.username
crid=user.user.id
except:
            returnawaitmessage.reply_text(_["cplay_4"])
ifcrid!=message.from_user.id:
            returnawaitmessage.reply_text(_["cplay_6"].format(chat.title,cusn))
awaitset_cmode(message.chat.id,chat.id)
returnawaitmessage.reply_text(_["cplay_3"].format(chat.title,chat.id))












