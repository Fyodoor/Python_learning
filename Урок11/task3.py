ip = input("Введите ip адресс: ")
ip_numbers = ip.split(".")
flag = 0

for i in range(len(ip_numbers)):
    ip_dig = int(ip_numbers[i])
    if ip_dig <= 255 and ip_dig >= 0:
        flag += 1
        
if flag == 4:
    print("YES")
else:
    print("NO")