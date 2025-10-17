utf-8utf-8coupledb={}


asyncdef_get_lovers(cid:int):
    chat_data=coupledb.get(cid,{})
lovers=chat_data.get("couple",{})
returnlovers


asyncdefget_image(cid:int):
    chat_data=coupledb.get(cid,{})
image=chat_data.get("img","")
returnimage


asyncdefget_couple(cid:int,date:str):
    lovers=await_get_lovers(cid)
returnlovers.get(date,False)


asyncdefsave_couple(cid:int,date:str,couple:dict,img:str):
    ifcidnotincoupledb:
        coupledb[cid]={"couple":{},"img":""}
coupledb[cid]["couple"][date]=couple
coupledb[cid]["img"]=img



