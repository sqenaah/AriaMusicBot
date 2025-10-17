utf-8utf-8





















importre
fromtypingimportUnion

importaiohttp
frombs4importBeautifulSoup
fromyoutubesearchpython.__future__importVideosSearch


classRessoAPI:
    def__init__(self):
        self.regex=r"^(https:\/\/m.resso.com\/)(.*)$"
self.base="https://m.resso.com/"

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
fortaginsoup.find_all("meta"):
            iftag.get("property",None)=="og:title":
                title=tag.get("content",None)
iftag.get("property",None)=="og:description":
                des=tag.get("content",None)
try:
                    des=des.split("·")[0]
except:
                    pass
ifdes=="":
            return
results=VideosSearch(title,limit=1)
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












