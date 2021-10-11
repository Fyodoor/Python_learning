s = input("Введите символ: ")
code1 = ord(s)

if code1 >= 65 and code1 <= 90 or code1 >= 97 and code1 <= 122:
    print(s.swapcase())
else:
    print(s)