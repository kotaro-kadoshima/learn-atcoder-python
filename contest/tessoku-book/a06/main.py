# 書く日の来場者数の累積を計算していく
N, Q = map(int, input().split())
A = list(map(int, input().split()))

ruiseki = [0]
sum = 0
for i in range(N):
    sum += A[i]
    ruiseki.append(sum)
    # print("{}: {}".format(i, sum))

for i in range(Q):
    L, R = map(int, input().split())
    # print("{}-{}".format(ruiseki[R], ruiseki[L]))
    print(ruiseki[R] - ruiseki[L - 1])
