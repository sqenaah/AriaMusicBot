utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.utilsimportextract_user,int_to_alpha
fromShrutiMusic.utils.databaseimport(
delete_authuser,
get_authuser,
get_authuser_names,
save_authuser,
)
fromShrutiMusic.utils.decoratorsimportAdminActual,language
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS,adminlist


@app.on_message(filters.command("auth")&filters.group&~BANNED_USERS)
@AdminActual
asyncdefauth(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
token=awaitint_to_alpha(user.id)
_check=awaitget_authuser_names(message.chat.id)
count=len(_check)
ifint(count)==25:
        returnawaitmessage.reply_text(_["auth_1"])
iftokennotin_check:
        assis={
"auth_user_id":user.id,
"auth_name":user.first_name,
"admin_id":message.from_user.id,
"admin_name":message.from_user.first_name,
}
get=adminlist.get(message.chat.id)
ifget:
            ifuser.idnotinget:
                get.append(user.id)
awaitsave_authuser(message.chat.id,token,assis)
returnawaitmessage.reply_text(_["auth_2"].format(user.mention))
else:
        returnawaitmessage.reply_text(_["auth_3"].format(user.mention))


@app.on_message(filters.command("unauth")&filters.group&~BANNED_USERS)
@AdminActual
asyncdefunauthusers(client,message:Message,_):
    ifnotmessage.reply_to_message:
        iflen(message.command)!=2:
            returnawaitmessage.reply_text(_["general_1"])
user=awaitextract_user(message)
token=awaitint_to_alpha(user.id)
deleted=awaitdelete_authuser(message.chat.id,token)
get=adminlist.get(message.chat.id)
ifget:
        ifuser.idinget:
            get.remove(user.id)
ifdeleted:
        returnawaitmessage.reply_text(_["auth_4"].format(user.mention))
else:
        returnawaitmessage.reply_text(_["auth_5"].format(user.mention))


@app.on_message(
filters.command(["authlist","authusers"])&filters.group&~BANNED_USERS
)
@language
asyncdefauthusers(client,message:Message,_):
    _wtf=awaitget_authuser_names(message.chat.id)
ifnot_wtf:
        returnawaitmessage.reply_text(_["setting_4"])
else:
        j=0
mystic=awaitmessage.reply_text(_["auth_6"])
text=_["auth_7"].format(message.chat.title)
forummin_wtf:
            _umm=awaitget_authuser(message.chat.id,umm)
user_id=_umm["auth_user_id"]
admin_id=_umm["admin_id"]
admin_name=_umm["admin_name"]
try:
                user=(awaitapp.get_users(user_id)).first_name
j+=1
except:
                continue
text+=f"{j}➤ {user}[<code>{user_id}</code>]\n"
text+=f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
awaitmystic.edit_text(text,reply_markup=close_markup(_))












