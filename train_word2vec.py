import re
import os
import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from gensim.models import word2vec
from gensim.models.phrases import Phrases, Phraser

file1 = open("sarcasm_tweets.txt")
file2 = open("nonsarcasm_tweets.txt")
def build_phrases(sentences):
    phrases = Phrases(sentences,
                      min_count=2,
                      threshold=10,
                      )
    return Phraser(phrases)

Tokenizer = TweetTokenizer()
wordtovec = []
stopwordlist = set(stopwords.words('english'))
processed = []

lines = file1.read().split("\n")


for line in lines[0:1840]:


    line = line.lower()
    processed.append(line)

lines = file2.read().split("\n")


for line in lines[0:1000]:


    line = line.lower()
    processed.append(line)





phrases = build_phrases(processed)


sentence_stream = [li.split(" ") for li in processed]
bigram = Phrases(sentence_stream, min_count=2, threshold=5)
for lin in processed:
    w = Tokenizer.tokenize(lin)
    wordtovec.append(bigram[w])

model = word2vec.Word2Vec(wordtovec, workers = 2, size = 20, min_count = 2, window = 5, sample = 0.001)
model.save("model")

model = word2vec.Word2Vec.load("model")
y1 = model.most_similar("good", topn=30)
y2 = model.most_similar("movie", topn=30)
y3 = model.most_similar("awesome", topn=30)

print(y1)
print(y2)
print(y3)

