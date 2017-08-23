# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer # frequency based DTM
from sklearn.feature_extraction.text import TfidfVectorizer # tf-idf based DTM


def display_features(features, feature_names):
    df = pd.DataFrame(data=features, columns=feature_names)
    print(df)

def bow_extractor(corpus, ngram_range=(1,1)):  # ngram_range=(1,1)) -> unigram
    # returns a frequency based DTM
    vectorizer = CountVectorizer(min_df=1, ngram_range=ngram_range) # if df < 1, then ignore those terms
    features = vectorizer.fit_transform(corpus) # transform texts to a frequency matrix
    return vectorizer, features  

def tfidf_extractor(corpus, ngram_range=(1,1)):
    # returns a tf-idf based DTM
    vectorizer = TfidfVectorizer(min_df=1, 
                                 norm='l2',
                                 smooth_idf=True,
                                 use_idf=True,
                                 ngram_range=ngram_range)
    features = vectorizer.fit_transform(corpus)
    return vectorizer, features

# the corpos is composed of 4 documents
CORPUS = [
'the sky is blue',
'sky is blue and sky is beautiful',
'the beautiful sky is so blue',
'i love blue cheese'
]

new_doc = ['loving this blue sky today']

# Freqeucny 기반의 DTM 생성하기
bow_vectorizer, bow_features = bow_extractor(CORPUS)
# You should remember what type of input data is provided
# CORPUS: a list of sentences

print(bow_features) # this prints out the words used in each document.

features = bow_features.todense() # dense matrix로 변환
feature_names = bow_vectorizer.get_feature_names() # 단어의 이름을 추출
display_features(features, feature_names) # DTM 형태로 출력


# about the new doc
# To represent the new document using the training set (i.e., CORPUS)

new_doc_features = bow_vectorizer.transform(new_doc)
new_doc_features = new_doc_features.todense() # returns 2D array
feature_names = bow_vectorizer.get_feature_names()
display_features(new_doc_features, feature_names)


# TF-IDF 기반의 DTM 생성하기
tfidf_vectorizer, tdidf_features = tfidf_extractor(CORPUS)
feature_names = tfidf_vectorizer.get_feature_names()
display_features(np.round(tdidf_features.todense(), 2), feature_names)
test_tfidf_features = tfidf_vectorizer.transform(new_doc)