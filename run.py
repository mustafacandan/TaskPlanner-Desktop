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
    
    def apply_filter(self, project=None, date_range=None):
        self.right_bot_frame.destroy()
        filters = {
            'project': project,
            'date_range': date_range
        }
        self.create_right_bot_frame(filters=filters)

    def add_task(self):
        def add_task_complete():
            db.add_task( 
                Task(user,datetime.now(),
                datetime.now(),
                project=project_var.get(),
                title=title_var.get(),
                desc=desc_var.get()))
            self.right_bot_frame.destroy()
            self.create_right_bot_frame()
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

        if db.get_projects(user):
            projects = [x[1] for x in  db.get_projects(user)]
        else:
            projects = ['No Project']

        project_list = tk.OptionMenu(add_task_win, project_var, *projects)
        project_list.grid(row=5, column=1, padx=5)

        loginButton = tk.Button(add_task_win, text='Add',
                                command=add_task_complete)
        loginButton.grid(row=6, column=1, pady=10, padx=100)

        ttk.Label(add_task_win,  text ="Add task").pack() 

    def add_project(self):
        def add_project_complete():
            print(title_var.get())

            db.add_project(title_var.get(), user)
            self.left_frame.destroy()
            self.create_left_frame()
            add_project_win.destroy()

        add_project_win = Toplevel(self.win) 
        # sets the geometry of toplevel 
        add_project_win.geometry("400x400") 

        title_var = tk.StringVar()
        title_lbl = tk.Label(add_project_win, text='Title of Project')
        title_lbl.grid(row=1, column=1, pady=5, padx=100)
        title_entry = tk.Entry(add_project_win, textvariable=title_var).grid(row=2, column=1, padx=100)


        loginButton = tk.Button(add_project_win, text='Add',
                                command=add_project_complete)
        loginButton.grid(row=6, column=1, pady=10, padx=100)

        ttk.Label(add_project_win,  text ="Add Projetc").pack() 


    def answer_mark(self):
        msg.showinfo(title= "?", message="Following project ToDos’ better via this software. You can add, categorize and remove projects. And you can track your projects.")

    def search_project(self):
        pass

    def history_project(self):
        pass
    
    
    def delete_project(self):
        msg.askquestion('Delete Current Project','Are you sure you really want to delete choosen project?', icon = 'warning')
        if msg == 'yes':
            Project.destroy()
            
        else: 
         pass

    def create_widgets(self):
        self.create_left_frame()
        self.create_right_top_frame()
        self.create_right_bot_frame()

    def create_left_frame(self):
        ## Left Frame
        self.left_frame = tk.Frame(self.win)
        self.left_frame.pack(side="left", fill=tk.BOTH, expand=1)

        self.right_frame = tk.Frame(self.win)
        self.right_frame.pack(side="right", fill=tk.BOTH, expand=1)

        ttk.Label(self.left_frame, text="Tasks").grid(column=0, row=0, columnspan=2, pady=10)

        self.inbox_btn = ttk.Button(self.left_frame, text="inbox", width=15, command=lambda: self.apply_filter(project=project[1]))
        self.inbox_btn.grid(column=0, row=1, columnspan=2, pady=20)

        self.today_btn = ttk.Button(self.left_frame, text="today", width=15, command=lambda: self.apply_filter(project=project[1]))
        self.today_btn.grid(column=0, row=2, columnspan=2, pady=20)

        self.all_btn = ttk.Button(self.left_frame, text="all", width=15, command=lambda: self.apply_filter(project=project[1]))
        self.all_btn.grid(column=0, row=3, columnspan=2, pady=20)

        # Projects 
        ttk.Label(self.left_frame, text="Projects").grid(column=0, row=4, columnspan=1, pady=10)
        self.all_btn = ttk.Button(self.left_frame, text="+", width=2, command=self.add_project)
        self.all_btn.grid(column=1, row=4, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.left_frame, text=' -- All -- ', width=15, command=lambda arg=None:  self.apply_filter(project=arg))
        self.all_btn.grid(column=0, columnspan=2, pady=20)

        for project in db.get_projects(user):
            self.all_btn = ttk.Button(self.left_frame, text=project[1], width=15, command=lambda arg=project[1]:  self.apply_filter(project=arg))
            self.all_btn.grid(column=0, columnspan=2, pady=20)

    def create_right_top_frame(self):   
        ## Right Top Frame
        self.right_top_frame = tk.Frame(self.right_frame)
        self.right_top_frame.pack(side="top", fill=tk.BOTH, expand=1)

        self.all_btn = ttk.Button(self.right_top_frame, text="Delete", width=15, command=self.delete_project)
        self.all_btn.grid(column=0, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="Add", width=15, command=self.add_task)
        self.all_btn.grid(column=1, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="Search", width=15, command=self.search_project)
        self.all_btn.grid(column=2, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="History", width=15, command=self.history_project)
        self.all_btn.grid(column=3, row=0, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.right_top_frame, text="?", width=4, command=self.answer_mark)
        self.all_btn.grid(column=4, row=0, columnspan=1, pady=4)

    def create_right_bot_frame(self, filters={}):
        ## Right Bot Frame
        self.right_bot_frame = tk.Frame(self.right_frame)
        self.right_bot_frame.pack(side="bottom", fill=tk.BOTH, expand=1)

        for task in db.get_tasks(user, filters=filters):
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

