from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("images/test.jpg")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Fonts/HelveticaBold.ttf", 90)

draw.text((100,100), "Vroom, Vroom, nu kor vi!",(255,255,255),font=font)
img.save("dankMoppeMeme.jpg")

