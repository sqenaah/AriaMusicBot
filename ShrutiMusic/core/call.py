utf-8utf-8





















importasyncio
importos
fromdatetimeimportdatetime,timedelta
fromtypingimportUnion

frompyrogramimportClient
frompyrogram.typesimportInlineKeyboardMarkup
frompytgcallsimportPyTgCalls,StreamType
frompytgcalls.exceptionsimport(
AlreadyJoinedError,
NoActiveGroupCall,
TelegramServerError,
)
frompytgcalls.typesimportUpdate
frompytgcalls.types.input_streamimportAudioPiped,AudioVideoPiped
frompytgcalls.types.input_stream.qualityimportHighQualityAudio,MediumQualityVideo
frompytgcalls.types.streamimportStreamAudioEnded

importconfig
fromShrutiMusicimportLOGGER,YouTube,app
fromShrutiMusic.miscimportdb
fromShrutiMusic.utils.databaseimport(
add_active_chat,
add_active_video_chat,
get_lang,
get_loop,
group_assistant,
is_autoend,
music_on,
remove_active_chat,
remove_active_video_chat,
set_loop,
)
fromShrutiMusic.utils.exceptionsimportAssistantErr
fromShrutiMusic.utils.formattersimportcheck_duration,seconds_to_min,speed_converter
fromShrutiMusic.utils.inline.playimportstream_markup
fromShrutiMusic.utils.stream.autoclearimportauto_clean
fromShrutiMusic.utils.thumbnailsimportgen_thumb
fromstringsimportget_string

autoend={}
counter={}


asyncdef_clear_(chat_id):
    db[chat_id]=[]
awaitremove_active_video_chat(chat_id)
awaitremove_active_chat(chat_id)


classCall(PyTgCalls):
    def__init__(self):
        self.userbot1=Client(
name="NandAss1",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING1),
)
self.one=PyTgCalls(
self.userbot1,
cache_duration=100,
)
self.userbot2=Client(
name="NandAss2",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING2),
)
self.two=PyTgCalls(
self.userbot2,
cache_duration=100,
)
self.userbot3=Client(
name="NandAss3",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING3),
)
self.three=PyTgCalls(
self.userbot3,
cache_duration=100,
)
self.userbot4=Client(
name="NandAss4",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING4),
)
self.four=PyTgCalls(
self.userbot4,
cache_duration=100,
)
self.userbot5=Client(
name="NandAss5",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING5),
)
self.five=PyTgCalls(
self.userbot5,
cache_duration=100,
)

asyncdefpause_stream(self,chat_id:int):
        assistant=awaitgroup_assistant(self,chat_id)
awaitassistant.pause_stream(chat_id)

asyncdefresume_stream(self,chat_id:int):
        assistant=awaitgroup_assistant(self,chat_id)
awaitassistant.resume_stream(chat_id)

asyncdefstop_stream(self,chat_id:int):
        assistant=awaitgroup_assistant(self,chat_id)
try:
            await_clear_(chat_id)
awaitassistant.leave_group_call(chat_id)
except:
            pass

asyncdefstop_stream_force(self,chat_id:int):
        try:
            ifconfig.STRING1:
                awaitself.one.leave_group_call(chat_id)
except:
            pass
try:
            ifconfig.STRING2:
                awaitself.two.leave_group_call(chat_id)
except:
            pass
try:
            ifconfig.STRING3:
                awaitself.three.leave_group_call(chat_id)
except:
            pass
try:
            ifconfig.STRING4:
                awaitself.four.leave_group_call(chat_id)
except:
            pass
try:
            ifconfig.STRING5:
                awaitself.five.leave_group_call(chat_id)
except:
            pass
try:
            await_clear_(chat_id)
except:
            pass

asyncdefspeedup_stream(self,chat_id:int,file_path,speed,playing):
        assistant=awaitgroup_assistant(self,chat_id)
ifstr(speed)!=str("1.0"):
            base=os.path.basename(file_path)
chatdir=os.path.join(os.getcwd(),"playback",str(speed))
ifnotos.path.isdir(chatdir):
                os.makedirs(chatdir)
out=os.path.join(chatdir,base)
ifnotos.path.isfile(out):
                ifstr(speed)==str("0.5"):
                    vs=2.0
ifstr(speed)==str("0.75"):
                    vs=1.35
ifstr(speed)==str("1.5"):
                    vs=0.68
ifstr(speed)==str("2.0"):
                    vs=0.5
proc=awaitasyncio.create_subprocess_shell(
cmd=(
"ffmpeg "
"-i "
f"{file_path} "
"-filter:v "
f"setpts={vs}*PTS "
"-filter:a "
f"atempo={speed} "
f"{out}"
),
stdin=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE,
)
awaitproc.communicate()
else:
                pass
else:
            out=file_path
dur=awaitasyncio.get_event_loop().run_in_executor(None,check_duration,out)
dur=int(dur)
played,con_seconds=speed_converter(playing[0]["played"],speed)
duration=seconds_to_min(dur)
stream=(
AudioVideoPiped(
out,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
additional_ffmpeg_parameters=f"-ss {played} -to {duration}",
)
ifplaying[0]["streamtype"]=="video"
elseAudioPiped(
out,
audio_parameters=HighQualityAudio(),
additional_ffmpeg_parameters=f"-ss {played} -to {duration}",
)
)
ifstr(db[chat_id][0]["file"])==str(file_path):
            awaitassistant.change_stream(chat_id,stream)
else:
            raiseAssistantErr("Umm")
ifstr(db[chat_id][0]["file"])==str(file_path):
            exis=(playing[0]).get("old_dur")
ifnotexis:
                db[chat_id][0]["old_dur"]=db[chat_id][0]["dur"]
db[chat_id][0]["old_second"]=db[chat_id][0]["seconds"]
db[chat_id][0]["played"]=con_seconds
db[chat_id][0]["dur"]=duration
db[chat_id][0]["seconds"]=dur
db[chat_id][0]["speed_path"]=out
db[chat_id][0]["speed"]=speed

asyncdefforce_stop_stream(self,chat_id:int):
        assistant=awaitgroup_assistant(self,chat_id)
try:
            check=db.get(chat_id)
check.pop(0)
except:
            pass
awaitremove_active_video_chat(chat_id)
awaitremove_active_chat(chat_id)
try:
            awaitassistant.leave_group_call(chat_id)
except:
            pass

asyncdefskip_stream(
self,
chat_id:int,
link:str,
video:Union[bool,str]=None,
image:Union[bool,str]=None,
):
        assistant=awaitgroup_assistant(self,chat_id)
ifvideo:
            stream=AudioVideoPiped(
link,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
else:
            stream=AudioPiped(link,audio_parameters=HighQualityAudio())
awaitassistant.change_stream(
chat_id,
stream,
)

asyncdefseek_stream(self,chat_id,file_path,to_seek,duration,mode):
        assistant=awaitgroup_assistant(self,chat_id)
stream=(
AudioVideoPiped(
file_path,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
)
ifmode=="video"
elseAudioPiped(
file_path,
audio_parameters=HighQualityAudio(),
additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
)
)
awaitassistant.change_stream(chat_id,stream)

asyncdefstream_call(self,link):
        assistant=awaitgroup_assistant(self,config.LOG_GROUP_ID)
awaitassistant.join_group_call(
config.LOG_GROUP_ID,
AudioVideoPiped(link),
stream_type=StreamType().pulse_stream,
)
awaitasyncio.sleep(0.2)
awaitassistant.leave_group_call(config.LOG_GROUP_ID)

asyncdefjoin_call(
self,
chat_id:int,
original_chat_id:int,
link,
video:Union[bool,str]=None,
image:Union[bool,str]=None,
):
        assistant=awaitgroup_assistant(self,chat_id)
language=awaitget_lang(chat_id)
_=get_string(language)
ifvideo:
            stream=AudioVideoPiped(
link,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
else:
            stream=(
AudioVideoPiped(
link,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
ifvideo
elseAudioPiped(link,audio_parameters=HighQualityAudio())
)
try:
            awaitassistant.join_group_call(
chat_id,
stream,
stream_type=StreamType().pulse_stream,
)
exceptNoActiveGroupCall:
            raiseAssistantErr(_["call_8"])
exceptAlreadyJoinedError:
            raiseAssistantErr(_["call_9"])
exceptTelegramServerError:
            raiseAssistantErr(_["call_10"])
awaitadd_active_chat(chat_id)
awaitmusic_on(chat_id)
ifvideo:
            awaitadd_active_video_chat(chat_id)
ifawaitis_autoend():
            counter[chat_id]={}
users=len(awaitassistant.get_participants(chat_id))
ifusers==1:
                autoend[chat_id]=datetime.now()+timedelta(minutes=1)

asyncdefchange_stream(self,client,chat_id):
        check=db.get(chat_id)
popped=None
loop=awaitget_loop(chat_id)
try:
            ifloop==0:
                popped=check.pop(0)
else:
                loop=loop-1
awaitset_loop(chat_id,loop)
awaitauto_clean(popped)
ifnotcheck:
                await_clear_(chat_id)
returnawaitclient.leave_group_call(chat_id)
except:
            try:
                await_clear_(chat_id)
returnawaitclient.leave_group_call(chat_id)
except:
                return
else:
            queued=check[0]["file"]
language=awaitget_lang(chat_id)
_=get_string(language)
title=(check[0]["title"]).title()
user=check[0]["by"]
original_chat_id=check[0]["chat_id"]
streamtype=check[0]["streamtype"]
videoid=check[0]["vidid"]
db[chat_id][0]["played"]=0
exis=(check[0]).get("old_dur")
ifexis:
                db[chat_id][0]["dur"]=exis
db[chat_id][0]["seconds"]=check[0]["old_second"]
db[chat_id][0]["speed_path"]=None
db[chat_id][0]["speed"]=1.0
video=Trueifstr(streamtype)=="video"elseFalse
if"live_"inqueued:
                n,link=awaitYouTube.video(videoid,True)
ifn==0:
                    returnawaitapp.send_message(
original_chat_id,
text=_["call_6"],
)
ifvideo:
                    stream=AudioVideoPiped(
link,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
else:
                    stream=AudioPiped(
link,
audio_parameters=HighQualityAudio(),
)
try:
                    awaitclient.change_stream(chat_id,stream)
exceptException:
                    returnawaitapp.send_message(
original_chat_id,
text=_["call_6"],
)
img=awaitgen_thumb(videoid)
button=stream_markup(_,chat_id)
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
elif"vid_"inqueued:
                mystic=awaitapp.send_message(original_chat_id,_["call_7"])
try:
                    file_path,direct=awaitYouTube.download(
videoid,
mystic,
videoid=True,
video=Trueifstr(streamtype)=="video"elseFalse,
)
except:
                    returnawaitmystic.edit_text(
_["call_6"],disable_web_page_preview=True
)
ifvideo:
                    stream=AudioVideoPiped(
file_path,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
else:
                    stream=AudioPiped(
file_path,
audio_parameters=HighQualityAudio(),
)
try:
                    awaitclient.change_stream(chat_id,stream)
except:
                    returnawaitapp.send_message(
original_chat_id,
text=_["call_6"],
)
img=awaitgen_thumb(videoid)
button=stream_markup(_,chat_id)
awaitmystic.delete()
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"
elif"index_"inqueued:
                stream=(
AudioVideoPiped(
videoid,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
ifstr(streamtype)=="video"
elseAudioPiped(videoid,audio_parameters=HighQualityAudio())
)
try:
                    awaitclient.change_stream(chat_id,stream)
except:
                    returnawaitapp.send_message(
original_chat_id,
text=_["call_6"],
)
button=stream_markup(_,chat_id)
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=config.STREAM_IMG_URL,
caption=_["stream_2"].format(user),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
else:
                ifvideo:
                    stream=AudioVideoPiped(
queued,
audio_parameters=HighQualityAudio(),
video_parameters=MediumQualityVideo(),
)
else:
                    stream=AudioPiped(
queued,
audio_parameters=HighQualityAudio(),
)
try:
                    awaitclient.change_stream(chat_id,stream)
except:
                    returnawaitapp.send_message(
original_chat_id,
text=_["call_6"],
)
ifvideoid=="telegram":
                    button=stream_markup(_,chat_id)
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=config.TELEGRAM_AUDIO_URL
ifstr(streamtype)=="audio"
elseconfig.TELEGRAM_VIDEO_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],check[0]["dur"],user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
elifvideoid=="soundcloud":
                    button=stream_markup(_,chat_id)
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=config.SOUNCLOUD_IMG_URL,
caption=_["stream_1"].format(
config.SUPPORT_GROUP,title[:23],check[0]["dur"],user
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="tg"
else:
                    img=awaitgen_thumb(videoid)
button=stream_markup(_,chat_id)
run=awaitapp.send_photo(
chat_id=original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{videoid}",
title[:23],
check[0]["dur"],
user,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"]=run
db[chat_id][0]["markup"]="stream"

asyncdefping(self):
        pings=[]
ifconfig.STRING1:
            pings.append(awaitself.one.ping)
ifconfig.STRING2:
            pings.append(awaitself.two.ping)
ifconfig.STRING3:
            pings.append(awaitself.three.ping)
ifconfig.STRING4:
            pings.append(awaitself.four.ping)
ifconfig.STRING5:
            pings.append(awaitself.five.ping)
returnstr(round(sum(pings)/len(pings),3))

asyncdefstart(self):
        LOGGER(__name__).info("Starting PyTgCalls Client...\n")
ifconfig.STRING1:
            awaitself.one.start()
ifconfig.STRING2:
            awaitself.two.start()
ifconfig.STRING3:
            awaitself.three.start()
ifconfig.STRING4:
            awaitself.four.start()
ifconfig.STRING5:
            awaitself.five.start()

asyncdefdecorators(self):
        @self.one.on_kicked()
@self.two.on_kicked()
@self.three.on_kicked()
@self.four.on_kicked()
@self.five.on_kicked()
@self.one.on_closed_voice_chat()
@self.two.on_closed_voice_chat()
@self.three.on_closed_voice_chat()
@self.four.on_closed_voice_chat()
@self.five.on_closed_voice_chat()
@self.one.on_left()
@self.two.on_left()
@self.three.on_left()
@self.four.on_left()
@self.five.on_left()
asyncdefstream_services_handler(_,chat_id:int):
            awaitself.stop_stream(chat_id)

@self.one.on_stream_end()
@self.two.on_stream_end()
@self.three.on_stream_end()
@self.four.on_stream_end()
@self.five.on_stream_end()
asyncdefstream_end_handler1(client,update:Update):
            ifnotisinstance(update,StreamAudioEnded):
                return
awaitself.change_stream(client,update.chat_id)


Nand=Call()












