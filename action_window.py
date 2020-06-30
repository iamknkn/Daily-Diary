import tkinter
import os
import operations
import textwindow

def enterwindow(window, y, u, p, name):
    """
    creates an action window that displays available actions
    :param window: window to be destroyed
    :param y: directory name
    :param u: username of user
    :param p: password of user
    :param name: name of user
    :return: None
    """
    def date():
        """
        checks if date is valid or not i =f valid further checks if directory exists
        :return: None
        """
        nonlocal d
        j = operations.datecheck(d)
        if j:
            x = operations.dateformat(j)
            if os.path.exists(os.path.join(y, x)):
                k = x[:2] + "/" + x[2:4] + "/" + x[4:]
                textwindow.new_window(readwrite, y, k, x, u, p, "read")
            else:
                ddd = tkinter.Label(readwrite, text="No record found on that date(file may be deleted or removed)")
                ddd["bg"] = "red"
                ddd["fg"] = "white"
                ddd.grid(row=6, column=2, sticky="news", pady=5)
        else:
            dr = tkinter.Label(readwrite, text="Date Error", bg="red", fg="white")
            dr.grid(row=6, column=2, sticky="news", pady=5)

    def today():
        """
        creates a directory for writing data for today and
        calls function to display text editor
        :return: None
        """
        j = operations.todays_date()
        x = operations.dateformat(j)
        operations.create_dir(y)
        operations.create_dir(y, x)
        k = x[:2] + "/" + x[2:4] + "/" + x[4:]
        textwindow.new_window(readwrite, y, k, x, u, p, "write")

    def otherday():
        """

        calls function to display text editor
        :return: None
        :return:
        """
        textwindow.new_window(readwrite, y, None, None, u, p, "write")

    def anyday():
        """
        calls functiont to read data written on any_day
        :return: None
        """
        nonlocal d
        tkinter.Label(readwrite, text="Enter date in dd/mm/yyyy format").grid(row=4, column=2, sticky="news", pady=5)
        tkinter.Entry(readwrite, textvariable=d, relief="solid").grid(row=5, column=2, sticky="news", pady=5)
        sub = tkinter.Button(readwrite, text="Submit", command=date, bg="blue", fg="white")
        sub.grid(row=5, column=3, sticky="news", pady=5)

    window.destroy()
    readwrite = tkinter.Tk()
    readwrite.title("Diary")
    readwrite.geometry("400x250+400+200")
    readwrite["background"] = "white"
    readwrite.maxsize(400, 250)
    readwrite.minsize(400, 250)
    readwrite["padx"] = 6
    tkinter.Label(readwrite, text="Welcome " + name + "! Choose Action", bg="white").grid(row=0, column=1,
                                                                                              columnspan=2, pady=10)
    td = tkinter.Button(readwrite, text="Write today's diary", command=today, bg="blue", fg="white", relief="flat")
    td.grid(row=1, column=2, sticky="news", pady=5)
    to = tkinter.Button(readwrite, text="Write for random date", command=otherday, bg="blue", fg="white", relief="flat")
    to.grid(row=2, column=2, sticky="news", pady=5)
    tq = tkinter.Button(readwrite, text="Read Updated Daily Routine", command=anyday, bg="blue", fg="white",
                        relief="flat")
    tq.grid(row=3, column=2, sticky="news", pady=5)
    d = tkinter.StringVar()
    readwrite.columnconfigure(0, weight=1)
    readwrite.columnconfigure(1, weight=1)
    readwrite.columnconfigure(2, weight=1)
    readwrite.columnconfigure(3, weight=1)
    readwrite.columnconfigure(4, weight=1)
