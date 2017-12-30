from secrets import *
import tweepy

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

import pyspeedtest
st = pyspeedtest.SpeedTest()
res = ""
res += "PING: " + str(format(st.ping(), '.2f')) + " ms\n"
res += "down: " + str(format(st.download() / 1000000.0, '.2f')) + "\n"
res += "up: " + str(format(st.upload() / 1000000.0, '.2f'))
print(res)

api.update_status(res)
