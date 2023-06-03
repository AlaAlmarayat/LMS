from tkinter import *

from modules.addBook import addBookPage
from modules.bookCheckout import bookCheckoutPage
from modules.bookReturn import returnBookPage
from modules.bookSearch import searchPage
from modules.bookSelect import bookSelectPage
from modules.design import background, bigButton


# --------------------------------mainPage---------------------------------------- #

def mainPage():
    """
    generate main page 
    """

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x800")
    
    background(root,"Library Management System")

    bigButton(root,"Book Search",searchPage ,0.28 ,0.4 ,0.45 ,0.1)
    bigButton(root,"Book Checkout",bookCheckoutPage ,0.28 ,0.5 ,0.45 ,0.1)
    bigButton(root,"Book Return",returnBookPage ,0.28 ,0.6 ,0.45 ,0.1)
    bigButton(root,"Book Select",bookSelectPage ,0.28 ,0.7 ,0.45 ,0.1)
    bigButton(root,"Add Book",addBookPage ,0.28 ,0.8 ,0.45 ,0.1)

    root.mainloop()
# --------------------------------mainPage---------------------------------------- #

mainPage()