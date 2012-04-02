import tweepy
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="xFjMcIk2Ryv48dDIdly99g"
consumer_secret="qxtSuGtehsMV9bd7NeanpBfoKoQbHjt6i8WXyvoF4"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="178537877-NiL3F5InaP5zGMNSzgcYXlf3IGkCAymut98wwFfB"
access_token_secret="LLjaumvC9Tw5E9k94OueGrN7T13p3ugS2OJfh5HGVY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# If the authentication was successful, you should
# see the name of the account print out
print api.me().name
#help(tweepy.API)
flw=tweepy.API.followers(api)
ustln=tweepy.API.user_timeline(api,user_id=flw[16].id,count=100,include_entities=True)
for i in ustln:
    print i.text
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status('Updating using OAuth authentication via Tweepy!')
print "Finish!"