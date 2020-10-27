from tkinter import *
def start_game(args):
        main_window1.destroy()
        if args == 1:
            import GEUSSWORD
            GEUSSWORD.main()
        elif args == 2:
            import picturegame
            picturegame.main()
        
def option():
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
option()
