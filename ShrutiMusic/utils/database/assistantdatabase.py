mportrandom

fromShrutiMusicimportuserbot
fromShrutiMusic.core.mongoimportmongodb

db=mongodb.assistants

assistantdict={}


asyncdefget_client(assistant:int):
    ifint(assistant)==1:
        returnuserbot.one
elifint(assistant)==2:
        returnuserbot.two
elifint(assistant)==3:
        returnuserbot.three
elifint(assistant)==4:
        returnuserbot.four
elifint(assistant)==5:
        returnuserbot.five


asyncdefsave_assistant(chat_id,number):
    number=int(number)
awaitdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":number}},
upsert=True,
)


asyncdefset_assistant(chat_id):
    fromShrutiMusic.core.userbotimportassistants

ran_assistant=random.choice(assistants)
assistantdict[chat_id]=ran_assistant
awaitdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":ran_assistant}},
upsert=True,
)
userbot=awaitget_client(ran_assistant)
returnuserbot


asyncdefget_assistant(chat_id:int)->str:
    fromShrutiMusic.core.userbotimportassistants

assistant=assistantdict.get(chat_id)
ifnotassistant:
        dbassistant=awaitdb.find_one({"chat_id":chat_id})
ifnotdbassistant:
            userbot=awaitset_assistant(chat_id)
returnuserbot
else:
            got_assis=dbassistant["assistant"]
ifgot_assisinassistants:
                assistantdict[chat_id]=got_assis
userbot=awaitget_client(got_assis)
returnuserbot
else:
                userbot=awaitset_assistant(chat_id)
returnuserbot
else:
        ifassistantinassistants:
            userbot=awaitget_client(assistant)
returnuserbot
else:
            userbot=awaitset_assistant(chat_id)
returnuserbot


asyncdefset_calls_assistant(chat_id):
    fromShrutiMusic.core.userbotimportassistants

ran_assistant=random.choice(assistants)
assistantdict[chat_id]=ran_assistant
awaitdb.update_one(
{"chat_id":chat_id},
{"$set":{"assistant":ran_assistant}},
upsert=True,
)
returnran_assistant


asyncdefgroup_assistant(self,chat_id:int)->int:
    fromShrutiMusic.core.userbotimportassistants

assistant=assistantdict.get(chat_id)
ifnotassistant:
        dbassistant=awaitdb.find_one({"chat_id":chat_id})
ifnotdbassistant:
            assis=awaitset_calls_assistant(chat_id)
else:
            assis=dbassistant["assistant"]
ifassisinassistants:
                assistantdict[chat_id]=assis
assis=assis
else:
                assis=awaitset_calls_assistant(chat_id)
else:
        ifassistantinassistants:
            assis=assistant
else:
            assis=awaitset_calls_assistant(chat_id)
ifint(assis)==1:
        returnself.one
elifint(assis)==2:
        returnself.two
elifint(assis)==3:
        returnself.three
elifint(assis)==4:
        returnself.four
elifint(assis)==5:
        returnself.five
