from tkinter import *

window=Tk()
window.geometry("700x500")
window.title(" Product Bill")



def calculate():
    Raisin=e1.get()
    dried_date=e2.get()
    figs=e3.get()
    Cashewnuts=e4.get()
    total=(int(Raisin)*220 + int(dried_date)*180 + int(figs)*750 +int(Cashewnuts)*720)
    l12= Label(window, text=total , font=("Comic Sans MS", 20, "bold") , fg="Red", bg="Black")
    l12.place(x=160, y=360)



l6=Label(window,text="Welcome CB Dry Fruits !!",font=("Comic Sans MS", 30, "bold"))
l6.place(x=350,y=20,anchor="center")



#------------Menu Section-------------------------------------------------

l1=Label(window,text="Dryfruits",font=("Comic Sans MS", 20, "bold"))
l1.place(x=500,y=65)

l2=Label(window,text="Raisin               Rs.220/Kg",font=("Comic Sans MS", 12, "bold"))
l2.place(x=450,y=120)

l3=Label(window,text="dried date          Rs.180/Kg",font=("Comic Sans MS", 12, "bold"))
l3.place(x=450,y=150)

l4=Label(window,text="figs                 Rs.750/Kg",font=("Comic Sans MS", 12, "bold"))
l4.place(x=450,y=180)

l5=Label(window,text="Cashewnuts         Rs.720/Kg",font=("Comic Sans MS", 12, "bold"))
l5.place(x=450,y=210)

#-------------------------billing sections-----------------------------



l7=Label(window,text="Select Items",font=("Comic Sans MS", 14, "bold"))
l7.place(x=150,y=70 ,)

l8=Label(window,text="Raisin",font=("Comic Sans MS", 14 ))
l8.place(x=20,y=120)

e1=Entry(window)
e1.place(x=20,y=150)

l9=Label(window,text="Dried date",font=("Comic Sans MS", 14 ))
l9.place(x=250,y=120)

e2=Entry(window)
e2.place(x=250,y=150)

l10=Label(window,text="Figs",font=("Comic Sans MS", 14 ))
l10.place(x=250,y=200)

e3=Entry(window)
e3.place(x=250,y=230)

l11=Label(window,text="Cashewnuts",font=("Comic Sans MS", 14 ))
l11.place(x=20,y=200)

e4=Entry(window)
e4.place(x=20,y=230)




b2=Button(window, text="Generate the Bill",width=20 , command = calculate , font=("Comic Sans MS", 14 ))
b2.place(x=90,y=300 ,)





window.mainloop()