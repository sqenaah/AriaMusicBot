utf-8utf-8





















fromosimportpath

fromyt_dlpimportYoutubeDL

fromShrutiMusic.utils.formattersimportseconds_to_min


classSoundAPI:
    def__init__(self):
        self.opts={
"outtmpl":"downloads/%(id)s.%(ext)s",
"format":"best",
"retries":3,
"nooverwrites":False,
"continuedl":True,
}

asyncdefvalid(self,link:str):
        if"soundcloud"inlink:
            returnTrue
else:
            returnFalse

asyncdefdownload(self,url):
        d=YoutubeDL(self.opts)
try:
            info=d.extract_info(url)
except:
            returnFalse
xyz=path.join("downloads",f"{info['id']}.{info['ext']}")
duration_min=seconds_to_min(info["duration"])
track_details={
"title":info["title"],
"duration_sec":info["duration"],
"duration_min":duration_min,
"uploader":info["uploader"],
"filepath":xyz,
}
returntrack_details,xyz












