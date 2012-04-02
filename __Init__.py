#import tweepy
#__author__ = 'User1'
import urllib2
import simplejson

# The request also includes the userip parameter which provides the end
# user's IP address. Doing so will help distinguish this legitimate
# server-side traffic from traffic which doesn't come from an end-user.
url = ('https://ajax.googleapis.com/ajax/services/search/web'
       '?v=1.0&q= &userip=USERS-IP-ADDRESS')

request = urllib2.Request(
    url, None, {'Referer': "http://twitter.com/"})
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
# now have some fun with the results...
#print results.