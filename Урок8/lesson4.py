n = int(input())

if n >= 10:
    maximum = max(str(n))
    minimum = min(str(n))
    print("максимальная цифра равна", maximum)
    print("минимальная цифра равна", minimum)
    
else:
    print("Число должго быть больше или равно 10")