import socket
import json
import tkinter as tk
from tkinter import ttk, Toplevel, Tk
from tkinter import messagebox as msg
from tkinter.messagebox import showinfo
from db_functions import Database
from models import User, Task
from datetime import datetime
from tkinter import font as tkfont
import yaml
import os
import sys
from tkinter import ttk, Tk, Toplevel
import tkinter as tk

root_dir = os.path.dirname(os.path.abspath(__file__))
l10n = yaml.safe_load(open(f'{root_dir}/translation.yml'))

db = Database()
db.create_tables()
user = User(id=db.get_last_user())

languages = ['en', 'tr']
lang = db.get_last_language()

root = Tk()

def goto_register():
    login.login_win.destroy() # hide login window
    register.win.deiconify() # show register window

def goto_dashboard():
    login.login_win.destroy() # hide login window
    register.win.destroy() # hide register window
    dashboard.win.deiconify() # show dashboard window

def change_language(lang):
    if lang in languages:
        lang = lang
        db.set_language(lang)

class Login():
    def __init__(self):
        self.login_win = Toplevel(root)
        self.login_win.title("Login - Task Planner")
        self.login_win.geometry("800x400+10+10")
        self.login_win.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.login_win)
        self.main_frame.pack(side="top", fill=tk.BOTH, expand=1)

        self.username = tk.StringVar()
        self.languageVar = tk.StringVar()
        self.languageVar.set("en")

        # Language List
        self.languageList = tk.OptionMenu(self.main_frame, self.languageVar, *languages)
        self.languageLabel = tk.Label(self.main_frame, text=l10n[lang]['Select Language'])
        self.languageLabel.grid(row=0, column=4, sticky="ne")
        self.languageList.grid(row=0, column=5, padx=5)

        self.change_language = ttk.Button(self.main_frame, text="Change Language", width=15, command=lambda: change_language(lang=self.languageVar.get()))
        self.change_language.grid(column=0, row=0, columnspan=1, pady=4)


        # Username
        self.usernameLabel = tk.Label(self.main_frame, text="E-mail")
        self.usernameLabel.grid(row=4, column=3, pady=5, padx=100)
        self.usernameEntryBox = tk.Entry(self.main_frame, textvariable=self.username).grid(row=5, column=3, padx=100)

        # password label and entry box
        self.password = tk.StringVar()
        self.passwordLabel = tk.Label(self.main_frame, text=l10n[lang]['Password'])
        self.passwordLabel.grid(row=6, column=3, padx=100)
        self.passwordEntryBox = tk.Entry(self.main_frame, textvariable=self.password, show="*")
        self.passwordEntryBox.grid(row=7, column=3, padx=100)

        self.loginButton = tk.Button(self.main_frame, text=l10n[lang]['Login'],
                                command=goto_dashboard)
        self.loginButton.grid(row=9, column=3, pady=10, padx=100)

        self.registerButton = tk.Button(self.main_frame, text=l10n[lang]['Register'],
                                   command=goto_register)
        self.registerButton.grid(row=10, column=3, pady=5,
                            padx=100)

class Register():
    def __init__(self):
        self.win = Toplevel(root)
        self.win.title("Register - Task Planner")
        self.win.geometry("800x400+10+10")
        self.win.resizable(False, False)
        self.win.withdraw() # hide lab window
        self.button2 = ttk.Button(self.win, text='Close', command=quit)
        # self.button2.pack(padx=100, pady=50)
        self.create_widgets()

    def create_widgets(self):
        self.newUsername = tk.StringVar()
        self.usernameLabel = tk.Label(self.win, text="E-Mail").grid(row=5, column=3, padx=100, pady=20)
        self.usernameEntryBox = tk.Entry(self.win, textvariable=self.newUsername).grid(row=5, column=4)

        # password label and entry box
        self.newPassword = tk.StringVar()
        self.passwordLabel = tk.Label(self.win, text=l10n[lang]['Password']).grid(row=6, column=3)
        self.passwordEntryBox = tk.Entry(self.win, textvariable=self.newPassword, show="*").grid(row=6, column=4)

        # Register
        self.RegisterButton = tk.Button(self.win, text=l10n[lang]['Register'], command=goto_dashboard).grid(row=7, column=4, pady=10)


class Dashboard():
    def __init__(self):
        self.win = Toplevel(root)
        self.win.title(l10n[lang]['Task Planner'])
        self.win.withdraw() # hide lab window
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
        title_lbl = tk.Label(add_task_win, text=l10n[lang]['Title'])
        title_lbl.grid(row=1, column=1, pady=5, padx=100)
        title_entry = tk.Entry(add_task_win, textvariable=title_var).grid(row=2, column=1, padx=100)

        desc_var = tk.StringVar()
        desc_lbl = tk.Label(add_task_win, text=l10n[lang]['Description'])
        desc_lbl.grid(row=3, column=1, pady=5, padx=100)
        desc_entry = tk.Entry(add_task_win, textvariable=desc_var).grid(row=4, column=1, padx=100)

        project_var = tk.StringVar()
        project_var.set(l10n[lang]['Projects'])

        if db.get_projects(user):
            projects = [x[1] for x in  db.get_projects(user)]
        else:
            projects = ['No Project']

        project_list = tk.OptionMenu(add_task_win, project_var, *projects)
        project_list.grid(row=5, column=1, padx=5)

        loginButton = tk.Button(add_task_win, text=l10n[lang]['Add'],
                                command=add_task_complete)
        loginButton.grid(row=6, column=1, pady=10, padx=100)

        ttk.Label(add_task_win,  text =l10n[lang]['Add Task']).pack() 

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
        title_lbl = tk.Label(add_project_win, text=l10n[lang]['Title'])
        title_lbl.grid(row=1, column=1, pady=5, padx=100)
        title_entry = tk.Entry(add_project_win, textvariable=title_var).grid(row=2, column=1, padx=100)


        loginButton = tk.Button(add_project_win, text=l10n[lang]['Add'],
                                command=add_project_complete)
        loginButton.grid(row=6, column=1, pady=10, padx=100)

        ttk.Label(add_project_win,  text =l10n[lang]['Add Project']).pack() 


    def answer_mark(self):
        msg.showinfo(title= "?", message="Following project ToDos’ better via this software. You can add, categorize and remove projects. And you can track your projects.")

    def search_project(self):
        pass

    def history_project(self):
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
        ttk.Label(self.left_frame, text=l10n[lang]['Projects']).grid(column=0, row=4, columnspan=1, pady=10)
        self.all_btn = ttk.Button(self.left_frame, text="+", width=2, command=self.add_project)
        self.all_btn.grid(column=1, row=4, columnspan=1, pady=4)

        self.all_btn = ttk.Button(self.left_frame, text=l10n[lang]['-- All --'], width=15, command=lambda arg=None:  self.apply_filter(project=arg))
        self.all_btn.grid(column=0, columnspan=2, pady=20)

        for project in db.get_projects(user):
            self.all_btn = ttk.Button(self.left_frame, text=project[1], width=15, command=lambda arg=project[1]:  self.apply_filter(project=arg))
            self.all_btn.grid(column=0, columnspan=2, pady=20)

    def create_right_top_frame(self):   
        ## Right Top Frame
        self.right_top_frame = tk.Frame(self.right_frame)
        self.right_top_frame.pack(side="top", fill=tk.BOTH, expand=1)

        self.all_btn = ttk.Button(self.right_top_frame, text=l10n[lang]['Add'], width=15, command=self.add_task)
        self.all_btn.grid(column=0, row=0, columnspan=1, pady=4)
       
        self.all_btn = ttk.Button(self.right_top_frame, text="?", width=4, command=self.answer_mark)
        self.all_btn.grid(column=3, row=0, columnspan=1, pady=4)

    def create_right_bot_frame(self, filters={}):
        ## Right Bot Frame
        self.right_bot_frame = tk.Frame(self.right_frame)
        self.right_bot_frame.pack(side="top", fill=tk.BOTH, expand=1)

        for task in db.get_tasks(user, filters=filters):
            task_text = f'{task.title}   |   {task.desc}   |   {task.project}     '
            ttk.Label(self.right_bot_frame, text=task_text).grid(column=0, columnspan=5, pady=10)


root.withdraw() # hide root window
login = Login()
register = Register()
dashboard = Dashboard()
root.mainloop()