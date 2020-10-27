from tkinter import*
from tkinter import messagebox
import time
count=0
counts=0
def main():
    def back():
        my_window.destroy()
        import option
        
    def exit_fromhere():
          my_window.destroy()
          m1=Tk()
          m1.title("exitscreen")
          m1.geometry('800x800')
          img=PhotoImage(file="score.png")
          
          l1=Label(image=img).place(x=0,y=0)
          l0=Label(l1,text="YOUR SCORE CARD",font=('georgia',50)).place(x=100,y=100)
          l2=Label(l1,text="Your total score is :"+str(points),font=('georgia',30)).place(x=150,y=250)
          l3=Label(l1,text="Correct Answers:"+str(count),font=('georgia',30)).place(x=150,y=350)
          l4=Label(l1,text="Total number of questions visited:"+str(counts),font=('georgia',30)).place(x=100,y=450)
          m1.mainloop()
          exit
          
    global main_window
    global l100
    my_window = Tk()
    my_window.geometry("800x800")
    my_window.resizable(0, 0)
    my_window.title("KIDS LEARNING GAME")
    my_window.configure(background="light blue")
    img1 = PhotoImage(file="back.png")
    img2=PhotoImage(file='welcome.png')
    l100=Label(my_window,image=img2).place(x=0,y=0)
    global abc
    global abc1
    
    def abc():
        global points,count,counts
        points=points+5
        count+=1
        score.configure(text="Score:-"+str(points))
        messagebox.showinfo('option check','correct !!\n keep it up')
        
    def abc1():
        messagebox.showerror('option check','wrong !!\n better luck next time')
        
    def option():
        l0.destroy()
        q2()
        
    lab_img1 = Button(l100,image=img1,bg='grey',fg="red",border=0,justify='center',command=back)
    lab_img1.pack(anchor='nw', pady=10, padx=10)
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25
    global p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p38,p39,p40
    p1=PhotoImage(file="mango.png")
    p2=PhotoImage(file="apple1.png")
    p3=PhotoImage(file="orange.png")
    p4=PhotoImage(file="coconut.png")
    p5=PhotoImage(file="lion.png")
    p6=PhotoImage(file="jaguar.png")
    p7=PhotoImage(file="tiger.png")
    p8=PhotoImage(file="elephant.png")
    p9=PhotoImage(file="pecock.png")
    p10=PhotoImage(file="parrot.png")
    p11=PhotoImage(file="humming bird.png")
    p12=PhotoImage(file="woodcutter.png")
    p13=PhotoImage(file="eye.png")
    p14=PhotoImage(file="forehead.png")
    p15=PhotoImage(file="nose.png")
    p16=PhotoImage(file="hand.png")
    p18=PhotoImage(file="purple-suede.png")
    p19=PhotoImage(file="red.png")
    p20=PhotoImage(file="black.png")
    p21=PhotoImage(file="green.png")
    p22=PhotoImage(file="lion.png")
    p23=PhotoImage(file="jaguar.png")
    p24=PhotoImage(file="tiger.png")
    p25=PhotoImage(file="thank you.png")
    p26=PhotoImage(file="canada.png")
    p27=PhotoImage(file="england.png")
    p28=PhotoImage(file="india.png")
    p29=PhotoImage(file="japan.png")
    p30=PhotoImage(file="taj.png")
    p31=PhotoImage(file="agorkwat.png")
    p32=PhotoImage(file="eiffel tower.png")
    p33=PhotoImage(file="statue of liberty.png")
    p34=PhotoImage(file="train.png")
    p35=PhotoImage(file="bicycle.png")
    p36=PhotoImage(file="car.png")
    p38=PhotoImage(file="bus.png")
    p39=PhotoImage(file="califlower.png")
    p40=PhotoImage(file="egg plant.png")
    p41=PhotoImage(file="onion.png")
    p42=PhotoImage(file="ladyfinger.png")
   
    

    score = Label(l100,text="Score:- 0",pady=10,bg="yellow",fg="black",font="Titillium  14 bold")
    score.pack(anchor="ne")
    global points,counts
    points=0
    def q10():
        global b1,b2,b3,b4,l3,counts
        counts+=1
        l3=Label(l100,text="Choose National Bird of India from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p11,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p10,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p12,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p9,compound="c",command=abc)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l3.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=exit_fromhere,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q9():
        global b1,b2,b3,b4,l2,counts
        counts+=1
        l2=Label(l100,text="Choose  Egg Plant  from   given  option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p39,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p40,compound="c",command=abc)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p41,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p42,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l2.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q10,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q8():
        
        global b1,b2,b3,b4,l0,counts
        counts+=1
        l0=Label(l100,text="Choose  Bus  from  given  option.",fg='black',bg='yellow',font=('bold',20),width=35)
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p34,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p35,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p36,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p38,compound="c",command=abc)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l0.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q9,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q7():
        global b1,b2,b3,b4,l1,counts
        counts+=1
        l1=Label(l100,text="Choose Angkor wat temple from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p30,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p33,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p32,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p31,compound="c",command=abc)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l1.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q8,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q6():
        global b1,b2,b3,b4,l1,counts
        counts+=1
        l1=Label(l100,text="Choose flag of India  from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p26,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p27,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p28,compound="c",command=abc)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p29,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l1.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q7,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q5():
        global b1,b2,b3,b4,l1,counts
        counts+=1
        l1=Label(l100,text="Choose black color from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p18,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p19,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p20,compound="c",command=abc)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p21,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l1.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q6,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    def q4():
        l1.destroy()
        global b1,b2,b3,b4,l2,counts
        counts+=1
        l2=Label(l100,text="Choose  eye from  given  option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p13,compound="c",command=abc)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p14,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p15,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p16,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l2.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q5,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    
    def q3():
        global b1,b2,b3,b4,l1,counts
        counts+=1
        l1=Label(l100,text="Choose peacock from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p9,compound="c",command=abc)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p10,compound="c",command=abc1)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p11,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p12,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l1.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q4,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
        
    
    def q2():
        l0.destroy()
       
        global b1,b2,b3,b4,l1,counts
        counts+=1
        l1=Label(l100,text="Choose Apple from given option.",fg='black',bg='yellow',font=('bold',20))
        Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
        b1=Button(l100,image=p1,compound="c",command=abc1)
        Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
        b2=Button(l100,image=p2,compound="c",command=abc)
        Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
        b3=Button(l100,image=p3,compound="c",command=abc1)
        Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
        b4=Button(l100,image=p4,compound="c",command=abc1)
        b1.place(x=130,y=100)
        b2.place(x=430,y=100)
        b3.place(x=130,y=400)
        b4.place(x=430,y=400)
        l1.place(x=20,y=50)
        b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=q3,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
     
    points=0
    counts+=1
    l0=Label(l100,text="Choose Tiger from given option.",fg='black',bg='yellow',font=('bold',20))
    Label(l100,text="1).",fg="red",font=("bold",18)).place(x=100,y=100)
    b1=Button(l100,image=p5,compound="c",command=abc1)
    Label(l100,text="2).",fg="red",font=("bold",18)).place(x=400,y=100)
    b2=Button(l100,image=p6,compound="c",command=abc1)
    Label(l100,text="3).",fg="red",font=("bold",18)).place(x=100,y=400)
    b3=Button(l100,image=p7,compound="c",command=abc)
    Label(l100,text="4).",fg="red",font=("bold",18)).place(x=400,y=400)
    b4=Button(l100,image=p8,compound="c",command=abc1)
    b1.place(x=130,y=100)
    b2.place(x=430,y=100)
    b3.place(x=130,y=400)
    b4.place(x=430,y=400)
    l0.place(x=20,y=50)
    b0=Button(l100,text='NEXT>>',pady=10,bg="green",command=option,borderwidth=4,width=8,font=('bold',12)).place(x=720, y=350)
    exit_game=Button(l100,text='EXIT>>',bg='red',borderwidth=4,font="Courier 15 bold",command=exit_fromhere)
    exit_game.place(x=717,y=440)
    
    my_window.mainloop()
main()    
