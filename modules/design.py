from tkinter import *
from tkinter import ttk 
# import numpy as np
# import matplotlib.pyplot as plt 

rootS = Tk
bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'

# --------------------------------background---------------------------------------- #
def background(root,title):
    """
    resuable GUI background 
    """

    same=True
    n=1
    # Adding a background image
    # background_image =Image.open("lib.jpg")
    # [imageSizeWidth, imageSizeHeight] = background_image.size
    # newImageSizeWidth = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n) 
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n) 
        
    # background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(background_image)

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
# --------------------------------background---------------------------------------- #

# --------------------------------button---------------------------------------- #        
def bigButton(root,buttonText,command,relx,rely,relwidth,relheight):
    """
    resuable GUI button 
    """
    btn = Button(root,text=buttonText,bg='alice blue', fg='black' ,command=command)
    btn.place(relx=relx,rely=rely, relwidth=relwidth,relheight=relheight)
# --------------------------------button---------------------------------------- #

# --------------------------------button---------------------------------------- #        
def smallButton(rootS,buttonText,width,command,x,y):
    """
    resuable GUI button 
    """
    btn = Button(rootS, text = buttonText,  width = width, font=('calibri', 12, 'normal'),command=command)
    btn.place(x = x, y = y)
# --------------------------------button---------------------------------------- #

# --------------------------------emptyView---------------------------------------- #
def tableView(rootS): 
    """
    resuable GUI table 
    """   
    # rootS.focus()
    global treeview
    scrollbarx = Scrollbar(rootS, orient=HORIZONTAL)  
    scrollbary = Scrollbar(rootS, orient=VERTICAL)    
    treeview = ttk.Treeview(rootS, columns=("Grene", "Title", "Author", "Loan Availabilty"), show='headings', height=22)  
    

    treeview.pack()
    treeview.heading('Grene', text="Grene", anchor=CENTER)
    treeview.column("Grene", stretch=NO, width = 100) 
    treeview.heading('Title', text="Title", anchor=CENTER)
    treeview.column("Title", stretch=NO)
    treeview.heading('Author', text="Author", anchor=CENTER)
    treeview.column("Author", stretch=NO)
    treeview.heading('Loan Availabilty', text="Loan Availabilty", anchor=CENTER)
    treeview.column("Loan Availabilty", stretch=NO)
    
    # listData = treeview 

    scrollbary.config(command=treeview.yview)
    scrollbary.place(x = 526, y = 7)
    scrollbarx.config(command=treeview.xview)
    scrollbarx.place(x = 220, y = 460)

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    
    
        

    return treeview
# --------------------------------emptyView---------------------------------------- #
