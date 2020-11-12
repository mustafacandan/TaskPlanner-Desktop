import tkinter as tk

win = tk.Tk()
win.title("Liars Dice 2020")
win.geometry("1000x550+100+100")

container_frame = tk.LabelFrame(win, text="FIND LOBBY")
container_frame.grid(column=1, row=1, padx=425, pady=150)

#there will be a excel like room list which include level, round number, number of player etc.

win.mainloop()