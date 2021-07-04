from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import re
from fpdf import FPDF
import tkinter as tk
import smtplib
import pyglet

# Create splash screen
animation = pyglet.image.load_animation('Splash Screen.gif')
animSprite = pyglet.sprite.Sprite(animation)
w = animSprite.width
h = animSprite.height

win = pyglet.window.Window(width=w, height=h, style='borderless')
win.set_location(200, 100)

r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pyglet.gl.glClearColor(r, g, b, alpha)


@win.event
def on_draw():
    win.clear()
    animSprite.draw()


def close(event):
    win.close()


pyglet.clock.schedule_once(close, 5.0)

pyglet.app.run()

root = Tk()
root.title("Income Tax Calculator")
root.geometry('1000x600')
root.maxsize(1000, 600)
root.minsize(1000, 600)
font1 = ("Times", 14, "bold")
font2 = ("Times", 13, "bold")

# ------------------------------- for only contact no., income and exemption/deduction -----------------------
class Keypad_digits(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text))
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace)
        x.grid(row=1, column=0,columnspan='4', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear)
        x.grid(row=1, column=4, columnspan='3',  sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide)
        x.grid(row=1, column=7, columnspan='3', sticky='news')


    def get(self):
        if self.target:
            return self.target.get()

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete(0, 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.5, anchor='c')

    def hide(self):
        self.target = None

        self.place_forget()
#-------------------------------------------------------

# ------------------------------- for name -----------------------
class Keypad_alphabets(tk.Frame):

    cells = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text))
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Space', command=self.space)
        x.grid(row=3, column=0, columnspan='6', sticky='news')

        x = tk.Button(self, text='tab', command=self.tab)
        x.grid(row=3, column=6, columnspan='5', sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace)
        x.grid(row=3, column=11,columnspan='5', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear)
        x.grid(row=3, column=16, columnspan='5',  sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide)
        x.grid(row=3, column=21, columnspan='5', sticky='news')


    def get(self):
        if self.target:
            return self.target.get()

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete(0, 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def space(self):
        if self.target:
            text = self.get()
            text = text + " "
            self.clear()
            self.append(text)

    def tab(self):
        if self.target:
            text = self.get()
            text = text + "     "
            self.clear()
            self.append(text)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.5, anchor='c')

    def hide(self):
        self.target = None

        self.place_forget()
#-------------------------------------------------------

# ------------------------------- for emailid -----------------------
class Keypad_emailid(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '.'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text))
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace)
        x.grid(row=0, column=12,columnspan='6', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear)
        x.grid(row=0, column=18, columnspan='4',  sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide)
        x.grid(row=0, column=22, columnspan='4', sticky='news')


    def get(self):
        if self.target:
            return self.target.get()

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete(0, 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def space(self):
        if self.target:
            text = self.get()
            text = text + " "
            self.clear()
            self.append(text)

    def tab(self):
        if self.target:
            text = self.get()
            text = text + "     "
            self.clear()
            self.append(text)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.5, anchor='c')

    def hide(self):
        self.target = None

        self.place_forget()
#-------------------------------------------------------


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


def des_f1():
    f1.destroy()


f1 = Frame(root, height=600, width=1000)
f1.propagate(0)
f1.pack(side='top')

c = Canvas(f1, width=1000, height=600, bg="blue")
c.pack()
p1 = PhotoImage(file='front.gif')
c.create_image(0, 0, image=p1, anchor=NW)

# Change logo in title bar
l = PhotoImage(file='Final_Logo.gif')
root.iconphoto(False, l)

HoverButton(f1, text="Start", activebackground="#6382b8", cursor="hand2", font=font1, foreground='white',
            command=des_f1, bg='#8b1c13', width=8, border=4).place(x=450, y=500)


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False


def check_contact(number):
    regex = '^[0-9]{10}$'
    if (re.search(regex, number)):
        return True
    else:
        return False


def check_name(name):
    if re.search('^[a-zA-z\s]+$', name):
        return True
    else:
        return False


def des_f2():
    user_name = e1.get()
    user_contact = e2.get()
    user_email = e3.get()

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
            f2.destroy()


myname = StringVar(root)
mycontact = StringVar(root)
myemailid = StringVar(root)


def on_i_click():
    messagebox.showinfo("Valid Entry", "Valid Names: eg.\tAlex\n\t\tAlex sharma\n\t\tAlex Panth Sharma\n\n"
                                       "Valid Number: eg. \t3819481747\n\t\t7858173627\n\t\t9843728184\n\n"
                                       "Valid Email Id: eg.\temail@example.com\n\t\tsomething@gmail.com\n\t\temail@subdomain.example.com\n\t\t1234567890@example.com\n\t\t_______@example.com\n\t\temail@example.co.jp\n\t\temail@example.ac.in\n\t\tfirstname-lastname@example.com\n\t\tsomeone@smething.org\n\n"
                        )


firstclick1 = True


def on_e1_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1

    if firstclick1:  # if this is the first time they clicked it
        firstclick1 = False
        e1.delete(0, "end")  # delete all the text in the entry
#myfirst change
#comments


firstclick2 = True


def on_e2_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick2

    if firstclick2:  # if this is the first time they clicked it
        firstclick2 = False
        e2.delete(0, "end")  # delete all the text in the entry


firstclick3 = True


def on_e3_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick3

    if firstclick3:  # if this is the first time they clicked it
        firstclick3 = False
        e3.delete(0, "end")  # delete all the text in the entry


f2 = Frame(root, height=600, width=1000, background='red')
f2.propagate(0)
f2.pack(side='top')

c = Canvas(f2, width=1000, height=600, bg="blue")
c.pack()
p2 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p2, anchor=NW)

HoverButton(f2, text="i", activebackground="#6382b8", cursor="hand2", command=on_i_click, font="Helvetica 10 bold",
            width=2, border=2).place(
    x=450, y=100)

keypad_emailid = Keypad_emailid(root)
keypad_alphabets = Keypad_alphabets(root)
keypad_digits1 = Keypad_digits(root)

l0 = Label(f2, text='Enter your details :-', font=font1)
l0.place(x=250, y=100)

l1 = Label(f2, text='Name', font=font1)
l1.place(x=250, y=140)
e1 = Entry(f2, textvariable=myname, width=50, border=2)
e1.insert(0, 'Enter Your Name...')
e1.bind('<FocusIn>', on_e1_click)
e1.place(x=450, y=140)

HoverButton(f2, text="⌨", activebackground="#6382b8", cursor="hand2", command=lambda:keypad_alphabets.show(e1),width=3, border=1).place(x=780, y=135)

l2 = Label(f2, text='Contact', font=font1)
l2.place(x=250, y=180)
e2 = Entry(f2, textvariable=mycontact, width=50, border=2)
e2.insert(0, 'Enter Your Contact...')
e2.bind('<FocusIn>', on_e2_click)
e2.place(x=450, y=180)

HoverButton(f2, text="⌨", activebackground="#6382b8", cursor="hand2", command=lambda:keypad_digits1.show(e2),width=3, border=1).place(x=780, y=175)

l3 = Label(f2, text='Email Id', font=font1)
l3.place(x=250, y=220)
e3 = Entry(f2, textvariable=myemailid, width=50, border=2)
e3.insert(0, 'Enter Your Email Id...')
e3.bind('<FocusIn>', on_e3_click)
e3.place(x=450, y=220)

HoverButton(f2, text="⌨", activebackground="#6382b8", cursor="hand2", command=lambda:keypad_emailid.show(e3), width=3, border=1).place(x=780, y=215)


def clear1():
    e1.delete(0, END)
    e1.insert(0, "")
    e2.delete(0, END)
    e2.insert(0, "")
    e3.delete(0, END)
    e3.insert(0, "")


HoverButton(f2, text="Next", activebackground="#6382b8", cursor="hand2", command=des_f2, width=10, border=4).place(
    x=500, y=300)
HoverButton(f2, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear1, width=10, border=4).place(
    x=600, y=300)


def tax_scheme():
    new_window = Toplevel(f2)
    new_window.title("Tax scheme")
    new_window.geometry("452x322")

    # #Change logo in title bar
    l = PhotoImage(file='Final_Logo.gif')
    new_window.iconphoto(False, l)

    # Removing maximize/minimize option from "Check Tax Scheme" pop-up.
    new_window.resizable(0, 0)
    Label(new_window, text="This is a Tax scheme", image=logo).pack()


# #Change logo in title bar
# l=PhotoImage(file='Final_Logo.gif')
# f2.iconphoto(False,l)

logo = PhotoImage(file="image.gif")
label = Label(f2, text="This is the main window")
label.pack(pady=10)
HoverButton(f2, text="Check Taxes Scheme", activebackground="#6382b8", cursor="hand2", command=tax_scheme).place(x=770,
                                                                                                                 y=500)


def des_f3():
    f3.destroy()


def details():
    messagebox.showinfo('Details',
                        'Name : ' + myname.get() + '\n\n'
                                                   'Contact : ' + mycontact.get() + '\n\n'
                                                                                    'Email Id : ' + myemailid.get() + '\n\n'
                        )


firstclick5 = True


def on_e5_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick5

    if firstclick5:  # if this is the first time they clicked it
        firstclick5 = False
        e5.delete(0, "end")  # delete all the text in the entry


firstclick6 = True


def on_e6_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick6

    if firstclick6:  # if this is the first time they clicked it
        firstclick6 = False
        e6.delete(0, "end")  # delete all the text in the entry


f3 = Frame(root, height=600, width=1000, background='yellow')
f3.propagate(0)
f3.pack(side='top')

c = Canvas(f3, width=1000, height=600, bg="blue")
c.pack()
p3 = PhotoImage(file='back.gif')
c.create_image(0, 0, image=p3, anchor=NW)

keypad_digits2 = Keypad_digits(root)

l4 = Label(f3, text='Enter the required data (in INR) :-', font=font1)
l4.place(x=250, y=100)

l5 = Label(f3, text='Annual Income', font=font1)
l5.place(x=250, y=160)
e5 = Entry(f3, width=50, border=2)
e5.insert(0, 'Enter Your Annual Income...')
e5.bind('<FocusIn>', on_e5_click)
e5.place(x=480, y=160)

HoverButton(f3, text="⌨", activebackground="#6382b8", cursor="hand2", command=lambda:keypad_digits2.show(e5),width=3, border=1).place(x=800, y=155)

l6 = Label(f3, text='Exemptions / Deductions', font=font1)
l6.place(x=250, y=200)
e6 = Entry(f3, width=50, border=2)
e6.insert(0, 'Enter Your Exemptions / deductions...')
e6.bind('<FocusIn>', on_e6_click)
e6.place(x=480, y=200)

HoverButton(f3, text="⌨", activebackground="#6382b8", cursor="hand2", command=lambda:keypad_digits2.show(e6),width=3, border=1).place(x=800, y=195)


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
        elif n == 4:
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


s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()


def no_send_message():
    mbox.showinfo("Sharing Status", "Message not sent")


def send_message():
    sender_email = "Ram98765Soni@gmail.com"
    sender_pass = "R@S98765@"
    to = myemailid.get()
    subject = "Tax Calculation Summary"
    email_body_info = f"Hello {myname.get()} \n Your tax calculation summary is \n Oldtax: {old} \n Newtax: {new} \n Taxsave: {tax_save}"
    finalMessage = 'Subject: {}\n\n{} '.format(subject, email_body_info)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, sender_pass)
    mbox.showinfo("Sharing Status", "Login successfull")
    server.sendmail(sender_email, to, finalMessage)
    mbox.showinfo("Sharing Status", "Message sent")


def delete():
    l8 = Label(f3, text="                                                                 ",
               font=font1,
               background="white")
    l8.place(x=480, y=300)
    l10 = Label(f3, text="                                                                ",
                font=font1,
                background="white")
    l10.place(x=480, y=340)
    l12 = Label(f3, text="                                                                ",
                font=font1,
                background="white")
    l12.place(x=480, y=380)
    l14 = Label(f3, text="                                                                ",
                font=font1,
                background="white")
    l14.place(x=480, y=420)
    # destroying the below label
    er1 = Label(f3, text="                                                                              ",
                font=font1,
                background="white")
    er1.place(x=540, y=100)


delete()


def clear2():
    e5.delete(0, END)
    e5.insert(0, "")
    e6.delete(0, END)
    e6.insert(0, "")


old = 0
new = 0
tax_save = 0
flag = False


def calculate():
    global flag
    flag = True

    delete()
    global at
    global ad

    at = e5.get()
    ad = e6.get()
    try:
        ta = int(at) - int(ad)
    except:
        messagebox.showerror("Invalid Input", "Please enter valid Annual Tax and/or Exemption.")
        return 0
    global old
    global new
    global tax_save
    old = oldtax(ta)
    new = newtax(int(ta))
    tax_save = abs(new - old)
    tax_save = round(tax_save, 2)
    if new > old:
        better = "Old tax"
    elif ta <= 250000:
        better = "Income tax not applicable (Taxable income < 250000)"
    else:
        better = "New tax"

    if int(ad) > int(at):
        old = 0
        new = 0
        tax_save = 0.0
        better = "Deductions cannot be more than income"
        det = " Enter the details correctly!!! "
        er1 = Label(f3, text=det, font=font1, bg='white', fg='red')
        er1.place(x=540, y=100)

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

    l13 = Label(f3, text='Better option', font=font1)
    l13.place(x=250, y=420)

    l14 = Label(f3, text=better, font=font1)
    l14.place(x=480, y=420)


HoverButton(f3, text="Calculate", activebackground="#6382b8", cursor="hand2", command=calculate, width=10,
            border=4).place(x=500, y=250)
HoverButton(f3, text="Reset", activebackground="#6382b8", cursor="hand2", command=delete, width=10, border=4).place(
    x=610, y=250)
HoverButton(f3, text="Clear", activebackground="#6382b8", cursor="hand2", command=clear2, width=10, border=4).place(
    x=720, y=250)


def sharemail():
    messagebox.showinfo("User's tax info ",
                        f"Name: {myname.get()} \n\n Income Tax calculation is: \n\n Oldtax: {old}  Newtax: {new}  Taxsave: {tax_save}")

    if mbox.askokcancel("Sharing Permission", "Do you Want to share this details?"):
        send_message()
    else:
        no_send_message()


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
        messagebox.showinfo(title="Learn More",
                            message=str(readme))


HoverButton(f3, text="Learn More", activebackground="#6382b8", cursor="hand2", command=learn_more,
            foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=420, y=500)

HoverButton(f3, text="User Details", activebackground="#6382b8", cursor="hand2", command=details, foreground='white',
            font=font1, width=10, border=4, bg='#ad0414').place(
    x=565, y=500)
HoverButton(f3, text="Credits", activebackground="#6382b8", cursor="hand2", command=credit, foreground='white',
            font=font1, width=8, border=4, bg='#ad0414').place(x=710, y=500)

HoverButton(f3, text="Share With Mail", activebackground="#6382b8", cursor="hand2", command=sharemail,
            foreground='white', font=font1, width=15, border=4, bg='#ad0414').place(x=50, y=500)


def pdfdown():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font('helvetica', '', 14)

    pdf.set_text_color(0, 0, 0)

    pdf.image('Image.png', x=0, y=0, w=210, h=297)

    pdf.text(47, 106, myname.get())
    pdf.text(59, 117, mycontact.get())
    pdf.text(56, 127, myemailid.get())

    pdf.text(84, 162, str(at))
    pdf.text(111, 174, str(ad))

    pdf.text(59, 210, str(old))
    pdf.text(61, 222, str(new))
    pdf.text(68, 234, str(tax_save))

    pdf.output('Automated PDF Report.pdf')
    mbox.showinfo("PDF Status", "PDF Downloaded")


HoverButton(f3, text="Generate PDF", cursor="hand2", activebackground="#6382b8", command=pdfdown, foreground='white',
            width=12,
            font=font1, border=4, bg='#ad0414').place(x=250, y=500)


def end():
    root.destroy()


def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()


HoverButton(f3, text="Exit", cursor="hand2", activebackground="#6382b8", command=exit_win, foreground='white', width=8,
            font=font1, border=4, bg='#ad0414').place(x=835, y=500)

root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
