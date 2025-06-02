H, W = map(int, input().split())
X = [[0]] * (H + 1 * W + 1)

for i in range(H):
    X[i] = list(map(int, input().split()))

for i in range(H):
    sum = 0
    for j in range(W):
        sum += X[i][j]
        X[i][j] = sum

for j in range(W):
    sum = 0
    for i in range(H):
        sum += X[i][j]
        X[i][j] = sum

for i in range(H):
    print(X[i])

Q = int(input())

for i in range(Q):
    A, B, C, D = map(int, input().split())
    print()
