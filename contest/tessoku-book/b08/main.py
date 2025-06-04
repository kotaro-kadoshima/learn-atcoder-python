N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

Q = int(input())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
