from tkinter import *
from PIL import ImageTk,Image
from modules.bookSelect import *
from modules.bookCheckout import *
from modules.bookReturn import * #PIL -> Pillow
from database import *  
from tkinter import messagebox 
from tkinter import ttk 
import numpy as np
import matplotlib.pyplot as plt

rootS = Tk
bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'

# listData = ttk.Treeview()
# global ws_ent

# --------------------------------background---------------------------------------- #
def background(root,title):
    """
    resuable GUI background 
    """

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
# --------------------------------background---------------------------------------- #

# --------------------------------button---------------------------------------- #        
def button(root,buttonText,rely,command):
    """
    resuable GUI button 
    """
    btn1 = Button(root,text=buttonText,bg='alice blue', fg='black' ,command=command)
    btn1.place(relx=0.28,rely=rely, relwidth=0.45,relheight=0.1)
# --------------------------------button---------------------------------------- #

# --------------------------------emptyView---------------------------------------- #
def emptyView(rootS): 
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

# --------------------------------mainPage---------------------------------------- #
def mainPage():
    """
    generate main page 
    """

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x800")
    
    background(root,"Library Management System")

    button(root,"Book Search",0.4,searchPage)
    button(root,"Book Checkout",0.5,bookCheckoutPage)
    button(root,"Book Return",0.6,returnBookPage)
    button(root,"Book Select",0.7,bookSelectPage)
    button(root,"Add Book",0.8,addBookPage)
    root.mainloop()
# --------------------------------mainPage---------------------------------------- #

# --------------------------------showData---------------------------------------- #
def onClickShowData():
    """
    get data from book log and view it in the table view 
    """
    
    global treeview ,searchEntry
    onClickReset() 
    searchString =str(searchEntry.get())

    if searchString == '':  
        logList = returnAllTitleLog()              
    else:    
        logList = searchTitleLog(searchString) 
        
    print(logList)
    for f in logList:
        treeview.insert("", END, values=f)
# --------------------------------showData---------------------------------------- #

# --------------------------------clear_all---------------------------------------- #
def onClickReset():
    """
    clear table view data
    """
    global treeview

    #    treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22)  
    for item in treeview.get_children():
        treeview.delete(item)
# --------------------------------clear_all---------------------------------------- #

# --------------------------------searchPage---------------------------------------- #
def searchPage():
    """
    generate search page view 
    """

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
    
    ws_btn1 = Button(rootS, text = 'Search',  width = 8, font=('calibri', 12, 'normal'),command=onClickShowData)
    ws_btn1.place(x = 350, y = 540)
    ws_btn2 = Button(rootS, text = 'Reset',  width = 8, font=('calibri', 12, 'normal',),command=onClickReset)
    ws_btn2.place(x = 450, y = 540)
    ws_btn3 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal'), command=rootS.destroy)
    ws_btn3.place(x = 550, y = 540)
    

    
    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()
# --------------------------------searchPage---------------------------------------- #

# --------------------------------retunBook---------------------------------------- #    
def onClickRetunBook():
    """
    return a book and update the database
    """
    global searchEntry
    returnAuth =""
    # print(ws_ent.get())
    id = str(searchEntry.get())
    result = getBookStatusByID(id)
    
    # result 0 means no data found 
    # result 1 means a book/s was found  
    if result == "":
       messagebox.showerror('Error',"Book does not Exist")

    if result == "available":
       messagebox.showerror('Error',"Book exists and available!\n Cannot be returned")

    if result != "available" and result != "":
       returnAuth = messagebox.askquestion('Success',"Book Exists and ready to be returned!\n Are you sure you want to do this?")
    
    if returnAuth == "yes":
        returnBook(id,"not available","available    ")
        addTransactionHistoryRecord (id)
# --------------------------------retunBook---------------------------------------- #

# --------------------------------returnBookPage---------------------------------------- # 
def returnBookPage():
    """
    generate return book page
    """
    global searchEntry
    rootS = Tk()
    rootS.title("Book Search")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Return a Book")


    ws_lbl = Label(rootS, text = "Book ID", font=('calibri', 12, 'normal'))
    ws_lbl.place(x = 190, y = 310)
    searchEntry = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    searchEntry.place(x = 100, y = 340)
    # searchString = str(ws_ent.get)
    

    ws_btn1 = Button(rootS, text = 'Return',  width = 8, font=('calibri', 12, 'normal'),command=onClickRetunBook)
    ws_btn1.place(x = 400, y = 340)    
    ws_btn2 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal',),command=rootS.destroy)
    ws_btn2.place(x = 500, y = 340) 
    

    
    # button(root,"Quit",0.9,root.destroy)

    rootS.mainloop()
# --------------------------------returnBookPage---------------------------------------- #

# --------------------------------bookCheckout---------------------------------------- #
def onClickBookCheckout():
    """
    checkout a book and update the database
    """
    global searchEntry
    returnAuth =""
    # print(ws_ent.get())
    id = str(searchEntry.get())
    result = getBookStatusByID(id)
    
    # result 0 means no data found 
    # result 1 means a book/s was found  
    if result == "":
       messagebox.showerror('Error',"Book does not Exist")

    if result == "available":
       returnAuth = messagebox.askquestion('Success',"Book Exists and ready to be returned!\n Are you sure you want to do this?")
       
    if result != "available" and result != "":
       messagebox.showerror('Error',"Book exists and not available!\n Cannot be checked out")
    
    if returnAuth == "yes":
       bookCheckOut(id,"available    ","not available")
       addTransactionHistoryRecord (id)
# --------------------------------bookCheckout---------------------------------------- #

# --------------------------------bookCheckoutPage---------------------------------------- # 
def bookCheckoutPage():
    """
    generate book checkout page
    """
    global searchEntry
    rootS = Tk()
    rootS.title("Book Checkout")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Book Checkout")


    ws_lbl = Label(rootS, text = "Book ID", font=('calibri', 12, 'normal'))
    ws_lbl.place(x = 190, y = 310)
    searchEntry = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    searchEntry.place(x = 100, y = 340)
    # searchString = str(ws_ent.get)
    

    ws_btn1 = Button(rootS, text = 'Checkout',  width = 8, font=('calibri', 12, 'normal'),command=onClickBookCheckout)
    ws_btn1.place(x = 400, y = 340)    
    ws_btn2 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal',),command=rootS.destroy)
    ws_btn2.place(x = 500, y = 340) 
# --------------------------------bookCheckoutPage---------------------------------------- #

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

    bookIDExist =insert(bookInfoFilePath ,booksList, booksTableHeader,"Books")
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
 
# --------------------------------addBookPage---------------------------------------- #
def bookSelectPage():
    """
    generate book recomendation page
    """
    global bookIdEntry,genreEntry,titleEntry,authorEntry,purchasePriceEntry,purchaseDateEntry
    # rootS = Tk()
    # rootS.title("Show Recommended Books")   
    # rootS.geometry("750x700+400+50")  
    # rootS.resizable(0, 0)       
    # background(rootS,"Add Book")
    
    logList = [
        ["1","1003", "Sci-fi", "Stars",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["2","1004", "Fantacy", "Aliens?",  "author_2",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["3","1003", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["4","1003", "English", "Eng 101",  "author_4",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["5","1003", "Novel", "Witcher",  "author_1",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["10","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["100","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["9","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["88","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["44","1009", "English", "Eng 101",  "author_4",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["99","1006", "Math", "Simple Math",  "author_3",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["93","1007", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
    ]
    # data['Social_Media_Popularity'] = (data['num_user_for_reviews']/
    #                                data['num_voted_users'])*data['movie_facebook_likes']

    # lets also check the Top 10 Most Popular Movies on Social Media
    # x = logList.sort_values(by = 'ID', ascending = False).head(10).reset_index()
    print(logList)
    genreDictionary=selectTopGenres(bookTransactionHistoryFilePath)
    # -------------- bar chart
    # x = range(1,5)
    # y = range(1,5)
    # plt.bar(x, y, fill=True, hatch='/')
    # plt.show()

    # --------------- pie chart 

    # data = np.random.rand(5)
    # patches = plt.pie(data)
    # patches
    # hatches = ['o' if value==min(data) else 'O' if value==max(data) else '' for value in data]
    # patches = plt.pie(data)
    # for i in range(len(patches[0])):
    #     patches[0][i].set(hatch = hatches[i], fill=False)
    # plt.show()

    plt.rcdefaults()
    fig, ax = plt.subplots()
    # for key in list(genreDictionary.keys()):
    # #    print(key, ":", genreDictionary[key])
    #     people = (key)
    #     performance = genreDictionary[key]
    genreDictionarySorted = dict() 

    sortedList = sorted(genreDictionary.items(), key=lambda item: item[1], reverse=True)
    # sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
    print(sortedList)  # [(1, 1), (3, 4), (2, 9)]
    genreDictionarySorted = {key: value for key, value in sortedList}

    genre = list(genreDictionarySorted.keys())
    count = list(genreDictionarySorted.values())
    
     # Example data
    # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(genreDictionarySorted))
    # performance = 3 + 10 * np.random.rand(len(people))
    # error = np.random.rand(len(genreDictionary))
    # count.sort(reverse=True)

    ax.barh(y_pos, count,  align='center')
    ax.set_yticks(y_pos, labels=genre)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Popularity based on number of Rheckouts/Returns')
    ax.set_title('Most Popular Book Genre')

    np.random.seed(19680801)

    plt.show()

    rootS.mainloop()
# --------------------------------addBookPage---------------------------------------- #

