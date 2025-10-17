importsocket
importtime

importheroku3
frompyrogramimportfilters

importconfig
fromShrutiMusic.core.mongoimportmongodb

from.loggingimportLOGGER

SUDOERS=filters.user()

HAPP=None
_boot_=time.time()


defis_heroku():
    return"heroku"insocket.getfqdn()


XCB=[
"/",
"@",
".",
"com",
":",
"git",
"heroku",
"push",
str(config.HEROKU_API_KEY),
"https",
str(config.HEROKU_APP_NAME),
"HEAD",
"master",
]


defdbb():
    globaldb
db={}
LOGGER(__name__).info(f"Local Database Initialized.")


asyncdefsudo():
    globalSUDOERS
SUDOERS.add(config.OWNER_ID)
sudoersdb=mongodb.sudoers
sudoers=awaitsudoersdb.find_one({"sudo":"sudo"})
sudoers=[]ifnotsudoerselsesudoers["sudoers"]
ifconfig.OWNER_IDnotinsudoers:
        sudoers.append(config.OWNER_ID)
awaitsudoersdb.update_one(
{"sudo":"sudo"},
{"$set":{"sudoers":sudoers}},
upsert=True,
)
ifsudoers:
        foruser_idinsudoers:
            SUDOERS.add(user_id)
LOGGER(__name__).info(f"Sudoers Loaded.")


defheroku():
    globalHAPP
ifis_heroku:
        ifconfig.HEROKU_API_KEYandconfig.HEROKU_APP_NAME:
            try:
                Heroku=heroku3.from_key(config.HEROKU_API_KEY)
HAPP=Heroku.app(config.HEROKU_APP_NAME)
LOGGER(__name__).info(f"Heroku App Configured")
exceptBaseException:
                LOGGER(__name__).warning(
f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
)i
