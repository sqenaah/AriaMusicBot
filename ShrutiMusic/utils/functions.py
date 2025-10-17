utf-8utf-8





















fromdatetimeimportdatetime,timedelta
fromreimportfindall
fromreimportsubasre_sub

frompyrogramimporterrors
frompyrogram.enumsimportMessageEntityType
frompyrogram.typesimportMessage

MARKDOWN="""
ʀᴇᴀᴅ ᴛʜᴇ ʙᴇʟᴏᴡ ᴛᴇxᴛ ᴄᴀʀᴇғᴜʟʟʏ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ғᴏʀᴍᴀᴛᴛɪɴɢ ᴡᴏʀᴋs!

<u>sᴜᴘᴘᴏʀᴛᴇᴅ ғɪʟʟɪɴɢs:</u>

{GROUPNAME} - ɢʀᴏᴜᴘ's ɴᴀᴍᴇ
{NAME} - ᴜsᴇʀ ɴᴀᴍᴇ
{ID} - ᴜsᴇʀ ɪᴅ
{FIRSTNAME} - ᴜsᴇʀ ғɪʀsᴛ ɴᴀᴍᴇ 
{SURNAME} - ɪғ ᴜsᴇʀ ʜᴀs sᴜʀɴᴀᴍᴇ sᴏ ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ sᴜʀɴᴀᴍᴇ ᴇʟsᴇ ɴᴏᴛʜɪɴɢ
{USERNAME} - ᴜsᴇʀ ᴜsᴇʀɴᴀᴍᴇ

{TIME} - ᴛᴏᴅᴀʏ  ᴛɪᴍᴇ
{DATE} - ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ 
{WEEKDAY} - ᴛᴏᴅᴀʏ ᴡᴇᴇᴋᴅᴀʏ 

<b><u>NOTE:</u></b> ғɪʟʟɪɴɢs ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ᴡᴇʟᴄᴏᴍᴇ ᴍᴏᴅᴜʟᴇ.

<u>sᴜᴘᴘᴏʀᴛᴇᴅ ғᴏʀᴍᴀᴛᴛɪɴɢ:</u>

<code>**Bold**</code> : ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <b>Bold</b> ᴛᴇxᴛ.
<code>~~strike~~</code>: ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <strike>strike</strike> ᴛᴇxᴛ.
<code>__italic__</code>: ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <i>italic</i> ᴛᴇxᴛ
<code>--underline--</code>: ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <u>underline</u> ᴛᴇxᴛ.
<code>`code words`</code>: ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <code>code</code> ᴛᴇxᴛ.
<code>||spoiler||</code>: ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <spoiler>Spoiler</spoiler> ᴛᴇxᴛ.
<code>[hyperlink](google.com)</code>: ᴛʜɪs ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ <a href='https://www.google.com'>hyperlink</a> text
<code>> hello</code>  ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ ᴀs <blockquote>hello</blockquote>
<b>Note:</b> ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ʙᴏᴛʜ ᴍᴀʀᴋᴅᴏᴡɴ & ʜᴛᴍʟ ᴛᴀɢs.


<u>ʙᴜᴛᴛᴏɴ ғᴏʀᴍᴀᴛᴛɪɴɢ:</u>

- > <blockquote>text ~ [button text, button link]</blockquote>


<u>ᴇxᴀᴍᴘʟᴇ:</u>

<b>example</b>  
<blockquote><i>button with markdown</i> <code>formatting</code> ~ [button text, https://google.com]</blockquote>
"""
WELCOMEHELP="""
/setwelcome - ʀᴇᴘʟʏ ᴛʜɪs ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴀɪɴɪɴɢ ᴄᴏʀʀᴇᴄᴛ
ғᴏʀᴍᴀᴛ ғᴏʀ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ, ᴄʜᴇᴄᴋ ᴇɴᴅ ᴏғ ᴛʜɪs ᴍᴇssᴀɢᴇ.

/delwelcome - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ.
/getwelcome - ɢᴇᴛ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ.

<b>SET_WELCOME -></b>

<b>ᴛᴏ sᴇᴛ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ ᴀs ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ. ᴀᴅᴅ ʏᴏᴜʀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ᴀs ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ. ᴛʜᴇ ᴄᴀᴘᴛɪᴏɴ ᴍᴜsᴇ ʙᴇ ɪɴ ᴛʜᴇ ғᴏʀᴍᴀᴛ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</b>

ғᴏʀ ᴛᴇxᴛ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ. ᴛʜᴇɴ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ 

ᴛʜᴇ ғᴏʀᴍᴀᴛ sʜᴏᴜʟᴅ ʙᴇ sᴏᴍᴇᴛʜɪɴɢ ʟɪᴋᴇ ʙᴇʟᴏᴡ.

{GROUPNAME} - ɢʀᴏᴜᴘ's ɴᴀᴍᴇ
{NAME} - ᴜsᴇʀ ғɪʀsᴛ ɴᴀᴍᴇ + sᴜʀɴᴀᴍᴇ
{ID} - ᴜsᴇʀ ɪᴅ
{FIRSTNAME} - ᴜsᴇʀ ғɪʀsᴛ ɴᴀᴍᴇ 
{SURNAME} - ɪғ ᴜsᴇʀ ʜᴀs sᴜʀɴᴀᴍᴇ sᴏ ᴛʜɪs ᴡɪʟʟ sʜᴏᴡ sᴜʀɴᴀᴍᴇ ᴇʟsᴇ ɴᴏᴛʜɪɴɢ
{USERNAME} - ᴜsᴇʀ ᴜsᴇʀɴᴀᴍᴇ

{TIME} - ᴛᴏᴅᴀʏ  ᴛɪᴍᴇ
{DATE} - ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ 
{WEEKDAY} - ᴛᴏᴅᴀʏ ᴡᴇᴇᴋᴅᴀʏ 


~ #This separater (~) should be there between text and buttons, remove this comment also

button=[Duck, https://duckduckgo.com]
button2=[Github, https://github.com]

<b>NOTES -></b>

ᴄʜᴇᴄᴋᴏᴜᴛ /markdownhelp ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ғᴏʀᴍᴀᴛᴛɪɴɢs ᴀɴᴅ ᴏᴛʜᴇʀ sʏɴᴛᴀx.
"""


defget_urls_from_text(text:str)->bool:
    regex=r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
return[x[0]forxinfindall(regex,str(text))]


defextract_text_and_keyb(ikb,text:str,row_width:int=2):
    keyboard={}
try:
        text=text.strip()
iftext.startswith("`"):
            text=text[1:]
iftext.endswith("`"):
            text=text[:-1]

if"~~"intext:
            text=text.replace("~~","¤¤")
text,keyb=text.split("~")
if"¤¤"intext:
            text=text.replace("¤¤","~~")

keyb=findall(r"\[.+\,.+\]",keyb)
forbtn_strinkeyb:
            btn_str=re_sub(r"[\[\]]","",btn_str)
btn_str=btn_str.split(",")
btn_txt,btn_url=btn_str[0],btn_str[1].strip()

ifnotget_urls_from_text(btn_url):
                continue
keyboard[btn_txt]=btn_url
keyboard=ikb(keyboard,row_width)
exceptException:
        return
returntext,keyboard


asyncdefcheck_format(ikb,raw_text:str):
    keyb=findall(r"\[.+\,.+\]",raw_text)
ifkeybandnot"~"inraw_text:
        raw_text=raw_text.replace("button=","\n~\nbutton=")
returnraw_text
if"~"inraw_textandkeyb:
        ifnotextract_text_and_keyb(ikb,raw_text):
            return""
else:
            returnraw_text
else:
        returnraw_text


asyncdefget_data_and_name(replied_message,message):
    text=message.text.markdownifmessage.textelsemessage.caption.markdown
name=text.split(None,1)[1].strip()
text=name.split(" ",1)
iflen(text)>1:
        name=text[0]
data=text[1].strip()
ifreplied_messageand(replied_message.stickerorreplied_message.video_note):
            data=None
else:
        ifreplied_messageand(replied_message.stickerorreplied_message.video_note):
            data=None
elif(
replied_messageandnotreplied_message.textandnotreplied_message.caption
):
            data=None
else:
            data=(
replied_message.text.markdown
ifreplied_message.text
elsereplied_message.caption.markdown
)
command=message.command[0]
match=f"/{command} "+name
ifnotmessage.reply_to_messageandmessage.text:
                ifmatch==data:
                    data="error"
elifnotmessage.reply_to_messageandnotmessage.text:
                ifmatch==data:
                    data=None
returndata,name


asyncdefextract_userid(message,text:str):
    """
    NOT TO BE USED OUTSIDE THIS FILE
    """

defis_int(text:str):
        try:
            int(text)
exceptValueError:
            returnFalse
returnTrue

text=text.strip()

ifis_int(text):
        returnint(text)

entities=message.entities
app=message._client
iflen(entities)<2:
        return(awaitapp.get_users(text)).id
entity=entities[1]
ifentity.type==MessageEntityType.MENTION:
        return(awaitapp.get_users(text)).id
ifentity.type==MessageEntityType.TEXT_MENTION:
        returnentity.user.id
returnNone


asyncdefextract_user_and_reason(message,sender_chat=False):
    args=message.text.strip().split()
text=message.text
user=None
reason=None

try:
        ifmessage.reply_to_message:
            reply=message.reply_to_message

ifnotreply.from_user:
                if(
reply.sender_chat
andreply.sender_chat!=message.chat.id
andsender_chat
):
                    id_=reply.sender_chat.id
else:
                    returnNone,None
else:
                id_=reply.from_user.id

iflen(args)<2:
                reason=None
else:
                reason=text.split(None,1)[1]
returnid_,reason


iflen(args)==2:
            user=text.split(None,1)[1]
returnawaitextract_userid(message,user),None


iflen(args)>2:
            user,reason=text.split(None,2)[1:]
returnawaitextract_userid(message,user),reason

returnuser,reason

excepterrors.UsernameInvalid:
        return"",""


asyncdefextract_user(message):
    return(awaitextract_user_and_reason(message))[0]


defget_file_id_from_message(
message,
max_file_size=3145728,
mime_types=["image/png","image/jpeg"],
):
    file_id=None
ifmessage.document:
        ifint(message.document.file_size)>max_file_size:
            return

mime_type=message.document.mime_type

ifmime_typesandmime_typenotinmime_types:
            return
file_id=message.document.file_id

ifmessage.sticker:
        ifmessage.sticker.is_animated:
            ifnotmessage.sticker.thumbs:
                return
file_id=message.sticker.thumbs[0].file_id
else:
            file_id=message.sticker.file_id

ifmessage.photo:
        file_id=message.photo.file_id

ifmessage.animation:
        ifnotmessage.animation.thumbs:
            return
file_id=message.animation.thumbs[0].file_id

ifmessage.video:
        ifnotmessage.video.thumbs:
            return
file_id=message.video.thumbs[0].file_id
returnfile_id


asyncdeftime_converter(message:Message,time_value:str)->datetime:
    unit=["m","h","d"]
check_unit="".join(list(filter(time_value[-1].lower().endswith,unit)))
currunt_time=datetime.now()
time_digit=time_value[:-1]
ifnottime_digit.isdigit():
        returnawaitmessage.reply_text("Incorrect time specified")
ifcheck_unit=="m":
        temp_time=currunt_time+timedelta(minutes=int(time_digit))
elifcheck_unit=="h":
        temp_time=currunt_time+timedelta(hours=int(time_digit))
elifcheck_unit=="d":
        temp_time=currunt_time+timedelta(days=int(time_digit))
else:
        returnawaitmessage.reply_text("Incorrect time specified.")
returntemp_time












