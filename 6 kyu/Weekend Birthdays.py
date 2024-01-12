def LeapYear(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    return False


date = input().split("-")
day = int(date[0])
mounth = int(date[1])

# если високосный год
if day == 29 and mounth == 2:
    day = 28

# берем значение месяца
mounthd = {1: [1, 10], 5: 2, 8: 3, 4: [2, 3, 11], 5: 6, 6: [12, 9], 0: [4, 7]}
for i in (mounthd):
    if isinstance(mounthd[i], list) and mounth in mounthd[i]:
        mounth = i
        break


"""1,10 - 1
5 - 2
8 - 3
2,3,11 - 4
6 - 5
12, 9 - 6
4,7 - 0
"""
Original_year = int(date[2])+1
year = (6+Original_year % 100+Original_year % 100/4) % 7

if LeapYear(Original_year):
    year -= 1

date = (day+mounth+year) % 7

# print(date)
day_of_weeks = ['Суббота', 'Воскресенье', 'Понедельник',
                'Вторник', 'Среда', 'Четверг', 'Пятница']


Find_year = 2024
while Original_year < Find_year:
    Original_year += 1
    year = (6+Original_year % 100+Original_year % 100/4) % 7

    if LeapYear(Original_year):
        year -= 1

    date = (day+mounth+year) % 7
    print(day_of_weeks[int(date)], sep="")
