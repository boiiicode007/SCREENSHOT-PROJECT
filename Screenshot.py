import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root=tk.Tk()
root.title('SS App')

canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()

def takeScreenshot():
    screenshot=pyautogui.screenshot()
    savePath=asksaveasfilename()
    screenshot.save(savePath+"_screenshot.png")

button=tk.Button(text='Take a Screenshot', command=takeScreenshot,font=10)
canvas1.create_window(150,150,window=button)

root.mainloop()



