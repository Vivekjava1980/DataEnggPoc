from textblob import TextBlob

from src.data.collect_data import tweets_df


# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'

# Apply sentiment analysis to the tweets
tweets_df['Sentiment'] = tweets_df['Text'].apply(analyze_sentiment)
print(tweets_df.head())
