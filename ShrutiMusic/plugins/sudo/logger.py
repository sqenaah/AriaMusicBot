utf-8utf-8





















frompyrogramimportfilters

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportadd_off,add_on
fromShrutiMusic.utils.decorators.languageimportlanguage


@app.on_message(filters.command(["logger"])&SUDOERS)
@language
asyncdeflogger(client,message,_):
    usage=_["log_1"]
iflen(message.command)!=2:
        returnawaitmessage.reply_text(usage)
state=message.text.split(None,1)[1].strip().lower()
ifstate=="enable":
        awaitadd_on(2)
awaitmessage.reply_text(_["log_2"])
elifstate=="disable":
        awaitadd_off(2)
awaitmessage.reply_text(_["log_3"])
else:
        awaitmessage.reply_text(usage)

@app.on_message(filters.command(["cookies"])&SUDOERS)
@language
asyncdeflogger(client,message,_):
    awaitmessage.reply_document("cookies/logs.csv")
awaitmessage.reply_text("Please check given file to cookies file choosing logs...")












