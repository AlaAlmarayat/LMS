

bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'

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

# --------------------------------searchLogID---------------------------------------- #
def searchLogID(ID):    
    """
    search book log by ID\n
    Book ID as an argument (int)\n
    return status 0 if not exist | 1 if exist 
    """
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
    search book log by ID\n
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

        for line in lines:
            # line.lower()
            # check if string present on a current line
            line = line[0:20]
            if line.find(ID) != -1:
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

        for line in lines:
            # line.lower()
            # check if string present on a current line
            id = line[0:14]
            if id.find(ID) != -1 and line.index != 0:
                # templine = line
                # line = line. strip('\n')
                searchResult=line.split("|")
                # fw.write('\n') 
                

    return searchResult  
# --------------------------------update---------------------------------------- #
