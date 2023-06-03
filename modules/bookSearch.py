
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


# # --------------------------------searchMemberID---------------------------------------- #
# def searchMemberID(ID):
#     """
#     search members by ID\n
#     ID as an argument (int)\n
#     return status 0 if not exist | 1 if exist 
#     """

#     with open(membersFilePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         status = 0
#         for line in lines:
#             if line.find(ID) != -1:
#                 status = 1
#                 break

#     return status
# # --------------------------------searchMemberID---------------------------------------- #

# # --------------------------------searchLogID---------------------------------------- #
# def getBookStatusByID(ID):    
#     """
#     search log by ID and get avilability status\n
#     Book ID as an argument (int)\n
#     return status 0 if not exist | 1 if exist 
#     """
#     # title.lower()
#     loanAvilabilityStatus = ""
#     with open(logFilePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         templist = []
#         resultList = []
        
       
#         for line in lines[1:]:
#             # line.lower()
#             # check if string present on a current line
#             # id = line[0:14]
#             templist2  = line.split("|")
#             id = str(templist[1]).replace(" ","")
#             fileId = int(id  )
#             ID = int(ID)

#             if fileId == ID and line.index != 0:
#             # if id.find(ID) != -1 and line.index != 0:
#                 line = line.replace(" ","")
#                 resultList  = line.split("|")
#                 loanAvilabilityStatus= resultList[6]
                

#     return loanAvilabilityStatus   
# # --------------------------------searchLogID---------------------------------------- #

# # --------------------------------searchTitleLog---------------------------------------- #
# def searchTitleLog(title):
#     """
#     search book log by title\n
#     title as an 1st argument (string)\n
#     return list of books
#     """
#     # title.lower()
#     with open(logFilePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         status = 0
#         templist = []
#         resultList = []

#         for line in lines[1:]:
#             # line.lower()
#             # check if string present on a current line
#             templist2  = line.split("|")
#             lineTitle = str(templist2[4]).replace(" ","").lower()
#             fileTitle = title.lower()
#             # ID = int(ID)

#             # if fileId == ID and line.index != 0:
                
#             if lineTitle.find(fileTitle) != -1 and lines.index != 0:
#                 line = line.replace(" ","")
#                 templist  = line.split("|")
#                 templist.pop(0)
#                 templist.pop(0)
#                 templist.pop(0)
                
#                 templist.pop(len(templist)-1)                
#                 templist.pop(len(templist)-1)                
#                 templist.pop(len(templist)-1)
#                 resultList.append(templist)
                

#     return resultList     
# # --------------------------------searchTitleLog---------------------------------------- #

# # --------------------------------returnAllTitleLog---------------------------------------- #
# def returnAllTitleLog():
#     """
#     get all book log data\n
#     return all book log data
#     """
     
#     with open(logFilePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         status = 0
#         templist = []
#         resultList = []
#         print(lines[0])
#         for line in lines[1:]:
            
#             line = line.replace(" ","")
#             templist  = line.split("|")
#             templist.pop(0)
#             templist.pop(0)
#             templist.pop(0)
            
#             templist.pop(len(templist)-1)                
#             templist.pop(len(templist)-1)                
#             templist.pop(len(templist)-1)
#             resultList.append(templist)
                

#     return resultList  
# # --------------------------------returnAllTitleLog---------------------------------------- #

# # --------------------------------searchTitle---------------------------------------- #
# def searchTitle(title):
#     """
#     search book by title\n
#     title as an 1st argument (string)\n
#     return list of books
#     """
#     # title.lower()
#     with open(bookInfoFilePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         status = 0
#         for line in lines:
#             # line.lower()
#             # check if string present on a current line
#             if line.find(title) != -1:
#                 print( line)
#                 status = 1
#                 # break
#         if status == 0: 
#            print('No Results Found')
# # --------------------------------returnAllTitleLog---------------------------------------- #

# # --------------------------------searchID---------------------------------------- #
# def searchID(filepath,ID):
#     """
#     search by ID\n
#     Book ID as an 1st argument (int)\n
#     return list of books
#     """
#     # title.lower()
#     with open(filepath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines()
#         global status
#         status = 0
#         searchResult = []
#         lineNumber = 0

#         for line in lines:
#             templist = []

#             if lineNumber == 0:  
#                 id = line[0:20]
#                 if id.find(ID) != -1 and line.index != 0:
#                     status = 1
#                     searchResult=line.split("|")
#                     break 
#             else:
#                 templist  = line.split("|")
#                 id = str(templist[1]).replace(" ","")
#                 fileId = int(id  )
#                 ID = int(ID)

#                 if fileId == ID and line.index != 0:
#                     # print(id, 'string exists in file')
#                     # print('Line Number:', lines.index(line))
#                     # print('Line:', line)
#                     status = 1
#                     searchResult=line.split("|")
#                     break
#                     # break

#     return searchResult
# # --------------------------------searchID---------------------------------------- #

# def getSearchStatus(filepath,ID):
#     global status
#     searchID(filepath,ID)

#     return status

# # --------------------------------update---------------------------------------- #
# def getBookByID(filePath,ID):
#     """
#     get Book By ID\n
#     Book ID as an 1st argument (int)\n
#     return book details
#     """

#     with open(filePath, 'r') as fp:
#         # read all lines in a list
#         lines = fp.readlines() 

#         for line in lines[1:]:
#             # line.lower()
#             # check if string present on a current line
#             # id = line[0:14]
#             templist2  = line.split("|")
#             id = str(templist2[1]).replace(" ","")
#             fileId = int(id  )
#             ID = int(ID)

#             if fileId == ID and line.index != 0:
#             # if id.find(ID) != -1 and line.index != 0:
#                 # templine = line
#                 # line = line. strip('\n')
#                 searchResult=line.split("|")
#                 # fw.write('\n') 
                

#     return searchResult  
# # --------------------------------update---------------------------------------- #

