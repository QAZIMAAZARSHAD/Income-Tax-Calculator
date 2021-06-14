from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk

root = Tk()
root.title("Income Tax Calculator")
root.geometry('1000x600')
root.maxsize(1000, 600)
root.minsize(1000, 600)
font1 = ("Times", 14, "bold")
font2 = ("Times", 13, "bold")


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


def destroy_frame1():
    frame1.destroy()


frame1 = Frame(root, height=600, width=1000)
frame1.propagate(0)
frame1.pack(side='top')

canva = Canvas(frame1, width=1000, height=600, bg="blue")
canva.pack()
p1 = PhotoImage(file='front.gif')
canva.create_image(0, 0, image=p1, anchor=NW)

HoverButton(frame1, text="Start", activebackground="#6382b8", cursor="hand2", font=font1, foreground='white',
            command=destroy_frame1, bg='#8b1c13', width=8, border=4).place(x=450, y=500)


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


def check_contact(number):
    regex = '^[0-9]{10}$'
    if re.search(regex, number):
        return True
    else:
        return False


def check_name(name):
    if re.search('^[a-zA-z\s]+$', name):
        return True
    else:
        return False


def destroy_frame2():
    user_name = entity1.get()
    user_contact = entity2.get()
    user_email = entity3.get()

    # Validating Correct Inputs
    if len(user_name) == 0 or len(user_contact) == 0 or len(user_email) == 0:
        messagebox.showerror("Invalid Details", "Please enter your Details.")
    else:
        if not check_name(user_name):
            messagebox.showerror("Invalid Name", "You have used an illegal input, try again")
        elif not check_contact(user_contact):
            messagebox.showerror("Invalid Number",
                                 "Please enter only numbers that are 10 digits long and shouldnt contain any other charecters")
        elif not check_email(user_email):
            messagebox.showerror("Invalid Email ID", "Please enter correct Email ID")
        else:
            frame2.destroy()


my_name = StringVar(root)
my_contact = StringVar(root)
my_emailId = StringVar(root)

first_click_1 = True


def on_e1_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click_1

    if first_click_1:  # if this is the first time they clicked it
        first_click_1 = False
        entity1.delete(0, "end")  # delete all the text in the entry


first_click_2 = True


def on_e2_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click_2

    if first_click_2:  # if this is the first time they clicked it
        first_click_2 = False
        entity2.delete(0, "end")  # delete all the text in the entry


first_click_3 = True


def on_e3_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click_3

    if first_click_3:  # if this is the first time they clicked it
        first_click_3 = False
        entity3.delete(0, "end")  # delete all the text in the entry


frame2 = Frame(root, height=600, width=1000, background='red')
frame2.propagate(0)
frame2.pack(side='top')

canva = Canvas(frame2, width=1000, height=600, bg="blue")
canva.pack()
p2 = PhotoImage(file='back.gif')
canva.create_image(0, 0, image=p2, anchor=NW)

label0 = Label(frame2, text='Enter your details :-', font=font1)
label0.place(x=250, y=100)

label1 = Label(frame2, text='Name', font=font1)
label1.place(x=250, y=140)
entity1 = Entry(frame2, textvariable=my_name, width=50, border=2)
entity1.insert(0, 'Enter Your Name...')
entity1.bind('<FocusIn>', on_e1_click)
entity1.place(x=450, y=140)

label2 = Label(frame2, text='Contact', font=font1)
label2.place(x=250, y=180)
entity2 = Entry(frame2, textvariable=my_contact, width=50, border=2)
entity2.insert(0, 'Enter Your Contact...')
entity2.bind('<FocusIn>', on_e2_click)
entity2.place(x=450, y=180)

label3 = Label(frame2, text='Email Id', font=font1)
label3.place(x=250, y=220)
entity3 = Entry(frame2, textvariable=my_emailId, width=50, border=2)
entity3.insert(0, 'Enter Your Email Id...')
entity3.bind('<FocusIn>', on_e3_click)
entity3.place(x=450, y=220)


def clear1():
    entity1.delete(0, END)
    entity1.insert(0, "")
    entity2.delete(0, END)
    entity2.insert(0, "")
    entity3.delete(0, END)
    entity3.insert(0, "")


HoverButton(frame2, text="Next", activebackground="#6382b8", cursor="hand2", command=destroy_frame2, width=10,
            border=4).place(
    x=500, y=300)
HoverButton(frame2, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear1, width=10, border=4).place(
    x=600, y=300)


def tax_scheme():
    new_window = Toplevel(frame2)
    new_window.title("Tax scheme")
    new_window.geometry("452x322")
    # Removing maximize/minimize option from "Check Tax Scheme" pop-up.
    new_window.resizable(0, 0)
    Label(new_window, text="This is a Tax scheme", image=logo).pack()


logo = PhotoImage(file="image.gif")
label = Label(frame2, text="This is the main window")
label.pack(pady=10)
HoverButton(frame2, text="Check Taxes Scheme", activebackground="#6382b8", cursor="hand2", command=tax_scheme).place(x=770,
                                                                                                                     y=500)


def destroy_frame3():
    frame3.destroy()


def details():
    messagebox.showinfo('Details',
                        'Name : ' + my_name.get() + '\n\n'
                                                    'Contact : ' + my_contact.get() + '\n\n'
                                                                                      'Email Id : ' + my_emailId.get() + '\n\n'
                        )


firstclick5 = True


def on_e5_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick5

    if firstclick5:  # if this is the first time they clicked it
        firstclick5 = False
        entity5.delete(0, "end")  # delete all the text in the entry


firstclick6 = True


def on_e6_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick6

    if firstclick6:  # if this is the first time they clicked it
        firstclick6 = False
        entity6.delete(0, "end")  # delete all the text in the entry


frame3 = Frame(root, height=600, width=1000, background='yellow')
frame3.propagate(0)
frame3.pack(side='top')

canva = Canvas(frame3, width=1000, height=600, bg="blue")
canva.pack()
p3 = PhotoImage(file='back.gif')
canva.create_image(0, 0, image=p3, anchor=NW)

label4 = Label(frame3, text='Enter the required data (in INR) :-', font=font1)
label4.place(x=250, y=100)

label5 = Label(frame3, text='Annual Income', font=font1)
label5.place(x=250, y=160)
entity5 = Entry(frame3, width=50, border=2)
entity5.insert(0, 'Enter Your Annual Income...')
entity5.bind('<FocusIn>', on_e5_click)
entity5.place(x=480, y=160)

label6 = Label(frame3, text='Exemptions / Deductions', font=font1)
label6.place(x=250, y=200)
entity6 = Entry(frame3, width=50, border=2)
entity6.insert(0, 'Enter Your Exemptions / deductions...')
entity6.bind('<FocusIn>', on_e6_click)
entity6.place(x=480, y=200)


def old_tax(taxable_amount):
    total_tax = 0
    n = 0
    while taxable_amount > 0:
        if n == 1:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 5 / 100
            else:
                total_tax = total_tax + taxable_amount * 5 / 100
        elif n == 2 or n == 3:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 20 / 100
            else:
                total_tax = total_tax + taxable_amount * 20 / 100
        elif n == 4:
            total_tax = total_tax + taxable_amount * 30 / 100
            break
        else:
            total_tax = 0
        taxable_amount = taxable_amount - 250000
        n = n + 1
    cess = total_tax * 4 / 100
    return total_tax + cess


def new_tax(taxable_amount):
    total_tax = 0
    n = 0
    while taxable_amount > 0:
        if n == 1:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 5 / 100
            else:
                total_tax = total_tax + taxable_amount * 5 / 100
        elif n == 2:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 10 / 100
            else:
                total_tax = total_tax + taxable_amount * 10 / 100
        elif n == 3:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 15 / 100
            else:
                total_tax = total_tax + taxable_amount * 15 / 100
        elif n == 4:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 20 / 100
            else:
                total_tax = total_tax + taxable_amount * 20 / 100
        elif n == 5:
            if taxable_amount >= 250000:
                total_tax = total_tax + 250000 * 25 / 100
            else:
                total_tax = total_tax + taxable_amount * 25 / 100
        elif n == 6:
            total_tax = total_tax + taxable_amount * 30 / 100
            break
        else:
            total_tax = 0
        taxable_amount = taxable_amount - 250000
        n = n + 1
    cess = total_tax * 4 / 100
    return total_tax + cess


def delete():
    label8 = Label(frame3, text="                                                                                         ",
               font=font1,
               background="white")
    label8.place(x=480, y=300)
    label10 = Label(frame3, text="                                                                                        ",
                font=font1,
                background="white")
    label10.place(x=480, y=340)
    label12 = Label(frame3, text="                                                                                        ",
                font=font1,
                background="white")
    label12.place(x=480, y=380)
    label14 = Label(frame3, text="                                                                                        ",
                font=font1,
                background="white")
    label14.place(x=480, y=420)
    # destroying the below label
    er1 = Label(frame3, text="                                                                                        ",
                font=font1,
                background="white")
    er1.place(x=600, y=100)


delete()


def clear2():
    entity5.delete(0, END)
    entity5.insert(0, "")
    entity6.delete(0, END)
    entity6.insert(0, "")


def calculate():
    delete()

    amount_taxable = entity5.get()
    amount_deduction = entity6.get()
    try:
        total_taxable_amount = int(amount_taxable) - int(amount_deduction)
    except:
        messagebox.showerror("Invalid Input", "Please enter valid Annual Tax and/or Exemption.")
        return 0
    old_tax_amount = old_tax(total_taxable_amount)
    new_tax_amount = new_tax(int(total_taxable_amount))
    tax_save = abs(new_tax_amount - old_tax_amount)
    tax_save = round(tax_save, 2)
    if new_tax_amount > old_tax_amount:
        better = "Old tax"
    elif total_taxable_amount <= 250000:
        better = "Income tax not applicable (Taxable income < 250000)"
    else:
        better = "New tax"

    if int(amount_deduction) > int(amount_taxable):
        old_tax_amount = 0
        new_tax_amount = 0
        tax_save = 0.0
        better = "Deductions cannot be more than income"
        det = " Enter the details correctly!!! "
        er1 = Label(frame3, text=det, font=font1, bg='white', fg='red')
        er1.place(x=500, y=100)

    label7 = Label(frame3, text='Old tax', font=font1)
    label7.place(x=250, y=300)

    label8 = Label(frame3, text=str(old_tax_amount), font=font1)
    label8.place(x=480, y=300)

    label9 = Label(frame3, text='New tax', font=font1)
    label9.place(x=250, y=340)

    label10 = Label(frame3, text=str(new_tax_amount), font=font1)
    label10.place(x=480, y=340)

    label11 = Label(frame3, text='Tax saving', font=font1)
    label11.place(x=250, y=380)

    label12 = Label(frame3, text=str(tax_save), font=font1)
    label12.place(x=480, y=380)

    label13 = Label(frame3, text='Better option', font=font1)
    label13.place(x=250, y=420)

    label14 = Label(frame3, text=better, font=font1)
    label14.place(x=480, y=420)


HoverButton(frame3, text="Calculate", activebackground="#6382b8", cursor="hand2", command=calculate, width=10,
            border=4).place(x=500, y=250)
HoverButton(frame3, text="Reset", activebackground="#6382b8", cursor="hand2", command=delete, width=10, border=4).place(
    x=610, y=250)
HoverButton(frame3, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear2, width=10, border=4).place(
    x=720, y=250)


def credit():
    messagebox.showinfo('Credits',
                        'Name\t\t\tReg. number\tRoll no.\n\nMohit Kumar Mahato\t11913514\t09\n\n'
                        'Rocky Sharaf\t\t11918040\t70\n\n'
                        'Qazi Maaz Arshad\t\t11906424\t26 \n\n'
                        'Special Thanks to Gagandeep Mam')


def learn_more():
    with open("learnMoreReadme.txt") as f:
        # reading file
        readme = f.read()

        # Display whole message
        messagebox.showinfo(title="Title",
                            message=str(readme))


HoverButton(frame3, text="Learn More", activebackground="#6382b8", cursor="hand2", command=learn_more,
            foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=280, y=500)

HoverButton(frame3, text="User Details", activebackground="#6382b8", cursor="hand2", command=details, foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=450, y=500)
HoverButton(frame3, text="Credits", activebackground="#6382b8", cursor="hand2", command=credit, foreground='white',
            font=font1, width=8, border=4, bg='#ad0414').place(x=630, y=500)


def end():
    root.destroy()


def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()


HoverButton(frame3, text="Exit", cursor="hand2", activebackground="#6382b8", command=exit_win, foreground='white', width=8,
            font=font1, border=4, bg='#ad0414').place(x=800, y=500)

root.mainloop()
