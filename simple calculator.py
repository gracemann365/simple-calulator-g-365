"""hey,i'm @gracemann
this is my maiden project 
review this and gimme all the feedback u can !!!!

using Tkinter gui library
tkinter is an interface to tk gui toolkit"""

from graphlib import TopologicalSorter
from pydoc_data import topics
import tkinter as tk
from turtle import color  # using tkinter gui toolkit



#all the functions you need to perform calculation

calculation =""
def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end") #deleting pre existing content to insert calculated result
    text_result.insert(1.0,calculation)

def evaluate_cal():
    global calculation
    try:
    
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")


#gui and intreaction

root=tk.Tk(className="Calculator-simple")
root.geometry("300x395")
root['bg']='black'



text_result=tk.Text(root,height=3,width=35,font=("Arial,16"))
text_result.grid(columnspan=6)
text_result['bg']='grey'
#buttons  : actions and positions using grid

#digits
btn_1=tk.Button(root,text="1",fg="orange" ,bg="black",command=lambda:add_to_cal(1),width=5,font=("Arial",14),bd=10)
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",fg="orange" ,bg="black",command=lambda:add_to_cal(2),width=5,font=("Arial",14),bd=10)
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",fg="orange",bg="black",command=lambda:add_to_cal(3),width=5,font=("Arial",14),bd=10)
btn_3.grid(row=3,column=1)

btn_4=tk.Button(root,text="4",fg="orange" ,bg="black",command=lambda:add_to_cal(4),width=5,font=("Arial",14),bd=10)
btn_4.grid(row=3,column=2)

btn_5=tk.Button(root,text="5",fg="orange" ,bg="black",command=lambda:add_to_cal(5),width=5,font=("Arial",14),bd=10)
btn_5.grid(row=4,column=1)

btn_6=tk.Button(root,text="6",fg="orange" ,bg="black",command=lambda:add_to_cal(6),width=5,font=("Arial",14),bd=10)
btn_6.grid(row=4,column=2)

btn_7=tk.Button(root,text="7",fg="orange" ,bg="black",command=lambda:add_to_cal(7),width=5,font=("Arial",14),bd=10)
btn_7.grid(row=5,column=1)

btn_8=tk.Button(root,text="8",fg="orange" ,bg="black",command=lambda:add_to_cal(8),width=5,font=("Arial",14),bd=10)
btn_8.grid(row=5,column=2)

btn_9=tk.Button(root,text="9",fg="orange" ,bg="black",command=lambda:add_to_cal(9),width=5,font=("Arial",14),bd=10)
btn_9.grid(row=6,column=1)

btn_0=tk.Button(root,text="0",fg="orange" ,bg="black",command=lambda:add_to_cal(0),width=5,font=("Arial",14),activebackground="red",bd=10)
btn_0.grid(row=6,column=2)


#operators
btn_plus=tk.Button(root,text="+",command=lambda:add_to_cal("+"),width=5,font=("Arial",14),bg="orange",bd=10)
btn_plus.grid(row=2,column=3)

btn_minus=tk.Button(root,text="-",command=lambda:add_to_cal("-"),width=5,font=("Arial",14),bg="orange",bd=10)
btn_minus.grid(row=3,column=3)

btn_div=tk.Button(root,text="/",command=lambda:add_to_cal("/"),width=5,font=("Arial",14),bg="orange",bd=10)
btn_div.grid(row=4,column=3)

btn_mul=tk.Button(root,text="*",command=lambda:add_to_cal("*"),width=5,font=("Arial",14),bg="orange",bd=10)
btn_mul.grid(row=5,column=3)


#others
btn_openPara=tk.Button(root,text="(",command=lambda:add_to_cal("("),width=5,font=("Arial",14),bg="orange",bd=10)
btn_openPara.grid(row=7,column=1)

btn_closePara=tk.Button(root,text=")",command=lambda:add_to_cal(")"),width=5,font=("Arial",14),bg="orange",bd=10)
btn_closePara.grid(row=7,column=2)

btn_equals=tk.Button(root,text="=",command=evaluate_cal,width=5,font=("Arial",14),bg="orange",bd=10)#CALLING REAL FUNCTIONS
btn_equals.grid(row=6,column=3)

btn_clear=tk.Button(root,text="C",command=clear_field,width=5,font=("Arial",14),bg="red",bd=10)
btn_clear.grid(row=7,column=3)

root.mainloop()
