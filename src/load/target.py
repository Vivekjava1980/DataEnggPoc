from sqlalchemy import create_engine

# Create a database connection (using SQLite for POC)
engine = create_engine('sqlite:///tweets.db', echo=True)

# Load data into the database
tweets_df.to_sql('tweets', con=engine, if_exists='replace', index=False)

print("Data loaded into the database successfully.")
