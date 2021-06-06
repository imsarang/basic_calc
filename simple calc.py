from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("simple calculator")
root.configure(bg="black")

e=Entry(root,borderwidth=5,width=50,bg='light grey')
e.grid(row=0,column=0,columnspan=4)

###########################################################################################
def click(number):    
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

    return

def clears():
    e.delete(0,END)
    return

def add():
    first_num=e.get()
    global f_num
    global operation
    operation = '+'
    f_num = int(first_num)
    e.delete(0,END)

    return

def sub():
    first_num=e.get()
    global f_num
    global operation
    operation = '-'
    f_num = int(first_num)
    e.delete(0,END)
    return

def multiply():
    first_num=e.get()
    global f_num
    global operation
    operation = 'x'
    f_num=int(first_num)
    e.delete(0,END)

    return

def divide():
    first_num=e.get()
    global f_num
    global operation
    operation = '/'
    f_num = int(first_num)
    e.delete(0,END)

    return

def modu():
    first_num=e.get()
    global f_num
    global operation
    f_num=int(first_num)
    operation='%'
    e.delete(0,END)
    return

def power():
    first_num=e.get()
    global f_num
    global operation
    f_num=int(first_num)
    operation='^'
    e.delete(0,END)
    return


def equal():
    second_num=e.get()
    e.delete(0,END)
    s_num=int(second_num)
    if operation == '+':
        e.insert(0,s_num + f_num)
    elif operation == '-':
        e.insert(0,s_num - f_num)
    elif operation == 'x':
        e.insert(0,s_num*f_num)
    elif operation == '/':
        e.insert(0,(f_num/s_num))
    elif operation =='%':
        e.insert(0,f_num%s_num)
    elif operation =='^':
        e.insert(0,f_num ** s_num)    

    return




'''def digit(t_num):
    global l
    l=[]
    t_num=int(e.get())
    if t_num%10!=0:
        l.append(t_num%10)
    
    if t_num<10:
        pass
    else:
        return digit(int(t_num/10))
'''
def backspace():
    tr_num = int(e.get())
    #digit(tr_num)
    t_num=int(tr_num/10)
    e.delete(0,END)
    e.insert(0,t_num)
    return

def msg():
    response=messagebox.askokcancel("","exit simple calculator ?")
    #l=Label(root,text=response).grid(row=8,column=0)
    if response==1:
        root.quit()
    
###################################################################################################

#creation of buttons
b1=Button(root,text="1",padx=30,pady=15,bg='pink',command=lambda:click(1))
b2=Button(root,text="2",padx=30,pady=15,bg='pink',command=lambda:click(2))
b3=Button(root,text="3",padx=30,pady=15,bg='pink',command=lambda:click(3))
b4=Button(root,text="4",padx=30,pady=15,bg='pink',command=lambda:click(4))
b5=Button(root,text="5",padx=30,pady=15,bg='pink',command=lambda:click(5))
b6=Button(root,text="6",padx=30,pady=15,bg='pink',command=lambda:click(6))
b7=Button(root,text="7",padx=30,pady=15,bg='pink',command=lambda:click(7))
b8=Button(root,text="8",padx=30,pady=15,bg='pink',command=lambda:click(8))
b9=Button(root,text="9",padx=30,pady=15,bg='pink',command=lambda:click(9))
b0=Button(root,text="0",padx=30,pady=15,bg='pink',command=lambda:click(0))

badd=Button(root,text="+",padx=30,pady=40,bg='yellow',command=add)
bsub=Button(root,text="-",padx=30,pady=40,bg='yellow',command=sub)
bmul=Button(root,text="x",padx=30,pady=15,bg='violet',command=multiply)
bdiv=Button(root,text="/",padx=30,pady=15,bg='violet',command=divide)
bequ=Button(root,text="=",padx=30,pady=15,bg='magenta',command=equal)
bclr=Button(root,text="clear",padx=140,pady=15,bg='purple',command=clears)
bback_space=Button(root,text="<-",padx=27,pady=15,bg='magenta',command=backspace)
bmod=Button(root,text="mod",padx=21,pady=15,bg='violet',command=modu)
bpower=Button(root,text="^",padx=28,pady=15,bg='violet',command=power)

bexit=Button(root,text='exit',padx=140,pady=15,bg='red',command=msg)

#display
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b0.grid(row=4,column=1)

badd.grid(row=1,column=3,rowspan=2)
bsub.grid(row=3,column=3,rowspan=2)
bmul.grid(row=4,column=0)
bdiv.grid(row=4,column=2)
bequ.grid(row=5,column=0)
bclr.grid(row=6,column=0,columnspan=4)
bback_space.grid(row=5,column=3)
bmod.grid(row=5,column=1)
bpower.grid(row=5,column=2)
bexit.grid(row=7,column=0,columnspan=4)

root.mainloop()
