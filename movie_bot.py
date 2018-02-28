from app_data import *
import tweepy
from imdb import IMDb
from random import randint
import time

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    imdb = IMDb()

    top250 = imdb.get_top250_movies()
    ranking_pos = randint(0, len(top250) - 1)
    movie = top250[ranking_pos]

    msg = 'Hey there, I have an interesting fact about {} for you!\n\n'.format(movie)

    imdb.update(movie, 'trivia')

    while True:
        while True:
            trivia_idx = randint(0, len(movie['trivia']) - 1)
            fact = movie['trivia'][trivia_idx]
            # tweets are only allowed to include <= 140 chars
            if len(fact) <= 140:
                break
        api.update_status(msg + fact)
        # post a tweet every 10 minutes
        print("sleeping for 10 minutes now..")
        time.sleep(600)
