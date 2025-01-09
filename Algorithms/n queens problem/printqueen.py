import tkinter as tk
import time

def drawqueens(n,a):
    t=tk.Tk()
    t.title("N Queens Problem.")
    #t.geometry("600x600")
    t.canvas=tk.Canvas(t,width=75*n,height=75*n,bg='white')
    t.canvas.pack()

    for i in range(n):
        for j in range(n):
            x0 , y0 = i*75, j*75
            x1 , y1 = x0+75, y0+75
            color="white" if (i+j)%2==0 else "gray"
            t.canvas.create_rectangle(x0,y0,x1,y1,fill=color)

    for i in range(n):
        x , y = (a[i]-1)*75+37.5 , i*75+37.5
        t.canvas.create_text(x,y,text='♛',font=('Arial',36))
    
    return t
def des(t):
    t.destroy()

    
n=8
a=[4, 6, 8, 2, 7, 1, 5,3]
t=drawqueens(n,a)


