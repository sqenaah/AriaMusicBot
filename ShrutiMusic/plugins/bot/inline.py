utf-8utf-8





















frompyrogram.typesimport(
InlineKeyboardButton,
InlineKeyboardMarkup,
InlineQueryResultPhoto,
)
fromyoutubesearchpython.__future__importVideosSearch

fromShrutiMusicimportapp
fromShrutiMusic.utils.inlinequeryimportanswer
fromconfigimportBANNED_USERS


@app.on_inline_query(~BANNED_USERS)
asyncdefinline_query_handler(client,query):
    text=query.query.strip().lower()
answers=[]
iftext.strip()=="":
        try:
            awaitclient.answer_inline_query(query.id,results=answer,cache_time=10)
except:
            return
else:
        a=VideosSearch(text,limit=20)
result=(awaita.next()).get("result")
forxinrange(15):
            title=(result[x]["title"]).title()
duration=result[x]["duration"]
views=result[x]["viewCount"]["short"]
thumbnail=result[x]["thumbnails"][0]["url"].split("?")[0]
channellink=result[x]["channel"]["link"]
channel=result[x]["channel"]["name"]
link=result[x]["link"]
published=result[x]["publishedTime"]
description=f"{views} | {duration} ᴍɪɴᴜᴛᴇs | {channel}  | {published}"
buttons=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="ʏᴏᴜᴛᴜʙᴇ 🎄",
url=link,
)
],
]
)
searched_text=f"""
❄ <b>ᴛɪᴛʟᴇ :</b> <a href={link}>{title}</a>

⏳ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration} ᴍɪɴᴜᴛᴇs
👀 <b>ᴠɪᴇᴡs :</b> <code>{views}</code>
🎥 <b>ᴄʜᴀɴɴᴇʟ :</b> <a href={channellink}>{channel}</a>
⏰ <b>ᴘᴜʙʟɪsʜᴇᴅ ᴏɴ :</b> {published}


<u><b>➻ ɪɴʟɪɴᴇ sᴇᴀʀᴄʜ ᴍᴏᴅᴇ ʙʏ {app.name}</b></u>"""
answers.append(
InlineQueryResultPhoto(
photo_url=thumbnail,
title=title,
thumb_url=thumbnail,
description=description,
caption=searched_text,
reply_markup=buttons,
)
)
try:
            returnawaitclient.answer_inline_query(query.id,results=answers)
except:
            return












