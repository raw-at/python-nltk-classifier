from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="3MsCGEMHc4Zosd5U2nAXZiEjM"
csecret="R2RTiDy8Mf7ujHuEwuIx6Q61UEOeqakO349nmBHFT9WqKU9V5O"
atoken="3284992050-1sZGL1lPx2diitwiU38kFTHlucZRgWtOrJpxBPW"
asecret="wyNRsEnnxph90M0GrJEdoQVZkFcF9p5Z3zuydN7tgRTe2"

class listener(StreamListener):

    def on_data(self, data):
        try:
        	all_data=json.loads(data)
        	tweet=all_data["text"]
        	sentiment_value, confidence=s.sentiment(tweet)

        	print(tweet.encode("utf-8"),sentiment_value,confidence)
        	if confidence*100 >= 80:
        		output = open("twitter-out.txt","a")
        		output.write(sentiment_value)
        		output.write('\n')
        		output.close()
        	return(True)
        except:
            return(True)
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])