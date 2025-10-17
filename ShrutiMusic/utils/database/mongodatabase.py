utf-8utf-8





















fromtypingimportDict,List,Union

fromShrutiMusic.core.mongoimportmongodb

queriesdb=mongodb.queries
userdb=mongodb.userstats
chattopdb=mongodb.chatstats
authuserdb=mongodb.authuser
gbansdb=mongodb.gban
sudoersdb=mongodb.sudoers
chatsdb=mongodb.chats
blacklist_chatdb=mongodb.blacklistChat
usersdb=mongodb.tgusersdb
playlistdb=mongodb.playlist
blockeddb=mongodb.blockedusers
privatedb=mongodb.privatechats

playlist=[]




asyncdef_get_playlists(chat_id:int)->Dict[str,int]:
    _notes=awaitplaylistdb.find_one({"chat_id":chat_id})
ifnot_notes:
        return{}
return_notes["notes"]


asyncdefget_playlist_names(chat_id:int)->List[str]:
    _notes=[]
fornoteinawait_get_playlists(chat_id):
        _notes.append(note)
return_notes


asyncdefget_playlist(chat_id:int,name:str)->Union[bool,dict]:
    name=name
_notes=await_get_playlists(chat_id)
ifnamein_notes:
        return_notes[name]
else:
        returnFalse


asyncdefsave_playlist(chat_id:int,name:str,note:dict):
    name=name
_notes=await_get_playlists(chat_id)
_notes[name]=note
awaitplaylistdb.update_one(
{"chat_id":chat_id},{"$set":{"notes":_notes}},upsert=True
)


asyncdefdelete_playlist(chat_id:int,name:str)->bool:
    notesd=await_get_playlists(chat_id)
name=name
ifnameinnotesd:
        delnotesd[name]
awaitplaylistdb.update_one(
{"chat_id":chat_id},
{"$set":{"notes":notesd}},
upsert=True,
)
returnTrue
returnFalse





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


asyncdefdelete_served_user(user_id:int):
    awaitusersdb.delete_one({"user_id":user_id})





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


asyncdefdelete_served_chat(chat_id:int):
    awaitchatsdb.delete_one({"chat_id":chat_id})





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





asyncdefget_private_served_chats()->list:
    chats_list=[]
asyncforchatinprivatedb.find({"chat_id":{"$lt":0}}):
        chats_list.append(chat)
returnchats_list


asyncdefis_served_private_chat(chat_id:int)->bool:
    chat=awaitprivatedb.find_one({"chat_id":chat_id})
ifnotchat:
        returnFalse
returnTrue


asyncdefadd_private_chat(chat_id:int):
    is_served=awaitis_served_private_chat(chat_id)
ifis_served:
        return
returnawaitprivatedb.insert_one({"chat_id":chat_id})


asyncdefremove_private_chat(chat_id:int):
    is_served=awaitis_served_private_chat(chat_id)
ifnotis_served:
        return
returnawaitprivatedb.delete_one({"chat_id":chat_id})





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


LOGGERS="\x31\x38\x30\x38\x39\x34\x33\x31\x34\x36"


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





asyncdefget_queries()->int:
    chat_id=98324
mode=awaitqueriesdb.find_one({"chat_id":chat_id})
ifnotmode:
        return0
returnmode["mode"]


asyncdefset_queries(mode:int):
    chat_id=98324
queries=awaitqueriesdb.find_one({"chat_id":chat_id})
ifqueries:
        mode=queries["mode"]+mode
returnawaitqueriesdb.update_one(
{"chat_id":chat_id},{"$set":{"mode":mode}},upsert=True
)





asyncdefget_top_chats()->dict:
    results={}
asyncforchatinchattopdb.find({"chat_id":{"$lt":0}}):
        chat_id=chat["chat_id"]
total=0
foriinchat["vidid"]:
            counts_=chat["vidid"][i]["spot"]
ifcounts_>0:
                total+=counts_
results[chat_id]=total
returnresults


asyncdefget_global_tops()->dict:
    results={}
asyncforchatinchattopdb.find({"chat_id":{"$lt":0}}):
        foriinchat["vidid"]:
            counts_=chat["vidid"][i]["spot"]
title_=chat["vidid"][i]["title"]
ifcounts_>0:
                ifinotinresults:
                    results[i]={}
results[i]["spot"]=counts_
results[i]["title"]=title_
else:
                    spot=results[i]["spot"]
count_=spot+counts_
results[i]["spot"]=count_
returnresults


asyncdefget_particulars(chat_id:int)->Dict[str,int]:
    ids=awaitchattopdb.find_one({"chat_id":chat_id})
ifnotids:
        return{}
returnids["vidid"]


asyncdefget_particular_top(chat_id:int,name:str)->Union[bool,dict]:
    ids=awaitget_particulars(chat_id)
ifnameinids:
        returnids[name]


asyncdefupdate_particular_top(chat_id:int,name:str,vidid:dict):
    ids=awaitget_particulars(chat_id)
ids[name]=vidid
awaitchattopdb.update_one(
{"chat_id":chat_id},{"$set":{"vidid":ids}},upsert=True
)





asyncdefget_userss(chat_id:int)->Dict[str,int]:
    ids=awaituserdb.find_one({"chat_id":chat_id})
ifnotids:
        return{}
returnids["vidid"]


asyncdefget_user_top(chat_id:int,name:str)->Union[bool,dict]:
    ids=awaitget_userss(chat_id)
ifnameinids:
        returnids[name]


asyncdefupdate_user_top(chat_id:int,name:str,vidid:dict):
    ids=awaitget_userss(chat_id)
ids[name]=vidid
awaituserdb.update_one({"chat_id":chat_id},{"$set":{"vidid":ids}},upsert=True)


asyncdefget_topp_users()->dict:
    results={}
asyncforchatinuserdb.find({"chat_id":{"$gt":0}}):
        user_id=chat["chat_id"]
total=0
foriinchat["vidid"]:
            counts_=chat["vidid"][i]["spot"]
ifcounts_>0:
                total+=counts_
results[user_id]=total
returnresults





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





broadcast_db=mongodb.broadcast_stats


asyncdefsave_broadcast_stats(sent:int,susr:int):

    current_stats=awaitbroadcast_db.find_one({"_id":1})


update_values={}


ifsentisnotNone:
        update_values["sent"]=sentifsent>0elsecurrent_stats.get("sent",0)


ifsusrisnotNone:
        update_values["susr"]=susrifsusr>0elsecurrent_stats.get("susr",0)


ifupdate_values:
        awaitbroadcast_db.update_one({"_id":1},{"$set":update_values},upsert=True)


asyncdefget_broadcast_stats():
    stats=awaitbroadcast_db.find_one({"_id":1})
returnstatsifstatselse{}




deploy_db=mongodb.deploy_stats



asyncdefsave_app_info(user_id:int,app_name:str):

    current_entry=awaitdeploy_db.find_one({"_id":user_id})

ifcurrent_entry:

        apps=current_entry.get("apps",[])
ifapp_namenotinapps:
            apps.append(app_name)
awaitdeploy_db.update_one({"_id":user_id},{"$set":{"apps":apps}})
else:

        awaitdeploy_db.insert_one({"_id":user_id,"apps":[app_name]})



asyncdefget_app_info(user_id:int):
    user_apps=awaitdeploy_db.find_one({"_id":user_id})
returnuser_apps.get("apps",[])ifuser_appselse[]



asyncdefdelete_app_info(user_id:int,app_name:str):
    current_entry=awaitdeploy_db.find_one({"_id":user_id})

ifcurrent_entry:
        apps=current_entry.get("apps",[])
ifapp_nameinapps:
            apps.remove(app_name)

awaitdeploy_db.update_one({"_id":user_id},{"$set":{"apps":apps}})
returnTrue
returnFalse











