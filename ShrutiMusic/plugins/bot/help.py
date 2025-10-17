utf-8utf-8

fromtypingimportUnion

frompyrogramimportfilters,types
frompyrogram.typesimportInlineKeyboardMarkup,Message

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_lang
fromShrutiMusic.utils.decorators.languageimportLanguageStart,languageCB
fromShrutiMusic.utils.inline.helpimport(
help_back_markup,
private_help_panel,
help_pannel_page1,
help_pannel_page2,
help_pannel_page3,
help_pannel_page4,
)
fromconfigimportBANNED_USERS,START_IMG_URL,SUPPORT_GROUP
fromstringsimportget_string,helpers


@app.on_message(filters.command(["help"])&filters.private&~BANNED_USERS)
@app.on_callback_query(filters.regex("help_page_1")&~BANNED_USERS)
asyncdefhelper_private(
client:app,update:Union[types.Message,types.CallbackQuery]
):
    is_callback=isinstance(update,types.CallbackQuery)
ifis_callback:
        try:
            awaitupdate.answer()
except:
            pass
chat_id=update.message.chat.id
language=awaitget_lang(chat_id)
_=get_string(language)
fromShrutiMusic.utils.inline.helpimporthelp_pannel_page1
keyboard=help_pannel_page1(_,True)
awaitupdate.edit_message_text(
_["help_1"].format(SUPPORT_GROUP),reply_markup=keyboard
)
else:
        try:
            awaitupdate.delete()
except:
            pass
language=awaitget_lang(update.chat.id)
_=get_string(language)
fromShrutiMusic.utils.inline.helpimporthelp_pannel_page1
keyboard=help_pannel_page1(_)
awaitupdate.reply_photo(
photo=START_IMG_URL,
caption=_["help_1"].format(SUPPORT_GROUP),
reply_markup=keyboard,
)


@app.on_message(filters.command(["help"])&filters.group&~BANNED_USERS)
@LanguageStart
asyncdefhelp_com_group(client,message:Message,_):
    fromShrutiMusic.utils.inline.helpimportprivate_help_panel
keyboard=private_help_panel(_)
awaitmessage.reply_text(_["help_2"],reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback")&~BANNED_USERS)
@languageCB
asyncdefhelper_cb(client,CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
cb=callback_data.split(None,1)[1]


defget_keyboard_for(cb):
        page1=["hb1","hb2","hb3","hb4","hb5","hb6","hb7","hb8","hb9","hb10"]
page2=["hb11","hb12","hb13","hb14","hb15","hb17","hb18","hb19","hb20","hb21"]
page3=["hb22","hb23","hb24","hb25","hb26","hb27","hb28","hb29","hb30","hb31"]
page4=["hb32","hb33","hb34","hb35","hb36","hb37","hb38"]

ifcbinpage1:
            returnhelp_back_markup(_,page=1)
elifcbinpage2:
            returnhelp_back_markup(_,page=2)
elifcbinpage3:
            returnhelp_back_markup(_,page=3)
elifcbinpage4:
            returnhelp_back_markup(_,page=4)
else:
            returnhelp_back_markup(_,page=1)


ifcb=="hb1":
        awaitCallbackQuery.edit_message_text(helpers.HELP_1,reply_markup=get_keyboard_for(cb))
elifcb=="hb2":
        awaitCallbackQuery.edit_message_text(helpers.HELP_2,reply_markup=get_keyboard_for(cb))
elifcb=="hb3":
        awaitCallbackQuery.edit_message_text(helpers.HELP_3,reply_markup=get_keyboard_for(cb))
elifcb=="hb4":
        awaitCallbackQuery.edit_message_text(helpers.HELP_4,reply_markup=get_keyboard_for(cb))
elifcb=="hb5":
        awaitCallbackQuery.edit_message_text(helpers.HELP_5,reply_markup=get_keyboard_for(cb))
elifcb=="hb6":
        awaitCallbackQuery.edit_message_text(helpers.HELP_6,reply_markup=get_keyboard_for(cb))
elifcb=="hb7":
        awaitCallbackQuery.edit_message_text(helpers.HELP_7,reply_markup=get_keyboard_for(cb))
elifcb=="hb8":
        awaitCallbackQuery.edit_message_text(helpers.HELP_8,reply_markup=get_keyboard_for(cb))
elifcb=="hb9":
        awaitCallbackQuery.edit_message_text(helpers.HELP_9,reply_markup=get_keyboard_for(cb))
elifcb=="hb10":
        awaitCallbackQuery.edit_message_text(helpers.HELP_10,reply_markup=get_keyboard_for(cb))
elifcb=="hb11":
        awaitCallbackQuery.edit_message_text(helpers.HELP_11,reply_markup=get_keyboard_for(cb))
elifcb=="hb12":
        awaitCallbackQuery.edit_message_text(helpers.HELP_12,reply_markup=get_keyboard_for(cb))
elifcb=="hb13":
        awaitCallbackQuery.edit_message_text(helpers.HELP_13,reply_markup=get_keyboard_for(cb))
elifcb=="hb14":
        awaitCallbackQuery.edit_message_text(helpers.HELP_14,reply_markup=get_keyboard_for(cb))
elifcb=="hb15":
        awaitCallbackQuery.edit_message_text(helpers.HELP_15,reply_markup=get_keyboard_for(cb))
elifcb=="hb16":
        awaitCallbackQuery.edit_message_text(helpers.HELP_16,reply_markup=get_keyboard_for(cb))
elifcb=="hb17":
        awaitCallbackQuery.edit_message_text(helpers.HELP_17,reply_markup=get_keyboard_for(cb))
elifcb=="hb18":
        awaitCallbackQuery.edit_message_text(helpers.HELP_18,reply_markup=get_keyboard_for(cb))
elifcb=="hb19":
        awaitCallbackQuery.edit_message_text(helpers.HELP_19,reply_markup=get_keyboard_for(cb))
elifcb=="hb20":
        awaitCallbackQuery.edit_message_text(helpers.HELP_20,reply_markup=get_keyboard_for(cb))
elifcb=="hb21":
        awaitCallbackQuery.edit_message_text(helpers.HELP_21,reply_markup=get_keyboard_for(cb))
elifcb=="hb22":
        awaitCallbackQuery.edit_message_text(helpers.HELP_22,reply_markup=get_keyboard_for(cb))
elifcb=="hb23":
        awaitCallbackQuery.edit_message_text(helpers.HELP_23,reply_markup=get_keyboard_for(cb))
elifcb=="hb24":
        awaitCallbackQuery.edit_message_text(helpers.HELP_24,reply_markup=get_keyboard_for(cb))
elifcb=="hb25":
        awaitCallbackQuery.edit_message_text(helpers.HELP_25,reply_markup=get_keyboard_for(cb))
elifcb=="hb26":
        awaitCallbackQuery.edit_message_text(helpers.HELP_26,reply_markup=get_keyboard_for(cb))
elifcb=="hb27":
        awaitCallbackQuery.edit_message_text(helpers.HELP_27,reply_markup=get_keyboard_for(cb))
elifcb=="hb28":
        awaitCallbackQuery.edit_message_text(helpers.HELP_28,reply_markup=get_keyboard_for(cb))
elifcb=="hb29":
        awaitCallbackQuery.edit_message_text(helpers.HELP_29,reply_markup=get_keyboard_for(cb))
elifcb=="hb30":
        awaitCallbackQuery.edit_message_text(helpers.HELP_30,reply_markup=get_keyboard_for(cb))
elifcb=="hb31":
        awaitCallbackQuery.edit_message_text(helpers.HELP_31,reply_markup=get_keyboard_for(cb))
elifcb=="hb32":
        awaitCallbackQuery.edit_message_text(helpers.HELP_32,reply_markup=get_keyboard_for(cb))
elifcb=="hb33":
        awaitCallbackQuery.edit_message_text(helpers.HELP_33,reply_markup=get_keyboard_for(cb))
elifcb=="hb34":
        awaitCallbackQuery.edit_message_text(helpers.HELP_34,reply_markup=get_keyboard_for(cb))
elifcb=="hb35":
        awaitCallbackQuery.edit_message_text(helpers.HELP_35,reply_markup=get_keyboard_for(cb))
elifcb=="hb36":
        awaitCallbackQuery.edit_message_text(helpers.HELP_36,reply_markup=get_keyboard_for(cb))
elifcb=="hb37":
        awaitCallbackQuery.edit_message_text(helpers.HELP_37,reply_markup=get_keyboard_for(cb))
elifcb=="hb38":
        awaitCallbackQuery.edit_message_text(helpers.HELP_38,reply_markup=get_keyboard_for(cb))













