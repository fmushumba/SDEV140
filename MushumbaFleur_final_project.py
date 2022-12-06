from tkinter import *
from PIL import ImageTk, Image


root = Tk()

#set app title and background
root.title("Audit+")
root.geometry("600x400")
root.state('zoomed')
root.configure(bg="#90ee90"),

#retrieving image
image1= Image.open('C:/Users/mushu/OneDrive/Documents/Python Scripts/Learning/SDEV140/tkinterapp/app_icon.jpg')
test= ImageTk.PhotoImage(image1)
image_label=Label(root, image= test)
image_label.image=test
image_label.place(x=400,y=100)


#user entry

def add_user_comments():
    user_comments= Text(root,
        width=30,
        height=20,
        borderwidth=5,
        bg="white",
        fg='green')
    user_comments.grid(row=4,column=0)

#labels
label1= Label(root,
    text=" Welcome to the auditing app that makes you life easy",
    padx=500,
    pady=5,
    
)
label1.grid(row=1 , column = 0, columnspan=5)

def area_click():
    area_label= Label(root,
        text='line 1',
        padx=30,
        pady=30
    )
    area_label.grid(row=4 , column=0) 
    
def add_GMP_Regulations():
    with open('C:/Users/mushu/Downloads/21 CFR Part 117 (up to date as of 11-30-2022).pdf','r') as file:
        file.read()
def darkMode():
    if darkmode.get() == 1:
        root.config(background='#90ee90')
    elif darkmode.get() == 0:
        root.config(background='black')


minimap = BooleanVar()
minimap.set(True)
darkmode = BooleanVar()
darkmode.set(False)

button1= Button(root,
    padx=60,
    pady=10,
    text='Click here to enter findings',
    fg="black",
    bg="green",
    command=add_user_comments
)

button1.grid(row=2, column= 0,)

# Adding Menu options (areas, 
menubar=Menu(root)
menubar.add_command(label=" Area scores", command=lambda: print("Hello"))
menubar.add_command(label="Images", command=lambda: print("Goodbye"))



Regulations=Menu(menubar,tearoff=False, background='#ff8000')
Regulations.add_command(label="GMP Regulation")
Regulations.add_command(label="Cleaning Regulation")
menubar.add_cascade(label='Regulations',underline=1, menu=Regulations)

#adding dark mode view option 
view = Menu(menubar, tearoff=0)
view.add_checkbutton(label="show minimap", onvalue=1, offvalue=0, variable=minimap)
view.add_checkbutton(label='Darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
menubar.add_cascade(label='View', menu=view)


root.config(menu=menubar)











root.mainloop()