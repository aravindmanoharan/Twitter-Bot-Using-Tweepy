#!/usr/bin/env python3

# Import all required packages.

from tweepy import OAuthHandler, API, Cursor
from datetime import datetime, timedelta

# Storing the credentials within these variables.

CONSUMER_KEY = "noegBXSsiZjXLUz7uFMhlAbmY"
CONSUMER_KEY_SECRET = "WyDNH0v1tssNyPaRdUpG95cVbVHEG5EPbJkttrqqOUorSCpcWz"
ACCESS_TOKEN = "992890811141443585-eg3hHMyezFm2WJzxTj5e6tZF1JtNzGC"
ACCESS_TOKEN_SECRET = "nOOu24DmL2dMX1ypEINCcV1JwU18kXHhEhbE7xztT5ciN"

# The screen name of the account whose tweets we are intended to scrap.

userName = '@BarackObama'
hashtags = []
mentions = []
hashtagsRT = []
mentionsRT = []
allTweets = []
tweetCount = 0

# Here 1000 is assigned to days so that our endDate will be 1000 days back. This is a parameter which can be tuned.

endDate = datetime.utcnow() - timedelta(days = 1000) 

# Authenticate your twitter account with tweepy using the above credentials.

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
authAPI = API(auth)
user = authAPI.get_user(userName)

# We create a loop continously to scrap data as much as we need i.e., here we are scraping till the endDate.

for status in Cursor(authAPI.user_timeline, id = userName, tweet_mode = 'extended').items():
    # Here status is a form of dictionary which has several parameters for each tweets.
    # Storing the tweets in a list called allTweets

    if "retweeted_status" in dir(status):
        allTweets.append(status.retweeted_status.full_text)
    else:
        allTweets.append(status.full_text)
    tweetCount += 1
    
    # We are also scraping the hashtags and the mentioned accounts in each tweets.
    
    if hasattr(status, "entities"):
        # If the tweet is been retweeted then we scrap the hashtags and the mentioned accounts from the source of the tweet.
        # All the hashtags and mentioned accoutns are stored in two list, hashtagsRT and mentionsRT respectively.
        # If the tweet doesn't have either hashtags or any mentioned accounts, then an empty string is stored to that respective variables.

        if "retweeted_status" in dir(status):
            entities = status.retweeted_status.entities
            if "hashtags" in entities:
                temp = []
                for values in entities["hashtags"]:
                    if values is not None:
                        if "text" in values:
                            hashtag = values["text"]
                            if hashtag is not None:
                                temp.append(hashtag)
                hashtagsRT.append(temp)
            if "user_mentions" in entities:
                temp = []
                for values in entities["user_mentions"]:
                    if values is not None:
                        if "screen_name" in values:
                            name = values["screen_name"]
                            if name is not None:
                                temp.append(name)
                mentionsRT.append(temp)
        else:
            temp = []
            hashtagsRT.append(temp)
            mentionsRT.append(temp)
        
        # If the content is tweeted from the user account, then we scrap the hashtags and the mentioned accounts from the user account itself.
        # All the hashtags and mentioned accoutns are stored in two list, hashtags and mentions respectively.
        # If a tweet doesn't have either hashtags or any mentioned accounts, then an empty string is stored to that respective variables.
        
        entities = status.entities
        if "hashtags" in entities:
            temp = []
            for values in entities["hashtags"]:
                if values is not None:
                    if "text" in values:
                        hashtag = values["text"]
                        if hashtag is not None:
                            temp.append(hashtag)
            hashtags.append(temp)
        if "user_mentions" in entities:
            temp = []
            for values in entities["user_mentions"]:
                if values is not None:
                    if "screen_name" in values:
                        name = values["screen_name"]
                        if name is not None:
                            temp.append(name)
            mentions.append(temp)
    
    # Break the loop if a tweet's created date exceeds the endDate.

    if status.created_at < endDate:
        break

# Storing informations like the total tweets account since the account created, when the account created, 
# Account is been activate for how many days, etc.

tweets = user.statuses_count
accountCreatedDate = user.created_at
delta = datetime.utcnow() - accountCreatedDate
accountAge = delta.days
print("RETRIEVING TWEETS OF " + userName)
print("NAME: " + user.name)
print("DESCRIPTION: " + user.description)
print("TOTAL TWEETS COUNT: " + str(user.statuses_count))
print("FOLLOWING COUNT: " + str(user.friends_count))
print("FOLLOWERS COUNT: " + str(user.followers_count))
print("ACCOUNT'S AGE (IN DAYS): " + str(accountAge))
if accountAge > 0:
    print("AVERAGE TWEETS PER DAY: " + "%.2f" %(float(tweets)/float(accountAge)))
print("DATE OF LAST PROCESSED TWEET: " + str(status.created_at))    
print("TOTAL NUMBER OF TWEETS PROCESSED: " + str(tweetCount))

# Finally saving all the collected tweets in a text file.

with open('tweets.txt', 'w') as fileWrite:
    for item in allTweets:
        text = item.split("\n")
        text = ' '.join(text).split()
        fileWrite.write(' '.join(text))
        fileWrite.write('\n')
