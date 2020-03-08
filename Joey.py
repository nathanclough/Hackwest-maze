from PIL import Image, ImageDraw, ImageColor
import Joey_GUI


def DrawMaze(Img, a):
    img = Image.open(Img).convert("RGB")
    draw = ImageDraw.Draw(img)
    i=0
    while i<len(a):
        draw.point((a[i][1],a[i][0]), fill=ImageColor.getcolor("white", "RGB"))
        i=i+1
    del draw
    img.save("SOLVED_MAZE.png")
    Joey_GUI.Display_Results(Img, "SOLVED_MAZE.png")

