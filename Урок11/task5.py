line = [1, 2, 3, 4, 1]
alone_s = []
i = 0

while i < len(line):
    symbol = line.count(line[i])
    if symbol == 1:
        alone_s.append(line[i])
    i += 1
    
print(*alone_s)