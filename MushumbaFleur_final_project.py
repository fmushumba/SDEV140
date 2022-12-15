from tkinter import *
from PIL import ImageTk, Image

#window 1
root = Tk()

#set app title and background
root.title("Audit+")
root.geometry("600x400")
root.state('zoomed')
root.configure(bg="#90ee90")


#Introduction label
label1= Label(root,
    text=" Welcome to the auditing app that makes your life easy",
    padx=460,
    pady=5,
    font=("algerian, 12")
    
)
label1.grid(row=1 , column = 0, columnspan=5)


#background image
image1= Image.open('C:/Users/mushu/OneDrive/Documents/Python Scripts/Learning/SDEV140/tkinterapp/app_icon.jpg')
test= ImageTk.PhotoImage(image1)
image_label=Label(root, image= test)
image_label.image=test
image_label.place(x=400,y=100)




#Window2
root2=Toplevel()

#Comparison image 

image2=ImageTk.PhotoImage(Image.open('C:/Users/mushu/OneDrive/Documents/Python Scripts/Learning/SDEV140/tkinterapp/dirty_factory2.png')) #first image 
image2_label=Label(root2,image=image2,)
image2_label.grid(row=3, column=0)

image3=ImageTk.PhotoImage(Image.open('C:/Users/mushu/OneDrive/Documents/Python Scripts/Learning/SDEV140/tkinterapp/dirty factory.png')) #second image 
image3_label=Label(root2,image=image2,)
image3_label.grid(row=3, column=3, columnspan=3)

# This function creates new window
def imageWindow():
    root2.title("past Images")
    root2.geometry("200x200")
    root2.state('zoomed')
    root2.configure(bg="black")
    new_window_items()  # function calls the label and quit functions


# Function adds items to new window
def new_window_items():    
    label2= Label(root2,  text = 'This window shows Past Pictures', font =('calibri', 15))
    label2.grid(row =1, column=2, columnspan=3)
    
     #Button to close window
    button5=Button(root2, padx=5, pady = 30, text= 'click here to close window', command=root2.destroy)
    button5.grid(row=5 , column = 2, columnspan=3)





#Call back functions 
    
#user entry
def add_user_findings():
    user_comments= Text(root,
        width=30,
        height=20,
        borderwidth=5,
        bg="white",
        fg='green')
    user_comments.grid(row=4,column=0)

#user recommendation entry 
def add_user_recommendation():
    user_comments= Text(root,
        width=30,
        height=20,
        borderwidth=5,
        bg="white",
        fg='green')
    user_comments.grid(row=4,column=3,columnspan=4)
    



# Menu option to open regulation file  
def add_GMP_Regulations():
    with open('C:/Users/mushu/Downloads/21 CFR Part 117 (up to date as of 11-30-2022).pdf','r') as file:
        file.read()

#Menu option to set dark mode 
def darkMode():
    if darkmode.get() == 1:
        root.config(background='#90ee90')
    elif darkmode.get() == 0:
        root.config(background='black')

darkmode = BooleanVar()
darkmode.set(False)




# Adding Menu options (areas, 
menubar=Menu(root)
menubar.add_command(label=" Area scores", command=lambda: print("Model being built , SORRY!"))
menubar.add_command(label="Images", command=imageWindow)


# Adding regulations otion 
Regulations=Menu(menubar,tearoff=False, background='#ff8000')
Regulations.add_command(label="GMP Regulation")
Regulations.add_command(label="Cleaning Regulation")
menubar.add_cascade(label='Regulations',underline=1, menu=Regulations)

#adding dark mode view option 
view = Menu(menubar, tearoff=0)

view.add_checkbutton(label='Darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
menubar.add_cascade(label='View', menu=view)


root.config(menu=menubar)

#buttons

#Findings button
button1= Button(root,
    padx=60,
    pady=10,
    text='Click here to enter findings',
    fg="black",
    bg="green",
    command=add_user_findings
)

button1.grid(row=2, column= 0,)

#recommendation button
button2= Button(root,
    padx=60,
    pady=10,
    text='Click here to Enter recommendation',
    fg="black",
    bg="green",
    command=add_user_recommendation
)
button2.grid(row=2, column= 3,columnspan=4)







root.mainloop()