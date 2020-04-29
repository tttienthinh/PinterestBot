from PIL import Image, ImageDraw, ImageFont

image = Image.open('test.jpeg')
marge_x, marge_y = image.size[0]/25, image.size[1]/25
font_size = int(image.size[0]/25)
text = "Clique pour voir l'original !"

draw = ImageDraw.Draw(image)
font_type = ImageFont.truetype('AbyssinicaSIL-R.ttf', font_size)
text_x, text_y = font_type.getsize(text)


draw.rectangle((0, 0, marge_x*2+text_x, marge_y*2+text_y), fill=(0, 128, 255))
draw.text(xy=(marge_x, marge_y), text=text, fill=(255, 255, 255), font=font_type)
# draw.rectangle((0, 0, marge_x*2+text_x, marge_y*2+text_y), fill=(255, 255, 255))
# draw.text(xy=(marge_x, marge_y), text=text, fill=(230, 0, 23), font=font_type)



image.show()
image.save("Sortie1.jpg", "JPEG")
