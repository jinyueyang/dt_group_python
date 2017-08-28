# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Fri Jul 14 17:43:28 2017

@author: yangjinyue
"""

import itchat

itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])

print("male friends: %.2f%%" % (float(male)/total*100) + "\n" +
"female friends: %.2f%%" % (float(female)/total*100) + "\n" +
"unknown friends: %.2f%%" % (float(other)/total*100))


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
    
Nickname = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')

from pandas import DataFrame
data = {'Nickname': Nickname, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('friends_data.csv', index=True, encoding='utf_8_sig')

import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("",signature)
    siglist.append(signature)
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text,cut_all=True)
word_space_split = "".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

coloring = np.array(Image.open("liukanshan.png"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring, max_font_size=60, random_state=42, scale=2).generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func = image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()