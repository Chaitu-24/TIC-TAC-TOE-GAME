#BY CHAITANYA AND VISHWAK 
from tkinter import *
root = Tk()
root.geometry("900x900")
player="X"
ls=[i for i in range(1,10)]

def disableall():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,l1,l2
    l1["bg"]="white"
    l2["bg"]="white"
    btn1['state']=DISABLED
    btn2['state']=DISABLED
    btn3['state']=DISABLED
    btn4['state']=DISABLED
    btn5['state']=DISABLED
    btn6['state']=DISABLED
    btn7['state']=DISABLED
    btn8['state']=DISABLED
    btn9['state']=DISABLED

def func1():
    global ls
    c=0
    for i in ls:
        if i in ["X","O"]:
            continue
        else:
            c=1
            break
    if(c==1):
        return -1
    else:
        return 1


def check():
    global ls
    if(ls[0]==ls[1]==ls[2]):
        return ls[1]
    elif(ls[3]==ls[4]==ls[5]):
        return ls[4]
    elif(ls[7]==ls[8]==ls[6]):
        return ls[7]
    elif(ls[0]==ls[3]==ls[6]):
        return ls[0]
    elif(ls[1]==ls[4]==ls[7]):
        return ls[1]
    elif(ls[2]==ls[5]==ls[8]):
        return ls[2]
    elif(ls[0]==ls[4]==ls[8]):
        return ls[0]
    elif(ls[2]==ls[4]==ls[6]):
        return ls[2]
    else:
        return func1()
        
    

def click1():
 
    global btn1,player,ls
    btn1['state']=DISABLED
    btn1['text']=player
    if player=="X":
        btn1['bg']="RED"
        player="O"
        ls[0]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn1['bg']="BLUE"
        player="X"
        ls[0]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

        
        
        
def click2():
  
    global btn2,player,ls
    btn2['state']=DISABLED
    btn2['text']=player
    if player=="X":
        btn2['bg']="RED"
        player="O"
        ls[1]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn2['bg']="BLUE"
        player="X"
        ls[1]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click3():
    global btn3,player,ls
    btn3['state']=DISABLED
    btn3['text']=player
    if player=="X":
        btn3['bg']="RED"
        player="O"
        ls[2]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn3['bg']="BLUE"
        player="X"
        ls[2]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click4():

    global btn4,player,ls
    btn4['state']=DISABLED
    btn4['text']=player
    if player=="X":
        btn4['bg']="RED"
        player="O"
        ls[3]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn4['bg']="BLUE"
        player="X"
        ls[3]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click5():

    global btn5,player,ls
    btn5['state']=DISABLED
    btn5['text']=player
    if player=="X":
        btn5['bg']="RED"
        player="O"
        ls[4]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn5['bg']="BLUE"
        player="X"
        ls[4]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click6():

    global btn6,player,ls
    btn6['state']=DISABLED
    btn6['text']=player
    if player=="X":
        btn6['bg']="RED"
        player="O"
        ls[5]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn6['bg']="BLUE"
        player="X"
        ls[5]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click7():
    global btn7,player,ls
    btn7['state']=DISABLED
    btn7['text']=player
    if player=="X":
        btn7['bg']="RED"
        player="O"
        ls[6]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn7['bg']="BLUE"
        player="X"
        ls[6]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
def click8():
    global btn8,player,ls
    btn8['state']=DISABLED
    btn8['text']=player
    if player=="X":
        btn8['bg']="RED"
        player="O"
        ls[7]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn8['bg']="BLUE"
        player="X"
        ls[7]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()

def click9():
    global btn9,player,ls
    btn9['state']=DISABLED
    btn9['text']=player
    if player=="X":
        btn9['bg']="RED"
        player="O"
        ls[8]="X"
        l1["bg"]="white"
        l2["bg"]="green"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
    else:
        btn9['bg']="BLUE"
        player="X"
        ls[8]="O"
        l1["bg"]="green"
        l2["bg"]="white"
        if(check()=="X" or check()=="O" or check()==1):
            if(check()=="X"):
                l3["text"]="X WON THE MATCH"
                l3["bg"]="violet"
            if(check()=="O"):
                l3["text"]="O WON THE MATCH"
                l3["bg"]="violet"
            if(check()==1):
                l3["text"]="-----:)DRAW(:-----"
                l3["bg"]="violet"
            disableall()
            
def playagain():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,l1,l2,player,ls
    ls=[i for i in range(1,10)]
    player="X"
    btn1['bg']="white"
    btn1['state']=NORMAL
    btn2['bg']="white"
    btn2['state']=NORMAL
    btn3['bg']="white"
    btn3['state']=NORMAL
    btn4['bg']="white"
    btn4['state']=NORMAL
    btn5['bg']="white"
    btn5['state']=NORMAL
    btn6['bg']="white"
    btn6['state']=NORMAL
    btn7['bg']="white"
    btn7['state']=NORMAL
    btn8['bg']="white"
    btn8['state']=NORMAL
    btn9['bg']="white"
    btn9['state']=NORMAL
    l1["bg"]="green"
    l2["bg"]="white"
    btn1['text']=""
    btn2['text']=""
    btn3['text']=""
    btn4['text']=""
    btn5['text']=""
    btn6['text']=""
    btn7['text']=""
    btn8['text']=""
    btn9['text']=""
    l3["text"]="DO OR DIE"
    l3["bg"]="#ab23ff"

    

title=Label(root,text="PLAYER X",font=15,relief="groove",bg="green",width=20)
title.grid(row=1,column=0)

l1=Label(root,text="PLAYER X",font=15,relief="groove",bg="green",width=20)
l1.grid(row=1,column=0)
l2=Label(root,text="PLAYER O",font=15,relief="groove",width=20)
l2.grid(row=1,column=4)
l3=Label(root,text="",font=15,width=20)
l3.place(x=330,y=350)
#Button 1
btn1=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click1,padx=2)
btn1.grid(row=0,column=1)
#Button 2
btn2=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click2,padx=2)
btn2.grid(row=0,column=2)
#Button 3
btn3=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click3,padx=2)
btn3.grid(row=0,column=3)
#Button 4
btn4=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click4,padx=2)
btn4.grid(row=1,column=1)
#Button 5
btn5=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click5,padx=2)
btn5.grid(row=1,column=2)
#Button 6
btn6=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click6,padx=2)
btn6.grid(row=1,column=3)
#Button 7
btn7=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click7,padx=2)
btn7.grid(row=2,column=1)
#Button 8
btn8=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click8,padx=2)
btn8.grid(row=2,column=2)
#Button 9
btn9=Button(root,text=" ", font=('arial', 10), width=15,height=5,command=click9,padx=2)
btn9.grid(row=2,column=3)
#PLAY AGAIN BUTTON
pa=Button(root,text="PLAY AGAIN", font=('arial', 10), width=15,height=5,command=playagain,padx=2)
pa.place(x=370,y=380)
root.mainloop()
