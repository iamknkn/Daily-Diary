import crypto
import os
import tkinter
import shelve
import operations


def new_window(window, path, dat, folder, use, pas, mode=None):
    """
    creates a new window and displays text editor to write or read

    :param window: previous window that needs to be destroyed
    :param path: path of directory
    :param dat: date on which text is written(/assumed to be)
    :param folder: sub directory to be created
    :param use: username of user
    :param pas: password of user
    :param mode: takes values "read" or "write" and perform the obvious operation
    :return: None
    """
    def write():
        """
        writes the encrypted text into a file located in the path '.'\\path\\folder
        :return: None
        """
        nonlocal text
        inf = text.get("1.0", "end")
        data = crypto.altertext(inf, use, pas, "encrypt")
        way = os.path.join(path, folder)
        with shelve.open(os.path.join(way, folder)) as cryp:
            cryp["data"] = data
            window.quit()

    def date():
        """
        checks if date entered is true for a random date and throws error
        if no error found, it calls write function
        :return: None
        """
        nonlocal d
        nonlocal fer
        nonlocal fer_field
        dc = operations.datecheck(d)
        if dc:
            nonlocal folder
            folder = operations.dateformat(dc)
            operations.create_dir(path)
            operations.create_dir(path, folder)
            write()
        else:
            fer.set("Date Error")
            fer_field["bg"] = "red"
            fer_field["fg"] = "white"

    window.destroy()                    # destroying previous window
    final = tkinter.Tk()                # creating a new window
    final.title("Encrypt")
    final["bg"] = "white"
    final.geometry("600x600")
    final.minsize(600, 600)
    final.maxsize(600, 600)
    if mode == "write":
        text = tkinter.Text(final, height=30, width=70, relief="solid", wrap=tkinter.WORD)
        text.grid(row=2, column=0, padx=10)
        scroll = tkinter.Scrollbar(final, orient=tkinter.VERTICAL, command=text.yview)
        scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
        text['yscrollcommand'] = scroll.set
        # writing for today's data
        if dat is not None:
            p = tkinter.Label(final, text="\t\t You are writing this diary on \t" + str(dat), bg="white")
            p.grid(row=0, column=0)
            su = tkinter.Button(final, text="Submit", command=write, bg="blue", fg="white")
            su.grid(row=5, column=0, sticky="w", padx=10, pady=10)
        # writing for random date that is not provided yet
        elif dat is None:
            d = tkinter.StringVar()
            x = tkinter.Label(final, text="\t Enter date in dd/mm/yyyy format------>", bg="white", width=10)
            x.grid(row=0, column=0, sticky="ew", pady=5)
            tkinter.Entry(final, textvariable=d, relief="solid", width=25).grid(row=0, column=0, sticky="e", pady=5)
            su = tkinter.Button(final, text="Submit", command=date, bg="blue", fg="white")
            su.grid(row=5, column=0, sticky="w", padx=10, pady=10)
            fer = tkinter.StringVar()
            fer_field = tkinter.Label(final, textvariable=fer)
            fer_field.grid(row=5, column=0, sticky="e")
    # reading written data
    elif mode == "read":
        text = tkinter.Text(final, height=30, width=70, relief="solid", wrap=tkinter.WORD)
        text.grid(row=2, column=0, padx=10)
        scroll = tkinter.Scrollbar(final, orient=tkinter.VERTICAL, command=text.yview)
        scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
        text['yscrollcommand'] = scroll.set
        su = tkinter.Button(final, text="Exit", command=final.quit, bg="blue", fg="white")
        su.grid(row=5, column=0, sticky="w", padx=10, pady=10)
        k = tkinter.Label(final, text="\t \t You are reading the diary written on \t" + str(dat), bg="white")
        k.grid(row=0, column=0)
        v = os.path.join(path, folder)
        with shelve.open(os.path.join(v, folder)) as crypt:
            j = crypt["data"]
            info = crypto.altertext(j, use, pas, "decrypt")
            text.insert(tkinter.END, info)
            if len(j) == 0:
                text.insert(tkinter.END, "NO content Found")
