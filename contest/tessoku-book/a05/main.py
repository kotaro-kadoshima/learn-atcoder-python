N, K = map(int, input().split())

count = 0
for x in range(1, N + 1):
    for y in range(1, N + 1):
        z = K - (x + y)
        if 0 < z and z <= N:
            count += 1
print(count)
