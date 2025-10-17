utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.databaseimportblacklist_chat,blacklisted_chats,whitelist_chat
fromShrutiMusic.utils.decorators.languageimportlanguage
fromconfigimportBANNED_USERS


@app.on_message(filters.command(["blchat","blacklistchat"])&SUDOERS)
@language
asyncdefblacklist_chat_func(client,message:Message,_):
    iflen(message.command)!=2:
        returnawaitmessage.reply_text(_["black_1"])
chat_id=int(message.text.strip().split()[1])
ifchat_idinawaitblacklisted_chats():
        returnawaitmessage.reply_text(_["black_2"])
blacklisted=awaitblacklist_chat(chat_id)
ifblacklisted:
        awaitmessage.reply_text(_["black_3"])
else:
        awaitmessage.reply_text(_["black_9"])
try:
        awaitapp.leave_chat(chat_id)
except:
        pass


@app.on_message(
filters.command(["whitelistchat","unblacklistchat","unblchat"])&SUDOERS
)
@language
asyncdefwhite_funciton(client,message:Message,_):
    iflen(message.command)!=2:
        returnawaitmessage.reply_text(_["black_4"])
chat_id=int(message.text.strip().split()[1])
ifchat_idnotinawaitblacklisted_chats():
        returnawaitmessage.reply_text(_["black_5"])
whitelisted=awaitwhitelist_chat(chat_id)
ifwhitelisted:
        returnawaitmessage.reply_text(_["black_6"])
awaitmessage.reply_text(_["black_9"])


@app.on_message(filters.command(["blchats","blacklistedchats"])&~BANNED_USERS)
@language
asyncdefall_chats(client,message:Message,_):
    text=_["black_7"]
j=0
forcount,chat_idinenumerate(awaitblacklisted_chats(),1):
        try:
            title=(awaitapp.get_chat(chat_id)).title
except:
            title="ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
j=1
text+=f"{count}. {title}[<code>{chat_id}</code>]\n"
ifj==0:
        awaitmessage.reply_text(_["black_8"].format(app.mention))
else:
        awaitmessage.reply_text(text)












