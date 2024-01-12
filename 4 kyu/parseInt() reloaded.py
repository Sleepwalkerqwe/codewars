    n = input().split()

    numbers = {'one': 1, 'two': 2, 'three': 3,
            'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000}
    new_n = []

    for i in n:
        new_n.extend(i.split("-"))

    n = new_n

    if 'and' in n:
        n.remove('and')

    s = 0  # s - сумма
    i = 0  # i - counter

    while i < len(n):
        if i < len(n)-1 and len(n) > 1:
            if numbers[n[i+1]] == 100 or numbers[n[i+1]] == 1000 or numbers[n[i+1]] == 1000000:
                s += (numbers[n[i]] * numbers[n[i+1]])
                i += 1
            else:
                s += numbers[n[i]]
        else:
            s += numbers[n[i]]
        i += 1

    print(s)
