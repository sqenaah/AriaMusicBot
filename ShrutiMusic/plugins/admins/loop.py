utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_loop,set_loop
fromShrutiMusic.utils.decoratorsimportAdminRightsCheck
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["loop","cloop"])&filters.group&~BANNED_USERS)
@AdminRightsCheck
asyncdefadmins(cli,message:Message,_,chat_id):
    usage=_["admin_17"]
iflen(message.command)!=2:
        returnawaitmessage.reply_text(usage)
state=message.text.split(None,1)[1].strip()
ifstate.isnumeric():
        state=int(state)
if1<=state<=10:
            got=awaitget_loop(chat_id)
ifgot!=0:
                state=got+state
ifint(state)>10:
                state=10
awaitset_loop(chat_id,state)
returnawaitmessage.reply_text(
text=_["admin_18"].format(state,message.from_user.mention),
reply_markup=close_markup(_),
)
else:
            returnawaitmessage.reply_text(_["admin_17"])
elifstate.lower()=="enable":
        awaitset_loop(chat_id,10)
returnawaitmessage.reply_text(
text=_["admin_18"].format(state,message.from_user.mention),
reply_markup=close_markup(_),
)
elifstate.lower()=="disable":
        awaitset_loop(chat_id,0)
returnawaitmessage.reply_text(
_["admin_19"].format(message.from_user.mention),
reply_markup=close_markup(_),
)
else:
        returnawaitmessage.reply_text(usage)












