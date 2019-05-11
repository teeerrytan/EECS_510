
# %%
import tweepy
import json

consumer_key = "g5manQ858eA80IslJJGF0U0yN"
consumer_secret = "2zoPUSZEBJZ8UXKWfmpZdyLQq1DjvTlfvfnx4U7oIuFEN15Gsy"
access_token = "2754165630-Ci9DAlH7JRfF1FhODOn18r2kCZrWIo2oyvCrcMj"
access_token_secret = "efJGuFgpN4p72N1BelR2mZnLswcYB892YZn2cspDSMx2w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# %%
# 接上面的代码(q = 关键字 ,count = 返回的数据量 . 推特一次最多返回100条??)
search_results = api.search(q='avengers', count=100)

# 对对象进行迭代
for tweet in search_results:
    # tweet还是一个对象,推特的相关信息在tweer._json里
    # 这里是检测消息是否含有'text'键,并不是所有TWitter返回的所有对象都是消息(有些可能是用来删除消息或者其他内容的动作--这个没有确认),区别就是消息对象中是否含有'text'键
    if 'text' in tweet._json:
        print(tweet._json['text'])
        # 这里是把内容给打印出来了,如果需要保存到文件需要用json库的dumps函数转换为字符串形式后写入到文件中
        #例如 :output_file.write(json.dumps(tweet._json))
