inset = int(input())
inset = bin(inset)
n = 0
for i in inset:
    if i == '1':
        n += 1
print(n)