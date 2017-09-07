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

img = Image.open("images/meme1.jpg")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Fonts/HelveticaBold.ttf", 90)

widthImg, heightImg = img.size

text1 = text_model.make_short_sentence(60).rstrip()
text2 = text_model.make_short_sentence(60).rstrip()

margin = offset = widthImg* 0.05
for line in textwrap.wrap(text1.upper(), width=19):
    draw.text((margin, offset), line, font=font, fill="#ffffff")
    offset += font.getsize(line)[1]

margin = widthImg* 0.05
offset = heightImg * 0.80
for line in textwrap.wrap(text2.upper(), width=19):
    draw.text((margin, offset), line, font=font, fill="#ffffff")
    offset += font.getsize(line)[1]


##draw.text((width* 0.10, height*0.05), text1.upper(), (255,255,255),font=font)
##draw.text((width* 0.10, height*0.80), text2.upper(), (255,255,255),font=font)


img.save("dankMoppeMeme.jpg")

