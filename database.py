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
def insert(filePath,listItems, listTableHeader,type):
    num_cols = len(listTableHeader)
    header_row = "| "+ " | ".join(listTableHeader) + " |"
    nice_horizontal_rule = ("|" + "-" * (len(header_row)-2)+"|")
    print(nice_horizontal_rule)
    print(header_row)
    print(nice_horizontal_rule)

    
    with open(filePath, 'a') as f:
      
      if searchID(listTableHeader[0])==0 and type == "Books":
           f.write(header_row)
           f.write('\n')
     
      if searchMemberID(listTableHeader[0])==0 and type == "Members" :
           f.write(header_row)
           f.write('\n')
      
      if type == "Logs":
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
        print(s)

        if searchID(item[0])==0 and type == "Books":
           f.write(s)
           f.write('\n')

        if searchMemberID(item[0])==0 and type == "Members":
           f.write(s)
           f.write('\n')

        if type == "Logs":
           f.write(s)
           f.write('\n')
        
      print(nice_horizontal_rule)
# ------------------------------------------------------------------------ #


def addBooks():
    booksList = [
        ["1", "Sci-fi", "Stars",  "author_1",  "10",  "1/8/2010" ],
        ["2", "Fantacy", "Aliens?",  "author_2",  "10",  "1/2/2014" ],
        ["3", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],
        ["4", "English", "Eng 101",  "author_4",  "10",  "3/7/1999" ],
        ["5", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
        ["10", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
        ["100", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
        ["9", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
        ["88", "Novel", "Witcher",  "author_1",  "10",  "19/5/1993" ],
        ["44", "English", "Eng 101",  "author_4",  "10",  "3/7/1999" ],
        ["99", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],    
        ["93", "Math", "Simple Math",  "author_3",  "10",  "22/5/2000" ],
    ]

    booksTableHeader = ["    ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Purchase Date  "]
    insert(bookInfoFilePath ,booksList, booksTableHeader,"Books")

def addMembers():
    membersList = []

    for i in range(10): 
        number=str(1000+i)
        membersList.append(number)

    membersTableHeader = ["    ID    "]




    insert(membersFilePath ,membersList, membersTableHeader,"Members")


def addLog():
    logList = [
        ["1","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["2","1004", "Fantacy", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["3","1003", "Math", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["4","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["5","1003", "Novel", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["10","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["100","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["9","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["88","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["44","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["99","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["93","1003", "Sci-fi", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["93","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["88","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
        ["10","1003", "English", "Stars",  "author_1",  "Availabile",  "1/8/2010" ,  "1/8/2010" ],
    ]

    logTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Loan Availability  ", "  Checkout Date  "  , "  Return Date  "]
    insert(logFilePath ,logList, logTableHeader,"Logs")

addLog()
# def desgin():

#     global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
#     root = Tk()
#     root.title("Library")
#     root.minsize(width=400,height=400)
#     root.geometry("600x500")
   
#     cur = con.cursor()
#     # Enter Table Names here
#     bookTable = "books" # Book Table
#     Canvas1 = Canvas(root)
    
#     Canvas1.config(bg="#ff6e40")
#     Canvas1.pack(expand=True,fill=BOTH)
        
#     headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
#     headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
#     headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
#     headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#     labelFrame = Frame(root,bg='black')
#     labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
#     # Book ID
#     lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
#     lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
#     bookInfo1 = Entry(labelFrame)
#     bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
#     # Title
#     lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
#     lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
#     bookInfo2 = Entry(labelFrame)
#     bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
#     # Book Author
#     lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
#     lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
#     bookInfo3 = Entry(labelFrame)
#     bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
#     # Book Status
#     lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
#     lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
#     bookInfo4 = Entry(labelFrame)
#     bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
#     #Submit Button
#     SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=addBooks)
#     SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
#     quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
#     quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
#     root.mainloop()