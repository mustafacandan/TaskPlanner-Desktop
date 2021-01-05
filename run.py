import socket
import json
import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as msg
from db_functions import Database
from models import User, Task
from datetime import datetime
db = Database()
db.create_tables()

user = User(id=db.get_last_user())

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

    def add_task(self):
        def add_task_complete():
            print(title_var.get(), desc_var.get(), project_var.get())

            db.add_task( 
                Task(user,datetime.now(),
                datetime.now(),
                project=project_var.get(),
                title=title_var.get(),
                desc=desc_var.get()))

            add_task_win.destroy()

        add_task_win = Toplevel(self.win) 
        # sets the geometry of toplevel 
        add_task_win.geometry("400x400") 

        title_var = tk.StringVar()
        title_lbl = tk.Label(add_task_win, text='Title of Task')
        title_lbl.grid(row=1, column=1, pady=5, padx=100)
        title_entry = tk.Entry(add_task_win, textvariable=title_var).grid(row=2, column=1, padx=100)

        desc_var = tk.StringVar()
        desc_lbl = tk.Label(add_task_win, text='Desc of Task')
        desc_lbl.grid(row=3, column=1, pady=5, padx=100)
        desc_entry = tk.Entry(add_task_win, textvariable=desc_var).grid(row=4, column=1, padx=100)

        project_var = tk.StringVar()
        project_var.set("Projects")

        projects = ['No Project'] if db.get_projects(user) else db.get_projects(user)

        project_list = tk.OptionMenu(add_task_win, project_var, *projects)
        project_list.grid(row=5, column=1, padx=5)

        loginButton = tk.Button(add_task_win, text='Add',
                                command=add_task_complete)
        loginButton.grid(row=6, column=1, pady=10, padx=100)

        ttk.Label(add_task_win,  text ="Add task").pack() 

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

        for project in db.get_projects(user):
            self.all_btn = ttk.Button(self.left_frame, text=project[1], width=15, command=self.filter_all)
            self.all_btn.grid(column=0, columnspan=2, pady=20)

   
        ## Right Top Frame
        self.all_btn = ttk.Button(self.right_top_frame, text="Add", width=15, command=self.add_task)
        self.all_btn.grid(column=0, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="Search", width=15, command=self.add_project)
        self.all_btn.grid(column=1, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="History", width=15, command=self.add_project)
        self.all_btn.grid(column=2, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="?", width=4, command=self.add_project)
        self.all_btn.grid(column=3, row=0, columnspan=1, pady=4)


        ## Right Bot Frame
        for task in db.get_tasks(user):
            task_text = f'{task.title}   |   {task.desc}   |   {task.project}     '
            ttk.Label(self.right_bot_frame, text=task_text).grid(column=0, columnspan=5, pady=10)


        ## Bindings
        self.win.bind("<F1>", lambda e: db.create_tables())
        self.win.bind("<F2>", lambda e: db.clear_history())
        # self.input_entry.bind("<Return>", lambda e: db.convert())



active_user = User('isim','email','pwd')
task1 = Task(active_user, None, 'Baslik', 'Aciklama', datetime.now(), datetime.now())


app = TaskPlanner()
app.win.mainloop()

