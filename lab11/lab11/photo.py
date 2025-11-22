#Read image
import numpy as np
from PIL import Image

# img = Image.open(r'MU.jpg')
# img.show()

# #Create a New Image
# new_img = Image.new("RGB", (200, 200), color="white")
# new_img.show()

# #Create a New Image
# new_img = Image.new("L", (200, 200), color="white")
# new_img.show()


# #Resize Image
# from PIL import Image
# img = Image.open(r"MU.jpg")
# # Resize to 100x100 pixels
# resized_img = img.resize((100, 100))
# resized_img.show()

# #Resize Image
# from PIL import Image
# img = Image.open(r"MU.jpg")
# # Resize to 100x100 pixels
# resized_img = img.resize((800, 400))
# resized_img.show()


# #Arithmetic Operations (Add, Subtract)
# from PIL import Image, ImageChops
# img1 = Image.open(r"MU.jpg").resize((300, 300))
# img2 = Image.open(r"MU.jpg").resize((300, 300))

# added = ImageChops.add(img1, img2)
# added.show()

# subtracted = ImageChops.subtract(img1, img2)
# subtracted.show()


# #Convert Image to Grayscale
img = Image.open(r"MU.jpg")
# gray = img.convert("L")   # "L" mode = grayscale
# gray.show()



red, green, blue = img.split()
zeroed_band = red.point(lambda _: 0)
red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

red_merge.show()
green_merge.show()
blue_merge.show()
