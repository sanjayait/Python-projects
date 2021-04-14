# Tutorial 17 Tic-Tac-Toe Game
from tkinter import *

root=Tk()
root.minsize(400,400)
root.resizable(0,0)

# Define function to change label of button
x=1
def show(b):
    global x
    x=x+1
    if x%2 == 0:
        if (b["text"]==""):
            b["text"]="O"
    else:
        if (b["text"]==""):
            b["text"]="X"
    # For Row 0        
    if btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O":
        btn1["bg"]="green"
        btn2["bg"]="green"
        btn3["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X":
        btn1["bg"]="green"
        btn2["bg"]="green"
        btn3["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Row 1       
    if btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O":
        btn4["bg"]="green"
        btn5["bg"]="green"
        btn6["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X":
        btn4["bg"]="green"
        btn5["bg"]="green"
        btn6["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Row 2       
    if btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O":
        btn7["bg"]="green"
        btn8["bg"]="green"
        btn9["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X":
        btn7["bg"]="green"
        btn8["bg"]="green"
        btn9["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Column 0        
    if btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O":
        btn1["bg"]="green"
        btn4["bg"]="green"
        btn7["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X":
        btn1["bg"]="green"
        btn4["bg"]="green"
        btn7["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Column 1       
    if btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O":
        btn2["bg"]="green"
        btn5["bg"]="green"
        btn8["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X":
        btn2["bg"]="green"
        btn5["bg"]="green"
        btn8["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Column 2       
    if btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O":
        btn3["bg"]="green"
        btn6["bg"]="green"
        btn9["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X":
        btn3["bg"]="green"
        btn6["bg"]="green"
        btn9["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Diagonal 1,5,9        
    if btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O":
        btn1["bg"]="green"
        btn5["bg"]="green"
        btn9["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X":
        btn1["bg"]="green"
        btn5["bg"]="green"
        btn9["bg"]="green"
        var.set("Player Two Is Winner.!!!")

    # For Diagonal 3,5,7        
    if btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O":
        btn3["bg"]="green"
        btn5["bg"]="green"
        btn7["bg"]="green"
        var.set("Player One Is Winner.!!!")
    
    if btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X":
        btn3["bg"]="green"
        btn5["bg"]="green"
        btn7["bg"]="green"
        var.set("Player Two Is Winner.!!!")

# Define reset function
def reset():
    global x
    btn1["text"]="";btn2["text"]="";btn3["text"]=""
    btn4["text"]="";btn5["text"]="";btn6["text"]=""
    btn7["text"]="";btn8["text"]="";btn9["text"]=""

    btn1["bg"]="lightblue";btn2["bg"]="lightblue";btn3["bg"]="lightblue"
    btn4["bg"]="lightblue";btn5["bg"]="lightblue";btn6["bg"]="lightblue"
    btn7["bg"]="lightblue";btn8["bg"]="lightblue";btn9["bg"]="lightblue"
    x=1
    var.set("")
    
# Create Button
# Row 0
btn1=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn1))
btn1.grid(row=0,column=0,)
btn2=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn2))
btn2.grid(row=0,column=1)
btn3=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn3))
btn3.grid(row=0,column=2)

# Row 1
btn4=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn4))
btn4.grid(row=1,column=0)
btn5=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn5))
btn5.grid(row=1,column=1)
btn6=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn6))
btn6.grid(row=1,column=2)

# Row 2
btn7=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn7))
btn7.grid(row=2,column=0)
btn8=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn8))
btn8.grid(row=2,column=1)
btn9=Button(root,text='',bg='lightblue',fg='black',width=25,height=5,command=lambda:show(btn9))
btn9.grid(row=2,column=2)

var=StringVar()
# Create Input Field
e1=Entry(root,font=("Arial",15),fg="green",textvariable=var)
e1.grid(row=3,column=0,columnspan=3,pady=25,ipady=10)

# Reset Button
btn10=Button(root,text='Reset',bg='lightgreen',fg='black',width=25,height=2,command=reset)
btn10.grid(row=4,column=0,columnspan=3)


root.mainloop()