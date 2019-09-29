# Example to send/receive values from Adafruit IO with the REST API client

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed
import json

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = '<YOUR-AIO-KEY>'
ADAFRUIT_IO_USERNAME = '<YOUR_USERNAME>'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# List all of your feeds from your account
feeds = aio.feeds()
print(feeds)

# Create a new feed
feed = Feed(name="NewFeed")
resp = aio.create_feed(feed)
print(resp)

# List a specific feed
feed = aio.feeds(resp.key)
print(feed)

# TODO: Send value to feed 

# Get feed value
feed = aio.feeds(resp.key)
data = aio.receive(feed.key) 
print(data.value)

# Delete a feed
aio.delete_feed(response.key)