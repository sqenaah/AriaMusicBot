fromtypingimportUnion

frompyrogram.typesimportInlineKeyboardButton


defsetting_markup(_):
    buttons=[
[
InlineKeyboardButton(text=_["ST_B_1"],callback_data="AU"),
InlineKeyboardButton(text=_["ST_B_3"],callback_data="LG"),
],
[
InlineKeyboardButton(text=_["ST_B_2"],callback_data="PM"),
],
[
InlineKeyboardButton(text=_["ST_B_4"],callback_data="VM"),
],
[
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close"),
],
]
returnbuttons


defvote_mode_markup(_,current,mode:Union[bool,str]=None):
    buttons=[
[
InlineKeyboardButton(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜",callback_data="VOTEANSWER"),
InlineKeyboardButton(
text=_["ST_B_5"]ifmode==Trueelse_["ST_B_6"],
callback_data="VOMODECHANGE",
),
],
[
InlineKeyboardButton(text="-2",callback_data="FERRARIUDTI M"),
InlineKeyboardButton(
text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
callback_data="ANSWERVOMODE",
),
InlineKeyboardButton(text="+2",callback_data="FERRARIUDTI A"),
],
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],
callback_data="settings_helper",
),
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close"),
],
]
returnbuttons


defauth_users_markup(_,status:Union[bool,str]=None):
    buttons=[
[
InlineKeyboardButton(text=_["ST_B_7"],callback_data="AUTHANSWER"),
InlineKeyboardButton(
text=_["ST_B_8"]ifstatus==Trueelse_["ST_B_9"],
callback_data="AUTH",
),
],
[
InlineKeyboardButton(text=_["ST_B_1"],callback_data="AUTHLIST"),
],
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],
callback_data="settings_helper",
),
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close"),
],
]
returnbuttons


defplaymode_users_markup(
_,
Direct:Union[bool,str]=None,
Group:Union[bool,str]=None,
Playtype:Union[bool,str]=None,
):
    buttons=[
[
InlineKeyboardButton(text=_["ST_B_10"],callback_data="SEARCHANSWER"),
InlineKeyboardButton(
text=_["ST_B_11"]ifDirect==Trueelse_["ST_B_12"],
callback_data="MODECHANGE",
),
],
[
InlineKeyboardButton(text=_["ST_B_13"],callback_data="AUTHANSWER"),
InlineKeyboardButton(
text=_["ST_B_8"]ifGroup==Trueelse_["ST_B_9"],
callback_data="CHANNELMODECHANGE",
),
],
[
InlineKeyboardButton(text=_["ST_B_14"],callback_data="PLAYTYPEANSWER"),
InlineKeyboardButton(
text=_["ST_B_8"]ifPlaytype==Trueelse_["ST_B_9"],
callback_data="PLAYTYPECHANGE",
),
],
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],
callback_data="settings_helper",
),
InlineKeyboardButton(text=_["CLOSE_BUTTON"],callback_data="close"),
],
]
returnbuttons
