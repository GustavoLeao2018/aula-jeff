def fat(n):
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)

for i in range(10):
    print(fat(i))