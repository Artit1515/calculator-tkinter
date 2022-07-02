from tkinter import*
import tkinter.messagebox 
import math
app=Tk()
app.title("calculator")
#app.geometry("600x600")


ansresult=""

dpshow=StringVar(value="0")

def enter(number):
    global ansresult
    ansresult=ansresult+str(number)
    dpshow.set(ansresult)

def clear():
    global ansresult
    ansresult=""
    dpshow.set(0)

def equal():
    global ansresult
    """if ansresult =="+" or ansresult =="-" or ansresult =="*" or ansresult =="/"or ansresult ==".":
      for i in ansresult:
            print(i)
            ansresult=""
            dpshow.set(0)
            return"""
    

    firstchar=ansresult[0]
    if firstchar == "*" or firstchar == "/" or firstchar == ")":
        ansresult=""
        dpshow.set("syntrax error")
        return

    finalans=float(eval(ansresult))
    dpshow.set(str(finalans))
    ansresult=str(finalans)

def delete():
    global ansresult
    ans=dpshow.get()
    lenght=len(ans)
    dp.delete(lenght-1,END)
    rubkar=dp.get()
    ansresult=rubkar
    if lenght == 1:
        dpshow.set(0)
        ansresult=""


def root():
    global ansresult
    sqroot= (math.sqrt(eval(ansresult)))
    dpshow.set(str(sqroot))
    ansresult=str(sqroot)


dp=Entry(font=90,width=35,textvariable=dpshow,justify="right")
dp.grid(columnspan=5)


myMenu = Menu()
app.config(menu=myMenu)
minimenu = Menu()

minimenu.add_command(label="scitific calculator mode")
minimenu.add_command(label="history")
minimenu.add_command(label="")




myMenu.add_cascade(label="more",menu=minimenu)




#ที่เก็บเลข
bt7=Button(text="7",padx=30,bg="light gray",pady=30,command=lambda:enter(7)).grid(row=2,column=0)
bt8=Button(text="8",padx=30,bg="light gray",pady=30,command=lambda:enter(8)).grid(row=2,column=1)
bt9=Button(text="9",padx=30,bg="light gray",pady=30,command=lambda:enter(9)).grid(row=2,column=2)

bt4=Button(text="4",padx=30,bg="light gray",pady=30,command=lambda:enter(4)).grid(row=3,column=0)
bt5=Button(text="5",padx=30,bg="light gray",pady=30,command=lambda:enter(5)).grid(row=3,column=1)
bt6=Button(text="6",padx=30,bg="light gray",pady=30,command=lambda:enter(6)).grid(row=3,column=2)

bt1=Button(text="1",padx=30,bg="light gray",pady=30,command=lambda:enter(1)).grid(row=4,column=0)
bt2=Button(text="2",padx=30,bg="light gray",pady=30,command=lambda:enter(2)).grid(row=4,column=1)
bt3=Button(text="3",padx=30,bg="light gray",pady=30,command=lambda:enter(3)).grid(row=4,column=2)

bt0=Button(text="0",padx=30,pady=30,bg="light gray",command=lambda:enter(0)).grid(row=5,column=0)
btdot=Button(text=".",padx=31.25,bg="light gray",pady=30,command=lambda:enter(".")).grid(row=5,column=1)
btequal=Button(text="=",padx=30,bg="light gray",pady=30,command=equal).grid(row=5,column=2)

btplus=Button(text="+",padx=30,bg="light gray",pady=30,command=lambda:enter("+")).grid(row=5,column=3)
btminus=Button(text="-",padx=31.75,bg="light gray",pady=30,command=lambda:enter("-")).grid(row=4,column=3)
btmultiply=Button(text="x",padx=31,bg="light gray",pady=30,command=lambda:enter("*")).grid(row=3,column=3)
btdivide=Button(text="÷",padx=30,bg="light gray",pady=30,command=lambda:enter("/")).grid(row=2,column=3)


btdelelte=Button(text="del",padx=26.5,bg="light gray",pady=30,command=delete).grid(row=1,column=3)
dtclear=Button(text="c",padx=30,bg="light gray",pady=30,command=clear).grid(row=1,column=2)
btopblacket=Button(text=")",padx=30.5,bg="light gray",pady=30,command=lambda:enter(")")).grid(row=1,column=1)
btclblacket=Button(text="(",padx=30.5,bg="light gray",pady=30,command=lambda:enter("(")).grid(row=1,column=0)


app.mainloop()