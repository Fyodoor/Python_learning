n = int(input())
spisok = []

for i in range(n):
    content = input()
    spisok.append(content)

srch = input("Поиск: ")

for i in spisok:
    if srch.lower() == i.lower():
        print(i)
