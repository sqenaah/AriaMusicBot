utf-8utf-8





















importasyncio
importos
importshutil
importsocket
fromdatetimeimportdatetime

importurllib3
fromgitimportRepo
fromgit.excimportGitCommandError,InvalidGitRepositoryError
frompyrogramimportfilters

importconfig
fromShrutiMusicimportapp
fromShrutiMusic.miscimportHAPP,SUDOERS,XCB
fromShrutiMusic.utils.databaseimport(
get_active_chats,
remove_active_chat,
remove_active_video_chat,
)
fromShrutiMusic.utils.decorators.languageimportlanguage
fromShrutiMusic.utils.pastebinimportNandBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


asyncdefis_heroku():
    return"heroku"insocket.getfqdn()


@app.on_message(filters.command(["getlog","logs","getlogs"])&SUDOERS)
@language
asyncdeflog_(client,message,_):
    try:
        awaitmessage.reply_document(document="log.txt")
except:
        awaitmessage.reply_text(_["server_1"])


@app.on_message(filters.command(["update","gitpull"])&SUDOERS)
@language
asyncdefupdate_(client,message,_):
    ifawaitis_heroku():
        ifHAPPisNone:
            returnawaitmessage.reply_text(_["server_2"])
response=awaitmessage.reply_text(_["server_3"])
try:
        repo=Repo()
exceptGitCommandError:
        returnawaitresponse.edit(_["server_4"])
exceptInvalidGitRepositoryError:
        returnawaitresponse.edit(_["server_5"])
to_exc=f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
os.system(to_exc)
awaitasyncio.sleep(7)
verification=""
REPO_=repo.remotes.origin.url.split(".git")[0]
forchecksinrepo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification=str(checks.count())
ifverification=="":
        returnawaitresponse.edit(_["server_6"])
updates=""
ordinal=lambdaformat:"%d%s"%(
format,
"tsnrhtdd"[(format//10%10!=1)*(format%10<4)*format%10::4],
)
forinfoinrepo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates+=f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
_update_response_="<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n<b><u>ᴜᴩᴅᴀᴛᴇs:</u></b>\n\n"
_final_updates_=_update_response_+updates
iflen(_final_updates_)>4096:
        url=awaitNandBin(updates)
nrs=awaitresponse.edit(
f"<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n<u><b>ᴜᴩᴅᴀᴛᴇs :</b></u>\n\n<a href={url}>ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs</a>"
)
else:
        nrs=awaitresponse.edit(_final_updates_,disable_web_page_preview=True)
os.system("git stash &> /dev/null && git pull")

try:
        served_chats=awaitget_active_chats()
forxinserved_chats:
            try:
                awaitapp.send_message(
chat_id=int(x),
text=_["server_8"].format(app.mention),
)
awaitremove_active_chat(x)
awaitremove_active_video_chat(x)
except:
                pass
awaitresponse.edit(f"{nrs.text}\n\n{_['server_7']}")
except:
        pass

ifawaitis_heroku():
        try:
            os.system(
f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
)
return
exceptExceptionaserr:
            awaitresponse.edit(f"{nrs.text}\n\n{_['server_9']}")
returnawaitapp.send_message(
chat_id=config.LOG_GROUP_ID,
text=_["server_10"].format(err),
)
else:
        os.system("pip3 install -r requirements.txt")
os.system(f"kill -9 {os.getpid()} && bash start")
exit()


@app.on_message(filters.command(["restart"])&SUDOERS)
asyncdefrestart_(_,message):
    response=awaitmessage.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
ac_chats=awaitget_active_chats()
forxinac_chats:
        try:
            awaitapp.send_message(
chat_id=int(x),
text=f"{app.mention} ɪs ʀᴇsᴛᴀʀᴛɪɴɢ...\n\nʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 15-20 sᴇᴄᴏɴᴅs.",
)
awaitremove_active_chat(x)
awaitremove_active_video_chat(x)
except:
            pass

try:
        shutil.rmtree("downloads")
shutil.rmtree("raw_files")
shutil.rmtree("cache")
except:
        pass
awaitresponse.edit_text(
"» ʀᴇsᴛᴀʀᴛ ᴘʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ sᴇᴄᴏɴᴅs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ sᴛᴀʀᴛs..."
)
os.system(f"kill -9 {os.getpid()} && bash start")












