a=int(input())
b=a%1000
first=b//100
second=b//10 %10
third=b%10
print("Сумма цифр числа", a, "равна", first+second+third)