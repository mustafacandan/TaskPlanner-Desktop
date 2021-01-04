import tkinter as tk
from tkinter import font as tkfont
import gettext


_ = gettext.gettext

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


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        LoginPageFrame = tk.LabelFrame(self, width=300)
        LoginPageFrame.grid(row=0, column=0, padx=10, pady=10, ipady=10)
        username = tk.StringVar()
        languageVar = tk.StringVar(self)
        languageVar.set("English")

        # Language List
        languageList = tk.OptionMenu(LoginPageFrame, languageVar, *languages)
        languageLabel = tk.Label(LoginPageFrame, text=_("Select Language"))
        languageLabel.grid(row=0, column=4, sticky="ne")
        languageList.grid(row=0, column=5, padx=5)

        # Username
        usernameLabel = tk.Label(LoginPageFrame, text=_("E-mail"))
        usernameLabel.grid(row=4, column=3, pady=5, padx=100)
        usernameEntryBox = tk.Entry(LoginPageFrame, textvariable=username).grid(row=5, column=3, padx=100)

        # password label and entry box
        password = tk.StringVar()
        passwordLabel = tk.Label(LoginPageFrame, text=_("Password"))
        passwordLabel.grid(row=6, column=3, padx=100)
        passwordEntryBox = tk.Entry(LoginPageFrame, textvariable=password, show="*")
        passwordEntryBox.grid(row=7, column=3, padx=100)

        loginButton = tk.Button(LoginPageFrame, text=_("Login"),
                                command=login)
        loginButton.grid(row=9, column=3, pady=10, padx=100)

        registerButton = tk.Button(LoginPageFrame, text=_("New User"),
                                   command=lambda: controller.show_frame("RegisterPage"))
        registerButton.grid(row=10, column=3, pady=5,
                            padx=100)


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        newUsername = tk.StringVar()
        RegisterPageFrame = tk.LabelFrame(self)
        RegisterPageFrame.pack(fill="both", expand="yes", padx=5, pady=10)

        usernameLabel = tk.Label(RegisterPageFrame, text=_("E-Mail")).grid(row=0, column=0)
        usernameEntryBox = tk.Entry(RegisterPageFrame, textvariable=newUsername).grid(row=0, column=1)

        # password label and entry box
        newPassword = tk.StringVar()
        passwordLabel = tk.Label(RegisterPageFrame, text=_("Password")).grid(row=1, column=0)
        passwordEntryBox = tk.Entry(RegisterPageFrame, textvariable=newPassword, show="*").grid(row=1, column=1)

        # Register
        RegisterButton = tk.Button(RegisterPageFrame, text=_("Register"), command=register).grid(row=3, column=0)


if __name__ == "__main__":
    app = SampleApp()
    app.title(_("Task Planner Login Page"))
    # app.resizable(False, False)
    app.geometry("600x270")
    app.mainloop()

