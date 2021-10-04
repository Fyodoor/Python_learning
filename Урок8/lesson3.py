n = int(input())
last_digit = n
sum = 0

while last_digit != 0:
    sum = sum + last_digit %10
    last_digit = last_digit // 10
    
if n / sum %1 == 0:
    print("yes")
else:
    print("no")