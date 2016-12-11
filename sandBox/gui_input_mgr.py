import Tkinter
import os
ip = '192.168.1.1'

def get_info(arg):
    exec(tfield.get("1.0", "current lineend"))

root = Tkinter.Tk()
tfield = Tkinter.Text(root)
tfield.pack()

tfield.bind("<Return>", get_info)
root.mainloop()
f.close()