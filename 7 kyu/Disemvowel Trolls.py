def disemvowel(string_):
    s = ''
    for i in string_:
        if i.lower() not in vowels:
            s += i
    return s

# or


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


vowels = ['a', 'e', 'i', 'o', 'u', 'y']
print(disemvowel('This website is for losers LOL!'))
