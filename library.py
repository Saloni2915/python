#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import customtkinter as ct
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector import Error
from tkinter import ttk


# In[2]:


class LMS:
    def __init__(self,root):
        global img2,f1
        self.root=root
        self.root.geometry(f"{1000}x{1100}")
        self.root.config(bg="black")
        self.root.title("Library management system")
        
        
        f1=Frame(root,width=1500,height=1000,bg="#2C555E")
        f1.pack(padx=20,pady=20)

        img1=Image.open(r"C:\Users\Ruchika soni\Downloads\lib.webp")
        img2=ImageTk.PhotoImage(img1)
        l1 = Label(f1,image=img2,height=1000,width=800)
        l1.place(x=0,y=0)

        l1=Label(f1,text="Welcome to \n newfair Library",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#EB7900")
        l1.place(relx=0.13,rely=0.2, relwidth=0.3, relheight=0.15)

        btn1 = Button(f1,text="Add Book Details",bg='black', fg='white',command=self.addbook)
        btn1.place(relx=0.16,rely=0.4, relwidth=0.25,relheight=0.1)

        btn2 = Button(f1,text="Delete Book",bg='black', fg='white',command=self.deletebook)
        btn2.place(relx=0.16,rely=0.5, relwidth=0.25,relheight=0.1)

        btn3 = Button(f1,text="View Book List",bg='black', fg='white',command=self.viewbook)
        btn3.place(relx=0.16,rely=0.6, relwidth=0.25,relheight=0.1)

        btn4 = Button(f1,text="Issue Book to Student",bg='black', fg='white',command=self.issuebook)
        btn4.place(relx=0.16,rely=0.7, relwidth=0.25,relheight=0.1)

        btn5 = Button(f1,text="Return Book",bg='black', fg='white',command=self.returnbook)
        btn5.place(relx=0.16,rely=0.8, relwidth=0.25,relheight=0.1)

        
    def registerbook(self):
        global e1
        book_id=e1.get()
        book_title=e2.get()
        book_author=e3.get()
        status=e4.get()
        
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        
     
    def addbook(self):
        global f2,e1,e2,e3,e4,e5,listbox
    
        f1.destroy()
    
   
        f2=Frame(self.root,width=800,height=750,bg="#1E3D13")
        f2.place(x=10,y=20)
        
        labelFrame = Frame(f2,bg='black')
        labelFrame.place(relx=0.12,rely=0.4,relwidth=0.8,relheight=0.3)
        
        
        l2=Label(f2,text="Add Books",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#498138")
        l2.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.15)

  
        # Book ID

        l21 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
        l21.place(relx=0.05,rely=0.1, relheight=0.08)

        e1 = Entry(labelFrame)
        e1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)

        # Title
        l22 = Label(labelFrame,text="Title : ", bg='black', fg='white')
        l22.place(relx=0.05,rely=0.3, relheight=0.08)

        e2 = Entry(labelFrame)
        e2.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

        # Book Author
        l23 = Label(labelFrame,text="Author : ", bg='black', fg='white')
        l23.place(relx=0.05,rely=0.5, relheight=0.08)

        e3 = Entry(labelFrame)
        e3.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

        # Book Status
        l24 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
        l24.place(relx=0.05,rely=0.7, relheight=0.08)

        e4 = Entry(labelFrame)
        e4.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)


        SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=self.registerbook)
        SubmitBtn.place(relx=0.10,rely=0.85, relwidth=0.15,relheight=0.08)

        quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
        quitBtn.place(relx=0.30,rely=0.85, relwidth=0.15,relheight=0.08)
        
        comboframe=Frame(self.root,width=700,height=700,bg="#3D083C")
        comboframe.place(x=820,y=20)
        
      
       
#         listbox=Listbox(comboframe,font=( "Time New Roman",30,"bold"),width=17,height=15)
#         listbox.pack(padx=10,pady=10)
        
#         listscrollbar=Scrollbar(listbox)
#         listscrollbar.place(side=RIGHT,fill=Y)
# #         Scrollbar.config(command=listbox.yview)
          
        
    def delebook(self):
        
        book_id=e5.get()
        e5.delete(0,END)
        
    def deletebook(self):
        global f3,e5
        
        f1.destroy()
   
        f3=Frame(root,width=1000,height=1000,bg="#3D083C")
        f3.pack(padx=20,pady=20)

        l3=Label(f3,text="Delete Book",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#A32F90")
        l3.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.15)

        labelFrame2 = Frame(f3,bg='black')
        labelFrame2.place(relx=0.15,rely=0.4,relwidth=0.8,relheight=0.4)

        # Book ID

        l31 = Label(labelFrame2,text="Book ID : ", bg='black', fg='white')
        l31.place(relx=0.05,rely=0.4, relheight=0.08)

        e5 = Entry(labelFrame2)
        e5.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)


        SubmitBtn2 = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=self.delebook)
        SubmitBtn2.place(relx=0.30,rely=0.85, relwidth=0.18,relheight=0.08)

        quitBtn2 = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
        quitBtn2.place(relx=0.55,rely=0.85, relwidth=0.18,relheight=0.08)
        
    def viewbook(self):
        global f4
        f1.destroy()

        f4=Frame(root,width=1000,height=1000,bg="#EF88BE")
        f4.pack(padx=20,pady=20)

        l4=Label(f4,text="View  Book",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#EA0976")
        l4.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.15)

        labelFrame3 = Frame(f4,bg='black')
        labelFrame3.place(relx=0.15,rely=0.4,relwidth=0.8,relheight=0.4)

        tree_view=ttk.Treeview(labelFrame3)
        tree_view.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

        my_columns=["Book_Id","Book_Title","Book_Author","Status"]

        tree_view.configure(columns=my_columns)

        tree_view.column("Book_Id",width=100,minwidth=50,anchor=CENTER)
        tree_view.column("Book_Title",width=100,minwidth=50,anchor=CENTER)
        tree_view.column("Book_Author",width=100,minwidth=50,anchor=CENTER)
        tree_view.column("Status",width=100,minwidth=50,anchor=CENTER)


        tree_view.heading("Book_Id",text="Book_Id")
        tree_view.heading("Book_Title",text="Book_Title",anchor=CENTER)
        tree_view.heading("Book_Author",text="Book_Author",anchor=CENTER)
        tree_view.heading("Status",text="Status",anchor=CENTER)
        tree_view["show"]="headings"


        SubmitBtn2 = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black')
        SubmitBtn2.place(relx=0.30,rely=0.85, relwidth=0.18,relheight=0.08)

        quitBtn2 = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
        quitBtn2.place(relx=0.55,rely=0.85, relwidth=0.18,relheight=0.08)
        
    def issue(self):
        book_id=e6.get()
        issuedto=e7.get()
        
        e6.delete(0,END)
        e7.delete(0,END)
        
    def issuebook(self):
        global f5,e6,e7
        f1.destroy()

        f5=Frame(root,width=1000,height=1000,bg="#173F3F")
        f5.pack(padx=20,pady=20)

        l5=Label(f5,text="Issue Book",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#2D7A7A")
        l5.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.15)

        labelFrame4 = Frame(f5,bg='black')
        labelFrame4.place(relx=0.15,rely=0.4,relwidth=0.8,relheight=0.4)


        l51 = Label(labelFrame4,text="Book ID :", bg='black', fg='white')
        l51.place(relx=0.05,rely=0.3, relheight=0.08)

        e6 = Entry(labelFrame4)
        e6.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)


        l52 = Label(labelFrame4,text="Issued to : ", bg='black', fg='white')
        l52.place(relx=0.05,rely=0.5, relheight=0.08)

        e7 = Entry(labelFrame4)
        e7.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

        SubmitBtn2 = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=self.issue)
        SubmitBtn2.place(relx=0.30,rely=0.85, relwidth=0.18,relheight=0.08)

        quitBtn2 = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
        quitBtn2.place(relx=0.55,rely=0.85, relwidth=0.18,relheight=0.08)

    def returnbook(self):
        global f6
    
        f1.destroy()

        f6=Frame(root,width=1000,height=1000,bg="#57005E")
        f6.pack(padx=20,pady=20)

        l6=Label(f6,text="Return Book",font=( "Time New Roman",30,"bold"),fg="white",bg="black",highlightthickness=5,highlightbackground="#9500A1")
        l6.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.15)

        labelFrame5 = Frame(f6,bg='black')
        labelFrame5.place(relx=0.15,rely=0.4,relwidth=0.8,relheight=0.4)

        # Book ID

        l61 = Label(labelFrame5,text="Book ID : ", bg='black', fg='white')
        l61.place(relx=0.05,rely=0.4, relheight=0.08)

        bookInfo8 = Entry(labelFrame5)
        bookInfo8.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)


        SubmitBtn2 = Button(root,text="Return",bg='#d1ccc0', fg='black')
        SubmitBtn2.place(relx=0.30,rely=0.85, relwidth=0.18,relheight=0.08)

        quitBtn2 = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
        quitBtn2.place(relx=0.55,rely=0.85, relwidth=0.18,relheight=0.08)


      
root=Tk()
c=LMS(root)
root.mainloop()


# In[ ]:





# In[ ]:




