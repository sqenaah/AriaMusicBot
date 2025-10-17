utf-8utf-8





















importasyncio
importos
importtime
fromtypingimportUnion

frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Voice

importconfig
fromShrutiMusicimportapp
fromShrutiMusic.utils.formattersimport(
check_duration,
convert_bytes,
get_readable_time,
seconds_to_min,
)


classTeleAPI:
    def__init__(self):
        self.chars_limit=4096
self.sleep=5

asyncdefsend_split_text(self,message,string):
        n=self.chars_limit
out=[(string[i:i+n])foriinrange(0,len(string),n)]
j=0
forxinout:
            ifj<=2:
                j+=1
awaitmessage.reply_text(x,disable_web_page_preview=True)
returnTrue

asyncdefget_link(self,message):
        returnmessage.link

asyncdefget_filename(self,file,audio:Union[bool,str]=None):
        try:
            file_name=file.file_name
iffile_nameisNone:
                file_name="ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴅɪᴏ"ifaudioelse"ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ"
except:
            file_name="ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴅɪᴏ"ifaudioelse"ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ"
returnfile_name

asyncdefget_duration(self,file):
        try:
            dur=seconds_to_min(file.duration)
except:
            dur="Unknown"
returndur

asyncdefget_duration(self,filex,file_path):
        try:
            dur=seconds_to_min(filex.duration)
except:
            try:
                dur=awaitasyncio.get_event_loop().run_in_executor(
None,check_duration,file_path
)
dur=seconds_to_min(dur)
except:
                return"Unknown"
returndur

asyncdefget_filepath(
self,
audio:Union[bool,str]=None,
video:Union[bool,str]=None,
):
        ifaudio:
            try:
                file_name=(
audio.file_unique_id
+"."
+(
(audio.file_name.split(".")[-1])
if(notisinstance(audio,Voice))
else"ogg"
)
)
except:
                file_name=audio.file_unique_id+"."+"ogg"
file_name=os.path.join(os.path.realpath("downloads"),file_name)
ifvideo:
            try:
                file_name=(
video.file_unique_id+"."+(video.file_name.split(".")[-1])
)
except:
                file_name=video.file_unique_id+"."+"mp4"
file_name=os.path.join(os.path.realpath("downloads"),file_name)
returnfile_name

asyncdefdownload(self,_,message,mystic,fname):
        lower=[0,8,17,38,64,77,96]
higher=[5,10,20,40,66,80,99]
checker=[5,10,20,40,66,80,99]
speed_counter={}
ifos.path.exists(fname):
            returnTrue

asyncdefdown_load():
            asyncdefprogress(current,total):
                ifcurrent==total:
                    return
current_time=time.time()
start_time=speed_counter.get(message.id)
check_time=current_time-start_time
upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="ᴄᴀɴᴄᴇʟ",
callback_data="stop_downloading",
),
]
]
)
percentage=current*100/total
percentage=str(round(percentage,2))
speed=current/check_time
eta=int((total-current)/speed)
eta=get_readable_time(eta)
ifnoteta:
                    eta="0 sᴇᴄᴏɴᴅs"
total_size=convert_bytes(total)
completed_size=convert_bytes(current)
speed=convert_bytes(speed)
percentage=int((percentage.split("."))[0])
forcounterinrange(7):
                    low=int(lower[counter])
high=int(higher[counter])
check=int(checker[counter])
iflow<percentage<=high:
                        ifhigh==check:
                            try:
                                awaitmystic.edit_text(
text=_["tg_1"].format(
app.mention,
total_size,
completed_size,
percentage[:5],
speed,
eta,
),
reply_markup=upl,
)
checker[counter]=100
except:
                                pass

speed_counter[message.id]=time.time()
try:
                awaitapp.download_media(
message.reply_to_message,
file_name=fname,
progress=progress,
)
try:
                    elapsed=get_readable_time(
int(int(time.time())-int(speed_counter[message.id]))
)
except:
                    elapsed="0 sᴇᴄᴏɴᴅs"
awaitmystic.edit_text(_["tg_2"].format(elapsed))
except:
                awaitmystic.edit_text(_["tg_3"])

task=asyncio.create_task(down_load())
config.lyrical[mystic.id]=task
awaittask
verify=config.lyrical.get(mystic.id)
ifnotverify:
            returnFalse
config.lyrical.pop(mystic.id)
returnTrue












