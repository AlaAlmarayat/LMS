
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
# from database import *  
from tkinter import messagebox 
from tkinter import ttk

ws = Tk()                       
ws.title("Python Guides")        
ws.geometry("750x700+400+50")  
ws.resizable(0, 0)            
# view_window      





def show():
    ws_ent.delete(0, END)     
    ws_ent.focus()
    treeview.selection()
    conn = None
    try:
         print("data")
    except Exception as e:
        print("error")
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
def search():
    treeview.selection()
    fetchdata = treeview.get_children()
    for f in fetchdata:
        treeview.delete(f)
    conn = None
    try:
        print("search data")
            
    except Exception as e:
        print("error search")

    finally:
        if conn is not None:
            conn.close()
def reset():
    show()  



scrollbarx = Scrollbar(ws, orient=HORIZONTAL)  
scrollbary = Scrollbar(ws, orient=VERTICAL)    
treeview = ttk.Treeview(ws, columns=("rollno", "name"), show='headings', height=22)  
treeview.pack()
treeview.heading('rollno', text="Roll No", anchor=CENTER)
treeview.column("rollno", stretch=NO, width = 100) 
treeview.heading('name', text="Name", anchor=CENTER)
treeview.column("name", stretch=NO)
scrollbary.config(command=treeview.yview)
scrollbary.place(x = 526, y = 7)
scrollbarx.config(command=treeview.xview)
scrollbarx.place(x = 220, y = 460)
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")


ws_lbl = Label(ws, text = "Name", font=('calibri', 12, 'normal'))
ws_lbl.place(x = 290, y = 518)
ws_ent = Entry(ws,  width = 20, font=('Arial', 15, 'bold'))
ws_ent.place(x = 220, y = 540)
ws_btn1 = Button(ws, text = 'Search',  width = 8, font=('calibri', 12, 'normal'), command = search)
ws_btn1.place(x = 480, y = 540)
ws_btn2 = Button(ws, text = 'Reset',  width = 8, font=('calibri', 12, 'normal'), command = reset)
ws_btn2.place(x = 600, y = 540)


show()  
ws.mainloop()