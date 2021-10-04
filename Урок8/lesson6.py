number = 1
sum_n = 0
count = 0

while number != 0:
    n = int(input())
    if n != 0:
        count += 1
        sum_n += n
    if n == 0:
        number = 0 
    
print(sum_n / count)
    