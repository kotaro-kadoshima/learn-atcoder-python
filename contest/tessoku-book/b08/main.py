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
