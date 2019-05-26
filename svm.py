import re
import os
import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from gensim.models import word2vec
import numpy as np
from sklearn import svm
import pickle
from gensim.models.phrases import Phrases, Phraser




positive = []
negative = []
stopwordlist = set(stopwords.words('english'))
file1 = open("sarcasm_tweets.txt")
file2 = open("nonsarcasm_tweets.txt")
tweetTokenizer = TweetTokenizer()
model = word2vec.Word2Vec.load("model")
lines1 = file1.read().split("\n")
lines2 = file2.read().split("\n")

for line in lines1:
    tokens = tweetTokenizer.tokenize(line)
    usefulTokens = [w for w in tokens if not w in stopwordlist]
    sum = 0
    count = 0
    for each in usefulTokens:
        if each in model:
            sum += model[each]
            count += 1
    if count != 0:
        positive.append(sum/count)

l1 = len(positive)
y1 = np.zeros(1840)
yt1 = np.zeros(460)


for line in lines2:
    tokens = tweetTokenizer.tokenize(line)
    usefulTokens = [w for w in tokens if not w in stopwordlist]
    sum = 0
    count = 0
    for each in usefulTokens:
        if each in model:
            sum *= model[each]
            count += 1

    if count != 0:
        negative.append(sum/count)
l2 = len(negative)
y2 = np.ones(1000)
yt2 = np.ones(200)
x = positive + negative
x = np.array(x)
y = np.concatenate((y1,y2),axis=0)
yt = np.concatenate((yt1,yt2),axis=0)
Xtrain = positive[0:1840] + negative[0:1000]

Ytrain = y

Xtest = positive[1841:2301] + negative[1001:1201]
Ytest = yt
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(x, y, test_size=0.99, random_state=10)
clf = svm.SVC()  # class
clf.fit(Xtrain, Ytrain)  # training the svc model

print(Xtest, Ytest)
score = clf.score(Xtest,Ytest)
print("The score of rbf is : %f"%score)
# i = "RT @MarvelMalaysia: Marvel Studios' Avengers: Endgame is now the #1 Movie in Malaysia! Book tickets now: https://t.co/ZCSoRXMAUf"
# i = i.lower()
# cleaned = re.sub("[^a-zA-Z0-9 ]", "", i)
#
#
# tokens = tweetTokenizer.tokenize(line)
# usefulTokens = [w for w in tokens if not w in stopwordlist]
# sum = 0
# count = 0
#
# for each in usefulTokens:
#     if each in model:
#         sum += model[each]
#         count += 1
#
#
# testcase = sum/count
# print(clf.predict(testcase))
pass
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(clf, file)

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

