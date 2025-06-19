N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 1
R = 10**9


def check(x):
    sum = 0
    for i in range(N):
        sum += x // A[i]
    return sum >= K


while L < R:
    C = (L + R) // 2
    if check(C):
        R = C
    else:
        L = C + 1

print(L)
