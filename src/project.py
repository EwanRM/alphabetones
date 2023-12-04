from PIL import Image, ImageDraw, ImageFont
import math, os

def avgpixel(pixel):
    # Averages RGB values for one pixel
    r, g, b, a = pixel
    avgvalue = (r+g+b) // 3
    return avgvalue

def avgtile(tlx, tly, edge, img):
    # Averages values from the previous function for a square tile of pixels of length "edge"
    ## For each pixel, adds avgpixel value to a sum value, then divides it by edge^2, number of pixels in tile
    ## tlx and tly are coords of the top left corner of the tile; location of tile in the image   
    sumvalue = 0
    x = 0
    y = 0
    for y in range(edge):
        for x in range(edge):
            pix = img.getpixel((tlx+x,tly+y))
            sumvalue += avgpixel(pix)
            x += 1
        y += 1
        x = 0
    avgvalue = sumvalue // edge // edge
    return avgvalue

def avglist(edge, img, width, height):
    # Generates a list of average color values for all tiles in an image
    ## Goes through the image tile by tile and executes the avgtile function
    ## Appends the returned value to a list
    tlx = 0
    tly = 0
    tilex = 0
    tiley = 0
    valuelist = []
    while tly <= (height - edge):
        tlx = 0
        tilex = 0
        while tlx <= (width - edge):
            avgvalue = avgtile(tlx,tly, edge, img)
            valuelist.append(avgvalue)
            tlx += edge
            tilex += 1
        tly += edge
        tiley += 1
    return valuelist, tilex, tiley


def makechar(img, tlx, tly, edge, char, fontsize, color):
    # Creates a text character in the center of a pixel tile with variable size and color
    myfont = ImageFont.truetype("arial.ttf", size=fontsize)
    draw = ImageDraw.Draw(img)  
    draw.text((tlx+(edge//2), tly+(edge//2)), char, fill=color, align="center", font=myfont, anchor='mm')


def main():
    
    # User inputs
    
    filename = input("Input file: ")
    outputheight = int(input("Output height resolution: "))
    
    edge = int(input("Tile edge length: "))

    chars = input("Text: ")
    charsize = float(input("Character size (1 = medium): "))

    print("(No commas)")
    rback, gback, bback = input("Background color: ").split()
    rhigh, ghigh, bhigh = input("Light color: ").split()
    rshad, gshad, bshad = input("Shadow color: ").split()
    shadow = int(input("Shadow threshold value: "))

    # Image generation specs

    ## Quality multiplier scales everything in output image based on desired resolution
    with Image.open(filename) as img:
        width = img.width
        height = img.height
    qualmult = outputheight / height
    widthnew = math.ceil(width * qualmult)
    heightnew = math.ceil(height * qualmult)
    edgenew = edge * qualmult

    ## All average tile values to determine letter generation size in the future
    with Image.open(filename) as img:
        valuelist, tilex, tiley = avglist(edge, img, width, height)

    ## List of user input letters to cycle through during letter generation
    charlist = []
    for char in chars:
        charlist.append(char)

    ## Color variables
    fillbackground = (int(rback),int(gback),int(bback))
    fillshadow = (int(rshad),int(gshad),int(bshad))
    fillhighlight = (int(rhigh),int(ghigh),int(bhigh))

    # Image creation

    ## Blank file
    imgletter = Image.new(mode="RGB", size=(widthnew,heightnew), color=fillbackground)
    imgletter.save("output.png")

    ## Starting point: top left of image, beginning of value and letter lists
    tlx = (widthnew - (edgenew * tilex)) / 2
    tly = (heightnew - (edgenew * tiley)) / 2
    idxvalue = 0
    currentvalue = valuelist[idxvalue]
    idxchar = 0
    currentchar = charlist[idxchar]

    # Image generation

    with Image.open("output.png") as finalimg:

        for i in range(tiley):
            tlx = (widthnew - (edgenew * tilex)) / 2
            for i in range(tilex):
                currentvalue = valuelist[idxvalue]
                # Font size increases when the user input for character size increases
                fontsize = currentvalue * edgenew // (60 / charsize)
                currentchar = charlist[idxchar]

                # If size is greater than shadow threshold, use highlight color; otherwise use shadow color
                if fontsize == 0:
                    pass
                else:
                    if currentvalue > shadow:
                        makechar(finalimg, tlx, tly, edgenew, currentchar, fontsize, fillhighlight)
                    else:
                        makechar(finalimg, tlx, tly, edgenew, currentchar, fontsize, fillshadow)
                
                idxvalue += 1
                idxchar += 1
                # Cycle back to start of text input after final character is used
                if idxchar > (len(charlist) - 1):
                    idxchar = 0

                tlx += edgenew
            tly += edgenew

        finalimg.save("alphabetone.png")
        os.remove("output.png")
        finalimg.show()

if __name__ == "__main__":
    main()