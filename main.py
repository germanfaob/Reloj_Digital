from tkinter import *
from time import strftime

# Main window
root = Tk()
root.title('Digital Clock')
root.geometry('600x400')
root.config(bg='black')
root.resizable(False, False)

# Icon
image_icon = PhotoImage(file = './img/icon.png')
root.iconphoto(False, image_icon)

# Functions
# Shows current date
def clock_date():
    display_date = strftime('%B-%A-%d-%Y')
    date.config(text=display_date)
    date.after(1000,clock_date)

# Shows current time
def clock_time():
    display_time = strftime('%H:%M:%S %p')
    time.config(text=display_time)
    time.after(1000,clock_time)

# Date label
date = Label(root, font=('mincho', 20), background='black', foreground='cyan')
date.pack(anchor='center')
date.config(padx=75, pady=30)

# Time label
time = Label(root, font=('mincho', 80), background='black', foreground='cyan')
time.pack(anchor = 'center')
time.config(pady=50)

clock_date()
clock_time()
mainloop()