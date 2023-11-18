from PIL import Image

def rgba_to_greyscale(pixel):
    r, g, b, a = pixel
    ave_value = (r + g + b) // 3
    return(r, ave_value, b*2, a)

def main():
    with Image.open("frog.png") as img:
        out_img = img.copy()
        for y in range(img.height):
            for x in range(img.width):
                pix = img.getpixel((x, y))
                out_img.putpixel((x, y), rgba_to_greyscale(pix))
        out_img.show()
        out_img = img.copy()
        out_img = out_img.convert('L')
        out_img.show()

if __name__ == "__main__":
    main()