x = [1, 2, 3]
y = [4, 5, 6]

n = len(x)
total = 0
for i in range(n):
    total += x[i] * y[i]
print(str(total))
