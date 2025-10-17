utf-8utf-8





















importasyncio
fromdatetimeimportdatetime
frompyrogram.enumsimportChatType
frompytgcalls.exceptionsimportGroupCallNotFound
importconfig
fromShrutiMusicimportapp
fromShrutiMusic.miscimportdb
fromShrutiMusic.core.callimportNand,autoend,counter
fromShrutiMusic.utils.databaseimportget_client,set_loop,is_active_chat,is_autoend,is_autoleave
importlogging

asyncdefauto_leave():
    whilenotawaitasyncio.sleep(900):
        fromShrutiMusic.core.userbotimportassistants
ender=awaitis_autoleave()
ifnotender:
            continue
fornuminassistants:
            client=awaitget_client(num)
left=0
try:
                asyncforiinclient.get_dialogs():
                    ifi.chat.typein[
ChatType.SUPERGROUP,
ChatType.GROUP,
ChatType.CHANNEL,
]:
                        if(
i.chat.id!=config.LOG_GROUP_ID
andi.chat.id!=-1002016928980andi.chat.id!=-1002200386150andi.chat.id!=-1001397779415
):
                            ifleft==20:
                                continue
ifnotawaitis_active_chat(i.chat.id):
                                try:
                                    awaitclient.leave_chat(i.chat.id)
left+=1
exceptExceptionase:
                                    logging.error(f"Error leaving chat {i.chat.id}: {e}")
continue
exceptExceptionase:
                logging.error(f"Error processing dialogs: {e}")

asyncio.create_task(auto_leave())

asyncdefauto_end():
    globalautoend,counter
whileTrue:
        awaitasyncio.sleep(60)
try:
            ender=awaitis_autoend()
ifnotender:
                continue
chatss=autoend
keys_to_remove=[]
nocall=False
forchat_idinchatss:
                try:
                    users=len(awaitNand.call_listeners(chat_id))
exceptGroupCallNotFound:
                    users=1
nocall=True
exceptException:
                    users=100
timer=autoend.get(chat_id)
ifusers==1:
                    res=awaitset_loop(chat_id,0)
keys_to_remove.append(chat_id)
try:
                        awaitdb[chat_id][0]["mystic"].delete()
exceptException:
                        pass
try:
                        awaitNand.stop_stream(chat_id)
exceptException:
                        pass
try:
                        ifnotnocall:
                            awaitapp.send_message(chat_id,"» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.")
exceptException:
                        pass
forchat_idinkeys_to_remove:
                delautoend[chat_id]
exceptExceptionase:
            logging.info(e)

asyncio.create_task(auto_end())












