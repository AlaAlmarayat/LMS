
from tkinter import *
from modules.database import *  
from tkinter import messagebox 
from tkinter import ttk 
import numpy as np
import matplotlib.pyplot as plt
from modules.database import returnAllTitleLog, searchTitleLog
from modules.design import tableView, smallButton

bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'

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
    for value in logList:
        treeview.insert("", END, values=value)
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

    global searchEntry,treeview
    rootS = Tk()
    rootS.title("Book Search")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    
    # treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22) 
    treeview = tableView(rootS,"Title", "Author", "Loan Availabilty")     

    searchLabel = Label(rootS, text = "Book Title", font=('calibri', 12, 'normal'))
    searchLabel.place(x = 190, y = 518)
    searchEntry = Entry(rootS,  width = 20, font=('Arial', 15, 'bold'))
    searchEntry.place(x = 100, y = 540)

    smallButton(rootS,"Search",8 ,onClickShowData ,350 , 540)
    smallButton(rootS,"Reset",8 ,onClickReset ,450 , 540)
    smallButton(rootS,"Exit",8 ,rootS.destroy,550 , 540)

    rootS.mainloop()
# --------------------------------searchPage---------------------------------------- #
