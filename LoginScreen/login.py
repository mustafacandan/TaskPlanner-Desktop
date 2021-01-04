import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3


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
        username = tk.StringVar()

        usernameLabel = tk.Label(self, text="Username").grid(row=0, column=0)
        usernameEntryBox = tk.Entry(self, textvariable=username).grid(row=0, column=1)

        # password label and entry box
        password = tk.StringVar()
        passwordLabel = tk.Label(self, text="Password").grid(row=1, column=0)
        passwordEntryBox = tk.Entry(self, textvariable=password, show="*").grid(row=1, column=1)

        loginButton = tk.Button(self, text="Login",
                                command=login).grid(row=3, column=1)

        registerButton = tk.Button(self, text="New User",
                                   command=lambda: controller.show_frame("RegisterPage")).grid(row=3, column=2)


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        newUsername = tk.StringVar()

        usernameLabel = tk.Label(self, text="Username").grid(row=0, column=0)
        usernameEntryBox = tk.Entry(self, textvariable=newUsername).grid(row=0, column=1)

        # password label and entry box
        newPassword = tk.StringVar()
        passwordLabel = tk.Label(self, text="Password").grid(row=1, column=0)
        passwordEntryBox = tk.Entry(self, textvariable=newPassword, show="*").grid(row=1, column=1)

        # Register
        RegisterButton = tk.Button(self, text="Register", command=register).grid(row=3, column=0)


if __name__ == "__main__":
    app = SampleApp()
    app.title("Task Planner Login Page")
    app.geometry("500x500")
    app.mainloop()
