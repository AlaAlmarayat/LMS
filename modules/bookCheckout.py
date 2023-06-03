from tkinter import *
from tkinter import messagebox 
from modules.database import *
from modules.design import background


# --------------------------------bookCheckout---------------------------------------- #
def onClickBookCheckout():
    """
    checkout a book and update the database
    """
    global searchEntry, memberEntry, rootS
    returnAuth =""
    # print(ws_ent.get())
    bookId = str(searchEntry.get())
    memberId = str(memberEntry.get())

    result = getBookStatusByID(bookId)
    
    # result 0 means no data found 
    # result 1 means a book/s was found  
    if result == "":
       messagebox.showerror('Error',"Book does not Exist")

    if result == "available":
       returnAuth = messagebox.askquestion('Success',"Book Exists and ready to be returned!\n Are you sure you want to do this?")
       
    if result != "available" and result != "":
       messagebox.showerror('Error',"Book exists and not available!\n Cannot be checked out")
    
    if returnAuth == "yes":
       update(bookId,memberId, 7,"not available")
       addTransactionHistoryRecord (bookId)
    
    rootS.destroy()
    # rootS.quite   
# --------------------------------bookCheckout---------------------------------------- #

# --------------------------------bookCheckoutPage---------------------------------------- # 
def bookCheckoutPage():
    """
    generate book checkout page
    """
    global searchEntry,memberEntry,rootS
    rootS = Tk()
    rootS.title("Book Checkout")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    background(rootS,"Book Checkout")

    labelFrame = Frame(rootS,bg='alice blue')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.3)

     # search Entry ID
    bookIdLabel = Label(labelFrame,text="Book ID : ", bg='alice blue', fg='black')
    bookIdLabel.place(relx=0.05,rely=0.2, relheight=0.1)
        
    searchEntry = Entry(labelFrame)
    searchEntry.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.1)
        
    # Genre
    memberLabel = Label(labelFrame,text="Member ID : ", bg='alice blue', fg='black')
    memberLabel.place(relx=0.05,rely=0.4, relheight=0.1)

    memberEntry = Entry(labelFrame)
    memberEntry.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.1)
      
      #Submit Button
    SubmitBtn = Button(rootS,text="Checkout",bg='alice blue', fg='black',command=onClickBookCheckout)
    SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(rootS,text="Quit",bg='alice blue', fg='black', command=rootS.destroy)
    quitBtn.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)

    
    
    # ws_lbl = Label(rootS, text = "Book ID", font=('calibri', 12, 'normal'))
    # ws_lbl.place(x = 190, y = 310)
    # searchEntry = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    # searchEntry.place(x = 100, y = 340)
    # searchString = str(ws_ent.get)
    

    # ws_btn1 = Button(rootS, text = 'Checkout',  width = 8, font=('calibri', 12, 'normal'),command=onClickBookCheckout)
    # ws_btn1.place(x = 400, y = 340)    
    # ws_btn2 = Button(rootS, text = 'Exit',  width = 8, font=('calibri', 12, 'normal',),command=rootS.destroy)
    # ws_btn2.place(x = 500, y = 340) 
# --------------------------------bookCheckoutPage---------------------------------------- #
