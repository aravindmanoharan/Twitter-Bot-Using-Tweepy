# Twitter-Bot-Using-Tweepy

Tweepy is a very useful library to create a bot that would like a tweet, follow an user and can also retweet based on certain hashtags. Therefore, this repository shows how to scrap user's data, their tweets, hashtags and tagged accoutns for each of their tweets. This twitter bot is written in Python using Tweepy library.

## Installation

You can install Tweepy using the pip package manager.
```
pip install tweepy
```

You can also clone the GitHub repository if you do not have pip installed.
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```

You’ll need to import Tweepy as follows:
```
from tweepy import OAuthHandler, API, Cursor
```

Please check the requirements.txt file if you need to install anymore packages.

## Credentials

Next, we need to link our Twitter account to our Python script. Go to [Twitter](apps.twitter.com) and sign in with your account. Create a Twitter application and generate a Consumer Key, Consumer Secret, Access Token, and Access Token Secret

Then store the credentials within variables and authenticate your account using Tweepy with these credentials.
```
CONSUMER_KEY = 'consumer key'
CONSUMER_KEY_SECRET = 'consumer secrets'
ACCESS_TOKEN = 'access token'
ACCESS_TOKEN_SECRET = 'access token secret'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth)
```

In order to check if your program is working you could add:
```
user = api.me()
print (user.name)
```

This should return the name of your Twitter account in the console.
