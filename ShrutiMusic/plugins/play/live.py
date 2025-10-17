utf-8utf-8





















frompyrogramimportfilters

fromShrutiMusicimportYouTube,app
fromShrutiMusic.utils.channelplayimportget_channeplayCB
fromShrutiMusic.utils.decorators.languageimportlanguageCB
fromShrutiMusic.utils.stream.streamimportstream
fromconfigimportBANNED_USERS


@app.on_callback_query(filters.regex("LiveStream")&~BANNED_USERS)
@languageCB
asyncdefplay_live_stream(client,CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
callback_request=callback_data.split(None,1)[1]
vidid,user_id,mode,cplay,fplay=callback_request.split("|")
ifCallbackQuery.from_user.id!=int(user_id):
        try:
            returnawaitCallbackQuery.answer(_["playcb_1"],show_alert=True)
except:
            return
try:
        chat_id,channel=awaitget_channeplayCB(_,cplay,CallbackQuery)
except:
        return
video=Trueifmode=="v"elseNone
user_name=CallbackQuery.from_user.first_name
awaitCallbackQuery.message.delete()
try:
        awaitCallbackQuery.answer()
except:
        pass
mystic=awaitCallbackQuery.message.reply_text(
_["play_2"].format(channel)ifchannelelse_["play_1"]
)
try:
        details,track_id=awaitYouTube.track(vidid,True)
except:
        returnawaitmystic.edit_text(_["play_3"])
ffplay=Trueiffplay=="f"elseNone
ifnotdetails["duration_min"]:
        try:
            awaitstream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
CallbackQuery.message.chat.id,
video,
streamtype="live",
forceplay=ffplay,
)
exceptExceptionase:
            print(f"Error: {e}")
ex_type=type(e).__name__
err=eifex_type=="AssistantErr"else_["general_2"].format(ex_type)
returnawaitmystic.edit_text(err)
else:
        returnawaitmystic.edit_text("» ɴᴏᴛ ᴀ ʟɪᴠᴇ sᴛʀᴇᴀᴍ.")
awaitmystic.delete()












