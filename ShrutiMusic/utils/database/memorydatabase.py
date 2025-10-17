importjson
importos
fromtypingimportDict,List,Union

importconfig
fromShrutiMusic.core.mongoimportmongodb

channeldb=mongodb.cplaymode
commanddb=mongodb.commands
cleandb=mongodb.cleanmode
playmodedb=mongodb.playmode
playtypedb=mongodb.playtypedb
langdb=mongodb.language
authdb=mongodb.adminauth
videodb=mongodb.Champuvideocalls
onoffdb=mongodb.onoffper
autoenddb=mongodb.autoend
notesdb=mongodb.notes
filtersdb=mongodb.filters


loop={}
playtype={}
playmode={}
channelconnect={}
langm={}
pause={}
mute={}
active=[]
activevideo=[]
nonadmin={}
vlimit=[]
maintenance=[]
autoend={}
greeting_message={"welcome":{},"goodbye":{}}


asyncdefget_filters_count()->dict:
    chats_count=0
filters_count=0
asyncforchatinfiltersdb.find({"chat_id":{"$lt":0}}):
        filters_name=awaitget_filters_names(chat["chat_id"])
filters_count+=len(filters_name)
chats_count+=1
return{
"chats_count":chats_count,
"filters_count":filters_count,
}


asyncdef_get_filters(chat_id:int)->Dict[str,int]:
    _filters=awaitfiltersdb.find_one({"chat_id":chat_id})
ifnot_filters:
        return{}
return_filters["filters"]


asyncdefget_filters_names(chat_id:int)->List[str]:
    _filters=[]
for_filterinawait_get_filters(chat_id):
        _filters.append(_filter)
return_filters


asyncdefget_filter(chat_id:int,name:str)->Union[bool,dict]:
    name=name.lower().strip()
_filters=await_get_filters(chat_id)
ifnamein_filters:
        return_filters[name]
returnFalse


asyncdefsave_filter(chat_id:int,name:str,_filter:dict):
    name=name.lower().strip()
_filters=await_get_filters(chat_id)
_filters[name]=_filter
awaitfiltersdb.update_one(
{"chat_id":chat_id},
{"$set":{"filters":_filters}},
upsert=True,
)


asyncdefdelete_filter(chat_id:int,name:str)->bool:
    filtersd=await_get_filters(chat_id)
name=name.lower().strip()
ifnameinfiltersd:
        delfiltersd[name]
awaitfiltersdb.update_one(
{"chat_id":chat_id},
{"$set":{"filters":filtersd}},
upsert=True,
)
returnTrue
returnFalse


asyncdefdeleteall_filters(chat_id:int):
    returnawaitfiltersdb.delete_one({"chat_id":chat_id})


asyncdefget_notes_count()->dict:
    chats_count=0
notes_count=0
asyncforchatinnotesdb.find({"chat_id":{"$exists":1}}):
        notes_name=awaitget_note_names(chat["chat_id"])
notes_count+=len(notes_name)
chats_count+=1
return{"chats_count":chats_count,"notes_count":notes_count}


asyncdef_get_notes(chat_id:int)->Dict[str,int]:
    _notes=awaitnotesdb.find_one({"chat_id":chat_id})
ifnot_notes:
        return{}
return_notes["notes"]


asyncdefget_note_names(chat_id:int)->List[str]:
    _notes=[]
fornoteinawait_get_notes(chat_id):
        _notes.append(note)
return_notes


asyncdefget_note(chat_id:int,name:str)->Union[bool,dict]:
    name=name.lower().strip()
_notes=await_get_notes(chat_id)
ifnamein_notes:
        return_notes[name]
returnFalse


asyncdefsave_note(chat_id:int,name:str,note:dict):
    name=name.lower().strip()
_notes=await_get_notes(chat_id)
_notes[name]=note

awaitnotesdb.update_one(
{"chat_id":chat_id},{"$set":{"notes":_notes}},upsert=True
)


asyncdefdelete_note(chat_id:int,name:str)->bool:
    notesd=await_get_notes(chat_id)
name=name.lower().strip()
ifnameinnotesd:
        delnotesd[name]
awaitnotesdb.update_one(
{"chat_id":chat_id},
{"$set":{"notes":notesd}},
upsert=True,
)
returnTrue
returnFalse


asyncdefdeleteall_notes(chat_id:int):
    returnawaitnotesdb.delete_one({"chat_id":chat_id})


asyncdefset_private_note(chat_id,private_note):
    awaitnotesdb.update_one(
{"chat_id":chat_id},{"$set":{"private_note":private_note}},upsert=True
)


asyncdefis_pnote_on(chat_id)->bool:
    GetNoteData=awaitnotesdb.find_one({"chat_id":chat_id})
ifnotGetNoteData==None:
        if"private_note"inGetNoteData:
            private_note=GetNoteData["private_note"]
returnprivate_note
else:
            returnFalse
else:
        returnFalse





asyncdefis_autoend()->bool:
    chat_id=123
mode=autoend.get(chat_id)
ifnotmode:
        user=awaitautoenddb.find_one({"chat_id":chat_id})
ifnotuser:
            autoend[chat_id]=False
returnFalse
autoend[chat_id]=True
returnTrue
returnmode


asyncdefautoend_on():
    chat_id=123
autoend[chat_id]=True
user=awaitautoenddb.find_one({"chat_id":chat_id})
ifnotuser:
        returnawaitautoenddb.insert_one({"chat_id":chat_id})


asyncdefautoend_off():
    chat_id=123
autoend[chat_id]=False
user=awaitautoenddb.find_one({"chat_id":chat_id})
ifuser:
        returnawaitautoenddb.delete_one({"chat_id":chat_id})



asyncdefget_loop(chat_id:int)->int:
    lop=loop.get(chat_id)
ifnotlop:
        return0
returnlop


asyncdefset_loop(chat_id:int,mode:int):
    loop[chat_id]=mode



asyncdefget_cmode(chat_id:int)->int:
    mode=channelconnect.get(chat_id)
ifnotmode:
        mode=awaitchanneldb.find_one({"chat_id":chat_id})
ifnotmode:
            returnNone
channelconnect[chat_id]=mode["mode"]
returnmode["mode"]
returnmode


asyncdefset_cmode(chat_id:int,mode:int):
    channelconnect[chat_id]=mode
awaitchanneldb.update_one(
{"chat_id":chat_id},{"$set":{"mode":mode}},upsert=True
)



asyncdefget_playtype(chat_id:int)->str:
    mode=playtype.get(chat_id)
ifnotmode:
        mode=awaitplaytypedb.find_one({"chat_id":chat_id})
ifnotmode:
            playtype[chat_id]="Everyone"
return"Everyone"
playtype[chat_id]=mode["mode"]
returnmode["mode"]
returnmode


asyncdefset_playtype(chat_id:int,mode:str):
    playtype[chat_id]=mode
awaitplaytypedb.update_one(
{"chat_id":chat_id},{"$set":{"mode":mode}},upsert=True
)



asyncdefget_playmode(chat_id:int)->str:
    mode=playmode.get(chat_id)
ifnotmode:
        mode=awaitplaymodedb.find_one({"chat_id":chat_id})
ifnotmode:
            playmode[chat_id]="Direct"
return"Direct"
playmode[chat_id]=mode["mode"]
returnmode["mode"]
returnmode


asyncdefset_playmode(chat_id:int,mode:str):
    playmode[chat_id]=mode
awaitplaymodedb.update_one(
{"chat_id":chat_id},{"$set":{"mode":mode}},upsert=True
)



asyncdefget_lang(chat_id:int)->str:
    mode=langm.get(chat_id)
ifnotmode:
        lang=awaitlangdb.find_one({"chat_id":chat_id})
ifnotlang:
            langm[chat_id]="en"
return"en"
langm[chat_id]=lang["lang"]
returnlang["lang"]
returnmode


asyncdefset_lang(chat_id:int,lang:str):
    langm[chat_id]=lang
awaitlangdb.update_one({"chat_id":chat_id},{"$set":{"lang":lang}},upsert=True)



asyncdefis_muted(chat_id:int)->bool:
    mode=mute.get(chat_id)
ifnotmode:
        returnFalse
returnmode


asyncdefmute_on(chat_id:int):
    mute[chat_id]=True


asyncdefmute_off(chat_id:int):
    mute[chat_id]=False



asyncdefis_music_playing(chat_id:int)->bool:
    mode=pause.get(chat_id)
ifnotmode:
        returnFalse
returnmode


asyncdefmusic_on(chat_id:int):
    pause[chat_id]=True


asyncdefmusic_off(chat_id:int):
    pause[chat_id]=False



asyncdefget_active_chats()->list:
    returnactive


asyncdefis_active_chat(chat_id:int)->bool:
    ifchat_idnotinactive:
        returnFalse
else:
        returnTrue


asyncdefadd_active_chat(chat_id:int):
    ifchat_idnotinactive:
        active.append(chat_id)


asyncdefremove_active_chat(chat_id:int):
    ifchat_idinactive:
        active.remove(chat_id)



asyncdefget_active_video_chats()->list:
    returnactivevideo


asyncdefis_active_video_chat(chat_id:int)->bool:
    ifchat_idnotinactivevideo:
        returnFalse
else:
        returnTrue


asyncdefadd_active_video_chat(chat_id:int):
    ifchat_idnotinactivevideo:
        activevideo.append(chat_id)


asyncdefremove_active_video_chat(chat_id:int):
    ifchat_idinactivevideo:
        activevideo.remove(chat_id)





CLEANMODE_DB=os.path.join(config.TEMP_DB_FOLDER,"cleanmode.json")
COMMAND_DB=os.path.join(config.TEMP_DB_FOLDER,"command.json")


defload_cleanmode():
    ifos.path.exists(CLEANMODE_DB):
        withopen(CLEANMODE_DB,"r")asfile:
            returnjson.load(file)
return[]


defload_command():
    ifos.path.exists(COMMAND_DB):
        withopen(COMMAND_DB,"r")asfile:
            returnjson.load(file)
return[]


defsave_cleanmode():
    withopen(CLEANMODE_DB,"w")asfile:
        json.dump(cleanmode,file)


defsave_command():
    withopen(COMMAND_DB,"w")asfile:
        json.dump(command,file)


cleanmode=load_cleanmode()
command=load_command()


asyncdefis_cleanmode_on(chat_id:int)->bool:
    returnchat_idnotincleanmode


asyncdefcleanmode_off(chat_id:int):
    ifchat_idnotincleanmode:
        cleanmode.append(chat_id)
save_cleanmode()


asyncdefcleanmode_on(chat_id:int):
    ifchat_idincleanmode:
        cleanmode.remove(chat_id)
save_cleanmode()


asyncdefis_commanddelete_on(chat_id:int)->bool:
    returnchat_idnotincommand


asyncdefcommanddelete_off(chat_id:int):
    ifchat_idnotincommand:
        command.append(chat_id)
save_command()


asyncdefcommanddelete_on(chat_id:int):
    ifchat_idincommand:
        command.remove(chat_id)
save_command()



asyncdefcheck_nonadmin_chat(chat_id:int)->bool:
    user=awaitauthdb.find_one({"chat_id":chat_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefis_nonadmin_chat(chat_id:int)->bool:
    mode=nonadmin.get(chat_id)
ifnotmode:
        user=awaitauthdb.find_one({"chat_id":chat_id})
ifnotuser:
            nonadmin[chat_id]=False
returnFalse
nonadmin[chat_id]=True
returnTrue
returnmode


asyncdefadd_nonadmin_chat(chat_id:int):
    nonadmin[chat_id]=True
is_admin=awaitcheck_nonadmin_chat(chat_id)
ifis_admin:
        return
returnawaitauthdb.insert_one({"chat_id":chat_id})


asyncdefremove_nonadmin_chat(chat_id:int):
    nonadmin[chat_id]=False
is_admin=awaitcheck_nonadmin_chat(chat_id)
ifnotis_admin:
        return
returnawaitauthdb.delete_one({"chat_id":chat_id})



asyncdefis_video_allowed(chat_idd)->str:
    chat_id=123456
ifnotvlimit:
        dblimit=awaitvideodb.find_one({"chat_id":chat_id})
ifnotdblimit:
            vlimit.clear()
vlimit.append(config.VIDEO_STREAM_LIMIT)
limit=config.VIDEO_STREAM_LIMIT
else:
            limit=dblimit["limit"]
vlimit.clear()
vlimit.append(limit)
else:
        limit=vlimit[0]
iflimit==0:
        returnFalse
count=len(awaitget_active_video_chats())
ifint(count)==int(limit):
        ifnotawaitis_active_video_chat(chat_idd):
            returnFalse
returnTrue


asyncdefget_video_limit()->str:
    chat_id=123456
ifnotvlimit:
        dblimit=awaitvideodb.find_one({"chat_id":chat_id})
ifnotdblimit:
            limit=config.VIDEO_STREAM_LIMIT
else:
            limit=dblimit["limit"]
else:
        limit=vlimit[0]
returnlimit


asyncdefset_video_limit(limt:int):
    chat_id=123456
vlimit.clear()
vlimit.append(limt)
returnawaitvideodb.update_one(
{"chat_id":chat_id},{"$set":{"limit":limt}},upsert=True
)



asyncdefis_on_off(on_off:int)->bool:
    onoff=awaitonoffdb.find_one({"on_off":on_off})
ifnotonoff:
        returnFalse
returnTrue


asyncdefadd_on(on_off:int):
    is_on=awaitis_on_off(on_off)
ifis_on:
        return
returnawaitonoffdb.insert_one({"on_off":on_off})


asyncdefadd_off(on_off:int):
    is_off=awaitis_on_off(on_off)
ifnotis_off:
        return
returnawaitonoffdb.delete_one({"on_off":on_off})





asyncdefis_maintenance():
    ifnotmaintenance:
        get=awaitonoffdb.find_one({"on_off":1})
ifnotget:
            maintenance.clear()
maintenance.append(2)
returnTrue
else:
            maintenance.clear()
maintenance.append(1)
returnFalse
else:
        if1inmaintenance:
            returnFalse
else:
            returnTrue


asyncdefmaintenance_off():
    maintenance.clear()
maintenance.append(2)
is_off=awaitis_on_off(1)
ifnotis_off:
        return
returnawaitonoffdb.delete_one({"on_off":1})


asyncdefmaintenance_on():
    maintenance.clear()
maintenance.append(1)
is_on=awaitis_on_off(1)
ifis_on:
        return
returnawaitonoffdb.insert_one({"on_off":1})





AUDIO_FILE=os.path.join(config.TEMP_DB_FOLDER,"audio.json")
VIDEO_FILE=os.path.join(config.TEMP_DB_FOLDER,"video.json")


defload_data(file_path):
    ifos.path.exists(file_path):
        withopen(file_path,"r")asfile:
            returnjson.load(file)
return{}


defsave_data(file_path,data):
    withopen(file_path,"w")asfile:
        json.dump(data,file,indent=4)


audio=load_data(AUDIO_FILE)
video=load_data(VIDEO_FILE)


asyncdefsave_audio_bitrate(chat_id:int,bitrate:str):
    audio[str(chat_id)]=bitrate
save_data(AUDIO_FILE,audio)


asyncdefsave_video_bitrate(chat_id:int,bitrate:str):
    video[str(chat_id)]=bitrate
save_data(VIDEO_FILE,video)


asyncdefget_aud_bit_name(chat_id:int)->str:
    returnaudio.get(str(chat_id),"HIGH")


asyncdefget_vid_bit_name(chat_id:int)->str:
    returnvideo.get(str(chat_id),"HD_720p")


asyncdefget_audio_bitrate(chat_id:int)->str:
    mode=audio.get(str(chat_id),"MEDIUM")
return{
"STUDIO":AudioQuality.STUDIO,
"HIGH":AudioQuality.HIGH,
"MEDIUM":AudioQuality.MEDIUM,
"LOW":AudioQuality.LOW,
}.get(mode,AudioQuality.MEDIUM)


asyncdefget_video_bitrate(chat_id:int)->str:
    mode=video.get(
str(chat_id),"SD_480p"
)
return{
"UHD_4K":VideoQuality.UHD_4K,
"QHD_2K":VideoQuality.QHD_2K,
"FHD_1080p":VideoQuality.FHD_1080p,
"HD_720p":VideoQuality.HD_720p,
"SD_480p":VideoQuality.SD_480p,
"SD_360p":VideoQuality.SD_360p,
}.get(mode,VideoQuality.SD_480p)
