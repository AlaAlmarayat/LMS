from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from database import *
from tkinter import messagebox 
from design import mainPage

mainPage()
# root = Tk()
# root.title("Library")
# root.minsize(width=400,height=400)
# root.geometry("900x800")

# same=True
# n=0.25
# # Adding a background image
# background_image =Image.open("lib.jpg")
# [imageSizeWidth, imageSizeHeight] = background_image.size
# newImageSizeWidth = int(imageSizeWidth*n)
# if same:
#     newImageSizeHeight = int(imageSizeHeight*n) 
# else:
#     newImageSizeHeight = int(imageSizeHeight/n) 
    
# background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(background_image)
# Canvas1 = Canvas(root)
# Canvas1.create_image(300,340,image = img)      
# Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
# Canvas1.pack(expand=True,fill=BOTH)

# headingFrame1 = Frame(root,bg="black",bd=5)
# headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
# headingLabel = Label(headingFrame1, text="Library Management System", bg='alice blue', fg='black', font=('Courier',15))
# headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# btn1 = Button(root,text="Book Search",bg='#dce1f5', fg='black')
# btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
# btn2 = Button(root,text="Book Checkout",bg='#dce1f5', fg='black' )
# btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
# btn3 = Button(root,text="Book Return",bg='#dce1f5', fg='black')
# btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
# btn4 = Button(root,text="Book Select",bg='#dce1f5', fg='black')
# btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
# btn5 = Button(root,text="Add Book",bg='#dce1f5', fg='black' )
# btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
# root.mainloop()