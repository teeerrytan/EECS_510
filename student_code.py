import math
import re

class Bayes_Classifier:

    def __init__(self):
        pass


    def train(self, lines):

        self.stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        word_dict_5 = {}
        word_dict_1 = {}
        self.word_dict = {}
        self.count1 = 0;
        self.count5 = 0;
        self.c1 = 0;
        self.c5 = 0;
        for i in lines:

            res = i.split("|")

            sentence = res[2]
            sentence = self.punc(sentence)
            score = res[0]
            words = sentence.split(" ")



            if score == '5':
                self.c5 += 1

                for j in words:

                    j = j.lower()
                    self.count5 += 1
                    self.word_dict[j] = 1
                    if j in word_dict_5:
                        word_dict_5[j] = word_dict_5[j] + 1
                    elif j not in word_dict_5:
                        word_dict_5[j] = 1

            if score == '1':
                self.c1 += 1

                for j in words:
                    self.count1 += 1
                    self.word_dict[j] = 1
                    if j in word_dict_1:
                        word_dict_1[j] = word_dict_1[j] + 1
                    elif j not in word_dict_1:
                        word_dict_1[j] = 1

        self.keys_1 = word_dict_1.keys()
        self.keys_5 = word_dict_5.keys()

        w1= len(self.word_dict)
        w2 = len(word_dict_1)
        w3= len(word_dict_5)
        self.featureset = {}
        for key in self.keys_1:


            p = (word_dict_1[key] + 1) / (len(self.word_dict) + self.count1)
            self.featureset[key, 1] = p

        for key in self.keys_5:
            p = (word_dict_5[key] + 1) / (len(self.word_dict) + self.count5)
            self.featureset[key, 5] = p

        pass







    def classify(self, lines):

        prediction = []
        for i in lines:

            res = i.split("|")
            sentence = res[2]
            sentence = self.punc(sentence)
            words = sentence.split(" ")

            p5 = self.c5 / (self.c1 + self.c5)
            p1 = self.c1 / (self.c1 + self.c5)



            for word in words:

                word = word.lower()
                if word not in self.keys_5:
                    self.featureset[word, 5] = 1 / (len(self.word_dict) + self.count5)
                if word not in self.keys_1:
                    self.featureset[word, 1] = 1 / (len(self.word_dict) + self.count1)

                if self.stop_words.count(word) == 1 or len(word) <= 2:
                    continue
                p5 = p5 + math.log(self.featureset[word, 5])
                p1 = p1 + math.log(self.featureset[word, 1])

            if p5 >= p1:
                prediction.append("5")
            else:
                prediction.append("1")



        return prediction

    def punc(self, line):

        punc = "!#$%&()*+,-./:;<=>?@[\]^_`{'~}"
        punc += '0123456789"'
        for word in punc:
            line = line.replace(word, ' ')

        return line