importtime

importpsutil

fromShrutiMusic.miscimport_boot_
fromShrutiMusic.utils.formattersimportget_readable_time


asyncdefbot_sys_stats():
    bot_uptime=int(time.time()-_boot_)
UP=f"{get_readable_time(bot_uptime)}"
CPU=f"{psutil.cpu_percent(interval=0.5)}%"
RAM=f"{psutil.virtual_memory().percent}%"
DISK=f"{psutil.disk_usage('/').percent}%"
returnUP,CPU,RAM,DISK
