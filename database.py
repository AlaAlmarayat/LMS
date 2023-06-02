from modules.bookSearch import * 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
from datetime import datetime

bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'


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
        status = 0
        
        # newvalues = [[]]
        templist = []
        with open(logFilePath, 'w') as fw:
            for line in lines:
                # line.lower()
                # check if string present on a current line
                id = line[0:20]
                if id.find(ID) != -1 and line.index != 0:
                    # templine = line
                    # line = line. strip('\n')

                    line = line.strip()
                    # line = line.replace(" ","")            
                    templist  = line.split("|")    
                    templist[2] = memberId 
                    templist[6] = newStatus 
                    currentDate = str(datetime.today().strftime('%d/%m/%Y'))
                    currentDate = " " + currentDate + " "*len(currentDate)
                    templist[dateToUpdate] = currentDate 

                    templist.pop(0)
                    templist.pop(len(templist)-1) 

                    # newvalues.append(newvalues)
                    
                    numCol = len(templist)

                    # for item in templist:
                    # # writing each row to a string,
                    # # then printing the string, is better for performance:)
                    
                    s = "|"
                    for i in range(numCol):
                        entry = str(templist[i])

                        listLen = len(templist[i])
                        if listLen == 0:
                            listLen = 10
                        s += (entry+ " "*(listLen - len(entry)-2)+ "|")

                    fw.write(s)
                    fw.write('\n')
                else: 
                   fw.write(line)
                #    fw.write('\n')
                

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
