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

# 1-indexedで累積和テーブルを作成
S = [[0] * (y_max + 2) for _ in range(x_max + 2)]
for i in range(N):
    S[X[i]][Y[i]] += 1

# T: 2次元累積和テーブル
T = [[0] * (y_max + 2) for _ in range(x_max + 2)]
for i in range(1, x_max + 2):
    for j in range(1, y_max + 2):
        T[i][j] = T[i][j - 1] + S[i][j]
for i in range(1, x_max + 2):
    for j in range(1, y_max + 2):
        T[i][j] += T[i - 1][j]

for i in range(Q):
    # 1-indexedでクエリを処理
    ans = T[a[i] - 1][b[i] - 1] + T[c[i]][d[i]] - T[c[i]][b[i] - 1] - T[a[i] - 1][d[i]]
    print(ans)
