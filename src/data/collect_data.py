from src.model import preprocess_data
from src.load import target
from src.transform import clean

import tweepy
import pandas as pd

# Twitter API credentials
API_KEY = '1bPHuRZXUn3rvbFxaw4vSQzIK'
API_SECRET = 'upG6xCuZWQoA9f9W2qs4J8D2Ukkp4rQbuqlPpyFvRemnIIp4ta'
ACCESS_TOKEN = '1802394139520049152-q1lmErle6fepX4ZjhYi65o5QPvZA1J'
ACCESS_TOKEN_SECRET = 'CiHWMjNQGbZ3GEZv2MrGcKI7pGtW90OVSkzhw4DIihh73'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAAGpvgEAAAAAMAcjH1llJkZtta8bIC0busgcNU8%3D8aMw4P6ej94lVgO02h0bhhCf5XEJgo8ZugC8RA9CisT97iziCQ'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
print("Inside twitter to get data")
# Fetch tweets based on a keyword

tweets = tweepy.Cursor(api.search_tweets, q= 'hashtag', lang="en").items(5)
tweet_data = [[tweet.created_at, tweet.text, tweet.user.screen_name] for tweet in tweets]
df = pd.DataFrame(tweet_data, columns=['Timestamp', 'Text', 'Username'])
print("Inside fetch twitts -" + df.info)

def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    tweet_data = [[tweet.created_at, tweet.text, tweet.user.screen_name] for tweet in tweets]
    df = pd.DataFrame(tweet_data, columns=['Timestamp', 'Text', 'Username'])
    print("Inside fetch twitts -"+df.info)
    return df

# Example: Fetch tweets related to "AI"
tweets_df = fetch_tweets("AI", count=100)
print(tweets_df.head())