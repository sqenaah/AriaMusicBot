utf-8utf-8























importos
importaiohttp
importaiofiles
importtraceback
frompathlibimportPath
fromPILimportImage,ImageDraw,ImageFilter,ImageFont,ImageEnhance
fromyoutubesearchpython.__future__importVideosSearch

CACHE_DIR=Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

CANVAS_W,CANVAS_H=1320,760
BG_BLUR=16
BG_BRIGHTNESS=1

LIME_BORDER=(158,255,49,255)
RING_COLOR=(98,193,169,255)
TEXT_WHITE=(245,245,245,255)
TEXT_SOFT=(230,230,230,255)
TEXT_SHADOW=(0,0,0,140)


FONT_REGULAR_PATH="ShrutiMusic/assets/font2.ttf"
FONT_BOLD_PATH="ShrutiMusic/assets/font3.ttf"


FONT_REGULAR=ImageFont.truetype(FONT_REGULAR_PATH,30)
FONT_BOLD=ImageFont.truetype(FONT_BOLD_PATH,30)


defchange_image_size(max_w,max_h,image):
    ratio=min(max_w/image.size[0],max_h/image.size[1])
returnimage.resize((int(image.size[0]*ratio),int(image.size[1]*ratio)),Image.LANCZOS)


defwrap_two_lines(draw,text,font,max_width):
    words=text.split()
line1,line2="",""
forwinwords:
        test=(line1+" "+w).strip()
ifdraw.textlength(test,font=font)<=max_width:
            line1=test
else:
            break
remaining=text[len(line1):].strip()
ifremaining:
        forwinremaining.split():
            test=(line2+" "+w).strip()
ifdraw.textlength(test,font=font)<=max_width:
                line2=test
else:
                break
return(line1+("\n"+line2ifline2else"")).strip()


deffit_title_two_lines(draw,text,max_width,font_path,start_size=58,min_size=30):
    size=start_size
whilesize>=min_size:
        try:
            f=ImageFont.truetype(font_path,size)
except:
            size-=1
continue
wrapped=wrap_two_lines(draw,text,f,max_width)
lines=wrapped.split("\n")
iflen(lines)<=2andall(draw.textlength(l,font=f)<=max_widthforlinlines):
            returnf,wrapped
size-=1
f=ImageFont.truetype(font_path,min_size)
returnf,wrap_two_lines(draw,text,f,max_width)


asyncdefgen_thumb(videoid:str):
    url=f"https://www.youtube.com/watch?v={videoid}"
try:
        results=VideosSearch(url,limit=1)
result=(awaitresults.next())["result"][0]

title=result.get("title","Unknown Title")
duration=result.get("duration","Unknown")
thumburl=result["thumbnails"][0]["url"].split("?")[0]
views=result.get("viewCount",{}).get("short","Unknown Views")
channel=result.get("channel",{}).get("name","Unknown Channel")

asyncwithaiohttp.ClientSession()assession:
            asyncwithsession.get(thumburl)asresp:
                ifresp.status==200:
                    thumb_path=CACHE_DIR/f"thumb{videoid}.png"
asyncwithaiofiles.open(thumb_path,"wb")asf:
                        awaitf.write(awaitresp.read())

base_img=Image.open(thumb_path).convert("RGBA")


bg=change_image_size(CANVAS_W,CANVAS_H,base_img).convert("RGBA")
bg=bg.filter(ImageFilter.GaussianBlur(BG_BLUR))
bg=ImageEnhance.Brightness(bg).enhance(BG_BRIGHTNESS)

canvas=Image.new("RGBA",(CANVAS_W,CANVAS_H),(0,0,0,255))
canvas.paste(bg,(0,0))
draw=ImageDraw.Draw(canvas)


frame_inset=12
draw.rectangle(
[frame_inset//2,frame_inset//2,CANVAS_W-frame_inset//2,CANVAS_H-frame_inset//2],
outline=LIME_BORDER,width=frame_inset
)


thumb_size=470
ring_width=20
circle_x=92
circle_y=(CANVAS_H-thumb_size)//2

circular_mask=Image.new("L",(thumb_size,thumb_size),0)
mdraw=ImageDraw.Draw(circular_mask)
mdraw.ellipse((0,0,thumb_size,thumb_size),fill=255)

art=base_img.resize((thumb_size,thumb_size))
art.putalpha(circular_mask)

ring_size=thumb_size+ring_width*2
ring_img=Image.new("RGBA",(ring_size,ring_size),(0,0,0,0))
rdraw=ImageDraw.Draw(ring_img)
ring_bbox=(ring_width//2,ring_width//2,ring_size-ring_width//2,ring_size-ring_width//2)
rdraw.ellipse(ring_bbox,outline=RING_COLOR,width=ring_width)

canvas.paste(ring_img,(circle_x-ring_width,circle_y-ring_width),ring_img)
canvas.paste(art,(circle_x,circle_y),art)


tl_font=ImageFont.truetype(FONT_BOLD_PATH,34)
draw.text((28+1,18+1),"ShrutiMusic",fill=TEXT_SHADOW,font=tl_font)
draw.text((28,18),"ShrutiMusic",fill=TEXT_WHITE,font=tl_font)


info_x=circle_x+thumb_size+60
max_text_w=CANVAS_W-info_x-48


np_font=ImageFont.truetype(FONT_BOLD_PATH,60)
np_text="NOW PLAYING"
np_w=draw.textlength(np_text,font=np_font)
np_x=info_x+(max_text_w-np_w)//2-95
np_y=circle_y+30
draw.text((np_x+2,np_y+2),np_text,fill=TEXT_SHADOW,font=np_font)
draw.text((np_x,np_y),np_text,fill=TEXT_WHITE,font=np_font)


title_font,title_wrapped=fit_title_two_lines(draw,title,max_text_w,FONT_BOLD_PATH,start_size=30,min_size=30)
title_y=np_y+110
draw.multiline_text((info_x+2,title_y+2),title_wrapped,fill=TEXT_SHADOW,font=title_font,spacing=8)
draw.multiline_text((info_x,title_y),title_wrapped,fill=TEXT_WHITE,font=title_font,spacing=8)


meta_font=ImageFont.truetype(FONT_REGULAR_PATH,30)
line_gap=46
meta_start_y=title_y+130
duration_label=duration
ifdurationand":"indurationand"Min"notindurationand"min"notinduration:
            duration_label=f"{duration} Mins"

defdraw_meta(y,text):
            draw.text((info_x+1,y+1),text,fill=TEXT_SHADOW,font=meta_font)
draw.text((info_x,y),text,fill=TEXT_SOFT,font=meta_font)

draw_meta(meta_start_y+0*line_gap,f"Views : {views}")
draw_meta(meta_start_y+1*line_gap,f"Duration : {duration_label}")
draw_meta(meta_start_y+2*line_gap,f"Channel : {channel}")

out=CACHE_DIR/f"{videoid}_styled.png"
canvas.save(out)

try:
            os.remove(thumb_path)
except:
            pass

returnstr(out)

exceptExceptionase:
        print(f"[gen_thumb Error] {e}")
traceback.print_exc()
returnNone








