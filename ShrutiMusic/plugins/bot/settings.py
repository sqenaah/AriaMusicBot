utf-8utf-8





















frompyrogramimportfilters
frompyrogram.enumsimportChatType
frompyrogram.errorsimportMessageNotModified
frompyrogram.typesimport(
CallbackQuery,
InlineKeyboardButton,
InlineKeyboardMarkup,
Message,
)

fromShrutiMusicimportapp
fromShrutiMusic.utils.databaseimport(
add_nonadmin_chat,
get_authuser,
get_authuser_names,
get_playmode,
get_playtype,
get_upvote_count,
is_nonadmin_chat,
is_skipmode,
remove_nonadmin_chat,
set_playmode,
set_playtype,
set_upvotes,
skip_off,
skip_on,
)
fromShrutiMusic.utilsimportbot_sys_stats
fromShrutiMusic.utils.decorators.adminsimportActualAdminCB
fromShrutiMusic.utils.decorators.languageimportlanguage,languageCB
fromShrutiMusic.utils.inline.settingsimport(
auth_users_markup,
playmode_users_markup,
setting_markup,
vote_mode_markup,
)
fromShrutiMusic.utils.inline.startimportprivate_panel
fromconfigimportBANNED_USERS,OWNER_ID


@app.on_message(
filters.command(["settings","setting"])&filters.group&~BANNED_USERS
)
@language
asyncdefsettings_mar(client,message:Message,_):
    buttons=setting_markup(_)
awaitmessage.reply_text(
_["setting_1"].format(app.mention,message.chat.id,message.chat.title),
reply_markup=InlineKeyboardMarkup(buttons),
)


@app.on_callback_query(filters.regex("settings_helper")&~BANNED_USERS)
@languageCB
asyncdefsettings_cb(client,CallbackQuery,_):
    try:
        awaitCallbackQuery.answer(_["set_cb_5"])
except:
        pass
buttons=setting_markup(_)
returnawaitCallbackQuery.edit_message_text(
_["setting_1"].format(
app.mention,
CallbackQuery.message.chat.id,
CallbackQuery.message.chat.title,
),
reply_markup=InlineKeyboardMarkup(buttons),
)


@app.on_callback_query(filters.regex("settingsback_helper")&~BANNED_USERS)
@languageCB
asyncdefsettings_back_markup(client,CallbackQuery:CallbackQuery,_):
    try:
        awaitCallbackQuery.answer()
except:
        pass
ifCallbackQuery.message.chat.type==ChatType.PRIVATE:
        awaitapp.resolve_peer(OWNER_ID)
OWNER=OWNER_ID
buttons=private_panel(_)
UP,CPU,RAM,DISK=awaitbot_sys_stats()
returnawaitCallbackQuery.edit_message_text(
_["start_2"].format(CallbackQuery.from_user.mention,app.mention,UP,DISK,CPU,RAM),
reply_markup=InlineKeyboardMarkup(buttons),
)
else:
        buttons=setting_markup(_)
returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)


@app.on_callback_query(
filters.regex(
pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$"
)
&~BANNED_USERS
)
@languageCB
asyncdefwithout_Admin_rights(client,CallbackQuery,_):
    command=CallbackQuery.matches[0].group(1)
ifcommand=="SEARCHANSWER":
        try:
            returnawaitCallbackQuery.answer(_["setting_2"],show_alert=True)
except:
            return
ifcommand=="PLAYMODEANSWER":
        try:
            returnawaitCallbackQuery.answer(_["setting_5"],show_alert=True)
except:
            return
ifcommand=="PLAYTYPEANSWER":
        try:
            returnawaitCallbackQuery.answer(_["setting_6"],show_alert=True)
except:
            return
ifcommand=="AUTHANSWER":
        try:
            returnawaitCallbackQuery.answer(_["setting_3"],show_alert=True)
except:
            return
ifcommand=="VOTEANSWER":
        try:
            returnawaitCallbackQuery.answer(
_["setting_8"],
show_alert=True,
)
except:
            return
ifcommand=="ANSWERVOMODE":
        current=awaitget_upvote_count(CallbackQuery.message.chat.id)
try:
            returnawaitCallbackQuery.answer(
_["setting_9"].format(current),
show_alert=True,
)
except:
            return
ifcommand=="PM":
        try:
            awaitCallbackQuery.answer(_["set_cb_2"],show_alert=True)
except:
            pass
playmode=awaitget_playmode(CallbackQuery.message.chat.id)
ifplaymode=="Direct":
            Direct=True
else:
            Direct=None
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            Group=True
else:
            Group=None
playty=awaitget_playtype(CallbackQuery.message.chat.id)
ifplayty=="Everyone":
            Playtype=None
else:
            Playtype=True
buttons=playmode_users_markup(_,Direct,Group,Playtype)
ifcommand=="AU":
        try:
            awaitCallbackQuery.answer(_["set_cb_1"],show_alert=True)
except:
            pass
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            buttons=auth_users_markup(_,True)
else:
            buttons=auth_users_markup(_)
ifcommand=="VM":
        mode=awaitis_skipmode(CallbackQuery.message.chat.id)
current=awaitget_upvote_count(CallbackQuery.message.chat.id)
buttons=vote_mode_markup(_,current,mode)
try:
        returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
exceptMessageNotModified:
        return


@app.on_callback_query(filters.regex("FERRARIUDTI")&~BANNED_USERS)
@ActualAdminCB
asyncdefaddition(client,CallbackQuery,_):
    callback_data=CallbackQuery.data.strip()
mode=callback_data.split(None,1)[1]
ifnotawaitis_skipmode(CallbackQuery.message.chat.id):
        returnawaitCallbackQuery.answer(_["setting_10"],show_alert=True)
current=awaitget_upvote_count(CallbackQuery.message.chat.id)
ifmode=="M":
        final=current-2
print(final)
iffinal==0:
            returnawaitCallbackQuery.answer(
_["setting_11"],
show_alert=True,
)
iffinal<=2:
            final=2
awaitset_upvotes(CallbackQuery.message.chat.id,final)
else:
        final=current+2
print(final)
iffinal==17:
            returnawaitCallbackQuery.answer(
_["setting_12"],
show_alert=True,
)
iffinal>=15:
            final=15
awaitset_upvotes(CallbackQuery.message.chat.id,final)
buttons=vote_mode_markup(_,final,True)
try:
        returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
exceptMessageNotModified:
        return


@app.on_callback_query(
filters.regex(pattern=r"^(MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$")
&~BANNED_USERS
)
@ActualAdminCB
asyncdefplaymode_ans(client,CallbackQuery,_):
    command=CallbackQuery.matches[0].group(1)
ifcommand=="CHANNELMODECHANGE":
        is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            awaitadd_nonadmin_chat(CallbackQuery.message.chat.id)
Group=None
else:
            awaitremove_nonadmin_chat(CallbackQuery.message.chat.id)
Group=True
playmode=awaitget_playmode(CallbackQuery.message.chat.id)
ifplaymode=="Direct":
            Direct=True
else:
            Direct=None
playty=awaitget_playtype(CallbackQuery.message.chat.id)
ifplayty=="Everyone":
            Playtype=None
else:
            Playtype=True
buttons=playmode_users_markup(_,Direct,Group,Playtype)
ifcommand=="MODECHANGE":
        try:
            awaitCallbackQuery.answer(_["set_cb_3"],show_alert=True)
except:
            pass
playmode=awaitget_playmode(CallbackQuery.message.chat.id)
ifplaymode=="Direct":
            awaitset_playmode(CallbackQuery.message.chat.id,"Inline")
Direct=None
else:
            awaitset_playmode(CallbackQuery.message.chat.id,"Direct")
Direct=True
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            Group=True
else:
            Group=None
playty=awaitget_playtype(CallbackQuery.message.chat.id)
ifplayty=="Everyone":
            Playtype=False
else:
            Playtype=True
buttons=playmode_users_markup(_,Direct,Group,Playtype)
ifcommand=="PLAYTYPECHANGE":
        try:
            awaitCallbackQuery.answer(_["set_cb_3"],show_alert=True)
except:
            pass
playty=awaitget_playtype(CallbackQuery.message.chat.id)
ifplayty=="Everyone":
            awaitset_playtype(CallbackQuery.message.chat.id,"Admin")
Playtype=False
else:
            awaitset_playtype(CallbackQuery.message.chat.id,"Everyone")
Playtype=True
playmode=awaitget_playmode(CallbackQuery.message.chat.id)
ifplaymode=="Direct":
            Direct=True
else:
            Direct=None
is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            Group=True
else:
            Group=None
buttons=playmode_users_markup(_,Direct,Group,Playtype)
try:
        returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
exceptMessageNotModified:
        return


@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$")&~BANNED_USERS)
@ActualAdminCB
asyncdefauthusers_mar(client,CallbackQuery,_):
    command=CallbackQuery.matches[0].group(1)
ifcommand=="AUTHLIST":
        _authusers=awaitget_authuser_names(CallbackQuery.message.chat.id)
ifnot_authusers:
            try:
                returnawaitCallbackQuery.answer(_["setting_4"],show_alert=True)
except:
                return
else:
            try:
                awaitCallbackQuery.answer(_["set_cb_4"],show_alert=True)
except:
                pass
j=0
awaitCallbackQuery.edit_message_text(_["auth_6"])
msg=_["auth_7"].format(CallbackQuery.message.chat.title)
fornotein_authusers:
                _note=awaitget_authuser(CallbackQuery.message.chat.id,note)
user_id=_note["auth_user_id"]
admin_id=_note["admin_id"]
admin_name=_note["admin_name"]
try:
                    user=awaitapp.get_users(user_id)
user=user.first_name
j+=1
except:
                    continue
msg+=f"{j}➤ {user}[<code>{user_id}</code>]\n"
msg+=f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
upl=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],callback_data=f"AU"
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data=f"close",
),
]
]
)
try:
                returnawaitCallbackQuery.edit_message_text(msg,reply_markup=upl)
exceptMessageNotModified:
                return
try:
        awaitCallbackQuery.answer(_["set_cb_3"],show_alert=True)
except:
        pass
ifcommand=="AUTH":
        is_non_admin=awaitis_nonadmin_chat(CallbackQuery.message.chat.id)
ifnotis_non_admin:
            awaitadd_nonadmin_chat(CallbackQuery.message.chat.id)
buttons=auth_users_markup(_)
else:
            awaitremove_nonadmin_chat(CallbackQuery.message.chat.id)
buttons=auth_users_markup(_,True)
try:
        returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
exceptMessageNotModified:
        return


@app.on_callback_query(filters.regex("VOMODECHANGE")&~BANNED_USERS)
@ActualAdminCB
asyncdefvote_change(client,CallbackQuery,_):
    ifCallbackQuery.matchesandCallbackQuery.matches[0].groups():command=CallbackQuery.matches[0].group(1)else:command=None
try:
        awaitCallbackQuery.answer(_["set_cb_3"],show_alert=True)
except:
        pass
mod=None
ifawaitis_skipmode(CallbackQuery.message.chat.id):
        awaitskip_off(CallbackQuery.message.chat.id)
else:
        mod=True
awaitskip_on(CallbackQuery.message.chat.id)
current=awaitget_upvote_count(CallbackQuery.message.chat.id)
buttons=vote_mode_markup(_,current,mod)

try:
        returnawaitCallbackQuery.edit_message_reply_markup(
reply_markup=InlineKeyboardMarkup(buttons)
)
exceptMessageNotModified:
        return












