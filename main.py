from tkinter import *
from tkinter import messagebox,filedialog
from PIL import *
from PIL import ImageTk,Image
from PIL.XVThumbImagePlugin import r

root = Tk()


# an class
def myClick():
    myLabel1 = Label(root, text="Clicked")
    myLabel1.pack()


# screen width and height
root.geometry("800x1000")

# title
root.title("Tkinter")

# image/photo
photo = PhotoImage(file="images.png")
imageLabel = Label(image=photo)
# a label
myLabel = Label(root,  text="Hello World")
myLabel.pack()

# textField
entry = Entry(root, width=50, borderwidth=4)
entry.pack()
# text on entry
entry.insert(0, "Enter your name : ")

# radiobutton
r = IntVar()
r.set(1)


def clickedRadioButton(value):
    label = Label(root, text=value)
    label.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clickedRadioButton(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clickedRadioButton(r.get())).pack()

# label for radiobutton
label = Label(root, text=r.get())
label.pack()

# button
myButton = Button(root, text="Press", command=myClick, fg="blue", bg="red")
myButton.pack()


# popup message
def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel,askyesno
    messagebox.showinfo("Popup title", "info")


Button(root, text="Popup", command=popup).pack()


# new windows
def openNewWindow():
    top = Toplevel()
    lbl = Label(top, text="Hello World").pack()
    topDestroyOrQuit = Button(top,text="Destroy", command=top.destroy).pack()

btnOpenNewWindow = Button(root, text="Open New Window", command=openNewWindow).pack()

# openDialogBox/Choosing file
def openDialogBox():
    global imageOfChoseFile
    root.filename = filedialog.askopenfilename(initialdir="/gui/images",title="Select a file", filetypes=(("png files","*"),("all_files","*.*")))
    myLabelFilename = Label(root, text=root.filename).pack()
    imageOfChoseFile = ImageTk.PhotoImage(Image.open(root.filename))
    labelImage = Label(image=imageOfChoseFile).pack()
btnDialogBox = Button(root, text="Select a file",command=openDialogBox).pack()

# slider
# vertical slider
vertical = Scale(root, from_=0, to=1000)
vertical.pack()
# horizontal slider
horizontal = Scale(root, from_=0, to=1000, orient=HORIZONTAL)
horizontal.pack()

ui_size_label = Label(root, text=str(horizontal.get())).pack()

def slide():
    ui_size_label = Label(root, text=str(horizontal.get())+"x"+str(vertical.get())).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
buttonSlider = Button(root,text="Check screen size",command=slide).pack()

# DropDown menus
options = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
clicked = StringVar()
clicked.set(options[0])

def showSelectedMenu():
    menusLabel = Label(root, text=clicked.get()).pack()
drop = OptionMenu(root,clicked,*options)
drop.pack()
showSelection = Button(root, text="Show Selection", command=showSelectedMenu).pack()


# run program
root.mainloop()
