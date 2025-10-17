utf-8utf-8





















frompykeyboardimportInlineKeyboard
frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,Message

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_lang,set_lang
fromShrutiMusic.utils.decoratorsimportActualAdminCB,language,languageCB
fromconfigimportBANNED_USERS
fromstringsimportget_string,languages_present


deflanuages_keyboard(_):
    keyboard=InlineKeyboard(row_width=2)
keyboard.add(
*[
(
InlineKeyboardButton(
text=languages_present[i],
callback_data=f"languages:{i}",
)
)
foriinlanguages_present
]
)
keyboard.row(
InlineKeyboardButton(
text=_["BACK_BUTTON"],
callback_data=f"settingsback_helper",
),
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data=f"close"),
)
returnkeyboard


@app.on_message(filters.command(["lang","setlang","language"])&~BANNED_USERS)
@language
asyncdeflangs_command(client,message:Message,_):
    keyboard=lanuages_keyboard(_)
awaitmessage.reply_text(
_["lang_1"],
reply_markup=keyboard,
)


@app.on_callback_query(filters.regex("LG")&~BANNED_USERS)
@languageCB
asyncdeflanuagecb(client,CallbackQuery,_):
    try:
        awaitCallbackQuery.answer()
except:
        pass
keyboard=lanuages_keyboard(_)
returnawaitCallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"languages:(.*?)")&~BANNED_USERS)
@ActualAdminCB
asyncdeflanguage_markup(client,CallbackQuery,_):
    langauge=(CallbackQuery.data).split(":")[1]
old=awaitget_lang(CallbackQuery.message.chat.id)
ifstr(old)==str(langauge):
        returnawaitCallbackQuery.answer(_["lang_4"],show_alert=True)
try:
        _=get_string(langauge)
awaitCallbackQuery.answer(_["lang_2"],show_alert=True)
except:
        _=get_string(old)
returnawaitCallbackQuery.answer(
_["lang_3"],
show_alert=True,
)
awaitset_lang(CallbackQuery.message.chat.id,langauge)
keyboard=lanuages_keyboard(_)
returnawaitCallbackQuery.edit_message_reply_markup(reply_markup=keyboard)












