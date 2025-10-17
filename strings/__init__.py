importos
fromtypingimportList

importyaml

languages={}
languages_present={}


defget_string(lang:str):
    returnlanguages[lang]


forfilenameinos.listdir(r"./strings/langs/"):
    if"en"notinlanguages:
        languages["en"]=yaml.safe_load(
open(r"./strings/langs/en.yml",encoding="utf8")
)
languages_present["en"]=languages["en"]["name"]
iffilename.endswith(".yml"):
        language_name=filename[:-4]
iflanguage_name=="en":
            continue
languages[language_name]=yaml.safe_load(
open(r"./strings/langs/"+filename,encoding="utf8")
)
foriteminlanguages["en"]:
            ifitemnotinlanguages[language_name]:
                languages[language_name][item]=languages["en"][item]
try:
        languages_present[language_name]=languages[language_name]["name"]
except:
        print("There is some issue with the language file inside bot.")
exit()
