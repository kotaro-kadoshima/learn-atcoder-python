N = int(input())
A = list(map(int, input().split()))
Q = int(input())

S = [[0, 0]]
sum_0 = 0
sum_1 = 0
for i in range(N):
    if A[i] == 0:
        sum_0 += 1
    else:
        sum_1 += 1
    S.append([sum_0, sum_1])

for i in range(Q):
    L, R = map(int, input().split())
    s_0, s_1 = [x - y for x, y in zip(S[R], S[L - 1])]

    if s_0 < s_1:
        print("win")
    elif s_0 > s_1:
        print("lose")
    else:
        print("draw")
