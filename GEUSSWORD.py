from tkinter import *
from random import *
from tkinter import messagebox
import time

#============================================================================================================================================================
GEUSS_WORD = ['DRBI', 'DGO', 'OENDYK', 'GFRIEFA', 'CEBABAG', 'CLIHI', 'ICRGAL', 'WETSE OTPAOT', 'RERAOCDIN', 'DRE', 'OELLYW', 'LBEU', 'ERGNE', 'OREAGN',
              'RPEULP', 'EMIL', 'ORWBN', 'NYAV', 'PNIK','HEDA', 'IHAR', 'EEY', 'SEAR', 'SEON', 'UHMTO', 'NICH', 'OEEAFHDR', 'AJW', 'EKEHC', 'CCLIER',
              'USQRAE','RITLANEG', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', 'IYLCECB', 'CRA', 'BSU', 'TIANR', 'UTKCR', 'NVA', 'LRTOMCCYEO', ]

GEUSS_ANSWER = ['BIRD', 'DOG', 'DONKEY', 'GIRAFFE', 'CABBAGE', 'CHILI', 'GARLIC', 'SWEET POTATO', 'CORIANDER','RED', 'YELLOW', 'BLUE', 'GREEN','ORANGE',
                'PURPLE', 'LIME', 'BROWN', 'NAVY', 'PINK','HEAD', 'HAIR', 'EYE', 'EARS', 'NOSE', 'MOUTH', 'CHIN', 'FOREHEAD', 'JAW', 'CHEEK','CIRCLE',
                'SQUARE','TRIANGLE','MOUSE', 'TIGER', 'RABBIT', 'RAT','BICYCLE', 'CAR', 'BUS', 'TRAIN', 'TRUCK', 'VAN','MOTORCYCLE', ]

 

ran_num = randrange(0, (len(GEUSS_WORD)))
jumbled_rand_word = GEUSS_WORD[ran_num]

points = 0
count=0
counts=0
#==============================================================================================================================================================
def main():
    
#==================================Functions=================================================================================================================   
    def back():
        my_window.destroy()
        import option
        

    def change():
        global ran_num,counts
        counts+=1
        ran_num = randrange(0, (len(GEUSS_WORD)))
        word.configure(text=GEUSS_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num,count,counts
        user_word = get_input.get().upper()
        if user_word == GEUSS_ANSWER[ran_num]:
            points += 5
            count+=1
            counts+=1
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            second.set("60")
            ran_num = randrange(0, (len(GEUSS_WORD)))
            word.configure(text=GEUSS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
            submit()
            
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)
        score
        count
        counts
    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=GEUSS_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

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
          l4=Label(l1,text="Total number of questions visited :"+str(counts),font=('georgia',30)).place(x=100,y=450)
          m1.mainloop()
          exit
          
    
        
    

#============================main window======================================================================================================================
    my_window = Tk()
    my_window.geometry("800x800")
    my_window.resizable(0, 0)
    my_window.title("KIDS LEARNING GAME")
    img1 = PhotoImage(file="back.png")
    img=PhotoImage(file="la.png")
    global counts
#================================WIDGETS======================================================================================================================   
    l1=Label(my_window,image=img).pack()
    
    lab_img1 = Button(l1,image=img1,bg='light blue',border=0,justify='center',command=back)
    lab_img1.place(x=0,y=10)

    score = Label(l1,text="Score:- 0",pady=10,bg="light blue",fg="black", font="Titillium  14 bold")
    score.place(x=390,y=70)

    word = Label(l1,text=jumbled_rand_word,pady=10,bg="light blue",fg="black",width=15,font="Titillium  40 bold",)
    word.place(x=195,y=140)

    get_input = Entry(l1,font="none 26 bold",borderwidth=10,justify='center',)
    get_input.place(x=250,y=240)

    submit = Button(l1,text="Submit",width=18,borderwidth=8,font=("", 13),fg="black",bg="light blue",command=check)
    submit.place(x=350,y=310)

    change_btn = Button(l1,text="Change Word",width=18,borderwidth=8,fg="black",bg="light blue",font=("", 13),command=change)
    change_btn.place(x=350,y=380)

    ans = Button(l1,text="Answer",width=18,borderwidth=8,fg="black",bg="light blue",font=("", 13),command=show_answer)
    ans.place(x=350,y=450)

    ans_lab = Label(l1,text="",fg="black",font="Courier 15 bold")
    ans_lab.place(x=390,y=520)
    
    
    second=StringVar()
    second.set("60")
    global secondEntry
    secondEntry= Label(l1, width=3,borderwidth=8, font=("Arial",18,""),textvariable=second)
    secondEntry.place(x=660,y=20)
    img3=PhotoImage(file='clockk.gif')
    clock_img=Button(l1,image=img3,borderwidth=4, ).place(x=580,y=20)
    exit_game=Button(l1,text='EXIT',bg='red',borderwidth=8,font="Courier 15 bold",command=exit_fromhere)
    exit_game.place(x=700,y=540)
    
    while(True):
          
        def submit():
            try:
                # stored in here :temp
                temp =int(second.get())
            except TclError:
                pass
            while temp >-1:
                mins,secs = divmod(temp,60)
                hours=0
                if secs <61:
                    hours, mins = divmod(mins, 60)
                    second.set("{0:2d}".format(secs))# using format () method to store the value up to# two decimal places
                    try:
                        secondEntry.update()# updating the GUI window after decrementing the# temp value every time
                        time.sleep(1)
                    except TclError:
                        break
                        
                    # when temp value = 0; then a messagebox pop's up
		    # with a message:"Time's up"
                if (temp == 0):
                    messagebox.showinfo("Time Countdown", "Time's up ")
                    change()
                    second.set("60")
                    submit()
                temp -= 1
                
        submit()
   
    my_window.mainloop()
main()
