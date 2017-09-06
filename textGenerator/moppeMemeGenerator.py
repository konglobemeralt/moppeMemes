import time, sys
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
    text = text_model.make_short_sentence(140)
    print(text)
    counter += 1


