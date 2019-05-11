import re
import os
import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

file = open('IMDB Dataset.csv')
reader = csv.reader(file)
rows = [row for row in reader]
sentDetector = nltk.data.load('tokenizers/punkt/english.pickle')

positive = []
negative = []

for i in rows:
    if i[1] == 'positive':
        positive.append(i[0])
    if i[1] == 'negative':
        negative.append(i[0])
pass

def Cleaner(List):
    newList = []
    cnt = 0
    for i in List:
        #cnt += 1
        #print(cnt)
        # sentences = sentDetector.tokenize(i.get_text())

        # for s in sentences:
        i = i.lower()
        cleaned = re.sub("[^a-zA-Z0-9 ]", "", i)
        newList.append(cleaned)

    return newList

cleanedpositive = Cleaner(positive)
cleanednegative = Cleaner(negative)
pass


fileObject = open('cleanedpositive.txt', 'w')
for i in cleanedpositive:
	fileObject.write(i)
	fileObject.write('\n')
fileObject.close()

fileObject = open('cleanednegative.txt', 'w')
for i in cleanednegative:
	fileObject.write(i)
	fileObject.write('\n')
fileObject.close()
