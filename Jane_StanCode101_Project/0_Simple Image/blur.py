"""
File: blur.py
Name: Jane Huang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    This program blur the image and add up the nearest 8 blocks
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred = blur(old_img)
    blurred.show()


def blur(old_img):
    """
    :param old_img: SimpleImage, the original smile face
    :return blurred: SimpleImage, the blurred simle face
    """
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for y in range(old_img.height):
        for x in range(old_img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i  # candidate pixel_x
                    pixel_y = y + i  # candidate pixel_y
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.blue
                            b_sum += pixel.green
                            count += 1
                new_pixel = blurred.get_pixel(x, y)
                new_pixel.red = r_sum / count
                new_pixel.green = g_sum / count
                new_pixel.blue = b_sum / count
    return blurred


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__ == '__main__':
    main()
