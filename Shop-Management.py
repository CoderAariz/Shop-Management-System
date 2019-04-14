from tkinter import *
from tkinter import messagebox
import mysql.connector
try:
    con=mysql.connector.connect(user='root',password='coolbuddy',database='shop_management',host='localhost')
    cur=con.cursor()

    def register():
        global register_screen
        register_screen=Toplevel(top,cursor='arrow')
        register_screen.title('New Registration')
        register_screen.geometry('600x600')
        register_screen.configure(background='light blue')
        Label(register_screen, text="Please enter the details below", fg="green",font='Times 20 bold',background='light blue').pack()
        Label(register_screen, text="",background='light blue').pack()
        reg_name=Label(register_screen,text='UserName:',background='light blue',font='Calibiri 14 bold')
        reg_name.pack()
        global reg_name_ent
        reg_name_ent=Entry(register_screen)
        reg_name_ent.pack()
        reg_pas=Label(register_screen,text='Password:',background='light blue',font='Calibiri 14 bold')
        reg_pas.pack()
        global reg_pas_ent
        reg_pas_ent=Entry(register_screen,show='*')
        reg_pas_ent.pack()
        Label(register_screen, text="",background='light blue').pack()
        regbtn=Button(register_screen,text='Register',command=registration,bg='yellow',width=10,height=1,padx=3,pady=3)
        regbtn.pack() 
        register_screen.mainloop()

    def registration():
        global new_user
        new_user=reg_name_ent.get()
        global new_password
        new_password=reg_pas_ent.get()
        register_screen.destroy()
        user_info=(new_user,new_password)
        add_user=("INSERT INTO login (username,password) VALUES (%s, %s)")
        cur.execute(add_user,user_info)
        con.commit()
        messagebox.showinfo('Registration','Registration successful.',)
        initial()

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
        global initial_screen
        initial_screen=Toplevel(top)
        initial_screen.configure(background='light blue')
        initial_screen.title('Welcome')
        initial_screen.geometry('600x600')
        Label(initial_screen,text='Welcome to Shop Management System',font='Times 20 bold ',background='light blue',foreground='black').pack()
        Label(initial_screen,text="",background='light blue').pack()
        Label(initial_screen,text="",background='light blue').pack()
        Label(initial_screen,text="",background='light blue').pack()
        search_btn=Button(initial_screen,text='Search',height=2,width=10,bg='yellow',command=search,font='Calibiri 14 bold')
        search_btn.pack()
        Label(initial_screen,text="",background='light blue').pack()
        Label(initial_screen,text="",background='light blue').pack()
        bill_btn=Button(initial_screen,text='Billing',height=2,width=10,bg='yellow',command=bill,font='Calibiri 14 bold')
        bill_btn.pack()
        Label(initial_screen,text="",background='light blue').pack()
        Label(initial_screen,text="",background='light blue').pack()
        exit_btn=Button(initial_screen,text='Kill Switch',height=2,width=10,bg='yellow',command=exit,font='Calibiri 14 bold')
        exit_btn.pack()
        initial_screen.mainloop()

    def bill():
            initial_screen.destroy()
            global bill_screen
            bill_screen=Toplevel(top)
            bill_screen.title('Bill Generation')
            bill_screen.geometry('600x600')
            bill_screen.configure(background='light blue')
            cst_name=Label(bill_screen,text='Customer Name:',background='light blue')
            cst_name.grid(row=1,column=0)
            cst_name_ent=Entry(bill_screen)
            cst_name_ent.grid(row=1,column=1)
            cst_add=Label(bill_screen,text='Address:',background='light blue')
            cst_add.grid(row=3,column=0)
            cst_add_ent=Entry(bill_screen)
            cst_add_ent.grid(row=3,column=1)
            cst_mob=Label(bill_screen,text='Mobile no.:',background='light blue')
            cst_mob.grid(row=5,column=0)
            cst_mob_ent=Entry(bill_screen)
            cst_mob_ent.grid(row=5,column=1)
            Label(bill_screen,text='Product Name:',background='light blue').grid(row=7,column=0)
            p1=Entry(bill_screen).grid(row=7,column=1)
            Label(bill_screen,text='Price:',background='light blue').grid(row=7,column=2)
            p11=Entry(bill_screen).grid(row=7,column=3)
            Label(bill_screen,text='Product Name:',background='light blue').grid(row=9,column=0)
            p2=Entry(bill_screen).grid(row=9,column=1)
            Label(bill_screen,text='Price:',background='light blue').grid(row=9,column=2)
            p22=Entry(bill_screen).grid(row=9,column=3)
            Label(bill_screen,text='Product Name:',background='light blue').grid(row=11,column=0)
            p3=Entry(bill_screen).grid(row=11,column=1)
            Label(bill_screen,text='Price:',background='light blue').grid(row=11,column=2)
            p33=Entry(bill_screen).grid(row=11,column=3)
            Label(bill_screen,text='Product Name:',background='light blue').grid(row=13,column=0)
            p4=Entry(bill_screen).grid(row=13,column=1)
            Label(bill_screen,text='Price:',background='light blue').grid(row=13,column=2)
            p44=Entry(bill_screen).grid(row=13,column=3)
            Label(bill_screen,text='Product Name:',background='light blue').grid(row=15,column=0)
            p5=Entry(bill_screen).grid(row=15,column=1)
            Label(bill_screen,text='Price:',background='light blue').grid(row=15,column=2)
            p55=Entry(bill_screen).grid(row=15,column=3)
            print=Button(bill_screen,text='Print Bill',bg='yellow',width=10,height=1,padx=3,pady=3).grid(row=25,column=2)
            bill_screen.mainloop()

    def search():
        initial_screen.destroy()
        global search
        search=Toplevel(top)
        search.geometry('800x600')
        search.configure(background='light blue')
        Label(search,background='light blue',text='Enter the product name to search the product',font='Times 24 bold').pack()
        Label(search,text=' ',background='light blue').pack()
        Label(search,text=' ',background='light blue').pack()
        product=Label(search,text='Product Name',background='light blue',font='Times 20 bold')
        product.pack()
        Label(search,text=' ',background='light blue').pack()
        Label(search,text=' ',background='light blue').pack()
        global product_e
        product_e=Entry(search)
        product_e.pack()
        Label(search,text=' ',background='light blue').pack()
        Label(search,text=' ',background='light blue').pack()
        search_btn=Button(search,text='Search',height=1,width=9,bg='yellow',font='calibiri 10 bold',command=prdct_search)
        search_btn.pack()
        search.mainloop()

    def prdct_search():
        try:
            global search_screen
            search_screen=Toplevel(top)
            search_screen.geometry('600x600')
            search_screen.configure(background='light blue')
            prd=(product_e.get(),)
            search.destroy()
            Label(search_screen,background='light blue',text='Product details',font='Times 20 bold').place(x=40,y=20)
            searchproduct=("select * from product where name=%s")
            cur.execute(searchproduct,prd)
            prdct=cur.fetchall()
            Label(search_screen,text='Product',background='light blue').grid(row=0,column=0)
            Label(search_screen,text='Price',background='light blue').grid(row=0,column=2)
            Label(search_screen,text=prdct[0][0],background='light blue').grid(row=2,column=0)
            Label(search_screen,text=prdct[0][1],background='light blue').grid(row=2,column=2)
            search_screen.mainloop()
        except:
            messagebox.showerror('Error','searching failed.')

    global top
    top=Tk(screenName='Aariz',baseName='shopping',className=' ',useTk=1)
    top.geometry('600x600')
    top.configure(background='light blue')
    top.title('Shop Management System')
    Label(top,text='Login to continue..',background='light blue',foreground='black',font='Georgia 18 bold underline').pack()
    Label(text=' ',background='light blue').pack()
    Label(text=' ',background='light blue').pack()
    name_l=Label(top,text='UserName:',background='light blue',font='Calibiri 14 bold')
    name_l.pack()
    global name_ent
    name_ent=Entry(top)
    name_ent.pack()
    Label(text=' ',background='light blue').pack()
    pas_l=Label(top,text='Password:',background='light blue',font='Calibiri 14 bold',foreground='black')
    pas_l.pack()
    global pas_ent
    pas_ent=Entry(top,show='*')
    pas_ent.pack()
    Label(text=' ',background='light blue').pack()
    log_btn=Button(top,text='Login',activebackground='blue',activeforeground='green',bg='yellow',width=16,height=1,padx=3,pady=3,command=login,font='Calibiri 9 bold')
    log_btn.pack()
    Label(text=' ',background='light blue').pack()
    reg_l=Label(top,text='New user? Register here.',background='light blue',font='Calibiri 14 bold')
    reg_l.pack()
    reg_btn=Button(top,text='Register',height=1,width=16,bg='yellow',activebackground='blue',activeforeground='green',padx=3,pady=3,command=register,font='Calibiri 9 bold')
    reg_btn.pack()
    top.mainloop()
except:
    messagebox.showerror('Error','Sorry an error occured in connection.')
finally:
    cur.close()
    con.close()
