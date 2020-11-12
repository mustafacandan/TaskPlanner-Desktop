import tkinter as tk

win = tk.Tk()
win.title("Liars Dice 2020")
win.geometry("1000x550+100+100")

container_frame = tk.LabelFrame(win, text="")
container_frame.grid(column=1, row=1, padx=425, pady=150)

tk.Label(container_frame, text="LIARS DICE 2020").grid(column=2, row=1)
tk.Label(container_frame, text="Enter Username:").grid(column=2, row=2)

def add_handler():
        result = tk.Label(container_frame, text="Entering", height = 5, width = 15).grid(column=2, row=3)

value1 = tk.IntVar()
value1_entry = tk.Entry(container_frame, width= 10)
value1_entry.grid(column=2, row=4)


var1 = tk.IntVar()
c1 = tk.Checkbutton(container_frame, text='Remember Me',variable=var1, onvalue=1, offvalue=0)
c1.grid(column=2, row=5)


enter_button = tk.Button(container_frame, text="ENTER GAME!", command=add_handler)
enter_button.grid(column=2, row=6, columnspan=2)


win.mainloop()