utf-8utf-8

importrandom

frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportdb
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(
filters.command(["shuffle","cshuffle"])&filters.group&~BANNED_USERS
)
@AdminRightsCheck
asyncdefadmins(Client,message:Message,_,chat_id):
    check=db.get(chat_id)
ifnotcheck:
        returnawaitmessage.reply_text(_["queue_2"])
try:
        popped=check.pop(0)
except:
        returnawaitmessage.reply_text(_["admin_15"],reply_markup=close_markup(_))
check=db.get(chat_id)
ifnotcheck:
        check.insert(0,popped)
returnawaitmessage.reply_text(_["admin_15"],reply_markup=close_markup(_))
random.shuffle(check)
check.insert(0,popped)
awaitmessage.reply_text(
_["admin_16"].format(message.from_user.mention),reply_markup=close_markup(_)
)
