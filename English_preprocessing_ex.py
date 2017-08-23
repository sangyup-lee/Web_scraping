# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:30:59 2017

@author: Sang
"""

import time
import nltk
import pickle
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'): # 형용사
        return 'a'
    elif treebank_tag.startswith('V'): # 동사
        return 'v'
    elif treebank_tag.startswith('N'): # 명사
        return 'n'
    elif treebank_tag.startswith('RB'): # 부사
        return 'r'
    else:
        return 'n'

article_dict = pickle.load(open('En_text.p', 'rb')) 
# 같은 folder에서 En_text.p 파일도 다운로드 받아야 합니다. 해당 파일은 하나의 영문기사를 
# dictionary 형태로 저장해 놓은 것입니다. 

title = article_dict[1]['title'] # 기사의 제목을 가져옵니다.
content = article_dict[1]['content'] # 기사 내용을 가지고 옵니다.

#-------------------------------------
# Text preprocessing
#-------------------------------------

# 1. 불필요한 symbols과 marks 제거하기
# 다른 문자나 기호도 추가로 제거할 수 있습니다. 
filtered_content = content.replace('!', '').replace(',','').replace('.','').replace('“','').replace('”','').replace('\n','')
filtered_content = filtered_content.replace('The New York Times', '')

# 2. Case conversion; 대문자를 소문자로 바꾸기
filtered_content = filtered_content.lower()

#------------------------------------
# Word tokenization

word_tokens = nltk.word_tokenize(filtered_content)
#-------------------------------------

#------------------------------------------------
# POS tagging
tokens_pos = nltk.pos_tag(word_tokens)

#-----------------------------------------
# Lemmatization

wlem = nltk.WordNetLemmatizer()
lemmatized_tokens = []
for word, pos in tokens_pos:
    #print(word, pos)
    WN_pos = get_wordnet_pos(pos)  #wordnet pos tag로 변환을 해줘야 합니다.
    new_word = wlem.lemmatize(word, WN_pos)
    #print('lemma: ', new_word)
    lemmatized_tokens.append((new_word,pos))

#print(lemmatized_tokens)
#------------------------------------------------
#------------------------------------------------
# 명사 단어만 추출하기
NN_words = []
for word, pos in lemmatized_tokens:
    if pos.find('NN') >= 0:
        NN_words.append(word)
#------------------------------------------------
#print(NN_words)


#------------------------------------------------
# Stopwords removal

stopwords_list = stopwords.words('english')
#print('stopwords: ', stopwords_list)
unique_NN_words = set(NN_words)
final_NN_words = NN_words

print(final_NN_words)
for word in unique_NN_words:
    if word in stopwords_list:
        while word in final_NN_words: final_NN_words.remove(word)
            

#------------------------------------------------
# 불용어 사전 직접 만들기
customized_stopwords = ['be', 'today', 'yesterday', "it’s", "don’t"] # 직접 만든 불용어 사전
unique_NN_words1 = set(final_NN_words)
for word in unique_NN_words1:
    if word in customized_stopwords:
        while word in final_NN_words: final_NN_words.remove(word)
#------------------------------------------------
print(final_NN_words)

#------------------------------------------------
# 단어 빈도 파악하기
c = Counter(final_NN_words)
print(c)
print(c.most_common(20))

#-------------------------------------------------
# Word cloud 만들기

cloud_text = ''
for word in final_NN_words:
    cloud_text = cloud_text +' '+ word

wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(cloud_text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
