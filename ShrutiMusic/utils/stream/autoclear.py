utf-8utf-8





















importos

fromconfigimportautoclean


asyncdefauto_clean(popped):
    try:
        rem=popped["file"]
autoclean.remove(rem)
count=autoclean.count(rem)
ifcount==0:
            if"vid_"notinremor"live_"notinremor"index_"notinrem:
                try:
                    os.remove(rem)
except:
                    pass
except:
        pass












