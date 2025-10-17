utf-8utf-8





















frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportYouTube,app
fromShrutiMusic.core.callimportNand
fromShrutiMusic.miscimportdb
fromShrutiMusic.utilsimportAdminRightsCheck,seconds_to_min
fromShrutiMusic.utils.inlineimportclose_markup
fromconfigimportBANNED_USERS


@app.on_message(
filters.command(["seek","cseek","seekback","cseekback"])
&filters.group
&~BANNED_USERS
)
@AdminRightsCheck
asyncdefseek_comm(cli,message:Message,_,chat_id):
    iflen(message.command)==1:
        returnawaitmessage.reply_text(_["admin_20"])
query=message.text.split(None,1)[1].strip()
ifnotquery.isnumeric():
        returnawaitmessage.reply_text(_["admin_21"])
playing=db.get(chat_id)
ifnotplaying:
        returnawaitmessage.reply_text(_["queue_2"])
duration_seconds=int(playing[0]["seconds"])
ifduration_seconds==0:
        returnawaitmessage.reply_text(_["admin_22"])
file_path=playing[0]["file"]
duration_played=int(playing[0]["played"])
duration_to_skip=int(query)
duration=playing[0]["dur"]
ifmessage.command[0][-2]=="c":
        if(duration_played-duration_to_skip)<=10:
            returnawaitmessage.reply_text(
text=_["admin_23"].format(seconds_to_min(duration_played),duration),
reply_markup=close_markup(_),
)
to_seek=duration_played-duration_to_skip+1
else:
        if(duration_seconds-(duration_played+duration_to_skip))<=10:
            returnawaitmessage.reply_text(
text=_["admin_23"].format(seconds_to_min(duration_played),duration),
reply_markup=close_markup(_),
)
to_seek=duration_played+duration_to_skip+1
mystic=awaitmessage.reply_text(_["admin_24"])
if"vid_"infile_path:
        n,file_path=awaitYouTube.video(playing[0]["vidid"],True)
ifn==0:
            returnawaitmessage.reply_text(_["admin_22"])
check=(playing[0]).get("speed_path")
ifcheck:
        file_path=check
if"index_"infile_path:
        file_path=playing[0]["vidid"]
try:
        awaitNand.seek_stream(
chat_id,
file_path,
seconds_to_min(to_seek),
duration,
playing[0]["streamtype"],
)
except:
        returnawaitmystic.edit_text(_["admin_26"],reply_markup=close_markup(_))
ifmessage.command[0][-2]=="c":
        db[chat_id][0]["played"]-=duration_to_skip
else:
        db[chat_id][0]["played"]+=duration_to_skip
awaitmystic.edit_text(
text=_["admin_25"].format(seconds_to_min(to_seek),message.from_user.mention),
reply_markup=close_markup(_),
)












