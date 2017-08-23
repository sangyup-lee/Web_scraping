    # -*- coding: utf-8 -*-
"""
@author: Sang
"""


import konlpy.tag
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import pickle

FONT_PATH = 'C:/Windows/Fonts/malgun.ttf'

# 1) 텍스트 데이터 가져 오기
article_dict = pickle.load(open('Kr_text.p', 'rb'))

content = article_dict[1]['content']


# 2) Text cleaning
filtered_content = content.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','')

# 3) 형태소 분석 = 형태소 단위로 tokenization + 형태소의 품사 tagging
twitter = konlpy.tag.Twitter()
twitter_morphs = twitter.pos(filtered_content)


"""
# 코모란을 사용하는 경우
komoran = konlpy.tag.Komoran()
komoran_morphs = komoran.pos(filtered_content)
print(komoran_morphs)
"""

# 4) 특정 품사 선택 -- 예) 명사
Noun_words = []
for word, pos in twitter_morphs:
    if pos == 'Noun':
        Noun_words.append(word)

# 5) 불용어 제거
stopwords = ['연합뉴스', '서울', '기자']        
unique_Noun_words = set(Noun_words)
for word in unique_Noun_words:
    if word in stopwords:
        while word in Noun_words: Noun_words.remove(word)

# 가장 많이 사용된 명사단어 20개 출력하기
print(Noun_words)    
c = Counter(Noun_words)
print(c.most_common(20))


# word cloud 만들기
new_text = ''
for word in Noun_words:
    new_text = new_text +' '+ word

wordcloud = WordCloud(max_font_size=40, relative_scaling=.5, font_path=FONT_PATH).generate(new_text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
