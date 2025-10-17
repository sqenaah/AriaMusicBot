utf-8utf-8





















importaiohttp

BASE="https://batbin.me/"


asyncdefpost(url:str,*args,**kwargs):
    asyncwithaiohttp.ClientSession()assession:
        asyncwithsession.post(url,*args,**kwargs)asresp:
            try:
                data=awaitresp.json()
exceptException:
                data=awaitresp.text()
returndata


asyncdefNandBin(text):
    resp=awaitpost(f"{BASE}api/v2/paste",data=text)
ifnotresp["success"]:
        return
link=BASE+resp["message"]
returnlink












