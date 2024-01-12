def binary(a):
    if a == "":
        return True
    n = 0
    for i in a:
        n = int(i)*2
    if n % 3 == 0:
        return (True)
    else:
        return (False)


a = input()
