utf-8utf-8





















importre
fromtypingimportUnion

importaiohttp
frombs4importBeautifulSoup
fromyoutubesearchpython.__future__importVideosSearch


classAppleAPI:
    def__init__(self):
        self.regex=r"^(https:\/\/music.apple.com\/)(.*)$"
self.base="https://music.apple.com/in/playlist/"

asyncdefvalid(self,link:str):
        ifre.search(self.regex,link):
            returnTrue
else:
            returnFalse

asyncdeftrack(self,url,playid:Union[bool,str]=None):
        ifplayid:
            url=self.base+url
asyncwithaiohttp.ClientSession()assession:
            asyncwithsession.get(url)asresponse:
                ifresponse.status!=200:
                    returnFalse
html=awaitresponse.text()
soup=BeautifulSoup(html,"html.parser")
search=None
fortaginsoup.find_all("meta"):
            iftag.get("property",None)=="og:title":
                search=tag.get("content",None)
ifsearchisNone:
            returnFalse
results=VideosSearch(search,limit=1)
forresultin(awaitresults.next())["result"]:
            title=result["title"]
ytlink=result["link"]
vidid=result["id"]
duration_min=result["duration"]
thumbnail=result["thumbnails"][0]["url"].split("?")[0]
track_details={
"title":title,
"link":ytlink,
"vidid":vidid,
"duration_min":duration_min,
"thumb":thumbnail,
}
returntrack_details,vidid

asyncdefplaylist(self,url,playid:Union[bool,str]=None):
        ifplayid:
            url=self.base+url
playlist_id=url.split("playlist/")[1]
asyncwithaiohttp.ClientSession()assession:
            asyncwithsession.get(url)asresponse:
                ifresponse.status!=200:
                    returnFalse
html=awaitresponse.text()
soup=BeautifulSoup(html,"html.parser")
applelinks=soup.find_all("meta",attrs={"property":"music:song"})
results=[]
foriteminapplelinks:
            try:
                xx=(((item["content"]).split("album/")[1]).split("/")[0]).replace(
"-"," "
)
except:
                xx=((item["content"]).split("album/")[1]).split("/")[0]
results.append(xx)
returnresults,playlist_id












