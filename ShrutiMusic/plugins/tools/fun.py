utf-8utf-8





















importrequests
frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp


@app.on_message(
filters.command(
[
"dice",
"ludo",
"dart",
"basket",
"basketball",
"football",
"slot",
"bowling",
"jackpot",
]
)
)
asyncdefdice(c,m:Message):
    command=m.text.split()[0]
ifcommand=="/dice"orcommand=="/ludo":

        value=awaitc.send_dice(m.chat.id,reply_to_message_id=m.id)
awaitvalue.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

elifcommand=="/dart":

        value=awaitc.send_dice(m.chat.id,emoji="🎯",reply_to_message_id=m.id)
awaitvalue.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

elifcommand=="/basket"orcommand=="/basketball":
        basket=awaitc.send_dice(m.chat.id,emoji="🏀",reply_to_message_id=m.id)
awaitbasket.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(basket.dice.value))

elifcommand=="/football":
        value=awaitc.send_dice(m.chat.id,emoji="⚽",reply_to_message_id=m.id)
awaitvalue.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

elifcommand=="/slot"orcommand=="/jackpot":
        value=awaitc.send_dice(m.chat.id,emoji="🎰",reply_to_message_id=m.id)
awaitvalue.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))
elifcommand=="/bowling":
        value=awaitc.send_dice(m.chat.id,emoji="🎳",reply_to_message_id=m.id)
awaitvalue.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))


bored_api_url="https://apis.scrimba.com/bored/api/activity"


@app.on_message(filters.command("bored",prefixes="/"))
asyncdefbored_command(client,message):
    response=requests.get(bored_api_url)
ifresponse.status_code==200:
        data=response.json()
activity=data.get("activity")
ifactivity:
            awaitmessage.reply(f"𝗙𝗲𝗲𝗹𝗶𝗻𝗴 𝗯𝗼𝗿𝗲𝗱? 𝗛𝗼𝘄 𝗮𝗯𝗼𝘂𝘁:\n\n {activity}")
else:
            awaitmessage.reply("Nᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
else:
        awaitmessage.reply("Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")


__MODULE__="Fᴜɴ"
__HELP__="""
**ʜᴀᴠɪɴɢ ꜰᴜɴ:**

• `/dice`: Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
• `/ludo`: Pʟᴀʏ Lᴜᴅᴏ.
• `/dart`: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
• `/basket` ᴏʀ `/basketball`: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
• `/football`: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
• `/slot` ᴏʀ `/jackpot`: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
• `/bowling`: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
• `/bored`: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""












