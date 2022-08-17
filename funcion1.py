import json

file = open('tweets.json')
data = json.load(file)


for i in data:
    print(i)


def most_ret(datas):
    return top_tweet

def most_user(datas):
    return top_user

def most_day(datas):
    return top_day

def most_hashtag(datas):
    return top_hashtag

if __name__ == "__main__":
    most_ret(data["content"])
    most_user(data["user"])
    most_day(data["date"])
    most_hashtag(data["content"])    