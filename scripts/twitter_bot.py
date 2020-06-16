import tweepy
import sys
import os

# Authentication credentials - dev.twitter.com
cfg = {
    'consumer_key': 'quI4EXqGt0qvBAuDl4q0ripBm',
    'consumer_secret': 'krTlB3yad0h43cLd4NoRAoNkFV7zmiim6TKCgp8DNElMUNSuKy',
    'access_token': '419716095-fxSL9wPlcwcsHij2z1FG4j3bml9b9vlNSobbJACY',
    'access_token_secret': 'fOfl8gbBKF8MmSFLumHXDHMmRWQ3pLDkfnRkTMHgWRM6e'
}
CONSUMER_KEY = "quI4EXqGt0qvBAuDl4q0ripBm"


def get_api_handler(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    
    api = tweepy.API(auth)
    user = api.get_user('twitter')
    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)
    
def main():
    api = get_api_handler(cfg)
    tweet = 'Hello, world from Tweepy!'
    api.update_status(tweet)


if __name__ == "__main__":
    main()
