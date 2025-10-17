importjson
importsubprocess


defget_readable_time(seconds:int)->str:
    count=0
ping_time=""
time_list=[]
time_suffix_list=["s","ᴍ","ʜ","ᴅᴀʏs"]
whilecount<4:
        count+=1
ifcount<3:
            remainder,result=divmod(seconds,60)
else:
            remainder,result=divmod(seconds,24)
ifseconds==0andremainder==0:
            break
time_list.append(int(result))
seconds=int(remainder)
foriinrange(len(time_list)):
        time_list[i]=str(time_list[i])+time_suffix_list[i]
iflen(time_list)==4:
        ping_time+=time_list.pop()+", "
time_list.reverse()
ping_time+=":".join(time_list)
returnping_time


defconvert_bytes(size:float)->str:
    """humanize size"""
ifnotsize:
        return""
power=1024
t_n=0
power_dict={0:" ",1:"Ki",2:"Mi",3:"Gi",4:"Ti"}
whilesize>power:
        size/=power
t_n+=1
return"{:.2f} {}B".format(size,power_dict[t_n])


asyncdefint_to_alpha(user_id:int)->str:
    alphabet=["a","b","c","d","e","f","g","h","i","j"]
text=""
user_id=str(user_id)
foriinuser_id:
        text+=alphabet[int(i)]
returntext


asyncdefalpha_to_int(user_id_alphabet:str)->int:
    alphabet=["a","b","c","d","e","f","g","h","i","j"]
user_id=""
foriinuser_id_alphabet:
        index=alphabet.index(i)
user_id+=str(index)
user_id=int(user_id)
returnuser_id


deftime_to_seconds(time):
    stringt=str(time)
returnsum(int(x)*60**ifori,xinenumerate(reversed(stringt.split(":"))))


defseconds_to_min(seconds):
    ifsecondsisnotNone:
        seconds=int(seconds)
d,h,m,s=(
seconds//(3600*24),
seconds//3600%24,
seconds%3600//60,
seconds%3600%60,
)
ifd>0:
            return"{:02d}:{:02d}:{:02d}:{:02d}".format(d,h,m,s)
elifh>0:
            return"{:02d}:{:02d}:{:02d}".format(h,m,s)
elifm>0:
            return"{:02d}:{:02d}".format(m,s)
elifs>0:
            return"00:{:02d}".format(s)
return"-"


defspeed_converter(seconds,speed):
    ifstr(speed)==str("0.5"):
        seconds=seconds*2
ifstr(speed)==str("0.75"):
        seconds=seconds+((50*seconds)//100)
ifstr(speed)==str("1.5"):
        seconds=seconds-((25*seconds)//100)
ifstr(speed)==str("2.0"):
        seconds=seconds-((50*seconds)//100)
collect=seconds
ifsecondsisnotNone:
        seconds=int(seconds)
d,h,m,s=(
seconds//(3600*24),
seconds//3600%24,
seconds%3600//60,
seconds%3600%60,
)
ifd>0:
            convert="{:02d}:{:02d}:{:02d}:{:02d}".format(d,h,m,s)
returnconvert,collect
elifh>0:
            convert="{:02d}:{:02d}:{:02d}".format(h,m,s)
returnconvert,collect
elifm>0:
            convert="{:02d}:{:02d}".format(m,s)
returnconvert,collect
elifs>0:
            convert="00:{:02d}".format(s)
returnconvert,collect
return"-"


defcheck_duration(file_path):
    command=[
"ffprobe",
"-loglevel",
"quiet",
"-print_format",
"json",
"-show_format",
"-show_streams",
file_path,
]

pipe=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
out,err=pipe.communicate()
_json=json.loads(out)

if"format"in_json:
        if"duration"in_json["format"]:
            returnfloat(_json["format"]["duration"])

if"streams"in_json:
        forsin_json["streams"]:
            if"duration"ins:
                returnfloat(s["duration"])

return"Unknown"


formats=[
"webm",
"mkv",
"flv",
"vob",
"ogv",
"ogg",
"rrc",
"gifv",
"mng",
"mov",
"avi",
"qt",
"wmv",
"yuv",
"rm",
"asf",
"amv",
"mp4",
"m4p",
"m4v",
"mpg",
"mp2",
"mpeg",
"mpe",
"mpv",
"m4v",
"svi",
"3gp",
"3g2",
"mxf",
"roq",
"nsv",
"flv",
"f4v",
"f4p",
"f4a",
"f4b",
]
