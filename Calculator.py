from tkinter import *


root = Tk()
root.title("CALCULATOR")

sign = ""
fnum = None

def clicked(num): 
    current = take1.get()
    take1.delete(0,END)
    take1.insert(0,str(current) + str(num))
    
def add():
    f1num  = take1.get()
    take1.delete(0,END)
    global fnum 
    global sign 
    fnum = int(f1num)
    sign = "+"
        
def sub():
    f1num  = take1.get()
    global fnum 
    global sign 
    fnum = int(f1num)
    sign = "-"
    take1.delete(0,END)
    
def mul():
    f1num  = take1.get()
    global fnum 
    global sign 
    fnum = int(f1num)
    sign = "*"
    take1.delete(0,END)
     
def div():
    f1num  = take1.get()
    global fnum 
    global sign 
    fnum = int(f1num)
    sign = "/"
    take1.delete(0,END)
    
def pow():
    f1num  = take1.get()
    global fnum 
    global sign 
    fnum = int(f1num)
    sign = "^"
    take1.delete(0,END) 
    
def answer():
    second_N = take1.get()
    take1.delete(0,END)
    
    if sign == "+":
        return take1.insert(0,fnum + int(second_N))    
    elif sign == "-":
        return take1.insert(0,fnum - int(second_N))
    elif sign == "*":
        return take1.insert(0,fnum * int(second_N))
    elif sign == "/":
        return take1.insert(0,fnum / int(second_N))
    elif sign == "^":
        return take1.insert(0,fnum ** int(second_N))
    else:                
        return take1.insert(0,"Invalid operation")
    
take1 = Entry (root, width=40, borderwidth=5)
take1.grid(row=0, column=0, padx= 10, pady=10, columnspan=4)
# for textbox hint
take1.insert(0,"")    

#hides the hint and second lambda replaces input with *
#take1.bind('<FocusIn>', lambda e1 : take1.delete(0,'end'), lambda e2 : take1.config(show="*"))
       
clearB = Button (root, text="Clear", padx =25, pady =10, command= lambda : take1.delete(0,END) ,bg="Grey",width=4)
clearB.grid(row=0,column=3)

       
#NUMBER BUTTONS
numB1 = Button (root, text="1", padx =25, pady =10, command= lambda : clicked(1),bg="Grey",width=4)
numB1.grid(row=1,column=0)
numB2 = Button (root, text="2", padx =25, pady =10, command= lambda : clicked(2),bg="Grey",width=4)
numB2.grid(row=1,column=1)
numB3 = Button (root, text="3", padx =25, pady =10, command= lambda : clicked(3),bg="Grey",width=4)
numB3.grid(row=1,column=2)

numB4 = Button (root, text="4", padx =25, pady =10, command= lambda : clicked(4),bg="Grey",width=4)
numB4.grid(row=2,column=0)
numB5 = Button (root, text="5", padx =25, pady =10, command= lambda : clicked(5),bg="Grey",width=4)
numB5.grid(row=2,column=1)
numB6 = Button (root, text="6", padx =25, pady =10, command= lambda : clicked(6),bg="Grey",width=4)
numB6.grid(row=2,column=2)

numB7 = Button (root, text="7", padx =25, pady =10, command= lambda : clicked(7),bg="Grey",width=4)
numB7.grid(row=3,column=0)
numB8 = Button (root, text="8", padx =25, pady =10, command= lambda : clicked(8),bg="Grey",width=4)
numB8.grid(row=3,column=1)
numB9 = Button (root, text="9", padx =25, pady =10, command= lambda : clicked(9),bg="Grey",width=4)
numB9.grid(row=3,column=2)

numB0 = Button (root, text="0", padx =25, pady =10, command= lambda : clicked(0),bg="Grey",width=4)
numB0.grid(row=4,column=0)

# OPERATOR BUTTONS
equB = Button (root,text="=",command=answer,bg="Grey",width=4, padx =25, pady =10,)
equB.grid(row=4,column=1)

addB = Button(root,text="+",command=add,bg="Grey",width=4, padx =25, pady =10,)
addB.grid(row=1,column=3)

subB = Button(root,text="-",command=sub,bg="Grey", width=4, padx =25, pady =10,)
subB.grid(row=2,column=3)

mulB = Button(root,text="*",command=mul,bg="Grey",width=4, padx =25, pady =10,)
mulB.grid(row=3,column=3)

divB = Button(root,text="/",command=div,bg="Grey",width=4, padx =25, pady =10,)
divB.grid(row=4,column=3)

powB = Button(root,text="^",command=pow,bg="Grey",width=4, padx =25, pady =10,)
powB.grid(row=4,column=2)


root.mainloop()
