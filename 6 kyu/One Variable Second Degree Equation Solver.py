def sec_deg_solver(a, b, c):
    if a == 0:
        if b != 0 and c != 0:
            return f"It is a first degree equation. Solution: {round(-1*(c/b),10)}"
        elif b == c and c == 0:
            return "The equation is indeterminate"
        elif b == 0 and c != 0:
            return "Impossible situation. Wrong entries"
        elif b != 0 and c == 0:
            return f"It is a first degree equation. Solution: 0.0"
    if discriminant(a, b, c) < 0:
        return "There are no real solutions"
    if discriminant(a, b, c) == 0:
        return f"It has one double solution: {(-b)/(2*a)}"
    arr = [round((-1*b+discriminant(a, b, c)**0.5)/(2*a), 10),
           round((-1*b-discriminant(a, b, c)**0.5)/(2*a), 10)]
    arr.sort()
    return f"Two solutions: {arr[0]}, {arr[1]}"


def discriminant(a, b, c):
    return (b**2-4*a*c)


print(sec_deg_solver(10, 2, -4))
