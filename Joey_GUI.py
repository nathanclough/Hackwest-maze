from tkinter import *
from PIL import Image
root = Tk()

def Enlarge(Sol_Img, Img):
    im=Image.open(Sol_Img)
    im2 = Image.open(Img)
    x = im.width
    im2 = im.resize(size=(9 * x, 9 * x))
    im2.show()
    im = im.resize(size=(9 * x, 9 * x))
    im.show()

def Display_Results(Img, Sol_Img):
    TempImg= Image.open(Sol_Img)
    w,h = TempImg.size
    i = Image.open(Img)
    s_i= Image.open(Sol_Img)
    width = (w*2)+60
    height = h+80
    root.title("SOLVED MAZE DISPLAY")
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    canvas.configure(bg="red")
    tempWidth=(w/2)+20
    canvas.create_text(tempWidth,20,text="Orignal Maze:", font='Forte 12 bold')
    canvas.create_text((w+tempWidth+20),20,text="Solved Maze:", font='Forte 12 bold')
    img=PhotoImage(file=Img)
    img2 = PhotoImage(file=Sol_Img)
    canvas.create_image(20,40, anchor=NW, image=img)
    temp=w+40
    canvas.create_image(temp,40, anchor=NW, image=img2)
    btn = Button(root,width=5, text="Exit", command=root.destroy, font = 'Impact 10', bg="black", fg="red")
    btn.place(x=width/2+20, y=height-28)
    btn = Button(root,width=5, text="Enlarge", command=lambda: Enlarge(Sol_Img, Img), font = 'Impact 10', bg="black", fg="red")
    btn.place(x=width/2-60, y=height-28)
    root.mainloop()