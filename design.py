from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from database import *  
from tkinter import messagebox 



def background(root,title):
    same=True
    n=1
    # Adding a background image
    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#9e9d9d")
    Canvas1.pack(expand=True,fill=BOTH)
    # Canvas1 = Canvas(root)
    # Canvas1.create_image(300,340,image = img)      
    # Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    # Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text=title, bg='alice blue', fg='black', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        

def button(root,buttonText,rely,command):
    btn1 = Button(root,text=buttonText,bg='alice blue', fg='black' ,command=command)
    btn1.place(relx=0.28,rely=rely, relwidth=0.45,relheight=0.1)


def labelFrame(root):    

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('Title','Author','Genre', 'Loan Availability'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    Label(labelFrame,text="%-10s%-30s%-30s%-20s"%("asd","asdasd","rtrtrtr","qwerzcvdr") ,bg='black', fg='white').place(relx=0.07,rely=y)

def mainPage():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x800")
    
    background(root,"Library Management System")

    button(root,"Book Search",0.4,searchPage)
    button(root,"Book Checkout",0.5,searchPage)
    button(root,"Book Return",0.6,searchPage)
    button(root,"Book Select",0.7,searchPage)
    button(root,"Add Book",0.8,searchPage)
    root.mainloop()


def searchPage():
    root = Tk()
    root.title("Book Search")
    root.minsize(width=400,height=400)
    root.geometry("800x700")

    background(root,"Search Books")
    labelFrame(root)
    button(root,"Quit",0.9,root.destroy)
    root.mainloop()
