from PIL import Image, ImageDraw, ImageFont

def main():
    with Image.open("still_life_desk.png") as img:
        myfont = ImageFont.truetype("arial.ttf", size=100)
        draw = ImageDraw.Draw(img)
        draw.text((img.width//2, img.height//2), "Ewan McInerney", align="center", font=myfont, anchor='mm')
        img.show()

if __name__ == "__main__":
    main()