"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Computes the Euclidean color distance between a pixel's RGB values and a target mean RGB color.

    This function measures how similar a pixel is to a reference color by treating the
    red, green, and blue channels as coordinates in a 3D color space. A smaller distance
    indicates a closer color match.

    Parameters:
        pixel (Pixel): The pixel whose RGB components (pixel.red, pixel.green, pixel.blue)
            will be compared.
        red (int): The reference mean red value.
        green (int): The reference mean green value.
        blue (int): The reference mean blue value.

    Returns:
        float: The Euclidean distance between the pixel's RGB values and the reference color.
    """
    red_distance = (pixel.red - red)**2
    green_distance = (pixel.green - green)**2
    blue_distance = (pixel.blue - blue)**2
    color_distance = (red_distance + green_distance + blue_distance)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    count = 0
    pixel_red_total, pixel_green_total, pixel_blue_total = 0, 0, 0
    rgb = []
    # images = [image1, image2, image3, image4.....]
    # image1[x,y]
    for pixel in pixels:
        count += 1
        pixel_red_total += pixel.red
        pixel_green_total += pixel.green
        pixel_blue_total += pixel.blue
    red = pixel_red_total/count
    green = pixel_green_total/count
    blue = pixel_blue_total/count
    rgb = [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Selects the pixel that is closest in color to the average color of a group of pixels.

    This function examines a list of pixels and determines which one has the smallest
    color distance to the average RGB values of all pixels in the list. It is useful
    for finding the most "representative" pixel in a set.

    Parameters:
        pixels (List[Pixel]): A list of Pixel objects to evaluate.

    Returns:
        Pixel: The pixel whose color is closest to the average color of the input list.
    """
    # Initialize the variables
    color_distance_min = float('inf')
    best_pixel = None

    # count all pixel's avg_rgb by get_average(pixels)
    avg_rgb = get_average(pixels)  # List[red, green, blue]
    red = avg_rgb[0]
    green = avg_rgb[1]
    blue = avg_rgb[2]

    for pixel in pixels:
        color_distance = get_pixel_dist(pixel, red, green, blue)
        if color_distance < color_distance_min:
            color_distance_min = color_distance
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display the solution image
    based on images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for y in range(height):
        for x in range(width):
            # get all pixels in the images and for a pixels (List[Pixel])
            pixels = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)
            # then get the best out of all images
            # get pixel 在for loop 裡面進行，get_best_pixel 也在for loop 進行才會完整得到一張圖
            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

# execute in Terminal with below text for windows
# 1. py -3.7 stanCodoshop.py clock-tower
# 2. py -3.7 stanCodoshop.py hoover
# 3. py -3.7 stanCodoshop.py math-corner
# 4. py -3.7 stanCodoshop.py monster