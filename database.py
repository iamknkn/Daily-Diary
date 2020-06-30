import shelve
import operations
import crypto
import os
import action_window


def checkdb(nam=None, use=None, pas=None, action=None, err=None, window=None):
    """
    checks database for login/signup purposes
    :param nam: name of user
    :param use: username of user
    :param pas: password of user
    :param action: action to be checked for takes values "login" and "signup"
    :param err: to display error message
    :param window: prsent window
    :return: None
    """
    u = use.get()
    p = pas.get()
    operations.create_dir(r'C:\Users\Public', 'Documents')
    operations.create_dir(r'C:\Users\Public\Documents', "Diary")
    operations.create_dir(r"C:\Users\Public\Documents\Diary", "user_data")
    try:
        with shelve.open(r"C:\Users\Public\Documents\Diary\user_data\info") as users:

            def checkusers(ab, cd=None):
                if len(users.keys()) == 0:
                    return 0
                for va in users.keys():
                    if ab == users[va]["qw"] and cd is None:
                        return 1
                    elif ab == users[va]["qw"] and cd is not None:
                        if users[va]["xae"] == cd:
                            return va
                        else:
                            return None
                    else:
                        pass
                return 0

            if action == "login":
                uc = crypto.altertext(u, "Admin", "Admin@100", "encrypt")
                pc = crypto.altertext(p, "Admin", "Admin@100", "encrypt")
                file = checkusers(uc, pc)
                if file:
                    na = crypto.altertext(users[file]["nat"], "Admin", "Admin@100", "decrypt")
                    k = 0
                    for j in p:
                        k += ord(j)
                    for j in u:
                        k += ord(j)
                    y = os.path.join(r"C:\Users\Public\Documents\Diary", na + str(k)[:3])
                    action_window.enterwindow(window, y, u, p, na)
                else:
                    raise FileNotFoundError

            elif action == "signup":
                name = nam.get()
                uc = crypto.altertext(u, "Admin", "Admin@100", "encrypt")
                error_check = operations.error_found(name, u, p)
                if error_check is not None:
                    err.set(error_check)
                elif checkusers(uc):
                    err.set("Username not Available")
                else:
                    count = 1
                    for _ in users.keys():
                        count += 1
                    place = str(count)
                    pc = crypto.altertext(p, "Admin", "Admin@100", "encrypt")
                    nc = crypto.altertext(name, "Admin", "Admin@100", "encrypt")
                    users[place] = {"nat": nc, "qw": uc, "xae": pc}
                    k = 0
                    for i in p:
                        k += ord(i)
                    for j in u:
                        k += ord(j)
                    y = os.path.join(r"C:\Users\Public\Documents\Diary", name + str(k)[:3])
                    action_window.enterwindow(window, y, u, p, name)
    except FileNotFoundError:
        err.set("Invalid Username/Password\n")
