import socket
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from db_functions import Database

db = Database()
db.create_db_table()

projects = [
    'Project A',
    'Project B',
    'Project C'
    ]

tags = ['urgent', 'can wait']

class TaskPlanner:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Task Planner")
        self.win.geometry("1280x748+10+10")
        self.win.resizable(False, False)
        self.create_widgets()
        # self.input_entry.focus_set()

    def show_history(self):
        pass
    
    def filter_today(self):
        pass
    
    def filter_all(self):
        pass

    def add_project(self):
        pass

    def filter_inbox(self):
        pass


    def create_widgets(self):
        self.left_frame = tk.Frame(self.win)
        self.left_frame.pack(side="left", fill=tk.BOTH, expand=1)

        self.right_frame = tk.Frame(self.win)
        self.right_frame.pack(side="right", fill=tk.BOTH, expand=1)

        self.right_top_frame = tk.Frame(self.right_frame)
        self.right_top_frame.pack(side="top", fill=tk.BOTH, expand=1)

        self.right_bot_frame = tk.Frame(self.right_frame)
        self.right_bot_frame.pack(side="bottom", fill=tk.BOTH, expand=1)


        ## Left Frame
        ttk.Label(self.left_frame, text="Tasks").grid(column=0, row=0, columnspan=2, pady=10)

        self.inbox_btn = ttk.Button(self.left_frame, text="inbox", width=15, command=self.filter_inbox)
        self.inbox_btn.grid(column=0, row=1, columnspan=2, pady=20)

        self.today_btn = ttk.Button(self.left_frame, text="today", width=15, command=self.filter_today)
        self.today_btn.grid(column=0, row=2, columnspan=2, pady=20)

        self.all_btn = ttk.Button(self.left_frame, text="all", width=15, command=self.filter_all)
        self.all_btn.grid(column=0, row=3, columnspan=2, pady=20)

        # Projects 
        ttk.Label(self.left_frame, text="Projects").grid(column=0, row=4, columnspan=1, pady=10)
        self.all_btn = ttk.Button(self.left_frame, text="+", width=2, command=self.add_project)
        self.all_btn.grid(column=1, row=4, columnspan=1, pady=4)

        for project in projects:
            self.all_btn = ttk.Button(self.left_frame, text=project, width=15, command=self.filter_all)
            self.all_btn.grid(column=0, columnspan=2, pady=20)


        # Tags
        ttk.Label(self.left_frame, text="Tags").grid(column=0, columnspan=2, pady=10)
        
        for tag in tags:
            self.all_btn = ttk.Button(self.left_frame, text=tag, width=15, command=self.filter_all)
            self.all_btn.grid(column=0, columnspan=2, pady=20)

   
        ## Right Top Frame
        self.all_btn = ttk.Button(self.right_top_frame, text="Add", width=15, command=self.add_project)
        self.all_btn.grid(column=0, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="Search", width=15, command=self.add_project)
        self.all_btn.grid(column=1, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="History", width=15, command=self.add_project)
        self.all_btn.grid(column=2, row=0, columnspan=1, pady=4)


        ## Right Bot Frame


        ## Bindings
        self.win.bind("<F1>", lambda e: db.create_db_table())
        self.win.bind("<F2>", lambda e: db.clear_history())
        # self.input_entry.bind("<Return>", lambda e: db.convert())


app = TaskPlanner()
app.win.mainloop()