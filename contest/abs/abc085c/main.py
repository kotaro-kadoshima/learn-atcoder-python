n, sum = map(int, input().split())

if n * 10000 == sum:
    print("{} {} {}".format(n, 0, 0))
    exit()

for x in range(n, -1, -1):
    for i in range(n - x, -1, -1):
        y = i
        z = n - x - i

        if 10000 * x + 5000 * y + 1000 * z == sum:
            print("{} {} {}".format(x, y, z))
            exit()

print("-1 -1 -1")
