utf-8utf-8





















frompyrogram.enumsimportMessageEntityType
frompyrogram.typesimportMessage,User

fromShrutiMusicimportapp


asyncdefextract_user(m:Message)->User:
    ifm.reply_to_message:
        returnm.reply_to_message.from_user
msg_entities=m.entities[1]ifm.text.startswith("/")elsem.entities[0]
returnawaitapp.get_users(
msg_entities.user.id
ifmsg_entities.type==MessageEntityType.TEXT_MENTION
elseint(m.command[1])
ifm.command[1].isdecimal()
elsem.command[1]
)












