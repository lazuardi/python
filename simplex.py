import os
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *

class App(object):
  def __init__(self,root):
    self.text = Text()
    self.text.pack()
    
    clbtn = Button(root,text="New", command=self.onNew).pack(side=LEFT)
    svbtn = Button(root,text="Save", command=self.onSave.pack(side=LEFT)
    opbtn = Button(root,text="Open",command = self.onOpen).pack(side=LEFT)
    exbtn = Button(root,text="Exit",command=self.onExit).pack(side=RIGHT)
  
  def onNew(self):
    new = self.text.delete(0.0, END)
    
  def onOpen(self):
    folder = "/media/ntfs/data/Document/"
    op = askopenfile(mode='r',initialdir = folder)
    text = op.read()
    if op != None:
      self.text.delete(0.0, END)
      self.text.insert(END,text)
    
  def onSave(self):
    format = [
    ("Text Files","*.txt"),
    ("Python Files","*.py*),
    ("Hyper Text Markup Language","*.html, *.htm") ]
    save = asksavefile(mode='w',filetypes=format)
    savetext = str(self.text.get(0.0,END))
    save.write(savetext)
    save.close()
  
  def onExit(self):
    sys.exit()
  
simplex = Tk()
simplex.wm_title("Simplex")
isi = App(simplex)
simplex.mainloop()
