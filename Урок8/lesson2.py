b = 5
count = 0
m = int(input())
while m > 0:
        if m %10 == b:
            count += 1
        m = m // 10
    
print(count)
    