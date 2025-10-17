utf-8utf-8

frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utils.databaseimportset_loop
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(
filters.command(["end","stop","cend","cstop"])&filters.group&~BANNED_USERS
)
@AdminRightsCheck
asyncdefstop_music(cli,message:Message,_,chat_id):
    ifnotlen(message.command)==1:
        return
awaitNand.stop_stream(chat_id)
awaitset_loop(chat_id,0)
awaitmessage.reply_text(
_["admin_5"].format(message.from_user.mention),reply_markup=close_markup(_)
)
