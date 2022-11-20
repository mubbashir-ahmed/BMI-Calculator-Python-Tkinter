# imports
import tkinter as tk
import datetime as dt
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def calc_age(self):
        today = dt.date.today()
        age = today.year-self.birthdate.year
        return age


def calc_bmi():
    kg = int(txtbx_weight.get())
    m = int(txtbx_height.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_conditions(bmi)


def bmi_conditions(bmi):
    p = Person(txtbx_name.get(), dt.date(int(txtbx_year.get()),
                             int(txtbx_month.get()), int(txtbx_date.get())))

    if bmi < 18.5:
        messagebox.showinfo('Information', 'Hello {human}!\nYou are {age} years old.\n' f'Your BMI is {bmi} (Underweight)'.format(
            human=p.name, age=p.calc_age()))
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Information', 'Hello {human}!\nYou are {age} years old.\n' f'Your BMI is {bmi} (Normal)'.format(
            human=p.name, age=p.calc_age()))
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Information', 'Hello {human}!\nYou are {age} years old.\n' f'Your BMI is {bmi} (Overweight)'.format(
            human=p.name, age=p.calc_age()))
    elif (bmi > 29.9):
        messagebox.showinfo('Information', 'Hello {human}!\nYou are {age} years old.\n' f'Your BMI is {bmi} (Obesity)'.format(
            human=p.name, age=p.calc_age()))
    else:
        messagebox.showerror('Information', 'Something Went Wrong! Please Try Again')


def reset_txtbx():
    txtbx_name.delete(0, 'end')
    txtbx_year.delete(0, 'end')
    txtbx_month.delete(0, 'end')
    txtbx_date.delete(0, 'end')
    txtbx_height.delete(0, 'end')
    txtbx_weight.delete(0, 'end')
    txtbx_name.focus()


# window settings
window = tk.Tk()
window.title("BMI Calculator")
window.resizable(False, False)
MyLeftPos = (window.winfo_screenwidth() - 400) / 2
MyTopPos = (window.winfo_screenheight() - 500) / 2
window.geometry("%dx%d+%d+%d" % (400, 500, MyLeftPos, MyTopPos))
icon = PhotoImage(file = 'icon.png')
window.iconphoto(False, icon)

# labels
lbl_name = tk.Label(text="Enter Your Name:", font=("Arial Bold", 10))
lbl_name.grid(column=1, row=1, sticky="w")

lbl_year = tk.Label(text="Enter Year of Birth:", font=("Arial Bold", 10))
lbl_year.grid(column=1, row=2, sticky="w")

lbl_month = tk.Label(text="Enter Month of Birth:", font=("Arial Bold", 10))
lbl_month.grid(column=1, row=3, sticky="w")

lbl_date = tk.Label(text="Enter Date of Birth:", font=("Arial Bold", 10))
lbl_date.grid(column=1, row=4, sticky="w")

lbl_height = tk.Label(text="Enter Height (cm):", font=("Arial Bold", 10))
lbl_height.grid(column=1, row=5, sticky="w")

lbl_weight = tk.Label(text="Enter Weight (kg):", font=("Arial Bold", 10))
lbl_weight.grid(column=1, row=6, sticky="w")

# entry fields (textboxes)
txtbx_name = tk.Entry(width=30)
txtbx_name.grid(column=2, row=1, sticky="w")

txtbx_year = tk.Entry(width=30)
txtbx_year.grid(column=2, row=2, sticky="w")

txtbx_month = tk.Entry(width=30)
txtbx_month.grid(column=2, row=3, sticky="w")

txtbx_date = tk.Entry(width=30)
txtbx_date.grid(column=2, row=4, sticky="w")

txtbx_height = tk.Entry(width=30)
txtbx_height.grid(column=2, row=5, sticky="w")

txtbx_weight = tk.Entry(width=30)
txtbx_weight.grid(column=2, row=6, sticky="w")

# textarea
txtarea_details = tk.Text(window, height=6, width=45)
txtarea_details.grid(column=1, row=10, columnspan=2)
txtarea_details.insert(
    tk.END, "Hello! Fill out the following details and\nClick \"Calculate\" to calculate your BMI.\nClick \"Reset\" to reset all text fields.\n\n\nDeveloped By: Mubbashir Ahmed")
txtarea_details.config(state="disabled");

# button
btn_reset = tk.Button(window, text="Reset", bg="pink", fg="black", font=(
    "Arial Bold", 11), width=19, command=reset_txtbx)
btn_reset.grid(column=1, row=9, pady=10, sticky="e")
btn_calc = tk.Button(window, text="Calculate", bg="lightblue", fg="black", font=(
    "Arial Bold", 11), width=19, command=calc_bmi)
btn_calc.grid(column=2, row=9, pady=10, sticky="w")

# image
image = Image.open('img.png')
image.thumbnail((396, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0, columnspan=2)

# window mainloop
window.mainloop()
