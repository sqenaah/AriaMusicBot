utf-8utf-8





















importasyncio

fromShrutiMusic.miscimportdb
fromShrutiMusic.utils.databaseimportget_active_chats,is_music_playing


asyncdeftimer():
    whilenotawaitasyncio.sleep(1):
        active_chats=awaitget_active_chats()
forchat_idinactive_chats:
            ifnotawaitis_music_playing(chat_id):
                continue
playing=db.get(chat_id)
ifnotplaying:
                continue
duration=int(playing[0]["seconds"])
ifduration==0:
                continue
ifdb[chat_id][0]["played"]>=duration:
                continue
db[chat_id][0]["played"]+=1


asyncio.create_task(timer())












