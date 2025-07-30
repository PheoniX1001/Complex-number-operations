import tkinter as tk
import math
import fractions as fr
import matplotlib.pyplot as plt

root=tk.Tk()
root.title("Complex number calculator")
label1=tk.Label(root,text="",font=("Aerial"))
label2=tk.Label(root,text="",font=("Aerial"))
label3=tk.Label(root,text="",font=("Aerial"))
label4=tk.Label(root,text="",font=("Aerial"))

def add():
    z=complex(inp1.get())
    w=complex(inp2.get())
    s=z+w
    label1.configure(text=f"z+w = {s}")
    label1.pack()

def sub():
    z=complex(inp1.get())
    w=complex(inp2.get())
    s2=z-w
    label4.configure(text=f"z-w = {s2}")
    label4.pack()    


def pro():
    z=complex(inp1.get())
    w=complex(inp2.get())
    p=z*w
    label2.configure(text=f"z.w = {p}")
    label2.pack()

def div():
    z=complex(inp1.get())
    w=complex(inp2.get())
    d=(z/w)
    dv=complex((round(d.real,3)),(round(d.imag,3)))
    label3.configure(text=f"z/w = {dv}")
    label3.pack()    

def plot():
    z=complex(inp1.get())
    plt.figure()
    plt.annotate(f"z({z.real},{z.imag})",(z.real,z.imag))
    plt.plot([0,z.real],[0,z.imag],ls="-",color='r')
    w=complex(inp2.get())
    plt.annotate(f"w({w.real},{w.imag})",(w.real,w.imag))
    plt.plot([0,w.real],[0,w.imag],ls="-",color='b')

    s=z+w
    s2=z-w
    p=z*w
    d=(z/w)
    dv=complex((round(d.real,3)),(round(d.imag,3)))
    plt.annotate(f"z+w({s.real},{s.imag})",(s.real,s.imag))
    plt.plot([0,s.real],[0,s.imag],ls="--",color="g")
    plt.annotate(f"z.w({p.real},{p.imag})",(p.real,p.imag))
    plt.plot([0,p.real],[0,p.imag],ls="--",color="brown")
    plt.annotate(f"z/w({dv.real},{dv.imag})",(dv.real,dv.imag))
    plt.plot([0,dv.real],[0,dv.imag],ls="--",color="violet")
    plt.annotate(f"z-w({s2.real},{s2.imag})",(s2.real,s2.imag))
    plt.plot([0,s2.real],[0,s2.imag],ls="--",color="yellow")
    plt.title('Complex Number Graph')
    plt.ylabel('Im')
    plt.xlabel("Re")
    plt.legend()
    plt.show()


    
war=tk.Label(root,text="\t**Please write imaginary unit as 'j' instead of 'i'**")
war.pack()
t1=tk.Label(root,text="\nEnter complex number(z):")
t1.pack()
inp1=tk.Entry(root,width=20)    
inp1.focus_set()
inp1.pack()

t2=tk.Label(root,text="Enter another complex number(w):")
t2.pack()
inp2=tk.Entry(root,width=20)
inp2.focus_set()
inp2.pack()

bt=tk.Button(root,text="Close",command=root.quit)
sum=tk.Button(root,text="Add",command=add)
min=tk.Button(root,text='Subtract',command=sub)
mul=tk.Button(root,text="Multiply",command=pro)
divs=tk.Button(root,text="Divide",command=div)
sp=tk.Label(root,text="\n")
pl=tk.Button(root,text="Plot",command=plot)

sum.pack()
min.pack()
mul.pack()
divs.pack()
pl.pack()
bt.pack()
root.geometry('600x400')
root.mainloop()