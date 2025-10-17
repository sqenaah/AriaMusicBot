utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utils.databaseimportis_music_playing,music_off
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["pause","cpause"])&filters.group&~BANNED_USERS)
@AdminRightsCheck
asyncdefpause_admin(cli,message:Message,_,chat_id):
    ifnotawaitis_music_playing(chat_id):
        returnawaitmessage.reply_text(_["admin_1"])
awaitmusic_off(chat_id)
awaitNand.pause_stream(chat_id)
awaitmessage.reply_text(
_["admin_2"].format(message.from_user.mention),reply_markup=close_markup(_)
)












