from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox

root = Tk()
root.title("Income Tax Calculator")
root.geometry('1000x600')
root.maxsize(1000, 600)
font1 = ("Times", 14, "bold")
font2 = ("Times", 13, "bold")

def des_f1():
    f1.destroy()

f1 = Frame(root, height=600, width=1000)
f1.propagate(0)
f1.pack(side='top')

c = Canvas(f1, width=1000, height=600, bg="blue")
c.pack()
p1 = PhotoImage(file='front.gif')
c.create_image(0, 0, image=p1, anchor=NW)

Button(f1, text="Start", font=font1, foreground='white', command=des_f1, bg='#8b1c13', width=8, border=4).place(x=450,y=500)
                                                                                                                
def des_f2():
    f2.destroy()


f2 = Frame(root, height=600, width=1000, background='red')
f2.propagate(0)
f2.pack(side='top')

c = Canvas(f2, width=1000, height=600, bg="blue")
c.pack()
p2 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p2, anchor=NW)

l0 = Label(f2, text='Enter your details :-', font=font1)
l0.place(x=250, y=100)

l1 = Label(f2, text='Name', font=font1)
l1.place(x=250, y=140)
e1 = Entry(f2, width=50, border=2)
e1.place(x=450, y=140)

l2 = Label(f2, text='Contact', font=font1)
l2.place(x=250, y=180)
e2 = Entry(f2, width=50, border=2)
e2.place(x=450, y=180)

l3 = Label(f2, text='Email Id', font=font1)
l3.place(x=250, y=220)
e3 = Entry(f2, width=50, border=2)
e3.place(x=450, y=220)

Button(f2, text="Next", command=des_f2, width=10, border=4).place(x=500, y=300)


def tax_scheme():
    new_window = Toplevel(f2)
    new_window.title("Tax scheme")
    new_window.geometry("452x322")
    Label(new_window, text="This is a Tax scheme", image=logo).pack()


logo = PhotoImage(file="image.gif")
label = Label(f2, text="This is the main window")
label.pack(pady=10)
Button(f2, text="Check Taxes Scheme", command=tax_scheme).place(x=770, y=500)


def des_f3():
    f3.destroy()


f3 = Frame(root, height=600, width=1000, background='yellow')
f3.propagate(0)
f3.pack(side='top')

c = Canvas(f3, width=1000, height=600, bg="blue")
c.pack()
p3 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p3, anchor=NW)

l4 = Label(f3, text='Enter the required data (in INR) :-', font=font1)
l4.place(x=250, y=100)

l5 = Label(f3, text='Annual Income', font=font1)
l5.place(x=250, y=160)
e5 = Entry(f3, width=50, border=2)
e5.place(x=480, y=160)

l6 = Label(f3, text='Exemptions / deductions', font=font1)
l6.place(x=250, y=200)
e6 = Entry(f3, width=50, border=2)
e6.place(x=480, y=200)


def oldtax(ta):
    total = 0
    n = 0
    while ta > 0:
        if n == 1:
            if ta >= 250000:
                total = total + 250000 * 5 / 100
            else:
                total = total + ta * 5 / 100
        elif n == 2 or n == 3:
            if ta >= 250000:
                total = total + 250000 * 20 / 100
            else:
                total = total + ta * 20 / 100
        elif n == 4 :
            total = total + ta * 30 / 100
            break
        else:
            total = 0
        ta = ta - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess


def newtax(ta):
    total = 0
    n = 0
    while ta > 0:
        if n == 1:
            if ta >= 250000:
                total = total + 250000 * 5 / 100
            else:
                total = total + ta * 5 / 100
        elif n == 2:
            if ta >= 250000:
                total = total + 250000 * 10 / 100
            else:
                total = total + ta * 10 / 100
        elif n == 3:
            if ta >= 250000:
                total = total + 250000 * 15 / 100
            else:
                total = total + ta * 15 / 100
        elif n == 4:
            if ta >= 250000:
                total = total + 250000 * 20 / 100
            else:
                total = total + ta * 20 / 100
        elif n == 5:
            if ta >= 250000:
                total = total + 250000 * 25 / 100
            else:
                total = total + ta * 25 / 100
        elif n == 6:
            total = total + ta * 30 / 100
            break
        else:
            total = 0
        ta = ta - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess


def delete():
    l8 = Label(f3, text="                                                                                         ",
               font=font1,
               background="white")
    l8.place(x=480, y=300)
    l10 = Label(f3, text="                                                                                        ",
                font=font1,
                background="white")
    l10.place(x=480, y=340)
    l12 = Label(f3, text="                                                                                        ",
                font=font1,
                background="white")
    l12.place(x=480, y=380)
    l14 = Label(f3, text="                                                                                        ",
                font=font1,
                background="white")
    l14.place(x=480, y=420)


delete()


def calculate():
    delete()

    at = e5.get()
    ad = e6.get()
    ta = int(at) - int(ad)
    old = oldtax(ta)
    new = newtax(int(at))
    tax_save = abs(new - old)
    tax_save = round(tax_save, 2)
    if new > old:
        better = "old tax"
    elif ta <= 250000:
        better = "Income tax not applicable (Taxable income < 250000)"
    else:
        better = "new tax"

    l7 = Label(f3, text='Old tax', font=font1)
    l7.place(x=250, y=300)

    l8 = Label(f3, text=str(old), font=font1)
    l8.place(x=480, y=300)

    l9 = Label(f3, text='New tax', font=font1)
    l9.place(x=250, y=340)

    l10 = Label(f3, text=str(new), font=font1)
    l10.place(x=480, y=340)

    l11 = Label(f3, text='Tax saving', font=font1)
    l11.place(x=250, y=380)

    l12 = Label(f3, text=str(tax_save), font=font1)
    l12.place(x=480, y=380)

    l13 = Label(f3, text='better option', font=font1)
    l13.place(x=250, y=420)

    l14 = Label(f3, text=better, font=font1)
    l14.place(x=480, y=420)


Button(f3, text="Calculate", command=calculate, width=10, border=4).place(x=500, y=250)
Button(f3, text="Reset", command=delete, width=10, border=4).place(x=610, y=250)


def credit():
    messagebox.showinfo('Credits',
                        'Name\t\t\tReg. number\tRoll no.\n\nMohit Kumar Mahato\t11913514\t09\n\n'
                        'Rocky Sharaf\t\t11918040\t70\n\n'
                        'Qazi Maaz Arshad\t\t11906424\t26 \n\n'
                        'Special Thanks to Gagandeep Mam')


Button(f3, text="Credits", command=credit, foreground='white', font=font1, width=8, border=4, bg='#ad0414').place(x=630,  y=500)

def end():
    root.destroy() 

def exit_win():
    ans = mbox.askyesno('Exit', 'Are you sure?')
    if (ans):
        root.destroy()  

Button(f3, text="Exit", command=exit_win, foreground='white', width=8, font=font1, border=4, bg='#ad0414').place(x=800,y=500)                                                                                                             
                                                                                                           

root.mainloop()
