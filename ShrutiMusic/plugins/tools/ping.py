utf-8utf-8





















fromdatetimeimportdatetime

frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utilsimportbot_sys_stats
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.inlineimportsupp_markup
fromconfigimportBANNED_USERS,PING_IMG_URL


@app.on_message(filters.command(["ping","alive"])&~BANNED_USERS)
@language
asyncdefping_com(client,message:Message,_):
    start=datetime.now()
response=awaitmessage.reply_photo(
photo=PING_IMG_URL,
caption=_["ping_1"].format(app.mention),
)
pytgping=awaitNand.ping()
UP,CPU,RAM,DISK=awaitbot_sys_stats()
resp=(datetime.now()-start).microseconds/1000
awaitresponse.edit_text(
_["ping_2"].format(resp,app.mention,UP,RAM,CPU,DISK,pytgping),
reply_markup=supp_markup(_),
)












