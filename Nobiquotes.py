import json
import time
from requests.models import Response
import tweepy
import requests
# Api authorization
auth = tweepy.OAuthHandler("API KEY", "API KEY SECRET")
auth.set_access_token("Access Token", "Access Token Secret")

# Create an API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful!")
except:
    print("Error during Authentication!")

def scheduler():
    time.sleep(3)
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    res = json.loads(response.text)
    print(res)
    api.update_status(res['content'])
    scheduler()
