from modules.bookSearch import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 


bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'


# ------------------------------------------------------------------------ #
def searchMemberID(ID):
    
    # title.lower()
    with open(membersFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines:
            # line.lower()
            # check if string present on a current line
            if line.find(ID) != -1:
                # print(id, 'string exists in file')
                # print('Line Number:', lines.index(line))
                # print('Line:', line)
                status = 1
                break

    return status
# ------------------------------------------------------------------------ #


# ------------------------------------------------------------------------ #
def searchLogID(ID):
    
    # title.lower()
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines:
            # line.lower()
            # check if string present on a current line
            if line.find(ID) != -1:
                # print(id, 'string exists in file')
                # print('Line Number:', lines.index(line))
                # print('Line:', line)
                status = 1
                break

    return status
# ------------------------------------------------------------------------ #


def searchLogID2(ID):    
    # title.lower()
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        templist = []
        resultList = []
        
       
        for line in lines:
            # line.lower()
            # check if string present on a current line
            id = line[0:14]
            if id.find(ID) != -1 and line.index != 0:
                line = line.replace(" ","")
                resultList  = line.split("|")
                loanAvilabilityStatus= resultList[6]
                

    return loanAvilabilityStatus   


def update(ID,oldStatus,newStatus):    
    # title.lower()
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        
        
        with open(logFilePath, 'w') as fw:
            for line in lines:
                # line.lower()
                # check if string present on a current line
                id = line[0:14]
                if id.find(ID) != -1 and line.index != 0:
                    # templine = line
                    # line = line. strip('\n')
                    fw.write(line.replace(oldStatus,newStatus))
                    # fw.write('\n')
                else: 
                   fw.write(line)
                #    fw.write('\n')
                

    return loanAvilabilityStatus  

# ------------------------------------------------------------------------ #
def searchTitleLog(title):
    
    # title.lower()
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        templist = []
        resultList = []

        for line in lines[1:]:
            # line.lower()
            # check if string present on a current line
            if line.find(title) != -1 and lines.index != 0:
                line = line.replace(" ","")
                templist  = line.split("|")
                templist.pop(0)
                templist.pop(0)
                templist.pop(0)
                
                templist.pop(len(templist)-1)                
                templist.pop(len(templist)-1)                
                templist.pop(len(templist)-1)
                resultList.append(templist)
                

    return resultList     

# ------------------------------------------------------------------------ #

def returnAllTitleLog():
    
    # title.lower()
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        templist = []
        resultList = []
        print(lines[0])
        for line in lines[1:]:
            
            line = line.replace(" ","")
            templist  = line.split("|")
            templist.pop(0)
            templist.pop(0)
            templist.pop(0)
            
            templist.pop(len(templist)-1)                
            templist.pop(len(templist)-1)                
            templist.pop(len(templist)-1)
            resultList.append(templist)
                

    return resultList  

# ------------------------------------------------------------------------ #
def insert(filePath,listItems, listTableHeader,type):
    num_cols = len(listTableHeader)
    header_row = "| "+ " | ".join(listTableHeader) + " |"
    nice_horizontal_rule = ("|" + "-" * (len(header_row)-2)+"|")
    print(nice_horizontal_rule)
    print(header_row)
    print(nice_horizontal_rule)
    status =""
    
    with open(filePath, 'a') as f:
      
      if searchID(listTableHeader[0])==0 and type == "Books":
           f.write(header_row)
           f.write('\n')
      elif searchMemberID(listTableHeader[0])==0 and type == "Members" :
           f.write(header_row)
           f.write('\n')
      elif searchLogID(listTableHeader[0])==0 and type == "Logs":
           f.write(header_row)
           f.write('\n')
           
      for item in listItems:
        # writing each row to a string,
        # then printing the string, is better for performance:)
        
        s = "|"
        for i in range(num_cols):
            entry = str(item[i])

            if type == "Members":
                entry = str(item)

            s += (" "+ entry+ " "*(len(listTableHeader[i]) - len(entry)+1)+ "|")
        

        if searchID(item[0])==0 and type == "Books":
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        elif searchMemberID(item[0])==0 and type == "Members":
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        elif  type == "Logs":
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        else: 
           status = "Book ID already exists!" 
           
     

      return status
# ------------------------------------------------------------------------ #


# def addBooks():
#     booksList = [
#         ["1", "Sci-fi", "Stars",  "author_1",  "10",  "1/8/2010" ],
#         ["2", "Fantacy", "Aliens?",  "author_2",  "10",  "1/2/2014" ],
#         ["3", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],
#         ["4", "English", "Eng 101",  "author_4",  "10",  "3/7/1999" ],
#         ["5", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
#         ["10", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
#         ["100", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
#         ["9", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
#         ["88", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
#         ["44", "English", "Eng 101",  "author_4",  "10",  "3/7/1999" ],
#         ["99", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],    
#         ["93", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],
#     ]

#     booksTableHeader = ["    ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Purchase Date  "]
#     insert(bookInfoFilePath ,booksList, booksTableHeader,"Books")

# def addMembers():
#     membersList = []

#     for i in range(10): 
#         number=str(1000+i)
#         membersList.append(number)

#     membersTableHeader = ["    ID    "]




#     insert(membersFilePath ,membersList, membersTableHeader,"Members")


# def addLog():
#     logList = [
#         ["1","1003", "Sci-fi", "Stars",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["2","1004", "Fantacy", "Aliens?",  "author_2",  "not available",  "1/8/2010" ,  "1/8/2010" ],
#         ["3","1003", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["4","1003", "English", "Eng 101",  "author_4",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["5","1003", "Novel", "Witcher",  "author_1",  "not available",  "1/8/2010" ,  "1/8/2010" ],
#         ["10","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["100","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["9","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["88","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
#         ["44","1009", "English", "Eng 101",  "author_4",  "not available",  "1/8/2010" ,  "1/8/2010" ],
#         ["99","1006", "Math", "Simple Math",  "author_3",  "not available",  "1/8/2010" ,  "1/8/2010" ],
#         ["93","1007", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
#     ]

#     logTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Loan Availability  ", "  Checkout Date  "  , "  Return Date  "]
#     insert(logFilePath ,logList, logTableHeader,"Logs")

