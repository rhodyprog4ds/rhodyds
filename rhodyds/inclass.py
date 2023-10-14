
import requests

class Tweet(object):
    def __init__(self, tweet_url, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = 'https://publish.twitter.com/oembed?url={}'.format(tweet_url)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

# Tweet("https://twitter.com/OReillyMedia/status/901048172738482176")
