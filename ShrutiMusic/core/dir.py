utf-8utf-8
importos

from..loggingimportLOGGER


defdirr():
    forfileinos.listdir():
        iffile.endswith(".jpg"):
            os.remove(file)
eliffile.endswith(".jpeg"):
            os.remove(file)
eliffile.endswith(".png"):
            os.remove(file)

if"downloads"notinos.listdir():
        os.mkdir("downloads")
if"cache"notinos.listdir():
        os.mkdir("cache")

LOGGER(__name__).info("Directories Updated.")
