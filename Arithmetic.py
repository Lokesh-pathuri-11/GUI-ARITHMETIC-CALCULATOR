from tkinter import *
window=Tk()
window.configure(background='white')
window.title("Arithmetic operations")
window.geometry("400x400")



def clickab() :
    n=text3.get()
    x=text1.get()
    y=text2.get()
    if (n=='a'):
        output.delete(0.0,END)
        z=eval(x)+eval(y)
        output.insert(END,z)
    elif (n=='b'):
        output.delete(0.0,END)
        z=eval(x)-eval(y)
        output.insert(END,z)
    elif (n=='c'):
        output.delete(0.0,END)
        z=eval(x)*eval(y)
        output.insert(END,z)
    elif (n=='d'):
        output.delete(0.0,END)
        z=eval(x)/eval(y)
        output.insert(END,z)
    else:
        window.destroy()
        exit()


Label(window,text="a.Addition",bg='white',fg='red').grid(sticky=W,row=1,column=0)
Label(window,text="b.Subtraction",bg='white',fg='red').grid(sticky=W,row=2,column=0)
Label(window,text="c.Multiplication",bg='white',fg='red').grid(sticky=W,row=3,column=0)
Label(window,text="d.Division",bg='white',fg='red').grid(sticky=W,row=4,column=0)
Label(window,text="Enter your option : ",bg='white',fg="black").grid(row=5,column=0,sticky=W)
text3=Entry(window,width=8,bg='yellow')
text3.grid(row=5,column=3,sticky=W)
Label(window,text="Enter the value of a : ",bg='white',fg="black").grid(sticky=W,row=7,column=0)
text1=Entry(window,width=8,bg='yellow')
text1.grid(row=7,column=3,sticky=W)
Label(window,text="Enter the value of b : ",bg='white',fg="black").grid(sticky=W,row=8,column=0)
text2=Entry(window,width=8,bg='yellow')
text2.grid(row=8,column=3,sticky=W)
take=Button(window,text='Submit',bg='black',fg='white',command=clickab)
take.grid(row=9,column=11,sticky=W)
Label(window,text="Output : ",bg='white',fg="black").grid(sticky=W,row=10,column=0)
output=Text(window,width=10,height=1,wrap=WORD,background='green')
output.grid(row=11,column=0,columnspan=2,sticky=W)
window.mainloop()
