utf-8utf-8fromtypingimportList,Optional,Union

frompyrogramimportClient,filters
frompyrogram.errorsimportChatAdminRequired
frompyrogram.raw.functions.channelsimportGetFullChannel
frompyrogram.raw.functions.messagesimportGetFullChat
frompyrogram.raw.functions.phoneimportCreateGroupCall,DiscardGroupCall
frompyrogram.raw.typesimportInputGroupCall,InputPeerChannel,InputPeerChat
frompyrogram.typesimportChatPrivileges,Message

fromShrutiMusicimportapp
fromShrutiMusic.core.callimportNand
fromShrutiMusic.utils.databaseimportget_assistant,set_loop
fromShrutiMusic.utils.permissionsimportadminsOnly

other_filters=filters.group&~filters.via_bot&~filters.forwarded
other_filters2=filters.private&~filters.via_bot&~filters.forwarded


defcommand(commands:Union[str,List[str]]):
    returnfilters.command(commands,"")


@app.on_message(filters.video_chat_started&filters.group)
asyncdefon_vc_start(_,msg):
    chat_id=msg.chat.id
try:
        awaitmsg.reply("<b>😍 ᴠɪᴅᴇᴏ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ 🥳</b>")

awaitset_loop(chat_id,0)
exceptExceptionase:
        awaitmsg.reply(f"<b>ᴇʀʀᴏʀ:</b> <code>{e}</code>")


asyncdefget_group_call(client:Client,message:Message,err_msg:str="")->Optional[InputGroupCall]:
    assistant=awaitget_assistant(message.chat.id)
chat_peer=awaitassistant.resolve_peer(message.chat.id)
ifisinstance(chat_peer,(InputPeerChannel,InputPeerChat)):
        ifisinstance(chat_peer,InputPeerChannel):
            full_chat=(awaitassistant.invoke(GetFullChannel(channel=chat_peer))).full_chat
elifisinstance(chat_peer,InputPeerChat):
            full_chat=(awaitassistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
iffull_chatisnotNone:
            returnfull_chat.call
awaitmessage.reply(f"<b>No group voice chat found</b> {err_msg}")
returnFalse


@app.on_message(filters.command(["vcstart","startvc"],["/","!"]))
@adminsOnly("can_manage_video_chats")
asyncdefstart_group_call(c:Client,m:Message):
    chat_id=m.chat.id
assistant=awaitget_assistant(chat_id)

ifassistantisNone:
        awaitm.reply("<b>Error:</b> Assistant not found!")
return

ass=awaitassistant.get_me()
assid=ass.id

msg=awaitm.reply("<b>Starting the Voice Chat...</b>")

try:
        peer=awaitassistant.resolve_peer(chat_id)
awaitassistant.invoke(
CreateGroupCall(
peer=InputPeerChannel(
channel_id=peer.channel_id,
access_hash=peer.access_hash,
),
random_id=assistant.rnd_id()//9000000000,
)
)
awaitmsg.edit_text("<b>🎧 Voice Chat Started Successfully ⚡️</b>")
awaitset_loop(chat_id,0)

exceptChatAdminRequired:
        try:
            awaitapp.promote_chat_member(
chat_id,
assid,
privileges=ChatPrivileges(
can_manage_chat=False,
can_delete_messages=False,
can_manage_video_chats=True,
can_restrict_members=False,
can_change_info=False,
can_invite_users=False,
can_pin_messages=False,
can_promote_members=False,
),
)

peer=awaitassistant.resolve_peer(chat_id)
awaitassistant.invoke(
CreateGroupCall(
peer=InputPeerChannel(
channel_id=peer.channel_id,
access_hash=peer.access_hash,
),
random_id=assistant.rnd_id()//9000000000,
)
)

awaitapp.promote_chat_member(
chat_id,
assid,
privileges=ChatPrivileges(
can_manage_chat=False,
can_delete_messages=False,
can_manage_video_chats=False,
can_restrict_members=False,
can_change_info=False,
can_invite_users=False,
can_pin_messages=False,
can_promote_members=False,
),
)

awaitmsg.edit_text("<b>🎧 Voice Chat Started Successfully ⚡️</b>")
awaitset_loop(chat_id,0)

exceptExceptionase:
            awaitmsg.edit_text(f"<b>❌ Give the bot full permissions and try again.</b>\n<code>{e}</code>")


@app.on_message(filters.command(["vcend","endvc"],["/","!"]))
@adminsOnly("can_manage_video_chats")
asyncdefstop_group_call(c:Client,m:Message):
    chat_id=m.chat.id
assistant=awaitget_assistant(chat_id)

ifassistantisNone:
        awaitm.reply("<b>Error:</b> Assistant not found!")
return

ass=awaitassistant.get_me()
assid=ass.id

msg=awaitm.reply("<b>Closing the Voice Chat...</b>")

try:
        group_call=awaitget_group_call(assistant,m,err_msg=", Voice Chat Already Ended")
ifnotgroup_call:
            awaitmsg.delete()
return

awaitassistant.invoke(DiscardGroupCall(call=group_call))
awaitmsg.edit_text("<b>🎧 Voice Chat Closed Successfully ⚡️</b>")
awaitset_loop(chat_id,0)

exceptExceptionase:
        if"GROUPCALL_FORBIDDEN"instr(e):
            try:
                awaitapp.promote_chat_member(
chat_id,
assid,
privileges=ChatPrivileges(
can_manage_chat=False,
can_delete_messages=False,
can_manage_video_chats=True,
can_restrict_members=False,
can_change_info=False,
can_invite_users=False,
can_pin_messages=False,
can_promote_members=False,
),
)

group_call=awaitget_group_call(assistant,m,err_msg=", Voice Chat Already Ended")
ifnotgroup_call:
                    awaitmsg.delete()
return

awaitassistant.invoke(DiscardGroupCall(call=group_call))

awaitapp.promote_chat_member(
chat_id,
assid,
privileges=ChatPrivileges(
can_manage_chat=False,
can_delete_messages=False,
can_manage_video_chats=False,
can_restrict_members=False,
can_change_info=False,
can_invite_users=False,
can_pin_messages=False,
can_promote_members=False,
),
)

awaitmsg.edit_text("<b>🎧 Voice Chat Closed Successfully ⚡️</b>")
awaitset_loop(chat_id,0)

exceptExceptionasex:
                awaitmsg.edit_text(f"<b>😡 Give the bot full permissions and try again.</b>\n<code>{ex}</code>")
else:
            awaitmsg.edit_text(f"<b>Error:</b> <code>{e}</code>")
