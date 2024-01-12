def to_weird_case(words):
    words = words.lower()
    a = ""
    count = 0
    for i in words:
        if count % 2 == 0:
            a += i.upper()
        else:
            a += i
        count += 1
        if i == " ":
            count = 0
    return words


print(to_weird_case("qe Qwe re h fsgds KAFODKSAFa"))
