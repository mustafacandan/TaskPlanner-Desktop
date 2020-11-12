import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Liars Dice 2020")
win.geometry("1000x550+100+100")

container_frame = tk.LabelFrame(win, text="MAIN MENU")
container_frame.grid(column=1, row=1, padx=425, pady=150)

createlobby_button = tk.Button(container_frame, text="CREATE LOBBY")
createlobby_button.grid(column=1, row=1, columnspan=2)

tk.Label(container_frame, text="Enter Code Here:").grid(column=3, row=2)

findlobby_button = tk.Button(container_frame, text="FIND LOBBY")
findlobby_button.grid(column=1, row=2, columnspan=2)

code1 = tk.IntVar()
code1_entry = tk.Entry(container_frame, width= 10)
code1_entry.grid(column=10, row=2)

startgame_button = tk.Button(container_frame, text="START GAME WITH RANDOM LOBBY!")
startgame_button.grid(column=1, row=3, columnspan=2)

settings_button = tk.Button(container_frame, text="SETTINGS")
settings_button.grid(column=1, row=4, columnspan=2)

def showCreditsMsg():  
    messagebox.showinfo('Liars Dice 2020', 'ALL RIGHTS RESERVED, 2020, \n *MostFucKing GUI_App CO.*')
 
credits_button = tk.Button(container_frame, text="CREDITS", command=showCreditsMsg)
credits_button.grid(column=1, row=5, columnspan=2)


win.mainloop()