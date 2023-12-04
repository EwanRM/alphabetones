# ALPHABETONES

## GitHub Repository: https://github.com/EwanRM/alphabetones.git
## Demo video URL: https://www.youtube.com/watch?v=zcGpHjPD5Pw

## Description

This program takes a user-input picture and converts it into a grid of colorful text characters that matches the picture's appearance. The output is similar stylistically to halftone shading that can be found in comic books, but with letters instead of dots. For example, a section of the image with a brighter RGB value is converted into a larger letter, and vice versa. The characters are a repetition of a user-input string. "project.py" in the src folder is the Python program to be executed. "frog1.png," "frog2.png," and "frog3.png" are all images that can be used to experiment with the program's features. The output image from the most recent run of the code will be named "alphabetone.png." This code can handle PNG files with format RGBA.

The output image, while the aspect ratio cannot be changed from the original picture, has a customizable resolution, so it is possible to create extremely large-scale graphics that can be appreciated on both big and small scales. Most importantly, the exact level of detail of the output image can be determined. The code works by obtaining square tiles of a specified dimension in pixels from the input image and averaging the brightness of each pixel to determine the size of the resulting characters. As these tile dimensions decrease, the image gets more tiles, more and smaller characters, and more granular detail.

If the tile size does not divide evenly into the picture's dimensions, the text grid will be "centered." For example, if an image is 1006 x 1006 pixels and each tile is 10 pixels square, the top left corner of the tile grid will fall on (3, 3) so that the grid will have 3 pixels around the border.

Within this detail, the size of the characters can be further customized with a simple multiplier - for example, a multiplier of 2 doubles the size of what the original algorithm outputs for each character. This can help if an input image is particularly light or dark, which, with normal text size, might result in too many large, overlapping characters or too many small, spaced-out characters for the user's desired aesthetic.

The background color of the output image can be customized. The user is able to input two different colors for the text itself - a "light" color and a "shadow" color. When a tile is evaluated and the average RGB value comes out to be brighter than a certain "shadow threshold," the light color is used for the character. Otherwise, as long as the value is greater than 0, the shadow color is used. The shadow threshold can also be specified.

The main feature that I wanted to include in this program that I was not able to was customizable rotation for the grid of text. I wanted the user to be able to make a diagonal grid out of a rectangular picture and specify the exact angle of that grid. The two issues that I kept encountering were (1) accurately dividing the input picture into diagonal tiles, which required confusing trigonometry, and (2) dealing with partial tiles at the edges of the image, which resulted in many errors.