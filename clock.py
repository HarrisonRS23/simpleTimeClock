import tkinter as tk
# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = tk.Tk()

root.geometry("500x500")
root.title("Time Clock")
root.resizable(width=False, height=False)


# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    timeLbl.config(text=string)
    timeLbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
timeLbl = tk.Label(root, font=('Helvetica', 40, 'bold'), foreground='white')
titleLBl = tk.Label(root,font=('Helvetica', 20, 'bold'), text='Simple Digital Clock', foreground='white')

# Placing clock at the centre
# of the tkinter window
titleLBl.pack(padx=5,pady=5)
timeLbl.pack(padx=40, pady=40)
time()

root.mainloop()
