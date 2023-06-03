# from modules.database import getTopGenres,insert
# from bookSearch import *
from tkinter import END, Button, Entry, Frame, Label, Tk, messagebox
from matplotlib import pyplot as plt
import numpy as np

from modules.database import getAveragePrice, returnAllTitleLog, searchTitleLog, selectTopGenres,selectTopBooks
from modules.design import background, smallButton, tableView
# from modules.database import selectTopGenres

# selectTopGenres(bookTransactionHistoryFilePath)    
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'
bookInfoFilePath ='.\\files\\Book_Info.txt'

# --------------------------------showData---------------------------------------- #
def onClickShowData():
    """
    get data from book log and view it in the table view 
    """
    
    global treeview ,searchEntry
    onClickReset() 
    # budget =int(searchEntry.get())
    searchString =str(searchEntry.get())
    # if int(searchEntry.get()).isnumeric():  
        
    if searchString == "" :
        messagebox.showerror('Error',"Budget could not be Empty")   
    else: # int(searchString).isnumeric():
        budget = int(searchEntry.get())
        recommededList = getAveragePrice(bookTransactionHistoryFilePath,bookInfoFilePath,budget)    
    # else:
    #     messagebox.showerror('Error',"Please enter a valid number")      
         

    
        
    # print(logList)
    for value in recommededList:
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

# --------------------------------bookSelectPage---------------------------------------- #
def bookSelectPage():
    """
    generate book select recommendations list 
    """

    global searchEntry,treeview
    rootS = Tk()
    rootS.title("Recommendations List")   
    rootS.geometry("750x700+400+50")  
    rootS.resizable(0, 0)       
    
    # treeview = ttk.Treeview(rootS, columns=("Title", "Author", "Grene", "Loan Availabilty"), show='headings', height=22) 
    treeview = tableView(rootS, "Number of Checkout/Returns", "Average Prices","Recommended Copies")     

    searchLabel = Label(rootS, text = "Budget: ", font=('calibri', 12, 'normal'))
    searchLabel.place(x = 100, y = 540)
    searchEntry = Entry(rootS,  width = 12, font=('Arial', 15, 'bold'))
    searchEntry.place(x = 180, y = 540)

    smallButton(rootS,"Generate recommendations",25 ,onClickShowData ,330 , 540)
    smallButton(rootS,"Clear",8 ,onClickReset,550 , 540)
    smallButton(rootS,"Top Book Titles",15 ,getTopBookTitles ,180 , 600)
    smallButton(rootS,"Top Genres",15 ,getTopGeneres,330 , 600)
    

    rootS.mainloop()
# --------------------------------bookSelectPage---------------------------------------- #



def getTopBookTitles():
    bookDictionary = selectTopBooks(bookTransactionHistoryFilePath)
    getTop(bookDictionary,"Titles")


def getTopGeneres():
    genereDictionary=selectTopGenres(bookTransactionHistoryFilePath)
    getTop(genereDictionary, "Genres")


def getTop(topicDictionary,type):
    """
    get top book Title/Genre recomendation chart
    """
    # topicDictionary=selectTopGenres(bookTransactionHistoryFilePath)
     
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    genreDictionarySorted = dict() 

    sortedList = sorted(topicDictionary.items(), key=lambda item: item[1], reverse=True)
    # sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
    print(sortedList)  # [(1, 1), (3, 4), (2, 9)]
    genreDictionarySorted = {key: value for key, value in sortedList}

    genre = list(genreDictionarySorted.keys())
    count = list(genreDictionarySorted.values())
    
    y_pos = np.arange(len(genreDictionarySorted))
    
    ax.barh(y_pos, count,  align='center')
    ax.set_yticks(y_pos, labels=genre)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Popularity based on number of Rheckouts/Returns')
    ax.set_title('Most Popular Book '+ type)

    np.random.seed(19680801)

    plt.show()
   


