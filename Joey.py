from PIL import Image, ImageDraw, ImageColor
import Joey_GUI


<<<<<<< HEAD

=======
>>>>>>> 9d3c0952a24a16db2af73e90e57cb1fbc285a3e3
def DrawMaze(Img,a):
    img = Image.open(Img).convert("RGB")
    draw = ImageDraw.Draw(img)
    i=0
    while i<len(a):
        draw.point((a[i][1],a[i][0]), fill=ImageColor.getcolor("red", "L"))
        i=i+1
    del draw
    img.save("SOLVED_MAZE.png")
    Joey_GUI.Display_Results(Img, "SOLVED_MAZE.png")

