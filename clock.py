import tkinter as tk
from time import strftime
import datetime
import calendar

# creating tkinter window
root = tk.Tk()

root.geometry("350x350")
root.title("Time Clock")
militaryTime = False

# Get the current date
current_date = datetime.datetime.now()

# Extract day, month, and year
day = current_date.day
month = current_date.month
year = current_date.year

# Convert month number to its name
month_name = calendar.month_name[month]

# Convert day number to its ordinal form (e.g., 1 -> 1st, 2 -> 2nd, etc.)
if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]

# Display the date in words
date_in_words = f" {month_name} {day}{suffix} {year}"
print("Date in words:", date_in_words)


# This function is used to
# display time on the label
def time():
    if militaryTime:
        string = strftime('%H:%M:%S %p')
    else:
        string = strftime('%I:%M:%S %p')  # %I for 12-hour format, %p for AM/PM

    timeLbl.config(text=string)
    timeLbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
timeLbl = tk.Label(root, font=('Helvetica', 40, 'bold'), foreground='white')
titleLBl = tk.Label(root,font=('Helvetica', 20, 'bold'), text='Simple Digital Clock', foreground='white')
dateLbLbl = tk.Label(root,font=('Helvetica', 30, 'bold'), foreground='white', text=date_in_words)

# Placing clock at the centre
# of the tkinter window
titleLBl.pack()
timeLbl.pack(pady=25)
dateLbLbl.pack(pady=30)
time()

root.mainloop()




