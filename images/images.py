from PIL import Image, ImageFilter

img = Image.open('../original.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
