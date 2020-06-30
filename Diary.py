import tkinter
import operations
import signup_window
import database

# noinspection PyShadowingNames
if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title("Diary")
    mainWindow.geometry("400x200+400+200")
    mainWindow["background"] = "white"
    mainWindow["padx"] = 72
    error = tkinter.StringVar()
    user_name = tkinter.StringVar()
    password = tkinter.StringVar()


    def passty():
        operations.changepasstype(show_pass, pass_field)

    def signupwind():
        signup_window.signup(mainWindow)

    def loginwind():
        database.checkdb(None, user_name, password, "login", error, mainWindow)

    tkinter.Label(mainWindow, textvariable=error, bg="white").grid(row=0, column=2, sticky="ew")
    tkinter.Label(mainWindow, text="Username", bg="white").grid(row=1, column=1, sticky="ew")
    user_field = tkinter.Entry(mainWindow, textvariable=user_name, bg="white").grid(row=1, column=2, sticky="ew")
    tkinter.Label(mainWindow, text="Password", bg="white").grid(row=2, column=1, sticky="ew")
    pass_field = tkinter.Entry(mainWindow, show="*", textvariable=password, bg="white")
    pass_field.grid(row=2, column=2, sticky="ew")
    show_pass = tkinter.Button(mainWindow, text="Show", command=passty, bg="blue", fg="white", relief="flat")
    show_pass.grid(row=2, column=3, sticky="w")
    LogIn = tkinter.Button(mainWindow, text="Log In", command=loginwind, bg="blue", fg="white", relief="flat")
    LogIn.grid(row=3, column=2, sticky="ew", pady=20)
    tkinter.Label(mainWindow, text=" New User? Register ---> ", bg="white", relief="flat").grid(row=4, column=2,
                                                                                                sticky="e")
    SignUp = tkinter.Button(mainWindow, text="Sign Up", command=signupwind, bg="blue", fg="white", relief="flat")
    SignUp.grid(row=4, column=3, sticky="w", pady=20)

    mainWindow.update()
    mainWindow.maxsize(400, 200)
    mainWindow.minsize(400, 200)
    mainWindow.mainloop()
