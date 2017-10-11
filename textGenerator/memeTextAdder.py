from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import time, sys
import random
import markovify
import traceback
import textwrap



random.seed()

counter = 0 
argfile = 'redditMoppeMemesCombined.txt'

with open(argfile) as f:
	text = f.read()
        # Build the model.
	text_model = markovify.Text(text)



for i in range(0, 1000):
    img = Image.open("images/meme1.jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Fonts/unicode.impact.ttf", 90)

    widthImg, heightImg = img.size

    try:
        text1 = text_model.make_short_sentence(60).rstrip().decode("utf-8")
    except AttributeError:
        print "unable to make short top sentence"
    try:
        text2 = text_model.make_short_sentence(60).rstrip().decode("utf-8")
    except AttributeError:
        print "unable to make short bottom sentence"
        
    margin = offset = widthImg* 0.05
    for line in textwrap.wrap(text1.upper(), width=26):
        try:
            draw.text((margin, offset), line, font=font, fill="#ffffff")
        except TypeError:
            print "Margin error, ignoring line"
        offset += font.getsize(line)[1]

    margin = widthImg* 0.05
    offset = heightImg * 0.80
    for line in textwrap.wrap(text2.upper(), width=26):
        try:
            draw.text((margin, offset), line, font=font, fill="#ffffff")
        except TypeError:
            print "Draw Text error, ignoring line"
        offset += font.getsize(line)[1]


    ##draw.text((width* 0.10, height*0.05), text1.upper(), (255,255,255),font=font)
    ##draw.text((width* 0.10, height*0.80), text2.upper(), (255,255,255),font=font)


    img.save("GeneratedMemes/dankMoppeMemeGenerated" + str(i) + ".jpg")
    print("Done with: " + str(i))
