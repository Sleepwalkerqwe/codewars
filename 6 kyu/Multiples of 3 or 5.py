def solution(number):
    i = 3
    s = 0
    while i < number:
        if i % 3 == 0 and i % 5 == 0:
            s += i
            i += 3
        else:
            if i % 3 == 0:
                s += i

            if i % 5 == 0:
                s += i

            i += 1
    return s
