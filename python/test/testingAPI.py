# API KEY = b659JiTJbR2zG0zh0oOv06Mhu
# API SECRET KEY = A97rWT7WkGu9bGZJkO0T28E5XJOYs1R36Yzr4nJVNCDihwUi7G
# BEARER TOKEN = AAAAAAAAAAAAAAAAAAAAANHTLwEAAAAA%2FxQsn%2BCfGYV8Ld1Dyx2UXiaZ6NI%3DOBdx42UBDU9ThF6CPfUY701ojlgFPX4ZnOIwVEhPVV321nGIuZ
# ACCESS TOKEN = 721099414-bqBLJ2TDXvKN61Ct5nwLeAqkEe9zIaU1ueLbr6u1 
# ACCESS TOKEN SECRET = Qfh78eUs6XrxwKROxxnqOsNrfiJhU55HB3PGXYLIC8b29

import tweepy

if __name__ == '__main__':   
    API_key = "b659JiTJbR2zG0zh0oOv06Mhu"
    API_secret_key = "A97rWT7WkGu9bGZJkO0T28E5XJOYs1R36Yzr4nJVNCDihwUi7G"
    access_token = "721099414-i0lDyCg4rUWcOKrPkJGLiH513yDMCjkWVa02ehFh"
    access_token_secret = "6ZDhWZBhO6VXbXqBVB5sIBPAZevke0wgU5tEANFjWa8m9"
    
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        
    print('____________________________________________________________________________\n')
    # Get the User object for twitter...
    user = api.get_user('koxelman')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)
    
    print('_____________________________________________________________________________\n')
#    api.update_status('Intentando automatizar el tedioso proceso de bloquear anarco capitalistas a mano.')
    
    users = api.search_users('\xf0\x9f\x90\x8d')
    for user in users:
        usr_id = user.id
        print(user.screen_name)
        api.create_block(usr_id)
