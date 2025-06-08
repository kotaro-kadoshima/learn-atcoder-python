N = int(input())
X = [0] * N
Y = [0] * N
x_max, y_max = 0, 0
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    if x_max < X[i]:
        x_max = X[i]
    if y_max < Y[i]:
        y_max = Y[i]


Q = int(input())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

# x座標とz座標を累積和に見立てる
S = [[0] * (y_max + 2) for _ in range(x_max + 2)]
for i in range(N):
    S[X[i]][Y[i]] += 1

# 累積和
T = [[0] * (y_max + 2) for _ in range(x_max + 2)]
for i in range(x_max):
    for j in range(y_max):
        T[i][j] = T[i][j - 1] + S[i][j]

for j in range(y_max):
    for i in range(x_max):
        T[i][j] = T[i - 1][j] + T[i][j]

for i in range(Q):
    print(T[a[i - 1]][c[i - 1]] + T[c[i]][d[i]] - T[c[i][b[i - 1]]] - T[c[i] - 1][d[i]])
