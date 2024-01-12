def scrabble_score(st):
    score = 0
    for i in st:

        if i.upper() in "AEIOULNRST":
            score += 1
        if i.upper() in "DG":
            score += 2
        if i.upper() in "BCMP":
            score += 3
        if i.upper() in "FHVWY":
            score += 4
        if i.upper() in "K":
            score += 5
        if i.upper() in "JX":
            score += 8
        if i.upper() in "QZ":
            score += 10
    return score
