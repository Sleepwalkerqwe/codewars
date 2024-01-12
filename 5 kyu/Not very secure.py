def alphanumeric(password):
    if password == "":
        return False
    for i in password:
        if i.lower() not in "1234567890qwertyuiopasdfghjklzxcvbnm":
            return False
    return True
