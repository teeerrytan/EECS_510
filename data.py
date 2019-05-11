import re
import os
import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

file = open('IMDB Dataset.csv')
reader = csv.reader(file)
rows = [row for row in reader]
sentDetector = nltk.data.load('tokenizers/punkt/english.pickle')
stop_words = set(stopwords.words('english'))


positive = []
negative = []

for i in rows:
    if i[1] == 'positive':
        positive.append(i[0])
    if i[1] == 'negative':
        negative.append(i[0])
pass


def convert(s):
    new = ""
    for x in s:
        new += x + " "
    return new


def Cleaner(List):
    newList = []
    cnt = 0
    for i in List:
        #cnt += 1
        # print(cnt)
        # sentences = sentDetector.tokenize(i.get_text())

        # for s in sentences:
        i = i.lower()
        cleaned = re.sub("[^a-zA-Z ]", "", i).split()
        filtered_cleaned = [
            word for word in cleaned if not word in stop_words]
        str = convert(filtered_cleaned)
        newList.append(str)

    return newList


cleanedpositive = Cleaner(positive)
cleanednegative = Cleaner(negative)
pass


fileObject = open('filteredpositive.txt', 'w')
for i in cleanedpositive:
    fileObject.write(i)
    fileObject.write('\n')
fileObject.close()

fileObject = open('filterednegative.txt', 'w')
for i in cleanednegative:
    fileObject.write(i)
    fileObject.write('\n')
fileObject.close()
