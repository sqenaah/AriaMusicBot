utf-8utf-8fromdatetimeimportdatetime,timedelta
importpytz
importos
importrandom
frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup
frompyrogram.enumsimportChatType
fromtelegraphimportupload_file
fromPILimportImage,ImageDraw
importrequests

fromShrutiMusic.utilsimportget_image,get_couple,save_couple
fromShrutiMusicimportapp



defget_today_date():
    timezone=pytz.timezone("Asia/Kolkata")
now=datetime.now(timezone)
returnnow.strftime("%d/%m/%Y")





defget_todmorrow_date():
    timezone=pytz.timezone("Asia/Kolkata")
tomorrow=datetime.now(timezone)+timedelta(days=1)
returntomorrow.strftime("%d/%m/%Y")





defdownload_image(url,path):
    response=requests.get(url)
ifresponse.status_code==200:
        withopen(path,"wb")asf:
            f.write(response.content)
returnpath



tomorrow=get_todmorrow_date()
today=get_today_date()


@app.on_message(filters.command(["couple","couples"]))
asyncdefctest(_,message):
    cid=message.chat.id
ifmessage.chat.type==ChatType.PRIVATE:
        returnawaitmessage.reply_text("Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")

p1_path="downloads/pfp.png"
p2_path="downloads/pfp1.png"
test_image_path=f"downloads/test_{cid}.png"
cppic_path="downloads/cppic.png"

try:
        is_selected=awaitget_couple(cid,today)
ifnotis_selected:
            msg=awaitmessage.reply_text("❣️")
list_of_users=[]

asyncforiinapp.get_chat_members(message.chat.id,limit=50):
                ifnoti.user.is_botandnoti.user.is_deleted:
                    list_of_users.append(i.user.id)

c1_id=random.choice(list_of_users)
c2_id=random.choice(list_of_users)
whilec1_id==c2_id:
                c1_id=random.choice(list_of_users)

photo1=(awaitapp.get_chat(c1_id)).photo
photo2=(awaitapp.get_chat(c2_id)).photo

N1=(awaitapp.get_users(c1_id)).mention
N2=(awaitapp.get_users(c2_id)).mention

try:
                p1=awaitapp.download_media(photo1.big_file_id,file_name=p1_path)
exceptException:
                p1=download_image(
"https://telegra.ph/file/05aa686cf52fc666184bf.jpg",p1_path
)
try:
                p2=awaitapp.download_media(photo2.big_file_id,file_name=p2_path)
exceptException:
                p2=download_image(
"https://telegra.ph/file/05aa686cf52fc666184bf.jpg",p2_path
)

img1=Image.open(p1)
img2=Image.open(p2)

background_image_path=download_image(
"https://telegra.ph/file/96f36504f149e5680741a.jpg",cppic_path
)
img=Image.open(background_image_path)

img1=img1.resize((437,437))
img2=img2.resize((437,437))

mask=Image.new("L",img1.size,0)
draw=ImageDraw.Draw(mask)
draw.ellipse((0,0)+img1.size,fill=255)

mask1=Image.new("L",img2.size,0)
draw=ImageDraw.Draw(mask1)
draw.ellipse((0,0)+img2.size,fill=255)

img1.putalpha(mask)
img2.putalpha(mask1)

draw=ImageDraw.Draw(img)

img.paste(img1,(116,160),img1)
img.paste(img2,(789,160),img2)

img.save(test_image_path)

TXT=f"""
<b>Tᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ:

{N1} + {N2} = 💚

Nᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow}!!</b>
            """

awaitmessage.reply_photo(
test_image_path,
caption=TXT,
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="Aᴅᴅ ᴍᴇ 🌋",
url=f"https://t.me/{app.username}?startgroup=true",
)
]
]
),
)

awaitmsg.delete()
a=upload_file(test_image_path)
forxina:
                img_url="https://graph.org/"+x
couple={"c1_id":c1_id,"c2_id":c2_id}
awaitsave_couple(cid,today,couple,img_url)

else:
            msg=awaitmessage.reply_text("❣️")
b=awaitget_image(cid)
c1_id=int(is_selected["c1_id"])
c2_id=int(is_selected["c2_id"])
c1_name=(awaitapp.get_users(c1_id)).first_name
c2_name=(awaitapp.get_users(c2_id)).first_name

TXT=f"""
<b>Tᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ 🎉:

[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❣️

Nᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow}!!</b>
            """
awaitmessage.reply_photo(
b,
caption=TXT,
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="Aᴅᴅ ᴍᴇ🌋",
url=f"https://t.me/{app.username}?startgroup=true",
)
]
]
),
)
awaitmsg.delete()

exceptExceptionase:
        print(str(e))
finally:
        try:
            os.remove(p1_path)
os.remove(p2_path)
os.remove(test_image_path)
os.remove(cppic_path)
exceptExceptionascleanup_error:
            print(f"Error during cleanup: {cleanup_error}")



