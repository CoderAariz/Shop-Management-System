from tkinter import *
from tkinter import messagebox
import mysql.connector
try:
    con=mysql.connector.connect(user='root',password='coolbuddy',database='shop_management',host='localhost')
    cur=con.cursor()

    def register():
        register_screen=Toplevel(top,cursor='arrow')
        register_screen.title('New Registration')
        register_screen.geometry('400x300')
        Label(register_screen, text="Please enter the details below", fg="green").pack()
        Label(register_screen, text="").pack()
        reg_name=Label(register_screen,text='UserName:')
        reg_name.pack()
        global reg_name_ent
        reg_name_ent=Entry(register_screen)
        reg_name_ent.pack()
        reg_pas=Label(register_screen,text='Password:')
        reg_pas.pack()
        global reg_pas_ent
        reg_pas_ent=Entry(register_screen,show='*')
        reg_pas_ent.pack()
        Label(register_screen, text="").pack()
        regbtn=Button(register_screen,text='Register',command=registration,bg='yellow',width=10,height=1,padx=3,pady=3)
        regbtn.pack() 
        register_screen.mainloop()

    def registration():
        global new_user
        new_user=reg_name_ent.get()
        global new_password
        new_password=reg_pas_ent.get()
        user_info=(new_user,new_password)
        add_user=("INSERT INTO login (username,password) VALUES (%s, %s)")
        cur.execute(add_user,user_info)
        con.commit()
        messagebox.showinfo('Registration','Registration successful.',)

    def login():
        try:
            loaduser=("select * from login where username= %s")
            user=(name_ent.get(),)
            password=pas_ent.get()
            cur.execute(loaduser,user)
            usercheck=cur.fetchall()
            u=usercheck[0][0]
            p=usercheck[0][1]
            if user[0]==u and password==p:
                initial()
            else:
                messagebox.showerror('Error','Username or Password is incorrect.Please try again.')
        except:
            messagebox.showerror('Error','There is an error in connection.')

    def initial():
        initial_screen=Toplevel(top)
        initial_screen.title('Welcome')
        initial_screen.geometry('400x300')
        Label(initial_screen,text='Welcome to Shop Management System').pack()
        search_btn=Button(initial_screen,text='Search',height=3,width=7,bg='yellow',command=search)
        search_btn.pack()
        Label(initial_screen,text="").pack()
        bill_btn=Button(initial_screen,text='Billing',height=3,width=7,bg='yellow',command=bill)
        bill_btn.pack()
        Label(initial_screen,text="").pack()
        exit_btn=Button(initial_screen,text='Kill Switch',height=3,width=7,bg='yellow',command=exit)
        exit_btn.pack()
        initial_screen.mainloop()

    def bill():
            bill_screen=Toplevel(top)
            bill_screen.title('Bill Generation')
            bill_screen.geometry('400x300')
            cst_name=Label(bill_screen,text='Customer Name:')
            cst_name.grid(row=0,column=0)
            cst_name_ent=Entry(bill_screen)
            cst_name_ent.grid(row=0,column=1)
            cst_add=Label(bill_screen,text='Address:')
            cst_add.grid(row=1,column=0)
            cst_add_ent=Entry(bill_screen)
            cst_add_ent.grid(row=1,column=1)
            cst_mob=Label(bill_screen,text='Mobile no.:')
            cst_mob.grid(row=2,column=0)
            cst_mob_ent=Entry(bill_screen)
            cst_mob_ent.grid(row=2,column=1)
            pn=Label(bill_screen,text='Enter No. of products:')
            pn.grid(row=3,column=0)
            pn_ent=Entry(bill_screen)
            pn_ent.grid(row=3,column=1)
            pn_no=int(pn_ent.get())
            for i in range(1,(pn_no+1)):
                product=Label(bill_screen,text='Product Name:')
                product.pack()
            bill_screen.mainloop()

    def search():
        search=Toplevel(top)
        search.geometry('400x300')
        product=Label(search,text='Product Name')
        product.grid(row=0,column=0)
        global product_e
        product_e=Entry(search)
        product_e.grid(row=0,column=1)
        search_btn=Button(search,text='Search',height=1,width=5,bg='yellow',command=prdct_search)
        search_btn.grid(row=1,column=0)
        search.mainloop()

    def prdct_search():
        try:
            search_screen=Toplevel(top)
            search_screen.geometry('400x300')
            prd=(product_e.get(),)
            searchproduct=("select * from product where name=%s")
            cur.execute(searchproduct,prd)
            prdct=cur.fetchall()
            Label(search_screen,text='Product').grid(row=0,column=0)
            Label(search_screen,text='Price').grid(row=0,column=2)
            Label(search_screen,text=prdct[0][0]).grid(row=2,column=0)
            Label(search_screen,text=prdct[0][1]).grid(row=2,column=2)
            search_screen.mainloop()
        except:
            messagebox.showerror('Error','searching failed.')

    top=Tk(screenName='Aariz',baseName='shopping',className=' ',useTk=1)
    top.geometry('400x300')
    top.title('Shop Management System')
    Label(top,text='Login to continue..').pack()
    Label(text=' ').pack()
    Label(text=' ').pack()
    name_l=Label(top,text='UserName:')
    name_l.pack()
    global name_ent
    name_ent=Entry(top)
    name_ent.pack()
    Label(text=' ').pack()
    pas_l=Label(top,text='Password:')
    pas_l.pack()
    global pas_ent
    pas_ent=Entry(top,show='*')
    pas_ent.pack()
    Label(text=' ').pack()
    log_btn=Button(top,text='Login',activebackground='blue',activeforeground='green',bg='yellow',width=10,height=1,padx=3,pady=3,command=login)
    log_btn.pack()
    Label(text=' ').pack()
    reg_l=Label(top,text='New user? Register here.')
    reg_l.pack()
    reg_btn=Button(top,text='Register',height=1,width=10,bg='yellow',activebackground='blue',activeforeground='green',padx=3,pady=3,command=register)
    reg_btn.pack()
    top.mainloop()
except:
    messagebox.showerror('Error','Sorry an error occured in connection.')
finally:
    cur.close()
    con.close()
