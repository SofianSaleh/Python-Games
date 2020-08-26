import tweepy
import time
import os
# print(os.environ.get('consumer_key'))


auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "Python"
nrTweets = 100

for tweet in tweepy.cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopAsyncIteration:
        break
