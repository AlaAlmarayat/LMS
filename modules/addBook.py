from tkinter import Button, Entry, Frame, Label, Tk, messagebox
from modules.database import insert
from modules.design import background

rootS = Tk
bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'

# --------------------------------addBook---------------------------------------- #
def onClickAddBook():
    """
    add a book to the database
    """
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

    bookIDExist = insert(bookInfoFilePath ,booksList, booksTableHeader,"Books")
    insert(logFilePath ,logList, logTableHeader,"Logs")

    if bookIDExist !="":
        messagebox.showerror('Error',bookIDExist)
    else: 
        rootS.destroy 
        messagebox.showinfo('Success',"Book added successfully!")           
# --------------------------------addBook---------------------------------------- #

# --------------------------------addBookPage---------------------------------------- #
def addBookPage():
    """
    generate add book form page
    """
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
    SubmitBtn = Button(rootS,text="SUBMIT",bg='alice blue', fg='black',command=onClickAddBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(rootS,text="Quit",bg='alice blue', fg='black', command=rootS.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()
# --------------------------------addBookPage---------------------------------------- #
 