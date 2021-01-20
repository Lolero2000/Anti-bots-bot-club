import tweepy

if __name__ == '__main__':
    
    with open('keys.txt') as f:
        creds = [line.rstrip() for line in f]
    API_key = creds[0]
    API_secret_key = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    
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
