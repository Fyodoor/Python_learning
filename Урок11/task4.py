numbers = input("Натуральные числа через пробел сюда -> ")
numbers_sp = numbers.split()
print(numbers_sp)
count = 0

for i in range(len(numbers_sp)):
    digit = numbers_sp[i]
    j =  i + 1
    while j < len(numbers_sp):
        digit_n = numbers_sp[j]
        if digit == digit_n:
            count += 1
        j += 1
        
print(count)