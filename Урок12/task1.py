number_1 = int(input())
number_2 = int(input())

def digit(n):
    total = 0
    while n > 0:
        n = n // 10
        total += 1
    return total

n1_dig = digit(number_1)
n2_dig = digit(number_2)

print(n1_dig*n2_dig)
        
        