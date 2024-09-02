import re

# Function to clean tweet text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove special characters
    text = text.strip().lower()  # Convert to lowercase and strip whitespace
    return text

# Apply cleaning function to tweet text
tweets_df['Cleaned_Text'] = tweets_df['Text'].apply(clean_text)
print(tweets_df[['Text', 'Cleaned_Text']].head())
