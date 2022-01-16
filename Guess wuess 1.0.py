from tkinter import *
from PIL import Image,ImageTk
 #functions
 
 #HOmepage
 #Quit



#Start Game


class homewindow:
    def selectlvl(self):
        self.master.withdraw()
        selectlevel(Toplevel(self.master))
    def __init__(self,window=None):
        self.master=window
        window.geometry("560x646+100+100")
        window.title("Guess Wuess")
        window.resizable(False,False)
                
        image=Image.open("cat.jpg")
        photo=ImageTk.PhotoImage(image)
        label=Label(root,image=photo)
        label.image=photo
        label.place(x=0,y=-200)

        #Home window Txt
        Label(root,text="Welcome to Guess Wuess",font="shizuru 23 bold",bg="#f4e033").place(x=74,y=50)

        #HOme window Buttons
        Button(root,text="   Start Game   ",font="ariel 15 bold",bg="black",fg="#f4e033",relief=SUNKEN,command=self.lvl1).place(x=210,y=160)
        Button(root,text="Select lvl",font="ariel 15 bold",bg="black",fg="#f4e033",command=self.selectlvl).place(x=235,y=210)
        Button(root,text="Quit",font="ariel 15 bold",bg="black",fg="#f4e033",command=quit).place(x=257,y=260)
    
    def lvl1(self):
        self.master.withdraw()
        window1(Toplevel(self.master))



        
class selectlevel:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Select level')
        window.geometry("450x500")
        image=Image.open("cat.jpg")
        #image=image.resize((,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=0,y=0)
        Label(window,text="Select the level you want to jump to",font="aerial 10 bold").place(x=100,y=20)
        b3=Button(window,text='Level-1',bg='black', height = 2, width = 10,fg='white',command=self.lvl)
        b3.place(x=180,y=100)
        b1=Button(window,text='Level-2',bg='black', height = 2, width = 10,fg='white',command=self.lvl2)
        b1.place(x=180,y=160)
        b2=Button(window,text='Level-3',bg='black', height = 2, width = 10,fg='white',command=self.lvl3)
        b2.place(x=180,y=240)
        b4=Button(window,text='Level-4',bg='black', height = 2, width = 10,fg='white',command=self.lvl4)
        b4.place(x=180,y=300)
        b5=Button(window,text='Level-5',bg='black', height = 2, width = 10,fg='white',command=self.lvl5)
        b5.place(x=180,y=360)
    def lvl(self):
        self.master.withdraw()
        window1(Toplevel(self.master))
        
        
    def lvl2(self):
        self.master.withdraw()
        window2(Toplevel(self.master))
    def lvl3(self):
        self.master.withdraw()
        window3(Toplevel(self.master))
    def lvl4(self):
        self.master.withdraw()
        window4(Toplevel(self.master))
    def lvl5(self):
        self.master.withdraw()
        window5(Toplevel(self.master))

        

    

        
class window1:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Lvl-1')
        window.geometry("500x400")
        image=Image.open("questionmark.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Hints:",font="aerial 10 bold").place(x=50,y=220)
        Label(window,text="1-King of the Jungle").place(x=50,y=240)
        Label(window,text="2-It Roars").place(x=50,y=260)
        b3=Button(window,text='Wolf',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong1)
        b3.place(x=260,y=320)
        b1=Button(window,text='Lion',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow1)
        b1.place(x=60,y=320)
        b2=Button(window,text='Tiger',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong1)
        b2.place(x=160,y=320)
        b4=Button(window,text='Leopard',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong1)
        b4.place(x=360,y=320)
    def withdrawwrong1(self):
        self.master.withdraw()
        wrongguess(Toplevel(self.master))
        
        
    def withdrawwindow1(self):
        self.master.withdraw()
        rightguess(Toplevel(self.master))

        
class wrongguess:
    def __init__(self,window=None):
        self.master=window
        window.title('Wrong Answer!!')
        window.geometry("500x400")
        image=Image.open("lion.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="You couldn't guess right",fg='red',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Exit",bg='black', height = 2, width = 7,fg='white',command=quit)
        b3.place(x=260,y=320)
        b2=Button(window,text='Return',bg='black', height = 2, width = 7,fg='white',command=self.withdrawwrongguess)
        b2.place(x=160,y=320)

    def withdrawwrongguess(self):
        self.master.withdraw()
        window1(Toplevel(self.master))




    
class rightguess:
    def __init__(self,window=None):
        self.master=window
        window.title('Right answer')
        window.geometry("500x400")
        image=Image.open("lion.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Congrats!! You GUessed Right",fg='green',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Next Lvl",bg='black', height = 2, width = 7,fg='white',command=self.withdrawrightguess)
        b3.place(x=260,y=320)
        b2=Button(window,text='Exit',bg='black', height = 2, width = 7,fg='white',command=quit)
        b2.place(x=160,y=320)


    def withdrawrightguess(self):
        self.master.withdraw()
        window2(Toplevel(self.master))

class window2:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Lvl-2')
        window.geometry("500x400")
        image=Image.open("questionmark.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Hints:",font="aerial 10 bold").place(x=50,y=220)
        Label(window,text="1-Founder Of Pakistan").place(x=50,y=240)
        Label(window,text="2-D.O.B 25 December").place(x=50,y=260)
        b3=Button(window,text='Quaid-e-Azam',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow2)
        b3.place(x=260,y=320)
        b1=Button(window,text='Allama Iqbal',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong2)
        b1.place(x=60,y=320)
        b2=Button(window,text='Liaquat Ali',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong2)
        b2.place(x=160,y=320)
        b4=Button(window,text='Sirsyed Ahmed',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong2)
        b4.place(x=360,y=320)
    def withdrawwrong2(self):
        self.master.withdraw()
        wrongguess2(Toplevel(self.master))
        
        
    def withdrawwindow2(self):
        self.master.withdraw()
        rightguess2(Toplevel(self.master))

        
class wrongguess2:
    def __init__(self,window=None):
        self.master=window
        window.title('Wrong Answer!!')
        window.geometry("500x400")
        image=Image.open("quaidjani.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="You couldn't guess right",fg='red',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Exit",bg='black', height = 2, width = 7,fg='white',command=quit)
        b3.place(x=260,y=320)
        b2=Button(window,text='Return',bg='black', height = 2, width = 7,fg='white',command=self.withdrawwrongguess2)
        b2.place(x=160,y=320)
    def withdrawwrongguess2(self):
        self.master.withdraw()
        window2(Toplevel(self.master))


        
        
class rightguess2:
    def __init__(self,window=None):
        self.master=window
        window.title('Right answer')
        window.geometry("500x400")
        image=Image.open("quaidjani.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Congrats!! You GUessed Right",fg='green',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Next Lvl",bg='black', height = 2, width = 7,fg='white',command=self.withdrawwindow2)
        b3.place(x=260,y=320)
        b2=Button(window,text='Previous',bg='black', height = 2, width = 7,fg='white',command=self.previous)
        b2.place(x=160,y=320)
    def previous(self):
        self.master.withdraw()
        window1(Toplevel(self.master)) 

    def withdrawwindow2(self):
        self.master.withdraw()
        window3(Toplevel(self.master))

class window3:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Lvl-3')
        window.geometry("500x400")
        image=Image.open("questionmark.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Hints:",font="aerial 10 bold").place(x=50,y=220)
        Label(window,text="1-The Blue Monster").place(x=50,y=240)
        Label(window,text="2-The Queen of Ocean").place(x=50,y=260)
        b3=Button(window,text='Dolphin',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong3)
        b3.place(x=260,y=320)
        b1=Button(window,text='Shark',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong3)
        b1.place(x=60,y=320)
        b2=Button(window,text='Sting Ray',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong3)
        b2.place(x=160,y=320)
        b4=Button(window,text='Whale',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow3)
        b4.place(x=360,y=320)
    def withdrawwrong3(self):
        self.master.withdraw()
        wrongguess3(Toplevel(self.master))
        
        
    def withdrawwindow3(self):
        self.master.withdraw()
        rightguess3(Toplevel(self.master))

        
class wrongguess3:
    def __init__(self,window=None):
        self.master=window
        window.title('Wrong Answer!!')
        window.geometry("500x400")
        image=Image.open("whale.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="You couldn't guess right",fg='red',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Exit",bg='black', height = 2, width = 5,fg='white',command=quit)
        b3.place(x=260,y=320)
        b2=Button(window,text='Return',bg='black', height = 2, width = 5,fg='white',command=self.withdrawwrongguess3)
        b2.place(x=180,y=320)
    def withdrawwrongguess3(self):
        self.master.withdraw()
        window3(Toplevel(self.master))

        
        
class rightguess3:
    def __init__(self,window=None):
        self.master=window
        window.title('Right answer')
        window.geometry("500x400")
        image=Image.open("whale.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Congrats!! You GUessed Right",fg='green',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Next Lvl",bg='black', height = 2, width = 7,fg='white',command=self.withdrawwindow3)
        b3.place(x=260,y=320)
        b2=Button(window,text='Previous',bg='black', height = 2, width = 7,fg='white',command=self.previous)
        b2.place(x=160,y=320)
    def previous(self):
        self.master.withdraw()
        window2(Toplevel(self.master))

    def withdrawwindow3(self):
        self.master.withdraw()
        window4(Toplevel(self.master))

class window4:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Lvl-4')
        window.geometry("500x400")
        image=Image.open("questionmark.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Hints:",font="aerial 10 bold").place(x=50,y=220)
        Label(window,text="1-Second Highest Peak of the world").place(x=50,y=240)
        Label(window,text="2-Located in Pakistan").place(x=50,y=260)
        b3=Button(window,text='Mount Everest',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong4)
        b3.place(x=260,y=320)
        b1=Button(window,text='Nanga Parbat',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong4)
        b1.place(x=60,y=320)
        b2=Button(window,text='K-2',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow4)
        b2.place(x=160,y=320)
        b4=Button(window,text='Broad Peak',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong4)
        b4.place(x=360,y=320)
    def withdrawwrong4(self):
        self.master.withdraw()
        wrongguess4(Toplevel(self.master))
        
        
    def withdrawwindow4(self):
        self.master.withdraw()
        rightguess4(Toplevel(self.master))

        
class wrongguess4:
    def __init__(self,window=None):
        self.master=window
        window.title('Wrong Answer!!')
        window.geometry("500x400")
        image=Image.open("K2.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="You couldn't guess right",fg='red',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Exit",bg='black', height = 2, width = 7,fg='white',command=quit)
        b3.place(x=260,y=320)
        b2=Button(window,text='Return',bg='black', height = 2, width = 7,fg='white',command=self.withdrawwrongguess4)
        b2.place(x=160,y=320)
    def withdrawwrongguess4(self):
        self.master.withdraw()
        window4(Toplevel(self.master))
        
        
class rightguess4:
    def __init__(self,window=None):
        self.master=window
        window.title('Right answer')
        window.geometry("500x400")
        image=Image.open("K2.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Congrats!! You GUessed Right",fg='green',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Next Lvl",bg='black', height = 2, width = 7,fg='white',command=self.withdrawwindow4)
        b3.place(x=260,y=320)
        b2=Button(window,text='Previous',bg='black', height = 2, width = 7,fg='white',command=self.previous)
        b2.place(x=160,y=320)
    def previous(self):
        self.master.withdraw()
        window3(Toplevel(self.master))

    def withdrawwindow4(self):
        self.master.withdraw()
        window5(Toplevel(self.master))

class window5:
    def __init__(self,window=None):
        self.master=window   # For secondary window use Toplevel 
        window.title('Lvl-4')
        window.geometry("500x400")
        image=Image.open("questionmark.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Hints:",font="aerial 10 bold").place(x=50,y=220)
        Label(window,text="1-G.O.A.T").place(x=50,y=240)
        Label(window,text="2-Footballer").place(x=50,y=260)
        b3=Button(window,text='Neymar',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong5)
        b3.place(x=260,y=320)
        b1=Button(window,text='Maradona',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong5)
        b1.place(x=60,y=320)
        b2=Button(window,text='Ronaldo',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwrong5)
        b2.place(x=160,y=320)
        b4=Button(window,text='Messi',bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow5)
        b4.place(x=360,y=320)
    def withdrawwrong5(self):
        self.master.withdraw()
        wrongguess5(Toplevel(self.master))
        
        
    def withdrawwindow5(self):
        self.master.withdraw()
        rightguess5(Toplevel(self.master))

        
class wrongguess5:
    def __init__(self,window=None):
        self.master=window
        window.title('Wrong Answer!!')
        window.geometry("500x400")
        image=Image.open("Messi.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="You couldn't guess right",fg='red',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="Exit",bg='black', height = 2, width = 7,fg='white',command=quit)
        b3.place(x=260,y=320)
        b2=Button(window,text='Return',bg='black', height = 2, width = 7,fg='white',command=self.withdrawwrongguess5)
        b2.place(x=160,y=320)
    def withdrawwrongguess5(self):
        self.master.withdraw()
        window5(Toplevel(self.master))
        
        
class rightguess5:
    def __init__(self,window=None):
        self.master=window
        window.title('Right answer')
        window.geometry("500x400")
        image=Image.open("Messi.jpg")
        image=image.resize((250,150))
        photo=ImageTk.PhotoImage(image)
        label=Label(window,image=photo)
        window.image=photo
        label.place(x=120,y=50)
        Label(window,text="Congrats!! You GUessed Right",fg='green',font="aerial 9 bold").place(x=170,y=220)
        b3=Button(window,text="End Game",bg='black', height = 2, width = 10,fg='white',command=self.withdrawwindow5)
        b3.place(x=260,y=320)
        b2=Button(window,text='Previous',bg='black', height = 2, width = 10,fg='white',command=self.previous)
        b2.place(x=160,y=320)
    def previous(self):
        self.master.withdraw()
        window4(Toplevel(self.master))

    def withdrawwindow5(self):
        self.master.withdraw()
            #window6(Toplevel(self.master))



        

        
root=Tk()
top=homewindow(root)
root.mainloop()


































































































