frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup

fromconfigimportSUPPORT_GROUP


defbotplaylist_markup(_):
    buttons=[
[
InlineKeyboardButton(text=_["S_B_9"],url=SUPPORT_GROUP),
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close"),
],
]
returnbuttons


defclose_markup(_):
    upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
]
]
)
returnupl


defsupp_markup(_):
    upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=_["S_B_9"],
url=SUPPORT_GROUP,
),
]
]
)
returnupl
