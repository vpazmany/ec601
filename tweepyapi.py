#!/usr/bin/env python
# encoding: utf-8
#Author - Michael Brunsman
#Credit to - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = "TvR4oQdoeWdXTHBw4cHLay6J0"
consumer_secret = "O7We3kEc9Krn3y2gRlnwkWjdA2l6lnyYhlf6c0DRIk1rIxS6MW"
access_key = "1171884339677683712-7DUmCemSPyvDUWXcdA8rt3uIznUfDS"
access_secret = "NSYM3WTlaNrFvsl24T42IuYBEbli9g7BNz8PtSppt034a"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    count = 5

    new_tweets = api.user_timeline(screen_name = screen_name,count=count, tweet_mode='extended')

    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    tweet_text = []
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=count,max_id=oldest, tweet_mode='extended')
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 2):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    #Send just the text of the tweets to json file
    for tweet in alltweets:
      tweet_text.append({
        'text': tweet.full_text
        })
      with open('tweet.json', 'w+') as f:
        json.dump(tweet_text,f)

    print("Done")
    print(len(alltweets))
    print(len(new_tweets))



if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@Starbucks")
    get_all_tweets("@DunkinDonuts")

