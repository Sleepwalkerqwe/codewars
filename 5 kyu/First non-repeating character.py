def first_non_repeating_letter(s):

    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i].lower() == s[j].lower():
                count += 1
            if count == 2:
                count = 0
                break
        if count == 1:
            return s[i]
    return ""
