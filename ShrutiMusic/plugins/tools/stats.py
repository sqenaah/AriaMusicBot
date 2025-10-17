utf-8utf-8





















importplatform
fromsysimportversionaspyver

importpsutil
frompyrogramimport__version__aspyrover
frompyrogramimportfilters
frompyrogram.errorsimportMessageIdInvalid
frompyrogram.typesimportInputMediaPhoto,Message
frompytgcalls.__version__import__version__aspytgver

importconfig
fromShrutiMusicimportapp
fromShrutiMusic.core.userbotimportassistants
fromShrutiMusic.miscimportSUDOERS,mongodb
fromShrutiMusic.pluginsimportALL_MODULES
fromShrutiMusic.utils.databaseimportget_served_chats,get_served_users,get_sudoers,is_autoend,is_autoleave
fromShrutiMusic.utils.decorators.languageimportlanguage,languageCB
fromShrutiMusic.utils.inline.statsimportback_stats_buttons,stats_buttons
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["stats","gstats"])&filters.group&~BANNED_USERS)
@language
asyncdefstats_global(client,message:Message,_):
    upl=stats_buttons(_,Trueifmessage.from_user.idinSUDOERSelseFalse)
awaitmessage.reply_photo(
photo=config.STATS_IMG_URL,
caption=_["gstats_2"].format(app.mention),
reply_markup=upl,
)


@app.on_callback_query(filters.regex("stats_back")&~BANNED_USERS)
@languageCB
asyncdefhome_stats(client,CallbackQuery,_):
    upl=stats_buttons(_,TrueifCallbackQuery.from_user.idinSUDOERSelseFalse)
awaitCallbackQuery.edit_message_text(
text=_["gstats_2"].format(app.mention),
reply_markup=upl,
)


@app.on_callback_query(filters.regex("TopOverall")&~BANNED_USERS)
@languageCB
asyncdefoverall_stats(client,CallbackQuery,_):
    awaitCallbackQuery.answer()
upl=back_stats_buttons(_)
try:
        awaitCallbackQuery.answer()
except:
        pass
awaitCallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
served_chats=len(awaitget_served_chats())
served_users=len(awaitget_served_users())
text=_["gstats_3"].format(
app.mention,
len(assistants),
len(BANNED_USERS),
served_chats,
served_users,
len(ALL_MODULES),
len(SUDOERS),
awaitis_autoend(),
config.DURATION_LIMIT_MIN,
awaitis_autoleave()
)
med=InputMediaPhoto(media=config.STATS_IMG_URL,caption=text)
try:
        awaitCallbackQuery.edit_message_media(media=med,reply_markup=upl)
exceptMessageIdInvalid:
        awaitCallbackQuery.message.reply_photo(
photo=config.STATS_IMG_URL,caption=text,reply_markup=upl
)


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
asyncdefbot_stats(client,CallbackQuery,_):
    ifCallbackQuery.from_user.idnotinSUDOERS:
        returnawaitCallbackQuery.answer(_["gstats_4"],show_alert=True)
upl=back_stats_buttons(_)
try:
        awaitCallbackQuery.answer()
except:
        pass
awaitCallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
p_core=psutil.cpu_count(logical=False)
t_core=psutil.cpu_count(logical=True)
ram=str(round(psutil.virtual_memory().total/(1024.0**3)))+" ɢʙ"
try:
        cpu_freq=psutil.cpu_freq().current
ifcpu_freq>=1000:
            cpu_freq=f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
else:
            cpu_freq=f"{round(cpu_freq, 2)}ᴍʜᴢ"
except:
        cpu_freq="ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
hdd=psutil.disk_usage("/")
total=hdd.total/(1024.0**3)
used=hdd.used/(1024.0**3)
free=hdd.free/(1024.0**3)
call=awaitmongodb.command("dbstats")
datasize=call["dataSize"]/1024
storage=call["storageSize"]/1024
served_chats=len(awaitget_served_chats())
served_users=len(awaitget_served_users())
text=_["gstats_5"].format(
app.mention,
len(ALL_MODULES),
platform.system(),
ram,
p_core,
t_core,
cpu_freq,
pyver.split()[0],
pyrover,
pytgver,
str(total)[:4],
str(used)[:4],
str(free)[:4],
served_chats,
served_users,
len(BANNED_USERS),
len(awaitget_sudoers()),
str(datasize)[:6],
storage,
call["collections"],
call["objects"],
)
med=InputMediaPhoto(media=config.STATS_IMG_URL,caption=text)
try:
        awaitCallbackQuery.edit_message_media(media=med,reply_markup=upl)
exceptMessageIdInvalid:
        awaitCallbackQuery.message.reply_photo(
photo=config.STATS_IMG_URL,caption=text,reply_markup=upl
)












