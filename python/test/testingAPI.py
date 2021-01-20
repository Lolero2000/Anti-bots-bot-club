# API KEY = b659JiTJbR2zG0zh0oOv06Mhu
# API SECRET KEY = A97rWT7WkGu9bGZJkO0T28E5XJOYs1R36Yzr4nJVNCDihwUi7G
# BEARER TOKEN = AAAAAAAAAAAAAAAAAAAAANHTLwEAAAAA%2FxQsn%2BCfGYV8Ld1Dyx2UXiaZ6NI%3DOBdx42UBDU9ThF6CPfUY701ojlgFPX4ZnOIwVEhPVV321nGIuZ
# ACCESS TOKEN = 721099414-bqBLJ2TDXvKN61Ct5nwLeAqkEe9zIaU1ueLbr6u1 
# ACCESS TOKEN SECRET = Qfh78eUs6XrxwKROxxnqOsNrfiJhU55HB3PGXYLIC8b29

import tweepy

API_key = "b659JiTJbR2zG0zh0oOv06Mhu"
API_secret_key = "A97rWT7WkGu9bGZJkO0T28E5XJOYs1R36Yzr4nJVNCDihwUi7G"
access_token = "721099414-bqBLJ2TDXvKN61Ct5nwLeAqkEe9zIaU1ueLbr6u1"
access_token_secret = "Qfh78eUs6XrxwKROxxnqOsNrfiJhU55HB3PGXYLIC8b29"

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))