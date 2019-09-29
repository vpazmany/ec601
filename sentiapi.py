from google.cloud import language_v1
from google.cloud.language_v1 import enums
import json
import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = "TvR4oQdoeWdXTHBw4cHLay6J0"
consumer_secret = "O7We3kEc9Krn3y2gRlnwkWjdA2l6lnyYhlf6c0DRIk1rIxS6MW"
access_key = "1171884339677683712-7DUmCemSPyvDUWXcdA8rt3uIznUfDS"
access_secret = "NSYM3WTlaNrFvsl24T42IuYBEbli9g7BNz8PtSppt034a"


def sample_analyze_sentiment(text_content_list):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    count_latte=0
    avg_sum_latte=0

    count_cap=0
    avg_sum_cap=0

    count_coldbrew=0
    avg_sum_coldbrew=0

    count_psl=0
    avg_sum_psl=0

    count_frappe=0
    avg_sum_frappe=0

    avg_latte=0
    avg_cap=0
    avg_frappe=0
    avg_psl=0
    avg_coldbrew=0

    for g in range(0,len(text_content_list)):
        text_content=text_content_list[g]
        client = language_v1.LanguageServiceClient()

        # text_content = 'I am so happy and joyful.'

        # Available types: PLAIN_TEXT, HTML
        type_ = enums.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type": type_, "language": language}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = enums.EncodingType.UTF8

        response = client.analyze_sentiment(document, encoding_type=encoding_type)
        # Get overall sentiment of the input document
        print(u"Document sentiment score: {}".format(response.document_sentiment.score))
        print(
            u"Document sentiment magnitude: {}".format(
                response.document_sentiment.magnitude
            )
        )
        # Get sentiment for all sentences in the document
        for sentence in response.sentences:

            print(u"Sentence text: {}".format(sentence.text.content))
            print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
            print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
            if 'latte' in sentence.text.content.lower():
                count_latte+=1
                avg_sum_latte= sentence.sentiment.magnitude
                avg_sum_latte+=avg_sum_latte/count_latte
            if 'cappucino' in sentence.text.content.lower():
                count_cap+=1
                avg_sum_cap+= sentence.sentiment.magnitude
                avg_cap= avg_sum_cap/count_cap
            if 'frappe' in sentence.text.content.lower():
                count_frappe+=1
                avg_sum_frappe+= sentence.sentiment.magnitude
                avg_frappe= avg_sum_frappe/count_frappe
            if 'cold brew' in sentence.text.content.lower():
                count_coldbrew+=1
                avg_sum_coldbrew+= sentence.sentiment.magnitude
                avg_coldbrew= avg_sum_coldbrew/count_coldbrew
            if 'pumpkin' in sentence.text.content.lower():
                count_psl+=1
                avg_sum_psl+= sentence.sentiment.magnitude
                avg_psl= avg_sum_psl/count_psl




        print('Latte Magnitude:',avg_latte,count_latte)
        print('Cappucino Magnitude:',avg_cap,count_cap)
        print('Frappe Magnitude:',avg_frappe,count_frappe)
        print('Pumpkin Magnitude:',avg_psl, count_psl)
        print('Coldbrew Magnitude:',avg_coldbrew, count_coldbrew)
        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(u"Language of the text: {}".format(response.language))
#!/usr/bin/env python
# encoding: utf-8
#Author - Michael Brunsman
#Credit to - Prateek Mehta

def get_all_hashtag_tweets(hashtag_input):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #make initial request for most recent tweets (200 is the maximum allowed count)
    count = 200

    hashtag_text = []

    hashtag = api.search(q=hashtag_input, lang="en", geocode = "42.3505,71.1054,5mi", count=count, tweet_mode='extended')

    for tweet in hashtag:
        hashtag_text.append({
            'text': tweet.full_text
            })
        with open('hashtag_'+ hashtag_input + '.json', 'w+') as f:
            json.dump(hashtag_text,f)

    print("Done")


def get_all_tweets_new(screen_name):

    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    count = 200

    new_tweets = api.user_timeline(screen_name = screen_name,count=count, tweet_mode='extended')

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    tweet_text = []
    hashtag_text = []
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

    #Send just the text of the tweets to json file
    for tweet in alltweets:
      tweet_text.append({
        'text': tweet.full_text
        })
      #with open('tweet_' + screen_name + '.json', 'w+') as f:
      with open('tweet'+'.json', 'w+') as f:
        json.dump(tweet_text,f)

    print("Done")

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

    get_all_tweets_new("@Starbucks")
    get_all_tweets_new("@DunkinDonuts")
    get_all_tweets_new("@AllegroCoffee")
    get_all_tweets_new("@pavementcoffee")
    get_all_tweets_new("@limeredteahouse")
    get_all_tweets_new("@CaffeNero_US")
    get_all_tweets_new("@bluestatecoffee")

    get_all_hashtag_tweets("#PSL")
    get_all_hashtag_tweets("#Frappuccino")
    get_all_hashtag_tweets('#PumpkinSpice')
    get_all_hashtag_tweets('#Latte')
    get_all_hashtag_tweets('#Cappuccino')
    get_all_hashtag_tweets('#ColdBrew')
    get_all_hashtag_tweets('#Americano')
    get_all_hashtag_tweets('#Frappe')
    get_all_hashtag_tweets('#Espresso')
    get_all_hashtag_tweets('#Peppermint')
    get_all_hashtag_tweets('#Dunkin')
    get_all_hashtag_tweets('#Starbucks')
    get_all_hashtag_tweets('#AllegroCoffee')
    get_all_hashtag_tweets('#pavementcoffee')
    get_all_hashtag_tweets('#limeredteahouse')
    get_all_hashtag_tweets('#CaffeNero')
    get_all_hashtag_tweets('#bluestatecoffee')

    json_fname='tweet.json'#'test_coffee.json'
    json_keyword='text'
    example_text=[]
    with open(json_fname,'r') as f:
      data = json.load(f)
      for x in data:
          example_text += [x[json_keyword]]
    sample_analyze_sentiment(example_text)
      #print(x['text'])
#print(data[json_keyword])
#example_text = data[json_keyword]#"it's pumpkin spice szn!!!!! Love pumpkin spice coffee!!!"
