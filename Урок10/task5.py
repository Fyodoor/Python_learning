first_letter = input("Введите первую строчную букуву: ")
second_letter = input("Введите вторую строчную букву: ")
code1 = ord(first_letter)
code2 = ord(second_letter)

if code1 > code2:
    for i in range(code2, code1 + 1):
        print(chr(i))    
        
if code2 > code1:
    for i in range(code1, code2 + 1):
        print(chr(i))    