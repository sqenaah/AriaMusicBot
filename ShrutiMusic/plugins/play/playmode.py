utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardMarkup,Message

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_playmode,get_playtype,is_nonadmin_chat
fromShrutiMusic.utils.decoratorsimportlanguage
fromShrutiMusic.utils.inline.settingsimportplaymode_users_markup
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["playmode","mode"])&filters.group&~BANNED_USERS)
@language
asyncdefplaymode_(client,message:Message,_):
    playmode=awaitget_playmode(message.chat.id)
ifplaymode=="Direct":
        Direct=True
else:
        Direct=None
is_non_admin=awaitis_nonadmin_chat(message.chat.id)
ifnotis_non_admin:
        Group=True
else:
        Group=None
playty=awaitget_playtype(message.chat.id)
ifplayty=="Everyone":
        Playtype=None
else:
        Playtype=True
buttons=playmode_users_markup(_,Direct,Group,Playtype)
response=awaitmessage.reply_text(
_["play_22"].format(message.chat.title),
reply_markup=InlineKeyboardMarkup(buttons),
)












