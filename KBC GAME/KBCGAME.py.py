from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLableA.place_forget()
    progressbarLableB.place_forget()
    progressbarLableC.place_forget()
    progressbarLableD.place_forget()
    
    b = event.widget
    value = b['text']
    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencepoleButton.config(state=NORMAL, image=audiencepole)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                    root2.destroy()
                    questionArea.delete(1, 0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLable.config(image=amountimage)
                mixer.music.stop()
                mixer.music.load('kbcwon.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('you won 0 pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)
                winLabel = Label(root2, text='You won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winLabel.pack()
                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closeButton.pack()
                happyimage = PhotoImage(file='happy.png')
                happyLable = Label(root2, image=happyimage, bg='black')
                happyLable.place(x=30, y=280)

                happyLable1 = Label(root2, image=happyimage, bg='black')
                happyLable1.place(x=400, y=280)

                root1.mainloop()
                breakpoint

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLable.config(image=amountImages[i])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencepoleButton.config(state=NORMAL, image=audiencepole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                root1.destroy()
                questionArea.delete(1, 0, END)
                questionArea.insert(END, questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLable.config(image=amountimage)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('you won 0 pounds')
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)
            loseLabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loseLabel.pack()
            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                 activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                 command=close)
            closeButton.pack()
            sadimage = PhotoImage(file='sad.png')
            sadLable = Label(root1, image=sadimage, bg='black')
            sadLable.place(x=30, y=280)

            sadLable1 = Label(root1, image=sadimage, bg='black')
            sadLable1.place(x=400, y=280)

            root1.mainloop()
            breakpoint


    
    
def lifeline50():
   lifeline50Button.config(image=image50x,state=DISABLED)
   if questionArea.get(1.0,'end-1c') ==questions[0]:
      optionButton1.config(text='')
      optionButton4.config(text='')

   if questionArea.get(1.0,'end-1c') ==questions[1]:
      optionButton1.config(text='')
      optionButton3.config(text='')

   if questionArea.get(1.0,'end-1c') ==questions[2]:
      optionButton2.config(text='')
      optionButton3.config(text='')

   if questionArea.get(1.0,'end-1c') ==questions[3]:
      optionButton1.config(text='')
      optionButton3.config(text='')


   if questionArea.get(1.0,'end-1c') ==questions[4]:
      optionButton2.config(text='')
      optionButton4.config(text='')     

   if questionArea.get(1.0,'end-1c') ==questions[5]:
      optionButton1.config(text='')
      optionButton4.config(text='')          


   if questionArea.get(1.0,'end-1c') ==questions[6]:
      optionButton2.config(text='')
      optionButton4.config(text='')

   if questionArea.get(1.0,'end-1c') ==questions[7]:
      optionButton1.config(text='')
      optionButton4.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[8]:
      optionButton1.config(text='')
      optionButton3.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[9]:
      optionButton1.config(text='')
      optionButton3.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[10]:
      optionButton1.config(text='')
      optionButton3.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[11]:
      optionButton1.config(text='')
      optionButton3.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[12]:
      optionButton1.config(text='')
      optionButton3.config(text='') 

   if questionArea.get(1.0,'end-1c') ==questions[13]:
      optionButton1.config(text='')
      optionButton3.config(text='') 


   if questionArea.get(1.0,'end-1c') ==questions[14]:
      optionButton1.config(text='')
      optionButton4.config(text='') 

   



def audiencepolelife():
    audiencepoleButton.config(image=audiencepolex, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLableA.place(x=580, y=320)
    progressbarLableB.place(x=620, y=320)
    progressbarLableC.place(x=660, y=320)
    progressbarLableD.place(x=700, y=320)

    question_text = questionArea.get(1.0, 'end-1c')
    if question_text == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)
    elif question_text == questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=90)
    elif question_text == questions[2]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=90)
    elif question_text == questions[4]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[5]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)
    elif question_text == questions[6]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)
    elif question_text == questions[8]:
        progressbarA.config(value=50)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=90)
    elif question_text == questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=60)
    elif question_text == questions[14]:
        progressbarA.config(value=40)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)


def phoneLifeline():
   mixer.music.load('calling.mp3')
   mixer.music.play()
   callButton.place(x=70,y=260)
   phoneLifelineButton.config(image=phoneImagex,state=DISABLED) 

def phoneclick():
   for i in  range(15):
      if questionArea.get(1.0,'end-1c')==questions[i]:
         engine.say(f'The anwser is {correct_answers[i]}')
         engine.runAndWait()





correct_answers=["Russia","366","Heron","Dinar","Sunlight","Vadodara","July 11","Vikrama Sarabhai",
                "Kiran Bedi","Nirmala Sitharaman","Pratibha Patel","7","Bill Gates & Paul Allen","Fear of height",
                "Stapes"]


questions = ("which is the largest country in the world?",
             "how many days are there in a leap year?",
             "which of these bird has the longest beek and feet?",
             "what is the national currency of kuwait?",
             "plant receive their nutrient?",
             "where is the railway staff college located?",
             "when is the world population day observed?",
             "who is the first  chairman of isro?",
             "who is the first female IPS officer in india?",
             "who is the first female finance minister of india?",
             "who is the first female president of india?",
             "How many continents are there in the world?",
             "Who are the founders of Microsoft?",
             "What is the acrophobia called?",
             "Which is the smallest bone in human body?")

first_option = ("Indian", "354", "Heron", "Euro", "Sunlight",
                "Pune", "July 11", "Satish Dhawan",
                "Sushma Swaraj", "Jayalalitha", "Ambika soni",
                "5", "Jeff Bezos & Step Jorz", "Fear of darkness", "arm")

second_option = ("America", "367", "Parrot", "Pound", "Atmosphere", "Delhi", "October 4",
                 "M.G.K Menon", "Kiran Bedi", "Nirmala Sitharaman", "Pratibha Patel",
                 "8", "Bill gates & Paul Allen", "Fear of light", "Nose")

third_option = ("Russia", "365", "Storks", "Dollar", "Leaf", "Vadodara", "May 31",
                "Vikrama Sarabhai", "Anna Rajam Malhotara", "Bondita chattarjee",
                "Indra Gandhi", "6", "elon musk", "Fear of water", "Stapes")

fourth_option = ("China", "366", "Ostrich", "Dinar", "Soil", "Patna", "September 04",
                 "S.Somanath", "Riya Sabe", "Sarojini Naidu", "Surekha Yadav",
                 "7", "Sundar Pichai", "Fear of height", "Hand")

root = Tk()
root.geometry('1270x652+0+0')
root.title('Quiz game')
root.config(bg="black")

current_question = 0

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topframe = Frame(leftframe, bg='black', pady=15)
topframe.grid()

centerframe = Frame(leftframe, bg='black', pady=15)
centerframe.grid(row=1, column=0)

buttomframe = Frame(leftframe, bg='black')
buttomframe.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-x.png')
lifeline50Button = Button(topframe, image=image50, bg='black', bd=0, activebackground='black', width=180, height=80,command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencepole = PhotoImage(file='audiencepole.png')
audiencepolex = PhotoImage(file='audiencepolex.png')

audiencepoleButton = Button(topframe, image=audiencepole, bg='black', bd=0, activebackground='black', width=180, height=80,command=audiencepolelife)
audiencepoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImagex = PhotoImage(file='phoneAFriendx.png')
phoneLifelineButton = Button(topframe, image=phoneImage, bg='black', bd=0, activebackground='black', width=180, height=80,command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage=PhotoImage(file='phone.png')

callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',command=phoneclick)

centerImage = PhotoImage(file='center.png')
logoLable = Label(centerframe, image=centerImage, bg='black', width=300, height=200)
logoLable.grid(row=0, column=0)

amountimage = PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='picture1.png')
amountimage2=PhotoImage(file='picture2.png')
amountimage3=PhotoImage(file='picture3.png')
amountimage4=PhotoImage(file='picture4.png')
amountimage5=PhotoImage(file='picture5.png')
amountimage6=PhotoImage(file='picture6.png')
amountimage7=PhotoImage(file='picture7.png')
amountimage8=PhotoImage(file='picture8.png')
amountimage9=PhotoImage(file='picture9.png')
amountimage10=PhotoImage(file='picture10.png')
amountimage11=PhotoImage(file='picture11.png')
amountimage12=PhotoImage(file='picture12.png')
amountimage13=PhotoImage(file='picture13.png')
amountimage14=PhotoImage(file='picture14.png')
amountimage15=PhotoImage(file='picture15.png')
amountImages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage4,amountimage5,amountimage6,amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,amountimage12,amountimage13,amountimage14,amountimage15]

amountLable = Label(rightframe, image=amountimage, bg='black')
amountLable.grid(row=0, column=0)

layoutImage = PhotoImage(file='lay.png')
layoutLable = Label(buttomframe, image=layoutImage, bg='black')
layoutLable.grid(row=0, column=0)

questionArea = Text(buttomframe, font=('arial', 18, 'bold'),
                    width=34, height=2, wrap='word', bg='black', fg='white', bd=0)
questionArea.place(x=70, y=10)
questionArea.insert(END, questions[0])

LabelA = Label(buttomframe, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
LabelA.place(x=60, y=110)

optionButton1=Button(buttomframe,text=first_option[0],font=('arial',18,'bold'),bg='black',fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)

LabelB = Label(buttomframe, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
LabelB.place(x=330, y=110)
optionButton2 = Button(buttomframe, text=second_option[0], font=('arial', 18, 'bold'), bg='black',
                       fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)

LabelC=Label(buttomframe,text='C:',bg='black',fg='white',font=('aria',16,'bold'))
LabelC.place(x=60,y=190)

optionButton3=Button(buttomframe,text=third_option[0],font=('arial',16,'bold'),
                     bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

LabelD=Label(buttomframe,text='D:',bg='black',fg='white',font=('aria',16,'bold'))
LabelD.place(x=330,y=190)

optionButton4=Button(buttomframe,text=fourth_option[0],font=('arial',16,'bold'),bg='black', 
                     fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLableA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLableB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLableC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLableD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')



optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)


root.mainloop()
