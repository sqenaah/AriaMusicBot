utf-8utf-8





















frommotor.motor_asyncioimportAsyncIOMotorClient

fromconfigimportMONGO_DB_URI

from..loggingimportLOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_=AsyncIOMotorClient(MONGO_DB_URI)
mongodb=_mongo_async_.Yukki
LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
exit()












