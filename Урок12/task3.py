month = int(input())
def day(month):
    month = month - 1
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    number = day[month]
    return number
print(day(month))