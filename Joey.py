from PIL import Image, ImageDraw, ImageColor
import Joey_GUI


def DrawMaze(a)
    draw = ImageDraw.Draw(im)
    while i<len(a):
        draw.point(a[i], fill=ImageColor.getcolor("red", "L"))
        i=i+1
    del draw


Img="baird200.png"
img = Image.open(Img).convert("RGB")

for i in a:
    i++;

im.save("SOLVED_MAZE.png")
Joey_GUI.Display_Results(Img, "SOLVED_MAZE.png")