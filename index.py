from tkinter import *
import mysql.connector


def start_main_page():
    def start_game(args):
        main_window1.destroy()
        if args == 1:
            import GEUSSWORD
            GEUSSWORD.main()
        elif args == 2:
            import picturegame
            picturegame.main()
        
    def option():
        Form.destroy()
        global main_window1
        main_window1=Tk()
        main_window1.title("GAME PAGE")
        main_window1.geometry("800x800")
        img=PhotoImage(file="option.png")
        l1=Label(main_window1,image=img).pack()
        lab_img1 = Button(l1,text="SELECT ONE OF THE FOLLOWING GAME",bg='purple',width=50,fg='white',borderwidth=8,justify='center',font=("Arial", 13),)
        sel_btn1 = Button(l1,text="WORDGAME",width=18,borderwidth=8,font=("", 18),fg="white",bg="purple",cursor="hand2",activebackground='yellow',command=lambda: start_game(1))
        sel_btn2 = Button(l1,text="PICTUREGAME",width=18,borderwidth=8,font=("", 18),fg="white",bg="purple",cursor="hand2",activebackground='yellow',command=lambda: start_game(2))
        lab_img1.place(x=150,y=50)
        sel_btn1.place(x=250,y=200)
        sel_btn2.place(x=250,y=400)
       
        main_window1.mainloop()



    def login():
        main_window.destroy()
        global Form
       
        Form=Tk()
        Form.geometry("600x600")
        global img
        img=PhotoImage(file="pa.png")
        l1=Label(Form,image=img).pack()
        
        mb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="veena123",
        database="LOGINMEMBER")
        mycursor.execute("CREATE DATABASE LOGINMEMBER")
        mycursor=mb.cursor()
        mycursor.execute("create table member(username VARCHAR(255),password VARCHAR(255))")
        
        lb1=Label(l1,text="PLEASE FILL YOUR DETAIL HERE *",fg="red",bg='#eddfdb',font=("bold",18)).place(x=120, y=20)
        lbl_username = Label(l1, text = "PLAYERNAME* :",bg='#e9e1d6' ,font=('arial', 14), bd=15)
        lbl_username.place(x=70,y=100)
        lbl_password = Label(l1, text = "PASSWORD*:",bg='#eddfdb' ,font=('arial', 14), bd=15)
        lbl_password.place(x=70,y=200)
        lbl_text = Label(l1,bg='#edd9a9',font=("bold",14))
        lbl_text.place(x=70,y=250)
        USERNAME = StringVar()
        PASSWORD = StringVar()
    
        username = Entry(l1, textvariable=USERNAME,borderwidth=8,width=15 ,font=('bold',18))
        username.place(x=250,y=100)
        password = Entry(l1, textvariable=PASSWORD,borderwidth=8, width=15,show="*", font=('bold',18))
        password.place(x=250,y=200)
        
        def insert():
           
            global v
            s="insert into member (username,password) values (%s,%s)"
            v=(USERNAME.get(),PASSWORD.get())
            mycursor.execute(s,v)
            mb.commit()
            
        def Login(event=None):
                if (USERNAME.get() == "" or PASSWORD.get() ==""):
                    lbl_text.config(text="Please complete the required field!", fg="red")
                else:
                    mycursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (USERNAME.get(), PASSWORD.get()))
                    x= mycursor.fetchall()
                    for i in x:
                        if  USERNAME.get()==i[0] and PASSWORD.get()==i[1]:
                            option()
                        else:
                            lbl_text.configure(text="Invalid username or password", fg="red")
                           
        
        btn_login = Button(l1, text="LOGIN",bg='green',borderwidth=8, width=10,font=("", 10), command=Login)
        btn_signup = Button(l1, text="SIGNUP",bg='green',borderwidth=8, command=insert,width=10,font=("", 10))
        btn_login.place(x=130,y=320)
        btn_signup.place(x=290,y=320)

        
    def show_option():
    
        start_btn.destroy()
        lab_img.destroy()
        login()
        
    global main_window
    main_window = Tk()

    main_window.geometry("800x800")
    main_window.resizable(0, 0)
    main_window.title("KIDS LEARNING GAME")
    main_window.configure(background="grey")
    

    img1 = PhotoImage(file="back.png")
    img=PhotoImage(file="kids.png")
    l1=Label(main_window,image=img).pack()
    lab_img = Label(l1,text="KIDS QUIZ",bg="#8c73ef",font=("georgia", 60))
    lab_img.place(x=200,y=0)
    start_btn = Button(l1,text="PLAY",width=18,borderwidth=8,fg="white",bg="purple",font=(" segoe script", 15),cursor="hand2",command=show_option)
    start_btn.place(x=300,y=500)
    
    main_window.mainloop()


start_main_page()
