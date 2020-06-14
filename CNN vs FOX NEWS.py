#импортирую библиотеки
from moviepy import *
from moviepy.editor import *
from pygame import *
#склеиваю видео
c11 = VideoFileClip("ZlatanI.mp4")
c11 
c11 = c11.subclip(55,157)
c11 = c11.margin(20)
c12 = c11.fx(vfx.mirror_x)
c13 = c11
c14 = c11.fx(vfx.mirror_x)
Zlatan = clips_array([[c11,c12],[c13,c14]])
Zlatan.resize(width=360)

ZEBEST = ImageClip("TinaT.jpg")
ZEBEST.preview()

Justin = ImageSequenceClip(["BIB1.jpg","BIB2.jpg","BIB3.jpg","BIB4.jpg"], fps=5)
Justin.resize(width=360)

BieberGif = VideoFileClip("BIB5.gif")
# на Windows  нет ImageMagick
#TX = TextClip("THe NEW VIRAL YOUTUBE VIDEO!!!!",fontsize=70,color='black')
#TX = txt_clip.set_pos('center').set_duration(10)
#W=ImageClip("white", fps = 10)
#TXT = CompositeVideoClip([W,TX])
#TXT.resize(width=360)
#TXT2 = TextClip("Give me my Oscar!",fontsize=70,color='white')
#TXT2 = txt_clip.set_pos('center').set_duration(10)

Kim = VideoFileClip("KIM.mp4")
Kim.resize(width=360)
Kim = Kim.fx(vfx.blackwhite)



lapka44 = concatenate_videoclips([Justin, Zlatan, Kim, BieberGif])
# редактирую звуковые дорожки

#Leps1 = AudioFileClip("Luis Fonsi.mp3").subclip(0,122)
#Leps2 = AudioFileClip("RussianPride.mp3").subclip(0,71)
#Leps3 = AudioFileClip("Luis Fonsi.mp3").subclip(0,13)




#рендер (Final Cut Pro)
#Zlatan.preview(fps=25)