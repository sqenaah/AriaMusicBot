utf-8utf-8importos
fromunidecodeimportunidecode
fromPILimportImageDraw,Image,ImageFont,ImageChops
frompyrogramimport*
frompyrogram.typesimport*
fromloggingimportgetLogger
fromShrutiMusicimportLOGGER
frompyrogram.typesimportMessage
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimport*
fromShrutiMusic.utils.databaseimportdb


try:
    wlcm=db.welcome
except:

    fromShrutiMusic.utils.databaseimportwelcomeaswlcm

LOGGER=getLogger(__name__)

classtemp:
    ME=None
CURRENT=2
CANCEL=False
MELCOW={}
U_NAME=None
B_NAME=None

defcircle(pfp,size=(450,450)):
    pfp=pfp.resize(size,Image.LANCZOS).convert("RGBA")
bigsize=(pfp.size[0]*3,pfp.size[1]*3)
mask=Image.new("L",bigsize,0)
draw=ImageDraw.Draw(mask)
draw.ellipse((0,0)+bigsize,fill=255)
mask=mask.resize(pfp.size,Image.LANCZOS)
mask=ImageChops.darker(mask,pfp.split()[-1])
pfp.putalpha(mask)
returnpfp

defwelcomepic(pic,user,chat,id,uname):
    background=Image.open("ShrutiMusic/assets/welcome.png")
pfp=Image.open(pic).convert("RGBA")
pfp=circle(pfp)
pfp=pfp.resize((450,450))
draw=ImageDraw.Draw(background)
font=ImageFont.truetype('ShrutiMusic/assets/font.ttf',size=45)
font2=ImageFont.truetype('ShrutiMusic/assets/font.ttf',size=90)
draw.text((65,250),f'NAME : {unidecode(user)}',fill="white",font=font)
draw.text((65,340),f'ID : {id}',fill="white",font=font)
draw.text((65,430),f"USERNAME : {uname}",fill="white",font=font)
pfp_position=(767,133)
background.paste(pfp,pfp_position,pfp)
background.save(f"downloads/welcome#{id}.png")
returnf"downloads/welcome#{id}.png"


@app.on_message(filters.command("welcome")&~filters.private)
asyncdefauto_state(_,message):
    usage="**❖ ᴜsᴀɢᴇ ➥** /welcome [on|off]"
iflen(message.command)==1:
        returnawaitmessage.reply_text(usage)

chat_id=message.chat.id
user=awaitapp.get_chat_member(message.chat.id,message.from_user.id)

ifuser.statusin(enums.ChatMemberStatus.ADMINISTRATOR,enums.ChatMemberStatus.OWNER):
        A=awaitwlcm.find_one({"chat_id":chat_id})
state=message.text.split(None,1)[1].strip().lower()

ifstate=="on":
            ifAandnotA.get("disabled",False):
                returnawaitmessage.reply_text("✦ Special Welcome Already Enabled")
awaitwlcm.update_one({"chat_id":chat_id},{"$set":{"disabled":False}},upsert=True)
awaitmessage.reply_text(f"✦ Enabled Special Welcome in {message.chat.title}")

elifstate=="off":
            ifAandA.get("disabled",False):
                returnawaitmessage.reply_text("✦ Special Welcome Already Disabled")
awaitwlcm.update_one({"chat_id":chat_id},{"$set":{"disabled":True}},upsert=True)
awaitmessage.reply_text(f"✦ Disabled Special Welcome in {message.chat.title}")

else:
            awaitmessage.reply_text(usage)
else:
        awaitmessage.reply("✦ Only Admins Can Use This Command")


@app.on_chat_member_updated(filters.group,group=-3)
asyncdefgreet_group(_,member:ChatMemberUpdated):
    chat_id=member.chat.id
A=awaitwlcm.find_one({"chat_id":chat_id})


ifAandA.get("disabled",False):
        return

if(
notmember.new_chat_member
ormember.new_chat_member.statusin{"banned","left","restricted"}
ormember.old_chat_member
):
        return

user=member.new_chat_member.userifmember.new_chat_memberelsemember.from_user
try:
        pic=awaitapp.download_media(
user.photo.big_file_id,file_name=f"pp{user.id}.png"
)
exceptAttributeError:
        pic="ShrutiMusic/assets/upic.png"

if(temp.MELCOW).get(f"welcome-{member.chat.id}")isnotNone:
        try:
            awaittemp.MELCOW[f"welcome-{member.chat.id}"].delete()
exceptExceptionase:
            LOGGER.error(e)

try:
        welcomeimg=welcomepic(
pic,user.first_name,member.chat.title,user.id,user.username
)
temp.MELCOW[f"welcome-{member.chat.id}"]=awaitapp.send_photo(
member.chat.id,
photo=welcomeimg,
caption=f"""
🌸✨ ──────────────────── ✨🌸

         🎊 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ғᴀᴍɪʟʏ</b> 🎊

🌹 <b>ɴᴀᴍᴇ</b> ➤ {user.mention}
🌺 <b>ᴜsᴇʀɴᴀᴍᴇ</b> ➤ @{user.username if user.username else "ɴᴏᴛ sᴇᴛ"}
🆔 <b>ᴜsᴇʀ ɪᴅ</b> ➤ <code>{user.id}</code>
🏠 <b>ɢʀᴏᴜᴘ</b> ➤ {member.chat.title}

═════════════════════════

💕 <b>ᴡᴇ'ʀᴇ sᴏ ʜᴀᴘᴘʏ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ʜᴇʀᴇ!</b> 
🎵 <b>ᴇɴᴊᴏʏ ᴛʜᴇ ʙᴇsᴛ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ</b> 🎵

✨ <b>ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sʜᴀʀᴇ ᴀɴᴅ ᴇɴᴊᴏʏ!</b> ✨

<blockquote><b>💝 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➤ <a href="https://t.me/{app.username}?start=help">Mᴜsɪᴄ ʙᴏᴛs🎶💖</a></b></blockquote>

🌸✨ ──────────────────── ✨🌸
""",
reply_markup=InlineKeyboardMarkup([
[InlineKeyboardButton("🎵 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🎵",url=f"https://t.me/{app.username}?startgroup=True")]
]),
)

exceptExceptionase:
        LOGGER.error(e)

try:
        os.remove(f"downloads/welcome#{user.id}.png")
os.remove(f"downloads/pp{user.id}.png")
exceptException:
        pass












