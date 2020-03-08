from PIL import Image, ImageDraw, ImageColor
import Joey_GUI


def DrawMaze(a):
    Img = "small.png"
    img = Image.open(Img).convert("RGB")
    draw = ImageDraw.Draw(img)
    i=0
    while i<len(a):
        draw.point(a[i], fill=ImageColor.getcolor("red", "L"))
        i=i+1
    del draw
    img.save("SOLVED_MAZE.png")
    Joey_GUI.Display_Results(Img, "SOLVED_MAZE.png")

