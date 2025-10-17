utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimport(
get_lang,
is_maintenance,
maintenance_off,
maintenance_on,
)
fromstringsimportget_string


@app.on_message(filters.command(["maintenance"])&SUDOERS)
asyncdefmaintenance(client,message:Message):
    try:
        language=awaitget_lang(message.chat.id)
_=get_string(language)
except:
        _=get_string("en")
usage=_["maint_1"]
iflen(message.command)!=2:
        returnawaitmessage.reply_text(usage)
state=message.text.split(None,1)[1].strip().lower()
ifstate=="enable":
        ifawaitis_maintenance()isFalse:
            awaitmessage.reply_text(_["maint_4"])
else:
            awaitmaintenance_on()
awaitmessage.reply_text(_["maint_2"].format(app.mention))
elifstate=="disable":
        ifawaitis_maintenance()isFalse:
            awaitmaintenance_off()
awaitmessage.reply_text(_["maint_3"].format(app.mention))
else:
            awaitmessage.reply_text(_["maint_5"])
else:
        awaitmessage.reply_text(usage)












