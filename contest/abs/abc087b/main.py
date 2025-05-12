a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(a + 1):
    for j in range(b + 1):
        rest = x - 500 * i - 100 * j
        if 0 <= rest <= 50 * c and rest % 50 == 0:
            count += 1

print(count)
