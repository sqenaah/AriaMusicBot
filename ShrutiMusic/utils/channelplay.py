utf-8utf-8





















fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimportget_cmode


asyncdefget_channeplayCB(_,command,CallbackQuery):
    ifcommand=="c":
        chat_id=awaitget_cmode(CallbackQuery.message.chat.id)
ifchat_idisNone:
            try:
                returnawaitCallbackQuery.answer(_["setting_7"],show_alert=True)
except:
                return
try:
            channel=(awaitapp.get_chat(chat_id)).title
except:
            try:
                returnawaitCallbackQuery.answer(_["cplay_4"],show_alert=True)
except:
                return
else:
        chat_id=CallbackQuery.message.chat.id
channel=None
returnchat_id,channel












