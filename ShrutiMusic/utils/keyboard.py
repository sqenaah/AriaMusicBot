utf-8utf-8





















frompykeyboardimportInlineKeyboard
frompyrogram.typesimportInlineKeyboardButtonasIkb

from.functionsimportget_urls_from_textasis_url


defkeyboard(buttons_list,row_width:int=2):
    buttons=InlineKeyboard(row_width=row_width)
data=[
(
Ikb(text=str(i[0]),callback_data=str(i[1]))
ifnotis_url(i[1])
elseIkb(text=str(i[0]),url=str(i[1]))
)
foriinbuttons_list
]
buttons.add(*data)
returnbuttons


defikb(data:dict,row_width:int=2):
    returnkeyboard(data.items(),row_width=row_width)












