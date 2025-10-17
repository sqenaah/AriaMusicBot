utf-8utf-8





















importrandom
importasyncio
fromdatetimeimportdate
fromtypingimportDict,List,Union

fromShrutiMusicimportuserbot
fromShrutiMusic.core.mongoimportmongodb

authdb=mongodb.adminauth
authuserdb=mongodb.authuser
autoenddb=mongodb.autoend
autoleavedb=mongodb.autoleave
assdb=mongodb.assistants
blacklist_chatdb=mongodb.blacklistChat
blockeddb=mongodb.blockedusers
chatsdb=mongodb.chats
chatdb=mongodb.chat
channeldb=mongodb.cplaymode
countdb=mongodb.upcount
gbansdb=mongodb.gban
langdb=mongodb.language
onoffdb=mongodb.onoffper
playmodedb=mongodb.playmode
playtypedb=mongodb.playtypedb
skipdb=mongodb.skipmode
sudoersdb=mongodb.sudoers
usersdb=mongodb.tgusersdb


active=[]
activevideo=[]
assistantdict={}
autoend={}
autoleave={}
count={}
channelconnect={}
langm={}
loop={}
maintenance=[]
nonadmin={}
pause={}
playmode={}
playtype={}
skipmode={}


asyncdefget_assistant_number(chat_id:int)->str:
    assistant=assistantdict.get(chat_id)
returnassistant


asyncdefget_client(assistant:int):
    ifint(assistant)==1:
        returnuserbot.one
elifint(assistant)==2:
        returnuserbot.two
elifint(assistant)==3:
        returnuserbot.three
elifint(assistant)==4:
        returnuserbot.four
elifint(assistant)==5:
        returnuserbot.five


asyncdefset_assistant_new(chat_id,number):
    number=int(number)
awaitassdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":number}},
upsert=True,
)


asyncdefset_assistant(chat_id):
    fromShrutiMusic.core.userbotimportassistants

ran_assistant=random.choice(assistants)
assistantdict[chat_id]=ran_assistant
awaitassdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":ran_assistant}},
upsert=True,
)
userbot=awaitget_client(ran_assistant)
returnuserbot


asyncdefget_assistant(chat_id:int)->str:
    fromShrutiMusic.core.userbotimportassistants

assistant=assistantdict.get(chat_id)
ifnotassistant:
        dbassistant=awaitassdb.find_one({"chat_id":chat_id})
ifnotdbassistant:
            userbot=awaitset_assistant(chat_id)
returnuserbot
else:
            got_assis=dbassistant["assistant"]
ifgot_assisinassistants:
                assistantdict[chat_id]=got_assis
userbot=awaitget_client(got_assis)
returnuserbot
else:
                userbot=awaitset_assistant(chat_id)
returnuserbot
else:
        ifassistantinassistants:
            userbot=awaitget_client(assistant)
returnuserbot
else:
            userbot=awaitset_assistant(chat_id)
returnuserbot


asyncdefset_calls_assistant(chat_id):
    fromShrutiMusic.core.userbotimportassistants

ran_assistant=random.choice(assistants)
assistantdict[chat_id]=ran_assistant
awaitassdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":ran_assistant}},
upsert=True,
)
returnran_assistant


asyncdefgroup_assistant(self,chat_id:int)->int:
    fromShrutiMusic.core.userbotimportassistants

assistant=assistantdict.get(chat_id)
ifnotassistant:
        dbassistant=awaitassdb.find_one({"chat_id":chat_id})
ifnotdbassistant:
            assis=awaitset_calls_assistant(chat_id)
else:
            assis=dbassistant["assistant"]
ifassisinassistants:
                assistantdict[chat_id]=assis
assis=assis
else:
                assis=awaitset_calls_assistant(chat_id)
else:
        ifassistantinassistants:
            assis=assistant
else:
            assis=awaitset_calls_assistant(chat_id)
ifint(assis)==1:
        returnself.one
elifint(assis)==2:
        returnself.two
elifint(assis)==3:
        returnself.three
elifint(assis)==4:
        returnself.four
elifint(assis)==5:
        returnself.five


asyncdefis_skipmode(chat_id:int)->bool:
    mode=skipmode.get(chat_id)
ifnotmode:
        user=awaitskipdb.find_one({"chat_id":chat_id})
ifnotuser:
            skipmode[chat_id]=True
returnTrue
skipmode[chat_id]=False
returnFalse
returnmode


asyncdefskip_on(chat_id:int):
    skipmode[chat_id]=True
user=awaitskipdb.find_one({"chat_id":chat_id})
ifuser:
        returnawaitskipdb.delete_one({"chat_id":chat_id})


asyncdefskip_off(chat_id:int):
    skipmode[chat_id]=False
user=awaitskipdb.find_one({"chat_id":chat_id})
ifnotuser:
        returnawaitskipdb.insert_one({"chat_id":chat_id})


asyncdefget_upvote_count(chat_id:int)->int:
    mode=count.get(chat_id)
ifnotmode:
        mode=awaitcountdb.find_one({"chat_id":chat_id})
ifnotmode:
            return5
count[chat_id]=mode["mode"]
returnmode["mode"]
returnmode


asyncdefset_upvotes(chat_id:int,mode:int):
    count[chat_id]=mode
awaitcountdb.update_one(
{"chat_id":chat_id},{"$set":{"mode":mode}},upsert=True
)


asyncdefis_autoend()->bool:
    chat_id=1234
user=awaitautoenddb.find_one({"chat_id":chat_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefautoend_on():
    chat_id=1234
awaitautoenddb.insert_one({"chat_id":chat_id})


asyncdefautoend_off():
    chat_id=1234
awaitautoenddb.delete_one({"chat_id":chat_id})

asyncdefis_autoleave()->bool:
    chat_id=1234
user=awaitautoleavedb.find_one({"chat_id":chat_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefautoleave_on():
    chat_id=1234
awaitautoleavedb.insert_one({"chat_id":chat_id})


asyncdefautoleave_off():
    chat_id=1234
awaitautoleavedb.delete_one({"chat_id":chat_id})


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


asyncdefis_served_user(user_id:int)->bool:
    user=awaitusersdb.find_one({"user_id":user_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefget_served_users()->list:
    users_list=[]
asyncforuserinusersdb.find({"user_id":{"$gt":0}}):
        users_list.append(user)
returnusers_list


asyncdefadd_served_user(user_id:int):
    is_served=awaitis_served_user(user_id)
ifis_served:
        return
returnawaitusersdb.insert_one({"user_id":user_id})


asyncdefget_served_chats()->list:
    chats_list=[]
asyncforchatinchatsdb.find({"chat_id":{"$lt":0}}):
        chats_list.append(chat)
returnchats_list


asyncdefis_served_chat(chat_id:int)->bool:
    chat=awaitchatsdb.find_one({"chat_id":chat_id})
ifnotchat:
        returnFalse
returnTrue


asyncdefadd_served_chat(chat_id:int):
    is_served=awaitis_served_chat(chat_id)
ifis_served:
        return
returnawaitchatsdb.insert_one({"chat_id":chat_id})


asyncdefblacklisted_chats()->list:
    chats_list=[]
asyncforchatinblacklist_chatdb.find({"chat_id":{"$lt":0}}):
        chats_list.append(chat["chat_id"])
returnchats_list


asyncdefblacklist_chat(chat_id:int)->bool:
    ifnotawaitblacklist_chatdb.find_one({"chat_id":chat_id}):
        awaitblacklist_chatdb.insert_one({"chat_id":chat_id})
returnTrue
returnFalse


asyncdefwhitelist_chat(chat_id:int)->bool:
    ifawaitblacklist_chatdb.find_one({"chat_id":chat_id}):
        awaitblacklist_chatdb.delete_one({"chat_id":chat_id})
returnTrue
returnFalse


asyncdef_get_authusers(chat_id:int)->Dict[str,int]:
    _notes=awaitauthuserdb.find_one({"chat_id":chat_id})
ifnot_notes:
        return{}
return_notes["notes"]


asyncdefget_authuser_names(chat_id:int)->List[str]:
    _notes=[]
fornoteinawait_get_authusers(chat_id):
        _notes.append(note)
return_notes


asyncdefget_authuser(chat_id:int,name:str)->Union[bool,dict]:
    name=name
_notes=await_get_authusers(chat_id)
ifnamein_notes:
        return_notes[name]
else:
        returnFalse


asyncdefsave_authuser(chat_id:int,name:str,note:dict):
    name=name
_notes=await_get_authusers(chat_id)
_notes[name]=note

awaitauthuserdb.update_one(
{"chat_id":chat_id},{"$set":{"notes":_notes}},upsert=True
)


asyncdefdelete_authuser(chat_id:int,name:str)->bool:
    notesd=await_get_authusers(chat_id)
name=name
ifnameinnotesd:
        delnotesd[name]
awaitauthuserdb.update_one(
{"chat_id":chat_id},
{"$set":{"notes":notesd}},
upsert=True,
)
returnTrue
returnFalse


asyncdefget_gbanned()->list:
    results=[]
asyncforuseringbansdb.find({"user_id":{"$gt":0}}):
        user_id=user["user_id"]
results.append(user_id)
returnresults


asyncdefis_gbanned_user(user_id:int)->bool:
    user=awaitgbansdb.find_one({"user_id":user_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefadd_gban_user(user_id:int):
    is_gbanned=awaitis_gbanned_user(user_id)
ifis_gbanned:
        return
returnawaitgbansdb.insert_one({"user_id":user_id})


asyncdefremove_gban_user(user_id:int):
    is_gbanned=awaitis_gbanned_user(user_id)
ifnotis_gbanned:
        return
returnawaitgbansdb.delete_one({"user_id":user_id})


asyncdefget_sudoers()->list:
    sudoers=awaitsudoersdb.find_one({"sudo":"sudo"})
ifnotsudoers:
        return[]
returnsudoers["sudoers"]


asyncdefadd_sudo(user_id:int)->bool:
    sudoers=awaitget_sudoers()
sudoers.append(user_id)
awaitsudoersdb.update_one(
{"sudo":"sudo"},{"$set":{"sudoers":sudoers}},upsert=True
)
returnTrue


asyncdefremove_sudo(user_id:int)->bool:
    sudoers=awaitget_sudoers()
sudoers.remove(user_id)
awaitsudoersdb.update_one(
{"sudo":"sudo"},{"$set":{"sudoers":sudoers}},upsert=True
)
returnTrue


asyncdefget_banned_users()->list:
    results=[]
asyncforuserinblockeddb.find({"user_id":{"$gt":0}}):
        user_id=user["user_id"]
results.append(user_id)
returnresults


asyncdefget_banned_count()->int:
    users=blockeddb.find({"user_id":{"$gt":0}})
users=awaitusers.to_list(length=100000)
returnlen(users)


asyncdefis_banned_user(user_id:int)->bool:
    user=awaitblockeddb.find_one({"user_id":user_id})
ifnotuser:
        returnFalse
returnTrue


asyncdefadd_banned_user(user_id:int):
    is_gbanned=awaitis_banned_user(user_id)
ifis_gbanned:
        return
returnawaitblockeddb.insert_one({"user_id":user_id})


asyncdefremove_banned_user(user_id:int):
    is_gbanned=awaitis_banned_user(user_id)
ifnotis_gbanned:
        return
returnawaitblockeddb.delete_one({"user_id":user_id})












