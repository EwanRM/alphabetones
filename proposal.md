# Title: Alphabetones
## Repository: https://github.com/EwanRM/alphabetones.git

# Description

This program will take a user-submitted picture and convert it into a grid of small, colorful letters that match the picture's appearance.
    The letters will be a repetition of a user-input word.

The final product will be similar to how dots are used in halftone shading, where size corresponds to regional value.

# Features

- The user can specify two hues to be used for the shadows and highlights of the picture.
 -  The code calculates the average value of a square tile of pixels in the picture, in the middle of which will be the letter.
 -  For any tiles that output below a certain value number, the shadow hue is used in the letter generation, and vice versa.

- The user can offset the rotation of the letter grid by a specifiable value.
 -  The tiles of the picture analyzed must be rotated, meaning that they will not fit exactly on the page.
 -  To solve this, the number of tiles across and down the grid will be scaled up so that it covers the whole picture.
 -  Any tiles completely off the grid will be ignored.

- The user can adjust the size of the tiles to convert to letters.
 -  The generated letter grid will be revealed with a "whoosh" animation, from one end of the screen to the other
 -  This animation will be rotated according to the rotation of the letter grid.
 -  Each row has a random amount of time to appear, so rows will reveal themselves faster or slower, making the animation more interesting.
    
# Challenges

- Different letters have different dimensions, so it might be difficult to translate that to square tiles.
 -  I might have to make rectangular or changing tiles if that becomes an aesthetic problem.

- For different pictures, the division between shadows and highlights might be different.
 -  Maybe make the shadow -> highlight transition value customizable.

- If the grid of tiles is tilted and tiles completely out of bounds must be ignored, the ones partially inbounds still need to be there.
 -  If any pixel in the tile is inbounds, keep it. Would that if statement slow the program down?

# Outcomes

- Ideal: A graphic art piece with letters as halftone shading with a customizable color scheme, level of detail, and rotation.
 -  Revealed with a whoosh animation
 -  Minimal: A grid of letters with smaller letters in dark spots and bigger letters in light spots.

# Milestones

- Week 1
 -  Process a picture by splitting it into tiles and outputting the average color value of each tile.
 -  Generate a grid of shapes, one in the center of each tile, and make the average value influence the size of each shape.

- Week 2
 -  Make these shapes into letters with different font sizes.
 -  Allow the user to specify a word and have each tile in a row from left to right spell that word repeatedly.

- Week 3
 -  Implement customizable hues for shadows and highlights.
 -  Allow the grid and tiles to be rotated; increase the size of the grid as needed, then delete tiles that extend beyond the screen.

- Week 4
 -  Create the reveal animation; possibly place long black rectangles over each row that slide off the screen.