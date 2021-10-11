line = input()
count = 0

for i in range(len(line) -1):
    if line[i] == line[i+1]:
        count += 1
        
print(count)