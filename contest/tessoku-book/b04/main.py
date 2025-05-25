N = input()
size = len(N)

sum = 0
for i in range(size):
    if int(N[i]) == 0:
        continue

    sum += 2 ** (size - 1 - i)
print(sum)
