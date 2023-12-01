import jieba
import wordcloud
import numpy as np
from PIL import Image
 
heart_mask = np.array(Image.open("heart.png"))
w = wordcloud.WordCloud(
    width=100,
    height=100,
    mask=heart_mask,
    background_color='white',
    font_path='msyh.ttc'
)
text ='每天进步一点点，做最好的自己；每天偷懒一点点，差之千里。'\
 '每天努力多一点和每天偷懒一点点经过一年的差距是巨大的。'\
 '每天多努力一点，积累下来就是巨大的财富。合抱之木，生于毫末；九层之台，起于累土；千里之行，始于足下。'\
 '积少成多，水滴石穿，每天都要进步，哪怕一点点。不积小流无以成江海，成功需要每天的积累和努力。'\
 '滴水穿石，量变可以变成质变。千里之行始于足下,不积跬步无以至千里。'\
 '每天进步一点点，日积月累，将会量变引起质变。每天退步一点点，经年累月，将会追悔莫及无法追赶。'\
 '勤学如春起之苗，不见其增，日有所长；辍学如磨刀之石，不见其损，日有所亏。'\
 '我们不能小看微小的积累与进步，这些终将让我们发生质变;也不能有任何懈怠与侥幸，这会让我们与优秀产生巨大差距。'
new_str = ' '.join(jieba.lcut(text))
w.generate(new_str)
w.to_file('x.png')