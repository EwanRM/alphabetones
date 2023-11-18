from PIL import Image, ImageDraw, ImageFont
import os

def avgpixel(pixel):
    r, g, b, a = pixel
    avgvalue = (r+g+b) // 3
    return avgvalue

def avgtile(tlx, tly, edge, filename):   
    sumvalue = 0
    x = 0
    y = 0
    with Image.open(filename) as img:   
        for y in range(edge):
            for x in range(edge):
                pix = img.getpixel((tlx+x,tly+y))
                sumvalue += avgpixel(pix)
                x += 2
            y += 2
            x = 0
    avgvalue = sumvalue // edge // edge
    return avgvalue

def avglist(edge, filename):
    tlx = 0
    tly = 0
    valuelist = []
    while tly < 1080:
        tlx = 0
        while tlx < 1920:
            avgvalue = avgtile(tlx,tly, edge, filename)
            valuelist.append(avgvalue)
            tlx += edge
        tly += edge
    return valuelist

def makeletter(x, y, edge, valuesize, filename):
    myfont = ImageFont.truetype("aptosblack.ttf", size=valuesize)
    rectangleshape = [(x,y),(x+edge,y+edge)]
    with Image.open(filename) as img:
        draw = ImageDraw.Draw(img)  
        draw.rectangle(rectangleshape, fill=(0,0,0), outline=None, width=1)
        draw.text((img.width//2, img.height//2), "a", align="center", font=myfont, anchor='mm')

def main():
    imgletter = Image.new(mode="RGB", size=(1920,1080), color=(0,0,0,255))
    imgletter.save("imgletter.png")

    edge = 60
    filename = "frog2.png"
    valuelist = avglist(edge, filename)    

    tlx = 0
    tly = 0
    index = 0
    letterindex = 0
    letterlist = ["F", "R", "O", "G"]
    fillshadow = (0,255,0)
    fillhighlight = (0,255,0)
    with Image.open("imgletter.png") as finalimg:
        while tly < 1080:
            tlx = 0
            while tlx < 1920:
                #makeletter(tlx,tly, edge, currentsize, finalimg)
                currentsize = valuelist[index]
                currentletter = letterlist[letterindex]
                print(currentsize)

                if currentsize == 0:
                    pass
                elif currentsize > 0 and currentsize < 32:
                    myfont = ImageFont.truetype("arial.ttf", size=currentsize)
                    rectangleshape = [(tlx,tly),(tlx+edge,tly+edge)]
                    draw = ImageDraw.Draw(finalimg)  
                    #draw.rectangle(rectangleshape, fill=(0,0,0), outline=None, width=1)
                    draw.text((tlx+(edge//2), tly+(edge//2)), currentletter, fill=fillshadow, align="center", font=myfont, anchor='mm')
                else:
                    myfont = ImageFont.truetype("arial.ttf", size=currentsize)
                    rectangleshape = [(tlx,tly),(tlx+edge,tly+edge)]
                    draw = ImageDraw.Draw(finalimg)  
                    #draw.rectangle(rectangleshape, fill=(0,0,0), outline=None, width=1)
                    draw.text((tlx+(edge//2), tly+(edge//2)), currentletter, fill=fillhighlight, align="center", font=myfont, anchor='mm')
                
                index += 1
                letterindex += 1
                if letterindex > 3:
                    letterindex = 0
                tlx += edge
            tly += edge
        finalimg.save("imgletterfinish.png")
        finalimg.show()

if __name__ == "__main__":
    main()