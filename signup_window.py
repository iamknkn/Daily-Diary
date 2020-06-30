import tkinter
import operations
import database


def signup(window):
    """

    :param window: previous window to be destroyed
    :return: None
    """
    window.destroy()
    signupwindow = tkinter.Tk()
    signupwindow.title("Diary")
    signupwindow.geometry("400x200+400+200")
    signupwindow["background"] = "white"
    signupwindow.update()
    signupwindow.maxsize(400, 200)
    signupwindow.minsize(400, 200)
    user_name = tkinter.StringVar()
    user_name.set("")
    error = tkinter.StringVar()
    password = tkinter.StringVar()
    name = tkinter.StringVar()
    name.set("")

    def register():
        """
        calls the checkdb method from database module
        :return: None
        """
        database.checkdb(name, user_name, password, "signup", error, signupwindow)

    def passtype():
        """
        calls the changepasstype method from passtype module
        :return:
        """
        operations.changepasstype(show_pass, pass_field)

    tkinter.Label(signupwindow, textvariable=error, bg="white").grid(row=0, column=1, columnspan=2, sticky="ew")
    tkinter.Label(signupwindow, text="Name", bg="white").grid(row=1, column=1, sticky="ew", padx=40)
    name_field = tkinter.Entry(signupwindow, textvariable=name, bg="white")
    name_field.grid(row=1, column=2, sticky="ew")
    tkinter.Label(signupwindow, text="Username", bg="white").grid(row=2, column=1, sticky="ew")
    user_field = tkinter.Entry(signupwindow, textvariable=user_name, bg="white")
    user_field.grid(row=2, column=2, sticky="ew")
    tkinter.Label(signupwindow, text="Password", bg="white").grid(row=3, column=1, sticky="ew")
    pass_field = tkinter.Entry(signupwindow, show="*", textvariable=password, bg="white")
    pass_field.grid(row=3, column=2, sticky="ew")
    show_pass = tkinter.Button(signupwindow, text="Show", command=passtype, bg="blue", fg="white", relief="flat")
    show_pass.grid(row=3, column=3, sticky="w")
    sign = tkinter.Button(signupwindow, text="Sign Up", command=register, bg="blue", fg="white", relief="flat")
    sign.grid(row=5, column=2, sticky="ew", pady=20)
