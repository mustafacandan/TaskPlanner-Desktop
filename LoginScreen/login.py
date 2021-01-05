import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import font as tkfont
import yaml
import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

cwd = os.getcwd()
languages = ['en','tr']
global lang
lang = 'tr'

l10n = yaml.safe_load(open(f'{ROOT_DIR}/translation.yml'))

# btn_login = l10n['tr']['btn_login']
# btn_register = l10n['en']['btn_register']


def login():
    print("Pressed Login Button")


def register():
    print("Pressed Register Button")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, RegisterPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


def ChangeLang(chosenLang):
    lang = chosenLang

class LoginPage(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        LoginPageFrame = tk.LabelFrame(self, width=300)
        LoginPageFrame.grid(row=0, column=0, padx=10, pady=10, ipady=10)
        username = tk.StringVar()
        languageVar = tk.StringVar(self)
        languageVar.set("en")

        # Language List
        languageList = tk.OptionMenu(LoginPageFrame, languageVar, *languages)
        languageLabel = tk.Label(LoginPageFrame, text=l10n[languageVar.get()]['Select Language'])
        languageLabel.grid(row=0, column=4, sticky="ne")
        languageList.grid(row=0, column=5, padx=5)



        # Username
        usernameLabel = tk.Label(LoginPageFrame, text="E-mail")
        usernameLabel.grid(row=4, column=3, pady=5, padx=100)
        usernameEntryBox = tk.Entry(LoginPageFrame, textvariable=username).grid(row=5, column=3, padx=100)

        # password label and entry box
        password = tk.StringVar()
        passwordLabel = tk.Label(LoginPageFrame, text=l10n[languageVar.get()]['Password'])
        passwordLabel.grid(row=6, column=3, padx=100)
        passwordEntryBox = tk.Entry(LoginPageFrame, textvariable=password, show="*")
        passwordEntryBox.grid(row=7, column=3, padx=100)

        loginButton = tk.Button(LoginPageFrame, text=l10n[languageVar.get()]['Login'],
                                command=login)
        loginButton.grid(row=9, column=3, pady=10, padx=100)

        registerButton = tk.Button(LoginPageFrame, text=l10n[languageVar.get()]['Register'],
                                   command=lambda: controller.show_frame("RegisterPage"))
        registerButton.grid(row=10, column=3, pady=5,
                            padx=100)

class WelcomeScreen():
    win = tk.Tk()

    def ContinueLogin(self):
        print("Continue Login")
        return

    def checkedTurkish_to_english(self):
        print("Checked Turkish")
        print(f"Turkish button var: {self.turkishLang.get()}")
        if self.englishLang.get():
            self.englishLang.set(0)

    def checkedEnglish_to_turkish(self):
        print("Checked English")
        print(f"English button var: {self.englishLang.get()}")
        if self.turkishLang.get():
            self.turkishLang.set(0)

    def __init__(self, languageOption):
        self.win = tk.Tk()
        self.win.title("Title Name of Welcome Screen")
        self.win.geometry("600x270")
        self.pw = tk.PanedWindow(self.win, orient="vertical")
        self.welcomeLabelFrame = tk.LabelFrame(self.pw, width=300)
        self.welcomeLabelFrame.grid(row=0, column=0, padx=10, pady=10, ipady=10)
        self.welcomeLabel = tk.Label(self.welcomeLabelFrame, text=l10n[languageOption]['Introduction'])
        self.welcomeLabel.grid(row=3, column=1, sticky="n", padx=200, pady=30)
        self.pw.add(self.welcomeLabelFrame)
        self.pw.pack(fill="both", expand=True)

        self.selectLanguageLabel = tk.Label(self.welcomeLabelFrame, text=l10n[languageOption]['Select Language'])
        self.selectLanguageLabel.grid(row=5, column=1, padx=100)

        self.turkishLang = tk.BooleanVar()
        self.englishLang = tk.BooleanVar()
        tk.Checkbutton(self.welcomeLabelFrame, text="Turkish", variable=self.turkishLang, command=lambda: self.checkedTurkish_to_english()).grid(row=6, column=1, padx=80)
        tk.Checkbutton(self.welcomeLabelFrame, text="English", variable=self.englishLang, command=lambda: self.checkedEnglish_to_turkish()).grid(row=7, column=1, padx=80)

        continueButton = tk.Button(self.welcomeLabelFrame, text="Continue",command=self.ContinueLogin() )
        continueButton.grid(row=8, column=1, padx=80, pady=30)

class RegisterPage(tk.Frame):
    def popupWindow(self):
        showinfo("Info","Registration Completed Successfully")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        newUsername = tk.StringVar()
        RegisterPageFrame = tk.LabelFrame(self)
        RegisterPageFrame.pack(fill="both", expand="yes", padx=5, pady=10)

        usernameLabel = tk.Label(RegisterPageFrame, text="E-Mail").grid(row=5, column=3, padx=100, pady=20)
        usernameEntryBox = tk.Entry(RegisterPageFrame, textvariable=newUsername).grid(row=5, column=4)

        # password label and entry box
        newPassword = tk.StringVar()
        passwordLabel = tk.Label(RegisterPageFrame, text=l10n[lang]['Password']).grid(row=6, column=3)
        passwordEntryBox = tk.Entry(RegisterPageFrame, textvariable=newPassword, show="*").grid(row=6, column=4)

        # Register
        RegisterButton = tk.Button(RegisterPageFrame, text=l10n[lang]['Register'], command=self.popupWindow).grid(row=7, column=4, pady=10)


if __name__ == "__main__":
    language = 'en'
    welcomeScreen= WelcomeScreen(language)
    welcomeScreen.win.mainloop()
    # app = SampleApp()
    # app.title(l10n[lang]['Title'])
    # # app.resizable(False, False)
    # app.geometry("600x270")
    # app.mainloop()

