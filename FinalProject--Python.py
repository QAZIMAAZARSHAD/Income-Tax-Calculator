from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import re
import tkinter as tk

root = Tk()
root.title("Income Tax Calculator")
root.geometry('1000x600')
root.maxsize(1000, 600)
root.minsize(1000, 600)
font1 = ("Times", 14, "bold")
font2 = ("Times", 13, "bold")


# Features

# Calculation of Tax Scheme's

# To calculate tax's with old Scheme

def old_tax(ta):
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
        elif n == 4:
            total = total + ta * 30 / 100
            break
        else:
            total = 0
        ta = ta - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess


# To calculate

def new_tax(amount):
    total = 0
    n = 0
    while amount > 0:
        if n == 1:
            if amount >= 250000:
                total = total + 250000 * 5 / 100
            else:
                total = total + amount * 5 / 100
        elif n == 2:
            if amount >= 250000:
                total = total + 250000 * 10 / 100
            else:
                total = total + amount * 10 / 100
        elif n == 3:
            if amount >= 250000:
                total = total + 250000 * 15 / 100
            else:
                total = total + amount * 15 / 100
        elif n == 4:
            if amount >= 250000:
                total = total + 250000 * 20 / 100
            else:
                total = total + amount * 20 / 100
        elif n == 5:
            if amount >= 250000:
                total = total + 250000 * 25 / 100
            else:
                total = total + amount * 25 / 100
        elif n == 6:
            total = total + amount * 30 / 100
            break
        else:
            total = 0
        amount = amount - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess


# calculating and Displaying tax's

def calculate_tax():
    delete()

    amount_taxable = entity5.get()
    amount_deduction = entity6.get()
    total_amount = int(amount_taxable) - int(amount_deduction)
    old_tax_amount = old_tax(total_amount)
    new_tax_amount = new_tax(int(total_amount))
    tax_save = abs(new_tax_amount - old_tax_amount)
    tax_save = round(tax_save, 2)
    if new_tax_amount > old_tax_amount:
        better = "old tax"
    elif total_amount <= 250000:
        better = "Income tax not applicable (Taxable income < 250000)"
    else:
        better = "new tax"

    if int(amount_deduction) > int(amount_taxable):
        old = 0
        new = 0
        tax_save = 0.0
        better = "Deductions cannot be more than income"
        det = " Enter the details correctly!!! "
        er1 = Label(frame3, text=det, font=font1, bg='white', fg='red')
        er1.place(x=500, y=100)

    label7 = Label(frame3, text='Old tax', font=font1)
    label7.place(x=250, y=300)

    label8 = Label(frame3, text=str(old), font=font1)
    label8.place(x=480, y=300)

    label9 = Label(frame3, text='New tax', font=font1)
    label9.place(x=250, y=340)

    label10 = Label(frame3, text=str(new), font=font1)
    label10.place(x=480, y=340)

    label11 = Label(frame3, text='Tax saving', font=font1)
    label11.place(x=250, y=380)

    label12 = Label(frame3, text=str(tax_save), font=font1)
    label12.place(x=480, y=380)

    label13 = Label(frame3, text='better option', font=font1)
    label13.place(x=250, y=420)

    label14 = Label(frame3, text=better, font=font1)
    label14.place(x=480, y=420)


# To Display both old and new Tax Scheme's

def tax_scheme():
    new_window = Toplevel(frame2)
    new_window.title("Tax scheme")
    new_window.geometry("452x322")
    # Removing maximize/minimize option from "Check Tax Scheme" pop-up.
    new_window.resizable(0, 0)
    Label(new_window, text="This is a Tax scheme", image=logo).pack()


# This is to show user Details
def display_user_details():
    messagebox.showinfo('Details',
                        'Name : ' + user_name.get() + '\n\n'
                                                      'Contact : ' + user_contact.get() + '\n\n'
                                                                                          'Email Id : ' + user_emailId.get() + '\n\n'
                        )


# To display Credits

def credit():
    messagebox.showinfo('Credits',
                        'Name\t\t\tReg. number\tRoll no.\n\nMohit Kumar Mahato\t11913514\t09\n\n'
                        'Rocky Sharaf\t\t11918040\t70\n\n'
                        'Qazi Maaz Arshad\t\t11906424\t26 \n\n'
                        'Special Thanks to Gagandeep Mam')


# To display Info Button

def learn_more():
    with open("learnMoreReadme.txt") as f:
        # reading file
        readme = f.read()

        # Display whole message
        messagebox.showinfo(title="Title",
                            message=str(readme))


# Validate User Input Data

# This is to validate email

def email_validator(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


# This is to Validate Contact Number

def contact_validator(number):
    regex = '^[0-9]{10}$'
    if re.search(regex, number):
        return True
    else:
        return False


# This is to validate Name

def name_validator(name):
    if re.search('^[a-zA-z\s]+$', name):
        return True
    else:
        return False


# Destroying Frames


def delete():
    label8 = Label(frame3,
                   text="                                                                                         ",
                   font=font1,
                   background="white")
    label8.place(x=480, y=300)
    label10 = Label(frame3,
                    text="                                                                                        ",
                    font=font1,
                    background="white")
    label10.place(x=480, y=340)
    label12 = Label(frame3,
                    text="                                                                                        ",
                    font=font1,
                    background="white")
    label12.place(x=480, y=380)
    label14 = Label(frame3,
                    text="                                                                                        ",
                    font=font1,
                    background="white")
    label14.place(x=480, y=420)

    # destroying the below label
    error1 = Label(frame3,
                   text="                                                                                        ",
                   font=font1,
                   background="white")
    error1.place(x=600, y=100)


def destroy_frame1():
    frame1.destroy()


def destroy_frame2():
    user_input_name = entity1.get()
    user_input_contact = entity2.get()
    user_input_email = entity3.get()

    # Validating Inputs
    if len(user_input_name) == 0 or len(user_input_contact) == 0 or len(user_input_email) == 0:
        messagebox.showerror("Invalid Details", "Please enter your Details.")
    else:
        if not name_validator(user_input_name):
            messagebox.showerror("Invalid Name", "You have used an illegal input, try again")
        elif not contact_validator(user_input_contact):
            messagebox.showerror("Invalid Number",
                                 "Please enter only numbers that are 10 digits long and shouldnt contain any other charecters")
        elif not email_validator(user_input_email):
            messagebox.showerror("Invalid Email ID", "Please enter correct Email ID")
        else:
            frame2.destroy()


def destroy_frame3():
    frame3.destroy()


def clear1():
    entity1.delete(0, END)
    entity1.insert(0, "")
    entity2.delete(0, END)
    entity2.insert(0, "")
    entity3.delete(0, END)
    entity3.insert(0, "")


def end():
    root.destroy()


def exit_win():
    choice = mbox.askyesno('Exit', 'Are you sure?')
    if choice:
        root.destroy()


def clear2():
    entity5.delete(0, END)
    entity5.insert(0, "")
    entity6.delete(0, END)
    entity6.insert(0, "")

###############################################

# UI

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


frame1 = Frame(root, height=600, width=1000)
frame1.propagate(0)
frame1.pack(side='top')

c = Canvas(frame1, width=1000, height=600, bg="blue")
c.pack()
p1 = PhotoImage(file='front.gif')
c.create_image(0, 0, image=p1, anchor=NW)

HoverButton(frame1, text="Start", activebackground="#6382b8", cursor="hand2", font=font1, foreground='white',
            command=destroy_frame1, bg='#8b1c13', width=8, border=4).place(x=450, y=500)

user_name = StringVar(root)
user_contact = StringVar(root)
user_emailId = StringVar(root)

frame2 = Frame(root, height=600, width=1000, background='red')
frame2.propagate(0)
frame2.pack(side='top')

c = Canvas(frame2, width=1000, height=600, bg="blue")
c.pack()
p2 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p2, anchor=NW)

label0 = Label(frame2, text='Enter your details :-', font=font1)
label0.place(x=250, y=100)

label1 = Label(frame2, text='Name', font=font1)
label1.place(x=250, y=140)
entity1 = Entry(frame2, textvariable=user_name, width=50, border=2)
entity1.place(x=450, y=140)

label2 = Label(frame2, text='Contact', font=font1)
label2.place(x=250, y=180)
entity2 = Entry(frame2, textvariable=user_contact, width=50, border=2)
entity2.place(x=450, y=180)

label3 = Label(frame2, text='Email Id', font=font1)
label3.place(x=250, y=220)
entity3 = Entry(frame2, textvariable=user_emailId, width=50, border=2)
entity3.place(x=450, y=220)

HoverButton(frame2, text="Next", activebackground="#6382b8", cursor="hand2", command=destroy_frame2, width=10,
            border=4).place(
    x=500, y=300)
HoverButton(frame2, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear1, width=10, border=4).place(
    x=600, y=300)

logo = PhotoImage(file="image.gif")
label = Label(frame2, text="This is the main window")
label.pack(pady=10)
HoverButton(frame2, text="Check Taxes Scheme", activebackground="#6382b8", cursor="hand2", command=tax_scheme).place(
    x=770,
    y=500)

frame3 = Frame(root, height=600, width=1000, background='yellow')
frame3.propagate(0)
frame3.pack(side='top')

c = Canvas(frame3, width=1000, height=600, bg="blue")
c.pack()
p3 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p3, anchor=NW)

label4 = Label(frame3, text='Enter the required data (in INR) :-', font=font1)
label4.place(x=250, y=100)

label5 = Label(frame3, text='Annual Income', font=font1)
label5.place(x=250, y=160)
entity5 = Entry(frame3, width=50, border=2)
entity5.place(x=480, y=160)

label6 = Label(frame3, text='Exemptions / deductions', font=font1)
label6.place(x=250, y=200)
entity6 = Entry(frame3, width=50, border=2)
entity6.place(x=480, y=200)

delete()

HoverButton(frame3, text="Calculate", activebackground="#6382b8", cursor="hand2", command=calculate_tax, width=10,
            border=4).place(x=500, y=250)
HoverButton(frame3, text="Reset", activebackground="#6382b8", cursor="hand2", command=delete, width=10, border=4).place(
    x=610, y=250)
HoverButton(frame3, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear2, width=10, border=4).place(
    x=720, y=250)

HoverButton(frame3, text="Learn More", activebackground="#6382b8", cursor="hand2", command=learn_more,
            foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=280, y=500)

HoverButton(frame3, text="User Details", activebackground="#6382b8", cursor="hand2", command=display_user_details,
            foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=450, y=500)
HoverButton(frame3, text="Credits", activebackground="#6382b8", cursor="hand2", command=credit, foreground='white',
            font=font1, width=8, border=4, bg='#ad0414').place(x=630, y=500)

HoverButton(frame3, text="Exit", cursor="hand2", activebackground="#6382b8", command=exit_win, foreground='white',
            width=8,
            font=font1, border=4, bg='#ad0414').place(x=800, y=500)

root.mainloop()
