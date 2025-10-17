utf-8utf-8





















fromtypingimportUnion

frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup


defqueue_markup(
_,
DURATION,
CPLAY,
videoid,
played:Union[bool,int]=None,
dur:Union[bool,int]=None,
):
    not_dur=[
[
InlineKeyboardButton(
text=_["QU_B_1"],
callback_data=f"GetQueued {CPLAY}|{videoid}",
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
]
]
dur=[
[
InlineKeyboardButton(
text=_["QU_B_2"].format(played,dur),
callback_data="GetTimer",
)
],
[
InlineKeyboardButton(
text=_["QU_B_1"],
callback_data=f"GetQueued {CPLAY}|{videoid}",
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
],
]
upl=InlineKeyboardMarkup(not_durifDURATION=="Unknown"elsedur)
returnupl


defqueue_back_markup(_,CPLAY):
    upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],
callback_data=f"queue_back_timer {CPLAY}",
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
]
]
)
returnupl


defaq_markup(_,chat_id):
    buttons=[
[
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
],
]
returnbuttons












