def greatest_product(st):
    product = 0
    for i in range(len(s)-4):
        newproduct = int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])*int(s[i+4])
        if newproduct > product:
            product = newproduct
    return product


s = "123834539327238239583"
