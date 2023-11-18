from PIL import Image, ImageFilter


def main():
    with Image.open("scamphibian.png") as img:
        blur_img = img.filter(ImageFilter.GaussianBlur((100,1)))
        sharp_img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=500, threshold=1))
        img.show()
        blur_img.show()
        sharp_img.show()


if __name__ == "__main__":
    main()