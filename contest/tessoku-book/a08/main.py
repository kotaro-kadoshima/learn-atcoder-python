H, W = map(int, input().split())
X = [0] * H
Z = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    X[i] = list(map(int, input().split()))


for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j - 1] + X[i - 1][j - 1]

for j in range(1, W + 1):
    for i in range(1, H + 1):
        Z[i][j] = Z[i - 1][j] + Z[i][j]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(Z[A - 1][B - 1] + Z[C][D] - Z[C][B - 1] - Z[A - 1][D])
