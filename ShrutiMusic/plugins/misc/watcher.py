utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand

welcome=20
close=30


@app.on_message(filters.video_chat_started,group=welcome)
@app.on_message(filters.video_chat_ended,group=close)
asyncdefwelcome(_,message:Message):
    awaitNand.stop_stream_force(message.chat.id)












