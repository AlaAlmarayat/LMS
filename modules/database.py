# from modules.bookSearch import * 
from tkinter import * 
from datetime import datetime

bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'

transactionHistoryTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Loan Availability  "]


def addTransactionHistoryRecord (ID):
    global bookID,memberID,genre,title, Author,purchasePrice,loanAvailability 

    bookInfo = getBookByID(bookInfoFilePath,ID)
    bookLogInfo = getBookByID(logFilePath,ID)
    
    print(bookInfo)
    print(bookLogInfo)
    transactionHistory = [[bookInfo[1],bookLogInfo[2],bookInfo[2],bookInfo[3],bookInfo[4],bookInfo[5],bookLogInfo[6]]]
     
    insert(bookTransactionHistoryFilePath ,transactionHistory, transactionHistoryTableHeader,"History") 

def selectTopGenres(logFilePath):
    return getTopGenres(logFilePath)     

# --------------------------------searchLogID---------------------------------------- #
def getBookStatusByID(ID):    
    """
    search log by ID and get avilability status\n
    Book ID as an argument (int)\n
    return status 0 if not exist | 1 if exist 
    """
    # title.lower()
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        templist = []
        resultList = []
        
       
        for line in lines[1:]:
            # line.lower()
            # check if string present on a current line
            # id = line[0:14]
            templist  = line.split("|")
            id = str(templist[1]).replace(" ","")
            fileId = int(id  )
            ID = int(ID)

            if fileId == ID and line.index != 0:
            # if id.find(ID) != -1 and line.index != 0:
                line = line.replace(" ","")
                resultList  = line.split("|")
                loanAvilabilityStatus= resultList[6]
                

    return loanAvilabilityStatus   
# --------------------------------searchLogID---------------------------------------- #

# --------------------------------searchTitleLog---------------------------------------- #
def searchTitleLog(title):
    """
    search book log by title\n
    title as an 1st argument (string)\n
    return list of books
    """
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
            templist2  = line.split("|")
            lineTitle = str(templist2[4]).replace(" ","").lower()
            fileTitle = title.lower()
            # ID = int(ID)

            # if fileId == ID and line.index != 0:
                
            if lineTitle.find(fileTitle) != -1 and lines.index != 0:
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
# --------------------------------searchTitleLog---------------------------------------- #

# --------------------------------returnAllTitleLog---------------------------------------- #
def returnAllTitleLog():
    """
    get all book log data\n
    return all book log data
    """
     
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
# --------------------------------returnAllTitleLog---------------------------------------- #

# --------------------------------searchTitle---------------------------------------- #
def searchTitle(title):
    """
    search book by title\n
    title as an 1st argument (string)\n
    return list of books
    """
    # title.lower()
    with open(bookInfoFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines:
            # line.lower()
            # check if string present on a current line
            if line.find(title) != -1:
                print( line)
                status = 1
                # break
        if status == 0: 
           print('No Results Found')
# --------------------------------returnAllTitleLog---------------------------------------- #

# --------------------------------searchID---------------------------------------- #
def searchID(filepath,ID):
    """
    search by ID\n
    Book ID as an 1st argument (int)\n
    return list of books
    """
    # title.lower()
    with open(filepath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        global status
        status = 0
        searchResult = []
        lineNumber = 0

        for line in lines:
            templist = []

            if lineNumber == 0:  
                id = line[0:20]
                if id.find(ID) != -1 and line.index != 0:
                    status = 1
                    searchResult=line.split("|")
                    break 
            else:
                templist  = line.split("|")
                id = str(templist[1]).replace(" ","")
                fileId = int(id  )
                ID = int(ID)

                if fileId == ID and line.index != 0:
                    # print(id, 'string exists in file')
                    # print('Line Number:', lines.index(line))
                    # print('Line:', line)
                    status = 1
                    searchResult=line.split("|")
                    break
                    # break

    return searchResult
# --------------------------------searchID---------------------------------------- #

def getSearchStatus(filepath,ID):
    global status
    searchID(filepath,ID)

    return status

# --------------------------------update---------------------------------------- #
def getBookByID(filePath,ID):
    """
    get Book By ID\n
    Book ID as an 1st argument (int)\n
    return book details
    """

    with open(filePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines() 

        for line in lines[1:]:
            # line.lower()
            # check if string present on a current line
            # id = line[0:14]
            templist2  = line.split("|")
            id = str(templist2[1]).replace(" ","")
            fileId = int(id  )
            ID = int(ID)

            if fileId == ID and line.index != 0:
            # if id.find(ID) != -1 and line.index != 0:
                # templine = line
                # line = line. strip('\n')
                searchResult=line.split("|")
                # fw.write('\n') 
                

    return searchResult  
# --------------------------------update---------------------------------------- #

# --------------------------------insert---------------------------------------- #
def insert(filePath,listItems, listTableHeader,type):
    """
    insert data into different files (database)\n
    File Path as an 1st argument (sting)\n
    List of Items as an 2nd argument (sting)\n
    TableHeader as an 3rd argument (sting)\n
    Data Type as an 4th argument (sting)\n
    return status of insert
    """

    num_cols = len(listTableHeader)
    header_row = "| "+ " | ".join(listTableHeader) + " |"
    nice_horizontal_rule = ("|" + "-" * (len(header_row)-2)+"|")
    print(nice_horizontal_rule)
    print(header_row)
    print(nice_horizontal_rule)
    status =""
    
    with open(filePath, 'a') as f:
      
    #   searchID(filePath,listTableHeader[0]) 
      if getSearchStatus(filePath,listTableHeader[0]) == 0:
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
        

        if getSearchStatus(filePath,item[0]) == 0 and type != "History":
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        elif type == "History":  
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        else: 
           status = "Book ID already exists!" 
           
     

      return status
# --------------------------------insert---------------------------------------- #

# --------------------------------update---------------------------------------- #
def update(ID,memberId, dateToUpdate,newStatus):
    """
    update book log by ID\n
    Book ID as an 1st argument (int)\n
    oldStatus as an 2nd argument (sting)\n
    newStatus as an 3rd argument (sting)\n
    return status Loan Avilability Status
    """

    # title.lower()
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        lineNumber = 0
        
        # newvalues = [[]]
        templist = []
        headerList = []

        with open(logFilePath, 'w') as fw:
            
            for line in lines:
                # line.lower()
                # check if string present on a current line
                if lineNumber == 0:
                    # line = line.strip()            
                    headerList  = line.split("|") 
                    headerList.pop(0)
                    headerList.pop(len(templist)-1) 
                    lineNumber += 1
                    fw.write(line)
                else:
                    templist2  = line.split("|")
                    id = str(templist2[1]).replace(" ","")
                    fileId = int(id  )
                    ID = int(ID)
                    if fileId == ID and line.index != 0:

                        # line = line.strip()
                        # line = line.replace(" ","")            
                        templist  = line.split("|")    
                        templist[2] = memberId 
                        templist[6] = newStatus 
                        currentDate = str(datetime.today().strftime('%d/%m/%Y'))
                        # currentDate = " " + currentDate + " "*len(currentDate)
                        templist[dateToUpdate] = currentDate 

                        templist.pop(0)
                        templist.pop(len(templist)-1) 

                        # newvalues.append(newvalues)
                        
                        numCol = len(headerList)

                        # for item in templist:
                        # # writing each row to a string,
                        # # then printing the string, is better for performance:)
                        
                        s = "|"
                        for i in range(numCol):
                            entry = str(templist[i])

                            s += (entry+ " "*(len(headerList[i]) - len(entry)+1)+ "|")

                        fw.write(s)
                        fw.write('\n')
                    else: 
                        fw.write(line)
                

    return loanAvilabilityStatus  
# --------------------------------update---------------------------------------- #

# --------------------------------searchLogID---------------------------------------- #
def getTopGenres(logFilePath):    
    """
    search log by ID and get avilability status\n
    Book ID as an argument (int)\n
    return status 0 if not exist | 1 if exist 
    """
    with open(logFilePath, 'r') as fp:
        
        text = fp.readlines()
        # Create an empty dictionary
        genreDictionary = dict()
        
        
        # Loop through each line of the file
        for line in text[1:]:
            # Remove the leading spaces and newline character
            line = line.strip()
            line = line.replace(" ","")            
            templist  = line.split("|")            
            genre = templist[3]
            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = genre.lower()
        
            # Split the line into words
            words = line.split(" ")
        
            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in genreDictionary:
                    # Increment count of word by 1
                    genreDictionary[word] = genreDictionary[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    genreDictionary[word] = 1
              

    return genreDictionary  
# --------------------------------searchLogID---------------------------------------- #
