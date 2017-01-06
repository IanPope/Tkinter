from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Death Star is in range", entrytxt)

def addtolist():
    entrytxt = entry1.get()
    if checkforduplicate() == False:
        listbox1.insert(END, entrytxt)
        findsize()
        entry1.delete(0,END)
    
def addtolist2(event):
    entrytxt = entry1.get()
    if checkforduplicate() == False:
        listbox1.insert(END, entrytxt)
        findsize()
        entry1.delete(0,END)

def clearlist(event):
    listbox1.delete(0, END) 
    
def checkforduplicate():
    names = listbox1.get(0, END) 
    if entry1.get() in names:
        print True
    else:
        return False
        
def findsize():
    label1.config(text=listbox1.size())
  

   




root = Tk() #gives us a blank canvas object to work with
root.title("My first GUI program withTkinter.")

button1 = Button(root, text="Super Lasor", bg="green", command=addtolist)
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="Death Star", bg="red", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW, rowspan=10)
listbox1.bind("<Button-3>", clearlist)

listbox1.insert(END, "Bob")
listbox1.insert(END, "John")
listbox1.insert(END, "Mary")

findsize()

image = Image.open("1483716194295-1492134974.jpg")
photo = ImageTk.PhotoImage(image)

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=12, column=0)

mainloop() #causes the windows to display on the screen until program closes
