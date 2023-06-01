from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from database import *  
from tkinter import messagebox 
from tkinter import ttk


rootS = Tk
bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
# listData = ttk.Treeview()
# global ws_ent

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

def emptyView(rootS):    
    # rootS.focus()
    global treeview
    scrollbarx = Scrollbar(rootS, orient=HORIZONTAL)  
    scrollbary = Scrollbar(rootS, orient=VERTICAL)    
    treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22)  
    

    treeview.pack()
    treeview.heading('Grene', text="Title", anchor=CENTER)
    treeview.column("Grene", stretch=NO, width = 100) 
    treeview.heading('Title', text="Author", anchor=CENTER)
    treeview.column("Title", stretch=NO)
    treeview.heading('Author', text="Grene", anchor=CENTER)
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

def mainPage():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x800")
    
    background(root,"Library Management System")

    button(root,"Book Search",0.4,searchPage)
    button(root,"Book Checkout",0.5,bookCheckoutPage)
    button(root,"Book Return",0.6,returnBookPage)
    button(root,"Book Select",0.7,searchPage)
    button(root,"Add Book",0.8,addBookPage)
    root.mainloop()

def showData():
    # rootS.delete(0, END)     
    # rootS.focus()
    global treeview ,searchEntry
    clear_all() 
    searchString =str(searchEntry.get())

    if searchString == '':  
        logList = returnAllTitleLog()              
    else:    
        logList = searchTitleLog(searchString) 
        
    print(logList)
    for f in logList:
        treeview.insert("", END, values=f)

def clear_all():
   global treeview
    
#    treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22)  
   for item in treeview.get_children():
      treeview.delete(item)

def searchPage():
    global searchEntry
    rootS = Tk()
    rootS.title("Book Search")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    
    # treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22) 
    emptyView(rootS)     

    searchLabel = Label(rootS, text = "Book Title", font=('calibri', 12, 'normal'))
    searchLabel.place(x = 190, y = 518)
    searchEntry = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    searchEntry.place(x = 100, y = 540)

    # searchString = str(ws_ent.get)
    # print(ws_ent.get)
    
    ws_btn1 = Button(rootS, text = 'Search',  width = 8, font=('calibri', 12, 'normal'),command=showData)
    ws_btn1.place(x = 350, y = 540)
    ws_btn2 = Button(rootS, text = 'Reset',  width = 8, font=('calibri', 12, 'normal',),command=clear_all)
    ws_btn2.place(x = 450, y = 540)
    ws_btn3 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal'), command=rootS.destroy)
    ws_btn3.place(x = 550, y = 540)
    

    
    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()
    
def retunBook():
    global ws_ent
    returnAuth =""
    # print(ws_ent.get())
    id = str(ws_ent.get())
    result = searchLogID2(id)
    
    # result 0 means no data found 
    # result 1 means a book/s was found  
    if result == "":
       messagebox.showerror('Error',"Book does not Exist")

    if result == "available":
       messagebox.showerror('Error',"Book exists and available!\n Cannot be returned")

    if result != "available" and result != "":
       returnAuth = messagebox.askquestion('Success',"Book Exists and ready to be returned!\n Are you sure you want to do this?")
    
    if returnAuth == "yes":
        update(id,"not available","available    ")
 
def returnBookPage():
    global ws_ent
    rootS = Tk()
    rootS.title("Book Search")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Return a Book")


    ws_lbl = Label(rootS, text = "Book ID", font=('calibri', 12, 'normal'))
    ws_lbl.place(x = 190, y = 310)
    ws_ent = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    ws_ent.place(x = 100, y = 340)
    # searchString = str(ws_ent.get)
    

    ws_btn1 = Button(rootS, text = 'Return',  width = 8, font=('calibri', 12, 'normal'),command=retunBook)
    ws_btn1.place(x = 400, y = 340)    
    ws_btn2 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal',),command=rootS.destroy)
    ws_btn2.place(x = 500, y = 340) 
    

    
    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()

def bookCheckout():
    global ws_ent
    returnAuth =""
    # print(ws_ent.get())
    id = str(ws_ent.get())
    result = searchLogID2(id)
    
    # result 0 means no data found 
    # result 1 means a book/s was found  
    if result == "":
       messagebox.showerror('Error',"Book does not Exist")

    if result == "available":
       returnAuth = messagebox.askquestion('Success',"Book Exists and ready to be returned!\n Are you sure you want to do this?")
       
    if result != "available" and result != "":
       messagebox.showerror('Error',"Book exists and not available!\n Cannot be checked out")
    
    if returnAuth == "yes":
        update(id,"available    ","not available",)
 
def bookCheckoutPage():
    global ws_ent
    rootS = Tk()
    rootS.title("Book Checkout")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Book Checkout")


    ws_lbl = Label(rootS, text = "Book ID", font=('calibri', 12, 'normal'))
    ws_lbl.place(x = 190, y = 310)
    ws_ent = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    ws_ent.place(x = 100, y = 340)
    # searchString = str(ws_ent.get)
    

    ws_btn1 = Button(rootS, text = 'Checkout',  width = 8, font=('calibri', 12, 'normal'),command=bookCheckout)
    ws_btn1.place(x = 400, y = 340)    
    ws_btn2 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal',),command=rootS.destroy)
    ws_btn2.place(x = 500, y = 340) 

def addBook():
    global bookIdEntry,genreEntry,titleEntry,authorEntry,purchasePriceEntry,purchaseDateEntry
    
    
    bookIdEntry = str(bookIdEntry.get())
    genreEntry = str(genreEntry.get())
    titleEntry = str(titleEntry.get())
    authorEntry= str(authorEntry.get())
    purchasePriceEntry= str(purchasePriceEntry.get())
    purchaseDateEntry= str(purchaseDateEntry.get())

    booksTableHeader = ["    ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Purchase Date  "]
    logTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Loan Availability  ", "  Checkout Date  "  , "  Return Date  "]

    booksList = [[bookIdEntry,genreEntry,titleEntry,authorEntry,purchasePriceEntry,purchaseDateEntry]]
    logList = [[bookIdEntry,"", genreEntry, titleEntry,  authorEntry,  "available",  "" ,  "" ]]

    bookIDExist =insert(bookInfoFilePath ,booksList, booksTableHeader,"Books")
    insert(logFilePath ,logList, logTableHeader,"Logs")

    if bookIDExist !="":
        messagebox.showerror('Error',bookIDExist)
    else: 
        messagebox.showinfo('Success',"Book added successfully!")     

def addBookPage():
    global bookIdEntry,genreEntry,titleEntry,authorEntry,purchasePriceEntry,purchaseDateEntry
    rootS = Tk()
    rootS.title("Add Book")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Add Book")
       

    labelFrame = Frame(rootS,bg='alice blue')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

     # Book ID
    bookIdLabel = Label(labelFrame,text="Book ID : ", bg='alice blue', fg='black')
    bookIdLabel.place(relx=0.05,rely=0.1, relheight=0.08)
        
    bookIdEntry = Entry(labelFrame)
    bookIdEntry.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    # Genre
    genreLabel = Label(labelFrame,text="Genre : ", bg='alice blue', fg='black')
    genreLabel.place(relx=0.05,rely=0.25, relheight=0.08)
        
    genreEntry = Entry(labelFrame)
    genreEntry.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # Title
    titleLabel = Label(labelFrame,text="Title : ", bg='alice blue', fg='black')
    titleLabel.place(relx=0.05,rely=0.40, relheight=0.08)
        
    titleEntry = Entry(labelFrame)
    titleEntry.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)
        
    # Author
    authorLabel = Label(labelFrame,text="Author : ", bg='alice blue', fg='black')
    authorLabel.place(relx=0.05,rely=0.55, relheight=0.08)
        
    authorEntry = Entry(labelFrame)
    authorEntry.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

    # Purchase Price JOD
    purchasePriceLabel = Label(labelFrame,text="Purchase Price JOD : ", bg='alice blue', fg='black')
    purchasePriceLabel.place(relx=0.05,rely=0.70, relheight=0.08)
        
    purchasePriceEntry = Entry(labelFrame)
    purchasePriceEntry.place(relx=0.3,rely=0.70, relwidth=0.62, relheight=0.08)

    # Purchase Date
    purchaseDateLabel = Label(labelFrame,text="Purchase Date : ", bg='alice blue', fg='black')
    purchaseDateLabel.place(relx=0.05,rely=0.85, relheight=0.08)
        
    purchaseDateEntry = Entry(labelFrame)
    purchaseDateEntry.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(rootS,text="SUBMIT",bg='alice blue', fg='black',command=addBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(rootS,text="Quit",bg='alice blue', fg='black', command=rootS.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()

# searchPage()