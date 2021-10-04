number = 1
positive_sum = 0
negative_sum = 0

while number != 0:
    n = int(input())
    if n > 0:
        positive_sum += 1
    if n < 0:
        negative_sum += 1
    if n == 0:
        number = 0
        
print(positive_sum * negative_sum)