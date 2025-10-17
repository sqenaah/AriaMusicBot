utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utils.databaseimportis_music_playing,music_on
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["resume","cresume"])&filters.group&~BANNED_USERS)
@AdminRightsCheck
asyncdefresume_com(cli,message:Message,_,chat_id):
    ifawaitis_music_playing(chat_id):
        returnawaitmessage.reply_text(_["admin_3"])
awaitmusic_on(chat_id)
awaitNand.resume_stream(chat_id)
awaitmessage.reply_text(
_["admin_4"].format(message.from_user.mention),reply_markup=close_markup(_)
)












