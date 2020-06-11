import os
import datetime


def changepasstype(s, p):
    """
    changes the visibility of password field p and displays the opposite option on button s

    :param s: button that displays "show" or "hide
    :param p:
    :return:
    """
    if s["text"] == "Show":
        p["show"] = ""
        s["text"] = " Hide "
    elif s["text"] == " Hide ":
        p["show"] = "*"
        s["text"] = "Show"


def todays_date():
    """
    :return: present datetime as object of datetime.datetime class
    """
    return datetime.datetime.now()


def create_dir(j, k=None):
    """
    checks if path exists and creates directory if path does not exists
    :param j:folder path to be created
    :param k: subfolder path to be created inside folder
    :return: 1 if path already exists else 0
    """
    exists = 1
    if k is not None:
        p = os.path.join(j, k)
    else:
        p = j
    if not os.path.exists(p):
        os.mkdir(p)
        exists = 0
    return exists


def dateformat(j):
    """

    :param j: object of class datetime.datetime
    :return: string of format "ddmmyyyy"
    """
    o = j.day
    if o < 10:
        x = "0" + str(o)
    else:
        x = str(o)
    o = j.month
    if o < 10:
        x += "0" + str(o) + str(j.year)
    else:
        x += str(o) + str(j.year)
    return x


def datecheck(xy):
    """
    checks if the date entered is valid or not

    :param xy: xy is a text field that gets the date from user in dd/mm/yyyy format
    :return: if date is valid datetime.datetime class with dd,mm,yy initialised else None
    """
    x = xy.get()
    try:
        j = x.index('/')
        dd = int(x[:j])
        x = x[j + 1:]
        j = x.index('/')
        mm = int(x[:j])
        yy = int(x[j + 1:])
        x = datetime.datetime(yy, mm, dd)
        return x
    except ValueError:
        return None


def error_found(name, u, p):
    """
    checks the validation of parameters
    :param name: name of user
    :param u: username of user
    :param p: password of user
    :return: error message
    """
    if len(name) < 3:
        return "Invalid Name"
    elif len(u) < 4:
        return "Username cant be empty or too short"
    elif len(u) > 15:
        return "Username too long"
    elif len(p) < 6:
        return "Password Length not sufficient"
    elif len(p) > 12:
        return "Password Length exceeded"
    elif not p.isalnum():
        return "Letters or Numbers only allowed for password"
    elif u == name:
        return "Name and Username can't be same"
    elif u == p:
        return "Username and Password can't be same"
    elif name == p:
        return "Name and Password can't be same"
    else:
        return None
