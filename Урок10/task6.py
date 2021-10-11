text = input()
digits = ""

for i in text:
    if i.isdigit():
        digits += i
print(digits)