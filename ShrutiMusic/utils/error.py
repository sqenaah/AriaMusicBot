utf-8utf-8





















importtraceback
fromfunctoolsimportwraps

frompyrogram.errors.exceptions.forbidden_403importChatWriteForbidden

fromconfigimportLOG_GROUP_ID
fromShrutiMusicimportapp


defsplit_limits(text):
    iflen(text)<2048:
        return[text]

lines=text.splitlines(True)
small_msg=""
result=[]
forlineinlines:
        iflen(small_msg)+len(line)<2048:
            small_msg+=line
else:
            result.append(small_msg)
small_msg=line

result.append(small_msg)

returnresult


defcapture_err(func):
    @wraps(func)
asyncdefcapture(client,message,*args,**kwargs):
        try:
            returnawaitfunc(client,message,*args,**kwargs)
exceptChatWriteForbidden:
            awaitapp.leave_chat(message.chat.id)
return
exceptExceptionaserr:
            errors=traceback.format_exc()
error_feedback=split_limits(
"**ERROR** | {} | {}\n```command\n{}```\n\n```python\n{}```\n".format(
0ifnotmessage.from_userelsemessage.from_user.mention,
(
0
ifnotmessage.chat
else(
f"@{message.chat.username}"
ifmessage.chat.username
elsef"`{message.chat.id}`"
)
),
message.textormessage.caption,
"".join(errors),
),
)
forxinerror_feedback:
                awaitapp.send_message(LOGGER_ID,x)
raiseerr

returncapture












