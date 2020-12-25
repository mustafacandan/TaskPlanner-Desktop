import tkinter as tk

win = tk.Tk()
win.title("Liars Dice 2020")
win.geometry("1000x550+100+100")



dice1_button = tk.Button(win, text="1", width= 5).grid(column=3, row=10, padx=5, pady=5)
dice2_button = tk.Button(win, text="2", width= 5).grid(column=5, row=10, padx=5, pady=5)
dice3_button = tk.Button(win, text="3", width= 5).grid(column=7, row=10, padx=5, pady=5)

#n = tk.IntVar() 
#numberchoosen = tk.Listbox(win, width = 5) 
#numberchoosen[] = ('1','2','3','4','5','6','7','8','9','10') 
#numberchoosen.grid(column = 9, row = 10) 
#numberchoosen.current()
#asd

bid_button = tk.Button(win, text="Bid", width= 20).grid(column=10, row=10, padx=5, pady=5, columnspan=2)

win.mainloop()