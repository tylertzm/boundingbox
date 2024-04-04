from matplotlib import pyplot as plt
from PIL import Image
# with Image.open("/Users/tyler/Desktop/Uni/Bildverarbeitung/Beleg 1/ct_image.png") as im:
#     im.show()

import numpy as np

img = Image.open("/Users/tyler/Desktop/Uni/Bildverarbeitung/Beleg 1/ct_image.png")
pixel_array1 = np.array(img.rotate(90))
pixel_array2 = np.array(img.rotate(45))

for x in range(img.width):
  for y in range(img.height):
    pixel = img.getpixel((x, y))
width, height = img.size
# print(str(width) + "x" + str(height))


def find_bounding_box1(img):
    non_zero = np.nonzero(pixel_array1)
    min_y, min_x = np.min(non_zero, axis=1)
    max_y, max_x = np.max(non_zero, axis=1)
    return min_x, min_y, max_x, max_y

min_x, min_y, max_x, max_y = find_bounding_box1(pixel_array1)

def find_bounding_box2(img):
    non_zero = np.nonzero(pixel_array1)
    min_y, min_x = np.min(non_zero, axis=1)
    max_y, max_x = np.max(non_zero, axis=1)
    return min_x, min_y, max_x, max_y

min_x, min_y, max_x, max_y = find_bounding_box2(pixel_array2)

cropped_image1 = pixel_array1[min_y:max_y+1, min_x:max_x+1]
cropped_image2 = pixel_array2[min_y:max_y+1, min_x:max_x+1]

plt.imshow(cropped_image1, cmap='gray')  # Assuming it's a grayscale image
plt.axis('off')  # Turn off axis
plt.show()

plt.imshow(cropped_image2, cmap='gray')  # Assuming it's a grayscale image
plt.axis('off')  # Turn off axis
plt.show()