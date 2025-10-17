utf-8utf-8





















importos
importrequests
frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup
fromShrutiMusicimportapp


defupload_file(file_path):
    url="https://catbox.moe/user/api.php"
data={"reqtype":"fileupload","json":"true"}
files={"fileToUpload":open(file_path,"rb")}
response=requests.post(url,data=data,files=files)

ifresponse.status_code==200:
        returnTrue,response.text.strip()
else:
        returnFalse,f"Error: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm"]))
asyncdefget_link_group(client,message):
    ifnotmessage.reply_to_message:
        returnawaitmessage.reply_text(
"Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ"
)

media=message.reply_to_message
file_size=0
ifmedia.photo:
        file_size=media.photo.file_size
elifmedia.video:
        file_size=media.video.file_size
elifmedia.document:
        file_size=media.document.file_size

iffile_size>200*1024*1024:
        returnawaitmessage.reply_text("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ᴜɴᴅᴇʀ 200MB.")

try:
        text=awaitmessage.reply("❍ ʜᴏʟᴅ ᴏɴ ʙᴀʙʏ....♡")

asyncdefprogress(current,total):
            try:
                awaittext.edit_text(f"📥 Dᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")
exceptException:
                pass

try:
            local_path=awaitmedia.download(progress=progress)
awaittext.edit_text("📤 Uᴘʟᴏᴀᴅɪɴɢ...")

success,upload_url=upload_file(local_path)

ifsuccess:
                awaittext.edit_text(
f"🌐 | <a href='{upload_url}'>👉 ʏᴏᴜʀ ʟɪɴᴋ ᴛᴀᴘ ʜᴇʀᴇ 👈</a>",
disable_web_page_preview=False,
reply_markup=InlineKeyboardMarkup(
[[InlineKeyboardButton("🌍 ᴘʀᴇss ᴀɴᴅ ʜᴏʟᴅ ᴛᴏ ᴠɪᴇᴡ",url=upload_url)]]
),
)
else:
                awaittext.edit_text(
f"⚠️ Aɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ\n{upload_url}"
)

try:
                os.remove(local_path)
exceptException:
                pass

exceptExceptionase:
            awaittext.edit_text(f"❌ Fɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ\n\n<i>Rᴇᴀsᴏɴ: {e}</i>")
try:
                os.remove(local_path)
exceptException:
                pass
return
exceptException:
        pass


__HELP__="""
**ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

- `/tgm`: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.

**ᴇxᴀᴍᴘʟᴇ:**
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ `/tgm` ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

**ɴᴏᴛᴇ:**
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""

__MODULE__="ᴛᴇʟᴇɢʀᴀᴘʜ"












