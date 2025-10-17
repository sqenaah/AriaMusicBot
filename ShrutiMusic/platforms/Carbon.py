utf-8utf-8





















importrandom
fromos.pathimportrealpath

importaiohttp
fromaiohttpimportclient_exceptions


classUnableToFetchCarbon(Exception):
    pass


themes=[
"3024-night",
"a11y-dark",
"blackboard",
"base16-dark",
"base16-light",
"cobalt",
"duotone-dark",
"dracula-pro",
"hopscotch",
"lucario",
"material",
"monokai",
"nightowl",
"nord",
"oceanic-next",
"one-light",
"one-dark",
"panda-syntax",
"parasio-dark",
"seti",
"shades-of-purple",
"solarized+dark",
"solarized+light",
"synthwave-84",
"twilight",
"verminal",
"vscode",
"yeti",
"zenburn",
]

colour=[
"#FF0000",
"#FF5733",
"#FFFF00",
"#008000",
"#0000FF",
"#800080",
"#A52A2A",
"#FF00FF",
"#D2B48C",
"#00FFFF",
"#808000",
"#800000",
"#00FFFF",
"#30D5C8",
"#00FF00",
"#008080",
"#4B0082",
"#EE82EE",
"#FFC0CB",
"#000000",
"#FFFFFF",
"#808080",
]


classCarbonAPI:
    def__init__(self):
        self.language="auto"
self.drop_shadow=True
self.drop_shadow_blur="68px"
self.drop_shadow_offset="20px"
self.font_family="JetBrains Mono"
self.width_adjustment=True
self.watermark=False

asyncdefgenerate(self,text:str,user_id):
        asyncwithaiohttp.ClientSession(
headers={"Content-Type":"application/json"},
)asses:
            params={
"code":text,
}
params["backgroundColor"]=random.choice(colour)
params["theme"]=random.choice(themes)
params["dropShadow"]=self.drop_shadow
params["dropShadowOffsetY"]=self.drop_shadow_offset
params["dropShadowBlurRadius"]=self.drop_shadow_blur
params["fontFamily"]=self.font_family
params["language"]=self.language
params["watermark"]=self.watermark
params["widthAdjustment"]=self.width_adjustment
try:
                request=awaitses.post(
"https://carbonara.solopov.dev/api/cook",
json=params,
)
exceptclient_exceptions.ClientConnectorError:
                raiseUnableToFetchCarbon("Can not reach the Host!")
resp=awaitrequest.read()
withopen(f"cache/carbon{user_id}.jpg","wb")asf:
                f.write(resp)
returnrealpath(f.name)












