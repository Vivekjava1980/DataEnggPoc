import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

tweets = scraper.get_tweets('imVkohli',mode='user',number=10)
#print(tweets)

# Fetch tweets based on a keyword

def fetch_tweets():
    final_tweets = []
    for tweet in tweets['tweets']:
     tweet_data = [tweet['text'],tweet['date'],tweet['stats']['comments']]
    final_tweets.append(tweet_data)
    print("final twiits"+str(final_tweets))
    df = pd.DataFrame(final_tweets, columns=['Comments', 'Text', 'Username'])
    print("Inside fetch twitts -")
    return df

# Example: Fetch tweets related to "AI"
tweets_df = fetch_tweets()
print(tweets_df.head())