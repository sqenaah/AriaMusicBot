utf-8utf-8





















importasyncio

frompyrogramimportfilters
frompyrogram.errorsimportFloodWait
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utilsimportget_readable_time
fromShrutiMusic.utils.databaseimport(
add_banned_user,
get_banned_count,
get_banned_users,
get_served_chats,
is_banned_user,
remove_banned_user,
)
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.extractionimportextract_user
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["gban","globalban"])&SUDOERS)
@language
asyncdefglobal_ban(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
ifuser.id==message.from_user.id:
        returnawaitmessage.reply_text(_["gban_1"])
elifuser.id==app.id:
        returnawaitmessage.reply_text(_["gban_2"])
elifuser.idinSUDOERS:
        returnawaitmessage.reply_text(_["gban_3"])
is_gbanned=awaitis_banned_user(user.id)
ifis_gbanned:
        returnawaitmessage.reply_text(_["gban_4"].format(user.mention))
ifuser.idnotinBANNED_USERS:
        BANNED_USERS.add(user.id)
served_chats=[]
chats=awaitget_served_chats()
forchatinchats:
        served_chats.append(int(chat["chat_id"]))
time_expected=get_readable_time(len(served_chats))
mystic=awaitmessage.reply_text(_["gban_5"].format(user.mention,time_expected))
number_of_chats=0
forchat_idinserved_chats:
        try:
            awaitapp.ban_chat_member(chat_id,user.id)
number_of_chats+=1
exceptFloodWaitasfw:
            awaitasyncio.sleep(int(fw.value))
except:
            continue
awaitadd_banned_user(user.id)
awaitmessage.reply_text(
_["gban_6"].format(
app.mention,
message.chat.title,
message.chat.id,
user.mention,
user.id,
message.from_user.mention,
number_of_chats,
)
)
awaitmystic.delete()


@app.on_message(filters.command(["ungban"])&SUDOERS)
@language
asyncdefglobal_un(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
is_gbanned=awaitis_banned_user(user.id)
ifnotis_gbanned:
        returnawaitmessage.reply_text(_["gban_7"].format(user.mention))
ifuser.idinBANNED_USERS:
        BANNED_USERS.remove(user.id)
served_chats=[]
chats=awaitget_served_chats()
forchatinchats:
        served_chats.append(int(chat["chat_id"]))
time_expected=get_readable_time(len(served_chats))
mystic=awaitmessage.reply_text(_["gban_8"].format(user.mention,time_expected))
number_of_chats=0
forchat_idinserved_chats:
        try:
            awaitapp.unban_chat_member(chat_id,user.id)
number_of_chats+=1
exceptFloodWaitasfw:
            awaitasyncio.sleep(int(fw.value))
except:
            continue
awaitremove_banned_user(user.id)
awaitmessage.reply_text(_["gban_9"].format(user.mention,number_of_chats))
awaitmystic.delete()


@app.on_message(filters.command(["gbannedusers","gbanlist"])&SUDOERS)
@language
asyncdefgbanned_list(client,message:Message,_):
    counts=awaitget_banned_count()
ifcounts==0:
        returnawaitmessage.reply_text(_["gban_10"])
mystic=awaitmessage.reply_text(_["gban_11"])
msg=_["gban_12"]
count=0
users=awaitget_banned_users()
foruser_idinusers:
        count+=1
try:
            user=awaitapp.get_users(user_id)
user=user.first_nameifnotuser.mentionelseuser.mention
msg+=f"{count}➤ {user}\n"
exceptException:
            msg+=f"{count}➤ {user_id}\n"
continue
ifcount==0:
        returnawaitmystic.edit_text(_["gban_10"])
else:
        returnawaitmystic.edit_text(msg)












