def altertext(text, uname, password, action):
    """

    :param text: data to be encrypted/ decrypted
    :param uname: username of user
    :param password: password of user
    :param action: takes values "encrypt" or "decrypt" to perform the obvious operation
    :return:
    """
    t = list(text)
    key = 0  # key is generated based on username and password
    for i in uname:
        if i.isnumeric():
            key += int(i)  # if numeric only value is added
        elif i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            pass  # vowels of username are not added to key
        else:
            key += ord(i)  # ascii value of element is added to key for other elements of username
    for i in password:
        if i.isnumeric():
            key += int(i)  # same as in key but in here vowels are also added
        else:
            key += ord(i)
    key %= 128
    if action == "encrypt":
        for i in range(0, len(t) - 1, 2):
            x = ord(t[i])  # every 2 characters are encrypted for each iteration of loop
            y = ord(t[i + 1])
            t[i] = chr((x + key) % 128)  # encryption of 1st char depends on key
            t[i + 1] = chr((y + x + key) % 128)  # encryption of 2nd char depends on key and the 1st char
        return "".join(t)  # result is returned
    if action == "decrypt":
        for i in range(0, len(t) - 1, 2):
            x = ord(t[i])
            t[i] = chr((x - key) % 128)  # logic is same as decryption but in the opposite way
            x = ord(t[i])
            y = ord(t[i + 1])
            t[i + 1] = chr((y - x - key) % 128)  # result is returned
        return "".join(t)
