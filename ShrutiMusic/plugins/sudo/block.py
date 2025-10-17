utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportadd_gban_user,remove_gban_user
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.extractionimportextract_user
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["block"])&SUDOERS)
@language
asyncdefuseradd(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
ifuser.idinBANNED_USERS:
        returnawaitmessage.reply_text(_["block_1"].format(user.mention))
awaitadd_gban_user(user.id)
BANNED_USERS.add(user.id)
awaitmessage.reply_text(_["block_2"].format(user.mention))


@app.on_message(filters.command(["unblock"])&SUDOERS)
@language
asyncdefuserdel(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
ifuser.idnotinBANNED_USERS:
        returnawaitmessage.reply_text(_["block_3"].format(user.mention))
awaitremove_gban_user(user.id)
BANNED_USERS.remove(user.id)
awaitmessage.reply_text(_["block_4"].format(user.mention))


@app.on_message(filters.command(["blocked","blockedusers","blusers"])&SUDOERS)
@language
asyncdefsudoers_list(client,message:Message,_):
    ifnotBANNED_USERS:
        returnawaitmessage.reply_text(_["block_5"])
mystic=awaitmessage.reply_text(_["block_6"])
msg=_["block_7"]
count=0
forusersinBANNED_USERS:
        try:
            user=awaitapp.get_users(users)
user=user.first_nameifnotuser.mentionelseuser.mention
count+=1
except:
            continue
msg+=f"{count}➤ {user}\n"
ifcount==0:
        returnawaitmystic.edit_text(_["block_5"])
else:
        returnawaitmystic.edit_text(msg)












