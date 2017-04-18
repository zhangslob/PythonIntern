# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import codecs

# 第一次运行程序时将分好的词存入文件
text = ''
with open('word.txt') as fin:#根据情况可加入encoding='utf-8'
    for line in fin.readlines():
         line = line.strip('\n')
         text += '/'.join(jieba.cut(line))
         text += ' '
fout = open('text.txt','wb')#以二进制写模式写入
pickle.dump(text,fout)
fout.close()

# 直接从文件读取数据
fr = open('text.txt','rb')
text = pickle.load(fr)

backgroud_Image = plt.imread('girl.jpg') #需要自己准备一张图片
wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片
                max_words = 2000,            # 设置最大现实的字数
                stopwords = STOPWORDS,        # 设置停用词
                font_path = 'MSYH.TTF',# 设置字体格式，如不设置显示不了中文
                max_font_size = 3000,            # 设置字体最大值
                random_state = 50,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
wc.generate(text)
image_colors = ImageColorGenerator(backgroud_Image)
#wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
