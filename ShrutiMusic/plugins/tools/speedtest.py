utf-8utf-8





















importasyncio

importspeedtest
frompyrogramimportfilters
frompyrogram.typesimportMessage

fromShrutiMusicimportapp
fromShrutiMusic.miscimportSUDOERS
fromShrutiMusic.utils.decorators.languageimportlanguage


deftestspeed(m,_):
    try:
        test=speedtest.Speedtest()
test.get_best_server()
m=m.edit_text(_["server_12"])
test.download()
m=m.edit_text(_["server_13"])
test.upload()
test.results.share()
result=test.results.dict()
m=m.edit_text(_["server_14"])
exceptExceptionase:
        returnm.edit_text(f"<code>{e}</code>")
returnresult


@app.on_message(filters.command(["speedtest","spt"])&SUDOERS)
@language
asyncdefspeedtest_function(client,message:Message,_):
    m=awaitmessage.reply_text(_["server_11"])
loop=asyncio.get_event_loop()
result=awaitloop.run_in_executor(None,testspeed,m,_)
output=_["server_15"].format(
result["client"]["isp"],
result["client"]["country"],
result["server"]["name"],
result["server"]["country"],
result["server"]["cc"],
result["server"]["sponsor"],
result["server"]["latency"],
result["ping"],
)
msg=awaitmessage.reply_photo(photo=result["share"],caption=output)
awaitm.delete()












