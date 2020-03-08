import os
from tkinter.filedialog import askopenfilename
import shutil

def opener():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected
    destination = "C:\Python projects\Hackwest-maze"
    try:
        shutil.copy(filename, destination)
    except shutil.SameFileError:
        pass
    file = os.path.basename(filename)
    return file
