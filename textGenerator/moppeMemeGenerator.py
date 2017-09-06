import tweepy, time, sys
import random
import markovify
import traceback

random.seed()

counter = 0 
argfile = 'moppeMemes.txt'
    
with open(argfile) as f:
	text = f.read()
        # Build the model.
	text_model = markovify.Text(text)

while counter < 100:  
    tweet = text_model.make_short_sentence(140)
    print(tweet)
    counter += 1


