from modules.bookSearch import * 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 


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
        # elif searchMemberID(item[0])==0 and type == "Members":
        #    print(s)
        #    f.write(s)
        #    f.write('\n')
        #    print(nice_horizontal_rule)
        # elif  type == "Logs":
        #    print(s)
        #    f.write(s)
        #    f.write('\n')
        #    print(nice_horizontal_rule)
        else: 
           status = "Book ID already exists!" 
           
     

      return status
# --------------------------------insert---------------------------------------- #

# --------------------------------update---------------------------------------- #
def update(ID,oldStatus,newStatus):
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
        
        
        with open(logFilePath, 'w') as fw:
            for line in lines:
                # line.lower()
                # check if string present on a current line
                id = line[0:20]
                if id.find(ID) != -1 and line.index != 0:
                    # templine = line
                    # line = line. strip('\n')
                    fw.write(line.replace(oldStatus,newStatus))
                    # fw.write('\n')
                else: 
                   fw.write(line)
                #    fw.write('\n')
                

    return loanAvilabilityStatus  
# --------------------------------update---------------------------------------- #


