H, W, N = map(int, input().split())
A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 各日を加算
X = [[0] * (W + 2) for _ in range(H + 2)]
Z = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    X[A[i]][B[i]] += 1
    X[A[i]][D[i] + 1] -= 1
    X[C[i] + 1][B[i]] -= 1
    X[C[i] + 1][D[i] + 1] += 1

# 累積和を計算
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = X[i][j] + Z[i][j - 1]
for j in range(1, W + 1):
    for i in range(1, H + 1):
        Z[i][j] = Z[i][j] + Z[i - 1][j]

# 出力
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if j >= 2:
            print(" ", end="")
        print(Z[i][j], end="")
    print("")
