from database import *
from modules.bookSearch import *

transactionHistoryTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Loan Availability  "]


bookInfoFilePath ='.\\files\\Book_Info.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'
logFilePath ='.\\files\\logfile.txt'

def addTransactionHistoryRecord (ID):
    global bookID,memberID,genre,title, Author,purchasePrice,loanAvailability 

    bookInfo = getBookByID(bookInfoFilePath,ID)
    bookLogInfo = getBookByID(logFilePath,ID)
    
    print(bookInfo)
    print(bookLogInfo)
    transactionHistory = [[bookInfo[1],bookLogInfo[2],bookInfo[2],bookInfo[3],bookInfo[4],bookInfo[5],bookLogInfo[6]]]
     
    insert(bookTransactionHistoryFilePath ,transactionHistory, transactionHistoryTableHeader,"History") 

      