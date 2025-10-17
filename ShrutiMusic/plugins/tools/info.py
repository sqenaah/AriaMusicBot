utf-8utf-8





















importasyncio
importrandom
importtime
fromtimeimporttime
fromtypingimportOptional,Union

fromPILimportImage,ImageDraw,ImageFont
frompyrogramimportenums,filters

fromShrutiMusicimportapp


user_last_message_time={}
user_command_count={}

SPAM_THRESHOLD=2
SPAM_WINDOW_SECONDS=5

random_photo=[
"https://telegra.ph/file/1949480f01355b4e87d26.jpg",
"https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
"https://telegra.ph/file/a7d663cd2de689b811729.jpg",
"https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
"https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]




get_font=lambdafont_size,font_path:ImageFont.truetype(font_path,font_size)
resize_text=lambdatext_size,text:(
(text[:text_size]+"...").upper()iflen(text)>text_sizeelsetext.upper()
)




asyncdefget_userinfo_img(
bg_path:str,
font_path:str,
user_id:Union[int,str],
profile_path:Optional[str]=None,
):
    bg=Image.open(bg_path)

ifprofile_path:
        img=Image.open(profile_path)
mask=Image.new("L",img.size,0)
draw=ImageDraw.Draw(mask)
draw.pieslice([(0,0),img.size],0,360,fill=255)

circular_img=Image.new("RGBA",img.size,(0,0,0,0))
circular_img.paste(img,(0,0),mask)
resized=circular_img.resize((400,400))
bg.paste(resized,(440,160),resized)

img_draw=ImageDraw.Draw(bg)

img_draw.text(
(529,627),
text=str(user_id).upper(),
font=get_font(46,font_path),
fill=(255,255,255),
)

path=f"downloads/userinfo_img_{user_id}.png"
bg.save(path)
returnpath




bg_path="ShrutiMusic/assets/Nand_Yadu1c.png"
font_path="ShrutiMusic/assets/font.ttf"




INFO_TEXT="""
❅─────✧❅✦❅✧─────❅
            ✦ ᴜsᴇʀ ɪɴғᴏ ✦

➻ ᴜsᴇʀ ɪᴅ ‣ {}
➻ ғɪʀsᴛ ɴᴀᴍᴇ ‣ {}
➻ ʟᴀsᴛ ɴᴀᴍᴇ ‣ {}
➻ ᴜsᴇʀɴᴀᴍᴇ ‣ {}
➻ ᴍᴇɴᴛɪᴏɴ ‣ {}
➻ ʟᴀsᴛ sᴇᴇɴ ‣ {}
➻ ᴅᴄ ɪᴅ ‣ {}
➻ ʙɪᴏ ‣ {}

❅─────✧❅✦❅✧─────❅
"""




asyncdefuserstatus(user_id):
    try:
        user=awaitapp.get_users(user_id)
x=user.status
ifx==enums.UserStatus.RECENTLY:
            return"Recently."
elifx==enums.UserStatus.LAST_WEEK:
            return"Last week."
elifx==enums.UserStatus.LONG_AGO:
            return"Long time ago."
elifx==enums.UserStatus.OFFLINE:
            return"Offline."
elifx==enums.UserStatus.ONLINE:
            return"Online."
except:
        return"**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"





@app.on_message(
filters.command(
["info","userinfo"],prefixes=["/","!","%",",","",".","@","#"]
)
)
asyncdefuserinfo(_,message):
    user_id=message.from_user.id
current_time=time()

last_message_time=user_last_message_time.get(user_id,0)

ifcurrent_time-last_message_time<SPAM_WINDOW_SECONDS:

        user_last_message_time[user_id]=current_time
user_command_count[user_id]=user_command_count.get(user_id,0)+1
ifuser_command_count[user_id]>SPAM_THRESHOLD:

            hu=awaitmessage.reply_text(
f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**"
)
awaitasyncio.sleep(3)
awaithu.delete()
return
else:

        user_command_count[user_id]=1
user_last_message_time[user_id]=current_time

chat_id=message.chat.id
user_id=message.from_user.id

ifnotmessage.reply_to_messageandlen(message.command)==2:
        try:
            user_id=message.text.split(None,1)[1]
user_info=awaitapp.get_chat(user_id)
user=awaitapp.get_users(user_id)
status=awaituserstatus(user.id)
id=user_info.id
dc_id=user.dc_id
first_name=user_info.first_name
last_name=user_info.last_nameifuser_info.last_nameelse"No last name"
username=user_info.usernameifuser_info.usernameelse"No Username"
mention=user.mention
bio=user_info.bioifuser_info.bioelse"No bio set"

ifuser.photo:

                photo=awaitapp.download_media(user.photo.big_file_id)
welcome_photo=awaitget_userinfo_img(
bg_path=bg_path,
font_path=font_path,
user_id=user.id,
profile_path=photo,
)
else:

                welcome_photo=random.choice(random_photo)

awaitapp.send_photo(
chat_id,
photo=welcome_photo,
caption=INFO_TEXT.format(
id,first_name,last_name,username,mention,status,dc_id,bio
),
reply_to_message_id=message.id,
)
exceptExceptionase:
            awaitmessage.reply_text(str(e))

elifnotmessage.reply_to_message:
        try:
            user_info=awaitapp.get_chat(user_id)
user=awaitapp.get_users(user_id)
status=awaituserstatus(user.id)
id=user_info.id
dc_id=user.dc_id
first_name=user_info.first_name
last_name=user_info.last_nameifuser_info.last_nameelse"No last name"
username=user_info.usernameifuser_info.usernameelse"No Username"
mention=user.mention
bio=user_info.bioifuser_info.bioelse"No bio set"

ifuser.photo:

                photo=awaitapp.download_media(user.photo.big_file_id)
welcome_photo=awaitget_userinfo_img(
bg_path=bg_path,
font_path=font_path,
user_id=user.id,
profile_path=photo,
)
else:

                welcome_photo=random.choice(random_photo)

awaitapp.send_photo(
chat_id,
photo=welcome_photo,
caption=INFO_TEXT.format(
id,first_name,last_name,username,mention,status,dc_id,bio
),
reply_to_message_id=message.id,
)
exceptExceptionase:
            awaitmessage.reply_text(str(e))

elifmessage.reply_to_message:
        user_id=message.reply_to_message.from_user.id
try:
            user_info=awaitapp.get_chat(user_id)
user=awaitapp.get_users(user_id)
status=awaituserstatus(user.id)
id=user_info.id
dc_id=user.dc_id
first_name=user_info.first_name
last_name=user_info.last_nameifuser_info.last_nameelse"No last name"
username=user_info.usernameifuser_info.usernameelse"No Username"
mention=user.mention
bio=user_info.bioifuser_info.bioelse"No bio set"

ifuser.photo:

                photo=awaitapp.download_media(user.photo.big_file_id)
welcome_photo=awaitget_userinfo_img(
bg_path=bg_path,
font_path=font_path,
user_id=user.id,
profile_path=photo,
)
else:

                welcome_photo=random.choice(random_photo)

awaitapp.send_photo(
chat_id,
photo=welcome_photo,
caption=INFO_TEXT.format(
id,first_name,last_name,username,mention,status,dc_id,bio
),
reply_to_message_id=message.id,
)
exceptExceptionase:
            awaitmessage.reply_text(str(e))


__MODULE__="Usᴇʀ Iɴғᴏ"
__HELP__="""
/ɪɴғᴏ [ᴜsᴇʀ_ɪᴅ]: Gᴇᴛ ᴅᴇᴛᴀɪᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
/ᴜsᴇʀɪɴғᴏ [ᴜsᴇʀ_ɪᴅ]: Aɪᴀs ғᴏʀ /ɪɴғᴏ.
"""












