import tkinter as tk
import tkinter.messagebox
#import numpy as np
import random

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=280,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        quit_btn = tk.Button(self)
        quit_btn['text'] ='閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side = 'bottom')


root = tk.Tk()
root.title("bingo!!")#title
root.geometry("400x300")
app = Aplication(root=root)
app.mainloop()