from tkinter import *
i=''
lb1t=''
lb2t=''
cond=0
ch1=chr(215)
ch2=chr(247)
ch3=chr(9003)
signs=['+','-',ch1,ch2]
def type1():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'1'
    if lb1t=='' or lb1t=='0':
        lb1t='1'
    lb1.config(text='{}'.format(lb1t))
def type2():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'2'
    if lb1t=='' or lb1t=='0':
        lb1t='2'
    lb1.config(text='{}'.format(lb1t))
def type3():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'3'
    if lb1t=='' or lb1t=='0':
        lb1t='3'
    lb1.config(text='{}'.format(lb1t))
def type4():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'4'
    if lb1t=='' or lb1t=='0':
        lb1t='4'
    lb1.config(text='{}'.format(lb1t))
def type5():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'5'
    if lb1t=='' or lb1t=='0':
        lb1t='5'
    lb1.config(text='{}'.format(lb1t))
def type6():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'6'
    if lb1t=='' or lb1t=='0':
        lb1t='6'
    lb1.config(text='{}'.format(lb1t))
def type7():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'7'
    if lb1t=='' or lb1t=='0':
        lb1t='7'
    lb1.config(text='{}'.format(lb1t))
def type8():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'8'
    if lb1t=='' or lb1t=='0':
        lb1t='8'
    lb1.config(text='{}'.format(lb1t))
def type9():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'9'
    if lb1t=='' or lb1t=='0':
        lb1t='9'
    lb1.config(text='{}'.format(lb1t))
def type0():
    global lb1t
    if lb1t!='' and lb1t!='0':
        lb1t=lb1t+'0'
    if lb1t=='' or lb1t=='0':
        lb1t='0'
    lb1.config(text='{}'.format(lb1t))
def typed():
    global lb1t
    if lb1t!='' and lb1t[-1]!='.':
        lb1t=lb1t+'.'
    if lb1t=='':
        lb1t='0.'
    lb1.config(text='{}'.format(lb1t))
def reset():
    global lb1t
    global lb2t
    lb1t =''
    lb2t =''
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def minus():
    global lb1t
    global lb2t
    if lb1t!='' and lb2t=='':
        lb2t=lb1t+'-'
        lb1t=''
    elif lb1t!='' and lb2t!='':
        equal()
        lb2t=lb2t+'-'
        lb1t=''
    elif lb1t=='' and lb2t!='' and lb2t[-1] not in signs:
        lb1t=''
        lb2t=lb2t+'-'
    elif lb1t=='' and lb2t=='':
        lb1t='-'
        lb2t=''
    elif lb1t=='' and lb2t[-1] in signs:
        lb1t='-'
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def plus():
    global lb1t
    global lb2t
    if lb1t!='' and lb2t=='':
        lb2t=lb1t+'+'
        lb1t=''
    elif lb1t!='' and lb2t!='':
        equal()
        lb2t=lb2t+'+'
        lb1t=''
    elif lb1t=='' and lb2t!=''and lb2t[-1] not in signs:
        lb1t=''
        lb2t=lb2t+'+'
    elif lb1t=='' and lb2t=='':
        lb1t=''
        lb2t=''
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def cross():
    global lb1t
    global lb2t
    if lb1t!='' and lb2t=='':
        lb2t=lb1t+ch1
        lb1t=''
    elif lb1t!='' and lb2t!='':
        equal()
        lb2t=lb2t+ch1
        lb1t=''
    elif lb1t=='' and lb2t!=''and lb2t[-1] not in signs:
        lb1t=''
        lb2t=lb2t+ch1
    elif lb1t=='' and lb2t=='':
        lb1t=''
        lb2t=''
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def divide():
    global lb1t
    global lb2t
    if lb1t!='' and lb2t=='':
        lb2t=lb1t+ch2
        lb1t=''
    elif lb1t!='' and lb2t!='':
        equal()
        lb2t=lb2t+ch2
        lb1t=''
    elif lb1t=='' and lb2t!=''and lb2t[-1] not in signs:
        lb1t=''
        lb2t=lb2t+ch2
    elif lb1t=='' and lb2t=='':
        lb1t=''
        lb2t=''
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def equal():
    global lb1t
    global lb2t
    if lb1t!='' and lb2t[-1] in signs:
        v1=float(lb2t[:-1])
        v2=float(lb1t)
        sign1=lb2t[-1]
        if sign1=='+':
            lb1t=''
            lb2t=str(v1+v2)
        if sign1=='-':
            lb1t=''
            lb2t=str(v1-v2)
        if sign1==ch1:
            lb1t=''
            lb2t=str(v1*v2)
        if sign1==ch2:
            lb1t=''
            try:
                lb2t=str(v1/v2)
            except:
                lb2t=''
    elif lb1t!='' and lb2t[-1] not in signs:
        lb2t=lb1t
        lb1t=''
    lb1.config(text='{}'.format(lb1t))
    lb2.config(text='{}'.format(lb2t))
def type20():
    type0()
    type0()
def bs():
    global lb1t
    if lb1t!='':
        lb1t=lb1t[:-1]
        lb1.config(text='{}'.format(lb1t))
window = Tk()
window.title('Calculator Plus')
window.minsize(420,450)
window.maxsize(420,450)
lb1=Label(window, text='',bg='white',fg='grey',font=('Times New Roman',20),width=23,bd=10)
lb1.grid(row=1,column=0,columnspan=4)
lb2=Label(window, text='',bg='white',fg='green',font=('Times New Roman',20),width=23,bd=10)
lb2.grid(row=0,column=0,columnspan=4)
b1=Button(window, text='1',command=type1,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b1.grid(row=5,column=0)
b2=Button(window, text='2',command=type2,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b2.grid(row=5,column=1)
b3=Button(window, text='3',command=type3,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b3.grid(row=5,column=2)
b4=Button(window, text='4',command=type4,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b4.grid(row=4,column=0)
b5=Button(window, text='5',command=type5,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b5.grid(row=4,column=1)
b6=Button(window, text='6',command=type6,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b6.grid(row=4,column=2)
b7=Button(window, text='7',command=type7,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b7.grid(row=3,column=0)
b8=Button(window, text='8',command=type8,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b8.grid(row=3,column=1)
b9=Button(window, text='9',command=type9,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b9.grid(row=3,column=2)
b10=Button(window, text='0',command=type0,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b10.grid(row=6,column=1)
b11=Button(window, text='+',command=plus,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b11.grid(row=3,column=3)
b12=Button(window, text='-',command=minus,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b12.grid(row=2,column=3)
b13=Button(window, text=ch1,command=cross,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b13.grid(row=2,column=2)
b14=Button(window, text=ch2,command=divide,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b14.grid(row=2,column=1)
b15=Button(window, text='=',command=equal,activebackground='green',width=5,height=3,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b15.grid(row=5,rowspan=2,column=3)
b16=Button(window, text='00',command=type20,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b16.grid(row=6,column=0)
b17=Button(window, text='.',command=typed,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b17.grid(row=6,column=2)
b18=Button(window, text='C',command=reset,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b18.grid(row=2,column=0)
b19=Button(window, text=ch3,command=bs,activebackground='green',width=5,bd=10,bg='black',fg='white',font=('Times New Roman',20))
b19.grid(row=4,column=3)
window.mainloop()
