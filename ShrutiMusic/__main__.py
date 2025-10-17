utf-8utf-8





















importasyncio
importimportlib
frompyrogramimportidle
frompyrogram.typesimportBotCommand
frompytgcalls.exceptionsimportNoActiveGroupCall
importconfig
fromShrutiMusicimportLOGGER,app,userbot
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportsudo
fromShrutiMusic.pluginsimportALL_MODULES
fromShrutiMusic.utils.databaseimportget_banned_users,get_gbanned
fromconfigimportBANNED_USERS


COMMANDS=[
BotCommand("start","🚀 Start bot"),
BotCommand("help","❓ Help menu and Many More Management Commands"),
BotCommand("ping","📡 Ping and system stats"),
BotCommand("play","🎵 Start streaming the requested track"),
BotCommand("vplay","📹 Start video streaming"),
BotCommand("playrtmps","📺 Play Live Video"),
BotCommand("playforce","⚠️ Force play audio track"),
BotCommand("vplayforce","⚠️ Force play video track"),
BotCommand("pause","⏸ Pause the stream"),
BotCommand("resume","▶️ Resume the stream"),
BotCommand("skip","⏭ Skip the current track"),
BotCommand("end","🛑 End the stream"),
BotCommand("stop","🛑 Stop the stream"),
BotCommand("queue","📄 Show track queue"),
BotCommand("auth","➕ Add a user to auth list"),
BotCommand("unauth","➖ Remove a user from auth list"),
BotCommand("authusers","👥 Show list of auth users"),
BotCommand("cplay","📻 Channel audio play"),
BotCommand("cvplay","📺 Channel video play"),
BotCommand("cplayforce","🚨 Channel force audio play"),
BotCommand("cvplayforce","🚨 Channel force video play"),
BotCommand("channelplay","🔗 Connect group to channel"),
BotCommand("loop","🔁 Enable/disable loop"),
BotCommand("stats","📊 Bot stats"),
BotCommand("shuffle","🔀 Shuffle the queue"),
BotCommand("seek","⏩ Seek forward"),
BotCommand("seekback","⏪ Seek backward"),
BotCommand("song","🎶 Download song (mp3/mp4)"),
BotCommand("speed","⏩ Adjust audio playback speed (group)"),
BotCommand("cspeed","⏩ Adjust audio speed (channel)"),
BotCommand("tagall","📢 Tag everyone"),
]

asyncdefsetup_bot_commands():
    """Setup bot commands during startup"""
try:

        awaitapp.set_bot_commands(COMMANDS)
LOGGER("ShrutiMusic").info("Bot commands set successfully!")

exceptExceptionase:
        LOGGER("ShrutiMusic").error(f"Failed to set bot commands: {str(e)}")

asyncdefinit():
    if(
notconfig.STRING1
andnotconfig.STRING2
andnotconfig.STRING3
andnotconfig.STRING4
andnotconfig.STRING5
):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
exit()

awaitsudo()

try:
        users=awaitget_gbanned()
foruser_idinusers:
            BANNED_USERS.add(user_id)
users=awaitget_banned_users()
foruser_idinusers:
            BANNED_USERS.add(user_id)
except:
        pass

awaitapp.start()


awaitsetup_bot_commands()

forall_moduleinALL_MODULES:
        importlib.import_module("ShrutiMusic.plugins"+all_module)

LOGGER("ShrutiMusic.plugins").info("Successfully Imported Modules...")

awaituserbot.start()
awaitNand.start()

try:
        awaitNand.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
exceptNoActiveGroupCall:
        LOGGER("ShrutiMusic").error(
"Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
)
exit()
except:
        pass

awaitNand.decorators()

LOGGER("ShrutiMusic").info(
"\x53\x68\x72\x75\x74\x69\x20\x4d\x75\x73\x69\x63\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73"
)

awaitidle()

awaitapp.stop()
awaituserbot.stop()
LOGGER("ShrutiMusic").info("Stopping Shruti Music Bot...🥺")

if__name__=="__main__":
    asyncio.get_event_loop().run_until_complete(init())












