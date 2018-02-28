import tweepy
import time
import sys
from app_data import *
from imdb import IMDb
from random import randint

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    imdb = IMDb()
    top250 = imdb.get_top250_movies()

    greetings = sys.stdin.readlines()

    while True:
        greeting_idx = randint(0, len(greetings) - 1)
        greeting = greetings[greeting_idx].strip()

        ranking_pos = randint(0, len(top250) - 1)
        movie = top250[ranking_pos]
        msg = '{} I have an interesting fact about {} for you!\n'.format(greeting, movie)
        imdb.update(movie, 'trivia')
        while True:
            trivia_idx = randint(0, len(movie['trivia']) - 1)
            fact = movie['trivia'][trivia_idx]
            # tweets are only allowed to include <= 140 chars
            if len(msg + fact) <= 140:
                break
        api.update_status(msg + fact)
        print(msg + fact)
        # post a tweet every hour
        print("sleeping for an hour now..")
        time.sleep(3600)
