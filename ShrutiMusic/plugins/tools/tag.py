utf-8utf-8





















importasyncio
frompyrogramimportfilters
frompyrogram.enumsimportChatMembersFilter,ParseMode
frompyrogram.errorsimportFloodWait
importrandom
importre

fromShrutiMusicimportapp

SPAM_CHATS=[]
EMOJI=[
"🦋🦋🦋🦋🦋",
"🧚🌸🧋🍬🫖",
"🥀🌷🌹🌺💐",
"🌸🌿💮🌱🌵",
"❤️💚💙💜🖤",
"💓💕💞💗💖",
"🌸💐🌺🌹🦋",
"🍔🦪🍛🍲🥗",
"🍎🍓🍒🍑🌶️",
"🧋🥤🧋🥛🍷",
"🍬🍭🧁🎂🍡",
"🍨🧉🍺☕🍻",
"🥪🥧🍦🍥🍚",
"🫖☕🍹🍷🥛",
"☕🧃🍩🍦🍙",
"🍁🌾💮🍂🌿",
"🌨️🌥️⛈️🌩️🌧️",
"🌷🏵️🌸🌺💐",
"💮🌼🌻🍀🍁",
"🧟🦸🦹🧙👸",
"🧅🍠🥕🌽🥦",
"🐷🐹🐭🐨🐻‍❄️",
"🦋🐇🐀🐈🐈‍⬛",
"🌼🌳🌲🌴🌵",
"🥩🍋🍐🍈🍇",
"🍴🍽️🔪🍶🥃",
"🕌🏰🏩⛩️🏩",
"🎉🎊🎈🎂🎀",
"🪴🌵🌴🌳🌲",
"🎄🎋🎍🎑🎎",
"🦅🦜🕊️🦤🦢",
"🦤🦩🦚🦃🦆",
"🐬🦭🦈🐋🐳",
"🐔🐟🐠🐡🦐",
"🦩🦀🦑🐙🦪",
"🐦🦂🕷️🕸️🐚",
"🥪🍰🥧🍨🍨",
"🥬🍉🧁🧇🔮",
]

defclean_text(text):
    """Escape markdown special characters"""
ifnottext:
        return""
returnre.sub(r'([_*()~`>#+-=|{}.!])',r'\\1',text)

asyncdefis_admin(chat_id,user_id):
    admin_ids=[
admin.user.id
asyncforadmininapp.get_chat_members(
chat_id,filter=ChatMembersFilter.ADMINISTRATORS
)
]
returnuser_idinadmin_ids

asyncdefprocess_members(chat_id,members,text=None,replied=None):
    tagged_members=0
usernum=0
usertxt=""
emoji_sequence=random.choice(EMOJI)
emoji_index=0

formemberinmembers:
        ifchat_idnotinSPAM_CHATS:
            break
ifmember.user.is_deletedormember.user.is_bot:
            continue

tagged_members+=1
usernum+=1

emoji=emoji_sequence[emoji_index%len(emoji_sequence)]
usertxt+=f"[{emoji}](tg://user?id={member.user.id}) "
emoji_index+=1

ifusernum==5:
            try:
                ifreplied:
                    awaitreplied.reply_text(
usertxt,
disable_web_page_preview=True,
parse_mode=ParseMode.MARKDOWN
)
else:
                    awaitapp.send_message(
chat_id,
f"{text}\n{usertxt}",
disable_web_page_preview=True,
parse_mode=ParseMode.MARKDOWN
)
awaitasyncio.sleep(2)
usernum=0
usertxt=""
emoji_sequence=random.choice(EMOJI)
emoji_index=0
exceptFloodWaitase:
                awaitasyncio.sleep(e.value+2)
exceptExceptionase:
                awaitapp.send_message(chat_id,f"Error while tagging: {str(e)}")
continue

ifusernum>0andchat_idinSPAM_CHATS:
        try:
            ifreplied:
                awaitreplied.reply_text(
usertxt,
disable_web_page_preview=True,
parse_mode=ParseMode.MARKDOWN
)
else:
                awaitapp.send_message(
chat_id,
f"{text}\n\n{usertxt}",
disable_web_page_preview=True,
parse_mode=ParseMode.MARKDOWN
)
exceptExceptionase:
            awaitapp.send_message(chat_id,f"Error sending final batch: {str(e)}")

returntagged_members

@app.on_message(
filters.command(["all","allmention","mentionall","tagall"],prefixes=["/","@"])
)
asyncdeftag_all_users(_,message):
    admin=awaitis_admin(message.chat.id,message.from_user.id)
ifnotadmin:
        returnawaitmessage.reply_text("Only admins can use this command.")

ifmessage.chat.idinSPAM_CHATS:
        returnawaitmessage.reply_text(
"Tagging process is already running. Use /cancel to stop it."
)

replied=message.reply_to_message
iflen(message.command)<2andnotreplied:
        returnawaitmessage.reply_text(
"Give some text to tag all, like: `@all Hi Friends`"
)

try:

        members=[]
asyncforminapp.get_chat_members(message.chat.id):
            members.append(m)

total_members=len(members)
SPAM_CHATS.append(message.chat.id)

text=None
ifnotreplied:
            text=clean_text(message.text.split(None,1)[1])

tagged_members=awaitprocess_members(
message.chat.id,
members,
text=text,
replied=replied
)

summary_msg=f"""
✅ Tagging completed!

Total members: {total_members}
Tagged members: {tagged_members}
"""
awaitapp.send_message(message.chat.id,summary_msg)

exceptFloodWaitase:
        awaitasyncio.sleep(e.value)
exceptExceptionase:
        awaitapp.send_message(message.chat.id,f"An error occurred: {str(e)}")
finally:
        try:
            SPAM_CHATS.remove(message.chat.id)
exceptException:
            pass

@app.on_message(
filters.command(["admintag","adminmention","admins","report"],prefixes=["/","@"])
)
asyncdeftag_all_admins(_,message):
    ifnotmessage.from_user:
        return

admin=awaitis_admin(message.chat.id,message.from_user.id)
ifnotadmin:
        returnawaitmessage.reply_text("Only admins can use this command.")

ifmessage.chat.idinSPAM_CHATS:
        returnawaitmessage.reply_text(
"Tagging process is already running. Use /cancel to stop it."
)

replied=message.reply_to_message
iflen(message.command)<2andnotreplied:
        returnawaitmessage.reply_text(
"Give some text to tag admins, like: `@admins Hi Friends`"
)

try:

        members=[]
asyncforminapp.get_chat_members(
message.chat.id,filter=ChatMembersFilter.ADMINISTRATORS
):
            members.append(m)

total_admins=len(members)
SPAM_CHATS.append(message.chat.id)

text=None
ifnotreplied:
            text=clean_text(message.text.split(None,1)[1])

tagged_admins=awaitprocess_members(
message.chat.id,
members,
text=text,
replied=replied
)

summary_msg=f"""
✅ Admin tagging completed!

Total admins: {total_admins}
Tagged admins: {tagged_admins}
"""
awaitapp.send_message(message.chat.id,summary_msg)

exceptFloodWaitase:
        awaitasyncio.sleep(e.value)
exceptExceptionase:
        awaitapp.send_message(message.chat.id,f"An error occurred: {str(e)}")
finally:
        try:
            SPAM_CHATS.remove(message.chat.id)
exceptException:
            pass

@app.on_message(
filters.command(
[
"stopmention",
"cancel",
"cancelmention",
"offmention",
"mentionoff",
"cancelall",
],
prefixes=["/","@"],
)
)
asyncdefcancelcmd(_,message):
    chat_id=message.chat.id
admin=awaitis_admin(chat_id,message.from_user.id)
ifnotadmin:
        returnawaitmessage.reply_text("Only admins can use this command.")

ifchat_idinSPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
exceptException:
            pass
returnawaitmessage.reply_text("Tagging process successfully stopped!")
else:
        returnawaitmessage.reply_text("No tagging process is currently running!")

MODULE="Tᴀɢᴀʟʟ"
HELP="""
@all or /all | /tagall or @tagall | /mentionall or @mentionall [text] or [reply to any message] - Tag all users in your group with random emojis (changes every 5 users)

/admintag or @admintag | /adminmention or @adminmention | /admins or @admins [text] or [reply to any message] - Tag all admins in your group with random emojis (changes every 5 users)

/stopmention or @stopmention | /cancel or @cancel | /offmention or @offmention | /mentionoff or @mentionoff | /cancelall or @cancelall - Stop any running tagging process

Note:

1. These commands can only be used by admins
2. The bot and assistant must be admins in your group
3. Users will be tagged with random emojis that link to their profiles
4. After completion, you'll get a summary with counts
5. Tags 5 users at a time with unique emoji sequence for each batch
"""












