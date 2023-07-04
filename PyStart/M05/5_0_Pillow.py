from PIL import Image # czemu tu nie czyta ale z cmd dziala

im = Image.open("flower.jpg")
thumbnail = im.resize((300, 300))
