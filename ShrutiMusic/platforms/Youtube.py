utf-8utf-8





















importasyncio
importos
importre
importjson
fromtypingimportUnion

importyt_dlp
frompyrogram.enumsimportMessageEntityType
frompyrogram.typesimportMessage
fromyoutubesearchpython.__future__importVideosSearch

fromShrutiMusic.utils.databaseimportis_on_off
fromShrutiMusic.utils.formattersimporttime_to_seconds

importos
importglob
importrandom
importlogging

defcookie_txt_file():
    folder_path=f"{os.getcwd()}/cookies"
filename=f"{os.getcwd()}/cookies/logs.csv"
txt_files=glob.glob(os.path.join(folder_path,'*.txt'))
ifnottxt_files:
        raiseFileNotFoundError("No .txt files found in the specified folder.")
cookie_txt_file=random.choice(txt_files)
withopen(filename,'a')asfile:
        file.write(f'Choosen File : {cookie_txt_file}\n')
returnf"""cookies/{str(cookie_txt_file).split("/")[-1]}"""


defcheck_existing_file(video_id,file_types=None,media_type=None):
    """Check if file already exists for given video_id and media type"""
iffile_typesisNone:
        file_types=["mp3","m4a","webm","mp4","mkv"]

download_folder="downloads"
ifnotos.path.exists(download_folder):
        os.makedirs(download_folder,exist_ok=True)
returnNone


ifmedia_type=="audio":
        file_types=["mp3","m4a","webm"]
elifmedia_type=="video":
        file_types=["mp4","webm","mkv"]

forextinfile_types:
        file_path=os.path.join(download_folder,f"{video_id}.{ext}")
ifos.path.exists(file_path):
            print(f"File already exists: {file_path}")
returnfile_path

returnNone


asyncdefcheck_file_size(link):
    asyncdefget_format_info(link):
        proc=awaitasyncio.create_subprocess_exec(
"yt-dlp",
"--cookies",cookie_txt_file(),
"-J",
link,
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE
)
stdout,stderr=awaitproc.communicate()
ifproc.returncode!=0:
            print(f'Error:\n{stderr.decode()}')
returnNone
returnjson.loads(stdout.decode())

defparse_size(formats):
        total_size=0
forformatinformats:
            if'filesize'informat:
                total_size+=format['filesize']
returntotal_size

info=awaitget_format_info(link)
ifinfoisNone:
        returnNone

formats=info.get('formats',[])
ifnotformats:
        print("No formats found.")
returnNone

total_size=parse_size(formats)
returntotal_size

asyncdefshell_cmd(cmd):
    proc=awaitasyncio.create_subprocess_shell(
cmd,
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE,
)
out,errorz=awaitproc.communicate()
iferrorz:
        if"unavailable videos are hidden"in(errorz.decode("utf-8")).lower():
            returnout.decode("utf-8")
else:
            returnerrorz.decode("utf-8")
returnout.decode("utf-8")


classYouTubeAPI:
    def__init__(self):
        self.base="https://www.youtube.com/watch?v="
self.regex=r"(?:youtube\.com|youtu\.be)"
self.status="https://www.youtube.com/oembed?url="
self.listbase="https://youtube.com/playlist?list="
self.reg=re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

asyncdefexists(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
ifre.search(self.regex,link):
            returnTrue
else:
            returnFalse

asyncdefurl(self,message_1:Message)->Union[str,None]:
        messages=[message_1]
ifmessage_1.reply_to_message:
            messages.append(message_1.reply_to_message)
text=""
offset=None
length=None
formessageinmessages:
            ifoffset:
                break
ifmessage.entities:
                forentityinmessage.entities:
                    ifentity.type==MessageEntityType.URL:
                        text=message.textormessage.caption
offset,length=entity.offset,entity.length
break
elifmessage.caption_entities:
                forentityinmessage.caption_entities:
                    ifentity.type==MessageEntityType.TEXT_LINK:
                        returnentity.url
ifoffsetin(None,):
            returnNone
returntext[offset:offset+length]

asyncdefdetails(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
results=VideosSearch(link,limit=1)
forresultin(awaitresults.next())["result"]:
            title=result["title"]
duration_min=result["duration"]
thumbnail=result["thumbnails"][0]["url"].split("?")[0]
vidid=result["id"]
ifstr(duration_min)=="None":
                duration_sec=0
else:
                duration_sec=int(time_to_seconds(duration_min))
returntitle,duration_min,duration_sec,thumbnail,vidid

asyncdeftitle(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
results=VideosSearch(link,limit=1)
forresultin(awaitresults.next())["result"]:
            title=result["title"]
returntitle

asyncdefduration(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
results=VideosSearch(link,limit=1)
forresultin(awaitresults.next())["result"]:
            duration=result["duration"]
returnduration

asyncdefthumbnail(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
results=VideosSearch(link,limit=1)
forresultin(awaitresults.next())["result"]:
            thumbnail=result["thumbnails"][0]["url"].split("?")[0]
returnthumbnail

asyncdefvideo(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]

video_id=link.split('v=')[-1].split('&')[0]

existing_file=check_existing_file(video_id,["mp4","webm","mkv"],"video")
ifexisting_file:
            return1,existing_file

proc=awaitasyncio.create_subprocess_exec(
"yt-dlp",
"--cookies",cookie_txt_file(),
"-g",
"-f",
"18/best",
f"{link}",
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE,
)
stdout,stderr=awaitproc.communicate()
ifstdout:
            return1,stdout.decode().split("\n")[0]
else:
            return0,stderr.decode()

asyncdefplaylist(self,link,limit,user_id,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.listbase+link
if"&"inlink:
            link=link.split("&")[0]
playlist=awaitshell_cmd(
f"yt-dlp -i --get-id --flat-playlist --cookies {cookie_txt_file()} --playlist-end {limit} --skip-download {link}"
)
try:
            result=playlist.split("\n")
forkeyinresult:
                ifkey=="":
                    result.remove(key)
except:
            result=[]
returnresult

asyncdeftrack(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
results=VideosSearch(link,limit=1)
forresultin(awaitresults.next())["result"]:
            title=result["title"]
duration_min=result["duration"]
vidid=result["id"]
yturl=result["link"]
thumbnail=result["thumbnails"][0]["url"].split("?")[0]
track_details={
"title":title,
"link":yturl,
"vidid":vidid,
"duration_min":duration_min,
"thumb":thumbnail,
}
returntrack_details,vidid

asyncdefformats(self,link:str,videoid:Union[bool,str]=None):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
ytdl_opts={"quiet":True,"cookiefile":cookie_txt_file()}
ydl=yt_dlp.YoutubeDL(ytdl_opts)
withydl:
            formats_available=[]
r=ydl.extract_info(link,download=False)
forformatinr["formats"]:
                try:
                    str(format["format"])
except:
                    continue
ifnot"dash"instr(format["format"]).lower():
                    try:
                        format["format"]
format["filesize"]
format["format_id"]
format["ext"]
format["format_note"]
except:
                        continue
formats_available.append(
{
"format":format["format"],
"filesize":format["filesize"],
"format_id":format["format_id"],
"ext":format["ext"],
"format_note":format["format_note"],
"yturl":link,
}
)
returnformats_available,link

asyncdefslider(
self,
link:str,
query_type:int,
videoid:Union[bool,str]=None,
):
        ifvideoid:
            link=self.base+link
if"&"inlink:
            link=link.split("&")[0]
a=VideosSearch(link,limit=10)
result=(awaita.next()).get("result")
title=result[query_type]["title"]
duration_min=result[query_type]["duration"]
vidid=result[query_type]["id"]
thumbnail=result[query_type]["thumbnails"][0]["url"].split("?")[0]
returntitle,duration_min,thumbnail,vidid

asyncdefdownload(
self,
link:str,
mystic,
video:Union[bool,str]=None,
videoid:Union[bool,str]=None,
songaudio:Union[bool,str]=None,
songvideo:Union[bool,str]=None,
format_id:Union[bool,str]=None,
title:Union[bool,str]=None,
)->str:
        ifvideoid:
            link=self.base+link

video_id=link.split('v=')[-1].split('&')[0]

loop=asyncio.get_running_loop()

defaudio_dl():
            existing_file=check_existing_file(video_id,["mp3","m4a","webm"],"audio")
ifexisting_file:
                returnexisting_file

ydl_optssx={
"format":"bestaudio[acodec!=opus]/bestaudio",
"outtmpl":"downloads/%(id)s.%(ext)s",
"geo_bypass":True,
"nocheckcertificate":True,
"quiet":True,
"cookiefile":cookie_txt_file(),
"no_warnings":True,
"concurrent_fragment_downloads":8,
"retries":3,
"fragment_retries":3,
"buffersize":16384,
"prefer_ffmpeg":True,
}
x=yt_dlp.YoutubeDL(ydl_optssx)
try:
                info=x.extract_info(link,download=False)
file_path=os.path.join("downloads",f"{info['id']}.{info['ext']}")
ifos.path.exists(file_path):
                    returnfile_path
x.download([link])
returnfile_path
exceptExceptionase:
                print(f"Audio download error: {e}")
returnNone

defvideo_dl():
            existing_file=check_existing_file(video_id,["mp4","webm","mkv"],"video")
ifexisting_file:
                returnexisting_file

ydl_optssx={
"format":"best[height<=720][ext=mp4]/best[height<=480][ext=mp4]/best[ext=mp4]/18/best",
"outtmpl":"downloads/%(id)s.%(ext)s",
"geo_bypass":True,
"nocheckcertificate":True,
"quiet":True,
"cookiefile":cookie_txt_file(),
"no_warnings":True,
"concurrent_fragment_downloads":8,
"retries":3,
"fragment_retries":3,
"buffersize":16384,
"ignoreerrors":False,
}
x=yt_dlp.YoutubeDL(ydl_optssx)
try:
                info=x.extract_info(link,download=False)
ifnotinfo:
                    print("No video info available")
returnNone
file_path=os.path.join("downloads",f"{info['id']}.{info['ext']}")
ifos.path.exists(file_path):
                    returnfile_path
x.download([link])
returnfile_path
exceptExceptionase:
                print(f"Video download error: {e}")
try:
                    ydl_optssx["format"]="worst[ext=mp4]/worst"
x=yt_dlp.YoutubeDL(ydl_optssx)
info=x.extract_info(link,download=False)
ifinfo:
                        file_path=os.path.join("downloads",f"{info['id']}.{info['ext']}")
ifnotos.path.exists(file_path):
                            x.download([link])
returnfile_path
exceptExceptionase2:
                    print(f"Fallback video download failed: {e2}")
returnNone

defsong_video_dl():
            custom_file_path=f"downloads/{title}.mp4"
ifos.path.exists(custom_file_path):
                print(f"Song video already exists: {custom_file_path}")
returncustom_file_path

formats=f"{format_id}+140"
fpath=f"downloads/{title}"
ydl_optssx={
"format":formats,
"outtmpl":fpath,
"geo_bypass":True,
"nocheckcertificate":True,
"quiet":True,
"no_warnings":True,
"cookiefile":cookie_txt_file(),
"prefer_ffmpeg":True,
"merge_output_format":"mp4",
"concurrent_fragment_downloads":8,
"retries":2,
"fragment_retries":2,
}
x=yt_dlp.YoutubeDL(ydl_optssx)
x.download([link])

defsong_audio_dl():
            custom_file_path=f"downloads/{title}.mp3"
ifos.path.exists(custom_file_path):
                print(f"Song audio already exists: {custom_file_path}")
returncustom_file_path

fpath=f"downloads/{title}.%(ext)s"
ydl_optssx={
"format":format_id,
"outtmpl":fpath,
"geo_bypass":True,
"nocheckcertificate":True,
"quiet":True,
"no_warnings":True,
"cookiefile":cookie_txt_file(),
"prefer_ffmpeg":True,
"concurrent_fragment_downloads":8,
"retries":2,
"fragment_retries":2,
"postprocessors":[
{
"key":"FFmpegExtractAudio",
"preferredcodec":"mp3",
"preferredquality":"128",
}
],
}
x=yt_dlp.YoutubeDL(ydl_optssx)
x.download([link])

ifsongvideo:
            awaitloop.run_in_executor(None,song_video_dl)
fpath=f"downloads/{title}.mp4"
returnfpath
elifsongaudio:
            awaitloop.run_in_executor(None,song_audio_dl)
fpath=f"downloads/{title}.mp3"
returnfpath
elifvideo:
            ifawaitis_on_off(1):
                direct=True
downloaded_file=awaitloop.run_in_executor(None,video_dl)
else:
                existing_file=check_existing_file(video_id,["mp4","webm","mkv"],"video")
ifexisting_file:
                    returnexisting_file,False

proc=awaitasyncio.create_subprocess_exec(
"yt-dlp",
"--cookies",cookie_txt_file(),
"-g",
"-f",
"best[height<=720]/18/best",
f"{link}",
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE,
)
stdout,stderr=awaitproc.communicate()
ifstdout:
                    downloaded_file=stdout.decode().split("\n")[0]
direct=False
else:
                   file_size=awaitcheck_file_size(link)
ifnotfile_size:
                     print("None file Size")
return
total_size_mb=file_size/(1024*1024)
iftotal_size_mb>250:
                     print(f"File size {total_size_mb:.2f} MB exceeds the 100MB limit.")
returnNone
direct=True
downloaded_file=awaitloop.run_in_executor(None,video_dl)
else:
            direct=True
downloaded_file=awaitloop.run_in_executor(None,audio_dl)
returndownloaded_file,direct












