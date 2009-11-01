from django.conf import settings
from django.core.cache import cache
import datetime, twitter

def latest_tweet(request):
    tweets = cache.get('tweets')

    if tweets:
        return dict(tweets=tweets)
        
    tweets = []
    
    for tweet in twitter.Api().GetUserTimeline("zainy"):
        if not tweet.in_reply_to_screen_name:
            tweets.append(tweet)
            if len(tweets) >= 3: break
    
    cache.set('tweets', tweets, 120)

    return dict(tweets=tweets)