s = ([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4,
     5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
count = 0
i = -1
answ = []
microansw = []
while i <= len(s)-1:
    i += 1
    microansw = []
    if i+1 > len(s):
        break
    if s[i] == s[i+1]-1:
        flag = True
        count = 1
        microansw.append(s[i])
        while flag == True:
            if i+1 >= len(s):
                break
            if s[i] == s[i+1]-1:
                count += 1
                microansw.append(s[i+1])
            else:
                break
            i += 1

        if count > 2:
            print(microansw[0], microansw[-1], sep='-', end=',')
        else:
            print(microansw[0], microansw[1], end=",", sep=",")
    else:
        print(s[i], end=",")
